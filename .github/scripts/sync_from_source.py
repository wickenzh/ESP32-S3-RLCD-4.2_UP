#!/usr/bin/env python3
# 校验并镜像公开源码仓库的 OTA 固件、Release 和版本清单。
"""Mirror validated firmware and manifests from the public source repository."""

from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


API_ROOT = "https://api.github.com"
API_ACCEPT = "application/vnd.github+json"
API_VERSION = "2022-11-28"
VERSION_RE = re.compile(r"^v(\d+)\.(\d+)\.(\d+)$")
SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
VERSIONS_KEEP = 10
LATEST_MAX_BYTES = 1800
RETRYABLE_HTTP_STATUS = {408, 429, 500, 502, 503, 504}


def log(message: str) -> None:
    print(message, file=sys.stderr, flush=True)


def version_key(version: str) -> tuple[int, int, int]:
    match = VERSION_RE.fullmatch(version)
    if not match:
        raise ValueError(f"invalid version: {version}")
    return tuple(int(part) for part in match.groups())


def validate_repository(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", value):
        raise ValueError(f"invalid GitHub repository: {value}")
    return value


def validate_metadata(value: object, label: str) -> dict[str, object]:
    if not isinstance(value, dict):
        raise ValueError(f"{label} metadata is missing")
    sha256 = str(value.get("sha256", "")).lower()
    size = value.get("size")
    if not SHA256_RE.fullmatch(sha256):
        raise ValueError(f"{label} sha256 is invalid")
    if not isinstance(size, int) or size <= 0:
        raise ValueError(f"{label} size is invalid")
    return {"sha256": sha256, "size": size}


def validate_source_manifests(
    latest: object,
    versions: object,
    requested_version: str,
) -> tuple[str, list[dict[str, object]]]:
    if not isinstance(latest, dict) or not isinstance(versions, dict):
        raise ValueError("source manifests must be JSON objects")
    latest_version = str(latest.get("version", ""))
    version_key(latest_version)
    if str(versions.get("latest", "")) != latest_version:
        raise ValueError("source latest.json and versions.json disagree")
    raw_items = versions.get("items")
    if not isinstance(raw_items, list) or not raw_items:
        raise ValueError("source versions.json has no items")

    unique: dict[str, dict[str, object]] = {}
    for raw_item in raw_items:
        if not isinstance(raw_item, dict):
            raise ValueError("source versions.json contains a non-object item")
        version = str(raw_item.get("version", ""))
        version_key(version)
        if version in unique:
            raise ValueError(f"duplicate source version: {version}")
        item = {
            "version": version,
            "notes": str(raw_item.get("notes", "")).strip(),
            "app": validate_metadata(raw_item.get("app"), f"{version} app"),
            "merged": validate_metadata(raw_item.get("merged"), f"{version} merged"),
        }
        unique[version] = item

    if latest_version not in unique:
        raise ValueError("latest source version is absent from versions.json")
    latest_app = validate_metadata(latest, "latest app")
    if latest_app != unique[latest_version]["app"]:
        raise ValueError("latest app metadata does not match versions.json")

    if requested_version:
        requested_key = version_key(requested_version)
        if requested_key > version_key(latest_version):
            raise ValueError(
                f"source manifest is behind requested version: {latest_version} < {requested_version}"
            )
        if requested_key < version_key(latest_version):
            log(
                f"Ignoring stale dispatch for {requested_version}; source latest is {latest_version}"
            )

    items = sorted(unique.values(), key=lambda item: version_key(str(item["version"])), reverse=True)
    return latest_version, items[:VERSIONS_KEEP]


def release_asset_url(repository: str, version: str, name: str) -> str:
    return f"https://github.com/{repository}/releases/download/{version}/{name}"


def encode_json(value: object) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def fit_latest_manifest(value: dict[str, object], notes: str) -> bytes:
    value["notes"] = notes
    encoded = encode_json(value)
    if len(encoded) <= LATEST_MAX_BYTES:
        return encoded
    suffix = "…"
    low = 0
    high = len(notes)
    best = ""
    while low <= high:
        middle = (low + high) // 2
        candidate = notes[:middle].rstrip() + suffix
        value["notes"] = candidate
        encoded = encode_json(value)
        if len(encoded) <= LATEST_MAX_BYTES:
            best = candidate
            low = middle + 1
        else:
            high = middle - 1
    value["notes"] = best
    encoded = encode_json(value)
    if len(encoded) > LATEST_MAX_BYTES:
        raise ValueError("target latest.json exceeds its device size limit")
    return encoded


def build_target_manifests(
    latest_version: str,
    items: list[dict[str, object]],
    target_repository: str,
) -> tuple[bytes, bytes, list[dict[str, object]]]:
    target_items: list[dict[str, object]] = []
    for source_item in items:
        version = str(source_item["version"])
        app_name = f"weather_clock_{version}.bin"
        merged_name = f"weather_clock_{version}_merged.bin"
        target_items.append({
            "version": version,
            "notes": source_item["notes"],
            "app": {
                "url": release_asset_url(target_repository, version, app_name),
                **source_item["app"],
            },
            "merged": {
                "url": release_asset_url(target_repository, version, merged_name),
                **source_item["merged"],
            },
        })
    latest_item = next(item for item in target_items if item["version"] == latest_version)
    latest = {
        "version": latest_version,
        "url": latest_item["app"]["url"],
        "sha256": latest_item["app"]["sha256"],
        "size": latest_item["app"]["size"],
    }
    return (
        fit_latest_manifest(latest, str(latest_item["notes"])),
        encode_json({"latest": latest_version, "items": target_items}),
        target_items,
    )


def render_readme(
    latest_version: str,
    items: list[dict[str, object]],
    source_repository: str,
) -> bytes:
    lines = [
        "# ESP32-S3 RLCD Weather Clock OTA",
        "",
        "这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。",
        "",
        "## 当前版本",
        "",
        f"- 最新版本：`{latest_version}`",
        "- Manifest：`firmware/latest.json`",
        "- 版本清单：`firmware/versions.json`",
        "",
        "## 自动同步来源",
        "",
        f"源码仓库 [`{source_repository}`](https://github.com/{source_repository}) 完成同版本固件构建、Release 附件和 OTA 清单后，会通过 GitHub `repository_dispatch` 立即通知本仓库。",
        "",
        "本仓库从源码仓库 Release 拉取 app 与 merged 固件，逐个校验文件大小和 SHA256，全部通过后才更新 Release、`latest.json`、`versions.json` 与本说明。该流程不再读取 Cloudflare R2，也不再使用定时轮询。",
        "",
        "## 文件用途",
        "",
        "- `firmware/latest.json`：设备切换到 GitHub 备用源时读取的最新版本清单。",
        "- `firmware/versions.json`：上位机读取最近 10 个版本及 app/merged 的 URL、大小和 SHA256。",
        "- `weather_clock_vX.X.X.bin`：设备 OTA 升级用 App 固件。",
        "- `weather_clock_vX.X.X_merged.bin`：串口完整刷写镜像。",
        "",
        "## 最近版本",
        "",
    ]
    for item in items:
        lines.extend([
            f"- `{item['version']}`",
            f"  - app sha256: `{item['app']['sha256']}`",
            f"  - merged sha256: `{item['merged']['sha256']}`",
        ])
    return ("\n".join(lines) + "\n").encode("utf-8")


class GitHubApi:
    def __init__(self, token: str) -> None:
        self._token = token

    def request(
        self,
        method: str,
        url: str,
        *,
        payload: object | None = None,
        body: bytes | None = None,
        accept: str = API_ACCEPT,
        allow_not_found: bool = False,
        timeout: int = 180,
    ) -> bytes | None:
        if payload is not None and body is not None:
            raise ValueError("payload and body are mutually exclusive")
        headers = {
            "Authorization": f"Bearer {self._token}",
            "Accept": accept,
            "X-GitHub-Api-Version": API_VERSION,
            "User-Agent": "weather-clock-source-ota-mirror",
        }
        data = body
        if payload is not None:
            data = json.dumps(payload, ensure_ascii=False).encode("utf-8")
            headers["Content-Type"] = "application/json"
        elif body is not None:
            headers["Content-Type"] = "application/octet-stream"

        for attempt in range(1, 6):
            request = urllib.request.Request(url, data=data, method=method, headers=headers)
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    return response.read()
            except urllib.error.HTTPError as exc:
                detail = exc.read().decode("utf-8", errors="replace")
                if exc.code == 404 and allow_not_found:
                    return None
                if attempt == 5 or exc.code not in RETRYABLE_HTTP_STATUS:
                    raise RuntimeError(
                        f"GitHub API {method} {url} failed: HTTP {exc.code} {detail[:500]}"
                    ) from exc
            except (OSError, TimeoutError) as exc:
                if attempt == 5:
                    raise RuntimeError(f"GitHub request failed: {method} {url}: {exc}") from exc
            time.sleep(attempt * 2)
        raise RuntimeError(f"GitHub request exhausted retries: {method} {url}")

    def json(
        self,
        method: str,
        url: str,
        *,
        payload: object | None = None,
        allow_not_found: bool = False,
    ) -> object | None:
        body = self.request(
            method,
            url,
            payload=payload,
            allow_not_found=allow_not_found,
        )
        if body is None:
            return None
        try:
            return json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise RuntimeError(f"GitHub API returned invalid JSON for {url}") from exc


def api_url(repository: str, suffix: str) -> str:
    return f"{API_ROOT}/repos/{repository}/{suffix.lstrip('/')}"


def load_repository_file(api: GitHubApi, repository: str, path: str) -> bytes:
    quoted_path = urllib.parse.quote(path, safe="/")
    response = api.json("GET", api_url(repository, f"contents/{quoted_path}?ref=main"))
    if not isinstance(response, dict) or response.get("encoding") != "base64":
        raise RuntimeError(f"unable to read {repository}/{path}")
    try:
        encoded = "".join(str(response.get("content", "")).split())
        return base64.b64decode(encoded, validate=True)
    except ValueError as exc:
        raise RuntimeError(f"invalid base64 content for {repository}/{path}") from exc


def parse_json_bytes(data: bytes, label: str) -> object:
    try:
        return json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as exc:
        raise ValueError(f"{label} is not valid UTF-8 JSON") from exc


def release_by_tag(api: GitHubApi, repository: str, version: str) -> dict[str, object] | None:
    result = api.json(
        "GET",
        api_url(repository, f"releases/tags/{version}"),
        allow_not_found=True,
    )
    if result is None:
        return None
    if not isinstance(result, dict):
        raise RuntimeError(f"invalid release response for {repository} {version}")
    return result


def release_assets(api: GitHubApi, repository: str, release_id: object) -> list[dict[str, object]]:
    if not isinstance(release_id, int):
        raise RuntimeError(f"release in {repository} has no numeric id")
    result = api.json("GET", api_url(repository, f"releases/{release_id}/assets?per_page=100"))
    if not isinstance(result, list):
        raise RuntimeError(f"invalid release asset response for {repository}")
    return [asset for asset in result if isinstance(asset, dict)]


def find_asset(assets: list[dict[str, object]], name: str) -> dict[str, object] | None:
    return next((asset for asset in assets if asset.get("name") == name), None)


def digest_matches(asset: dict[str, object], expected_sha: str) -> bool | None:
    digest = str(asset.get("digest", ""))
    if not digest:
        return None
    return digest.lower() == f"sha256:{expected_sha}"


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def download_asset(
    api: GitHubApi,
    repository: str,
    asset: dict[str, object],
    destination: Path,
) -> None:
    asset_id = asset.get("id")
    if not isinstance(asset_id, int):
        raise RuntimeError(f"release asset in {repository} has no numeric id")
    data = api.request(
        "GET",
        api_url(repository, f"releases/assets/{asset_id}"),
        accept="application/octet-stream",
        timeout=300,
    )
    if data is None:
        raise RuntimeError(f"unable to download release asset {asset_id}")
    destination.write_bytes(data)


def verify_download(path: Path, metadata: dict[str, object], label: str) -> None:
    size = int(metadata["size"])
    sha256 = str(metadata["sha256"])
    if path.stat().st_size != size:
        raise RuntimeError(f"{label} size mismatch: {path.stat().st_size} != {size}")
    actual_sha = file_sha256(path)
    if actual_sha != sha256:
        raise RuntimeError(f"{label} sha256 mismatch: {actual_sha} != {sha256}")


def asset_is_valid(
    api: GitHubApi,
    repository: str,
    asset: dict[str, object] | None,
    metadata: dict[str, object],
    temp_dir: Path,
    label: str,
) -> bool:
    if asset is None or int(asset.get("size") or 0) != int(metadata["size"]):
        return False
    digest_state = digest_matches(asset, str(metadata["sha256"]))
    if digest_state is not None:
        return digest_state
    destination = temp_dir / f"verify-{asset.get('id')}.bin"
    download_asset(api, repository, asset, destination)
    try:
        verify_download(destination, metadata, label)
    except RuntimeError:
        return False
    return True


def ensure_target_release(
    api: GitHubApi,
    target_repository: str,
    version: str,
    notes: str,
    latest: bool,
) -> dict[str, object]:
    release = release_by_tag(api, target_repository, version)
    payload = {
        "name": version,
        "body": render_release_body(version, notes),
        "draft": False,
        "prerelease": False,
    }
    if release is None:
        payload.update({
            "tag_name": version,
            "target_commitish": "main",
            "make_latest": "true" if latest else "false",
        })
        created = api.json("POST", api_url(target_repository, "releases"), payload=payload)
        if not isinstance(created, dict):
            raise RuntimeError(f"unable to create target release {version}")
        return created
    release_id = release.get("id")
    if not isinstance(release_id, int):
        raise RuntimeError(f"target release {version} has no numeric id")
    if latest:
        payload["make_latest"] = "true"
    updated = api.json(
        "PATCH",
        api_url(target_repository, f"releases/{release_id}"),
        payload=payload,
    )
    if not isinstance(updated, dict):
        raise RuntimeError(f"unable to update target release {version}")
    return updated


def render_release_body(version: str, notes: str) -> str:
    return (
        f"ESP32-S3 RLCD 4.2 天气时钟 {version} OTA 固件。\n\n"
        f"{notes.strip()}\n\n"
        "附件说明：\n"
        f"- `weather_clock_{version}.bin`：设备 OTA 升级固件。\n"
        f"- `weather_clock_{version}_merged.bin`：包含分区表的完整刷写固件。"
    )


def upload_asset(
    api: GitHubApi,
    release: dict[str, object],
    name: str,
    source: Path,
) -> None:
    upload_url = str(release.get("upload_url", "")).split("{", 1)[0]
    if not upload_url.startswith("https://"):
        raise RuntimeError("target release has no usable upload URL")
    query = urllib.parse.urlencode({"name": name})
    api.request("POST", f"{upload_url}?{query}", body=source.read_bytes(), timeout=300)


def sync_release_assets(
    api: GitHubApi,
    source_repository: str,
    target_repository: str,
    item: dict[str, object],
    latest: bool,
    temp_dir: Path,
) -> None:
    version = str(item["version"])
    target_release = release_by_tag(api, target_repository, version)
    target_assets = (
        release_assets(api, target_repository, target_release.get("id"))
        if target_release is not None
        else []
    )
    target_is_complete = all(
        asset_is_valid(
            api,
            target_repository,
            find_asset(target_assets, f"weather_clock_{version}{suffix}"),
            item[kind],
            temp_dir,
            f"target weather_clock_{version}{suffix}",
        )
        for kind, suffix in (("app", ".bin"), ("merged", "_merged.bin"))
    )
    if target_is_complete:
        ensure_target_release(
            api,
            target_repository,
            version,
            str(item["notes"]),
            latest,
        )
        log(f"Kept validated target release {version}")
        return

    source_release = release_by_tag(api, source_repository, version)
    if source_release is None:
        raise RuntimeError(
            f"target release is incomplete and source release is missing: {version}"
        )
    source_assets = release_assets(api, source_repository, source_release.get("id"))
    target_release = ensure_target_release(
        api,
        target_repository,
        version,
        str(item["notes"]),
        latest,
    )
    target_assets = release_assets(api, target_repository, target_release.get("id"))

    for kind, suffix in (("app", ".bin"), ("merged", "_merged.bin")):
        name = f"weather_clock_{version}{suffix}"
        metadata = item[kind]
        source_asset = find_asset(source_assets, name)
        if source_asset is None:
            raise RuntimeError(f"source release asset is missing: {name}")
        if int(source_asset.get("size") or 0) != int(metadata["size"]):
            raise RuntimeError(f"source release asset size disagrees with manifest: {name}")
        source_digest = digest_matches(source_asset, str(metadata["sha256"]))
        if source_digest is False:
            raise RuntimeError(f"source release asset digest disagrees with manifest: {name}")

        target_asset = find_asset(target_assets, name)
        if asset_is_valid(
            api,
            target_repository,
            target_asset,
            metadata,
            temp_dir,
            f"target {name}",
        ):
            log(f"Kept validated target asset {name}")
            continue

        source_path = temp_dir / name
        download_asset(api, source_repository, source_asset, source_path)
        verify_download(source_path, metadata, f"source {name}")
        if target_asset is not None:
            asset_id = target_asset.get("id")
            if not isinstance(asset_id, int):
                raise RuntimeError(f"stale target asset has no numeric id: {name}")
            api.request("DELETE", api_url(target_repository, f"releases/assets/{asset_id}"))
        upload_asset(api, target_release, name, source_path)
        refreshed_assets = release_assets(api, target_repository, target_release.get("id"))
        uploaded = find_asset(refreshed_assets, name)
        if not asset_is_valid(
            api,
            target_repository,
            uploaded,
            metadata,
            temp_dir,
            f"uploaded {name}",
        ):
            raise RuntimeError(f"uploaded target asset failed verification: {name}")
        target_assets = refreshed_assets
        log(f"Uploaded and verified target asset {name}")


def atomic_write(path: Path, content: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=f".{path.name}.", dir=path.parent)
    try:
        with os.fdopen(fd, "wb") as handle:
            handle.write(content)
        os.replace(temporary, path)
    except Exception:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source-repository", required=True)
    parser.add_argument("--target-repository", required=True)
    parser.add_argument("--requested-version", default="")
    parser.add_argument("--latest", required=True, type=Path)
    parser.add_argument("--versions", required=True, type=Path)
    parser.add_argument("--readme", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source_repository = validate_repository(args.source_repository)
    target_repository = validate_repository(args.target_repository)
    requested_version = args.requested_version.strip()
    if requested_version:
        version_key(requested_version)
    token = os.environ.get("GITHUB_TOKEN", "").strip()
    if not token:
        raise SystemExit("GITHUB_TOKEN is not configured")
    api = GitHubApi(token)
    source_latest = parse_json_bytes(
        load_repository_file(api, source_repository, "firmware/latest.json"),
        "source latest.json",
    )
    source_versions = parse_json_bytes(
        load_repository_file(api, source_repository, "firmware/versions.json"),
        "source versions.json",
    )
    latest_version, source_items = validate_source_manifests(
        source_latest,
        source_versions,
        requested_version,
    )
    latest_bytes, versions_bytes, target_items = build_target_manifests(
        latest_version,
        source_items,
        target_repository,
    )

    with tempfile.TemporaryDirectory(prefix="weather-clock-ota-mirror-") as temp_name:
        temp_dir = Path(temp_name)
        for item in reversed(source_items):
            sync_release_assets(
                api,
                source_repository,
                target_repository,
                item,
                str(item["version"]) == latest_version,
                temp_dir,
            )

    atomic_write(args.latest, latest_bytes)
    atomic_write(args.versions, versions_bytes)
    atomic_write(
        args.readme,
        render_readme(latest_version, target_items, source_repository),
    )
    print(latest_version)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
