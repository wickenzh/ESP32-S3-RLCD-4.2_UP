# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.6.16`
- Manifest：`firmware/latest.json`
- 版本清单：`firmware/versions.json`

## 自动同步来源

源码仓库 [`wickenzh/ESP32-S3-RLCD-4.2`](https://github.com/wickenzh/ESP32-S3-RLCD-4.2) 完成同版本固件构建、Release 附件和 OTA 清单后，会通过 GitHub `repository_dispatch` 立即通知本仓库。

本仓库从源码仓库 Release 拉取 app 与 merged 固件，逐个校验文件大小和 SHA256，全部通过后才更新 Release、`latest.json`、`versions.json` 与本说明。该流程不再读取 Cloudflare R2，也不再使用定时轮询。

## 文件用途

- `firmware/latest.json`：设备切换到 GitHub 备用源时读取的最新版本清单。
- `firmware/versions.json`：上位机读取最近 10 个版本及 app/merged 的 URL、大小和 SHA256。
- `weather_clock_vX.X.X.bin`：设备 OTA 升级用 App 固件。
- `weather_clock_vX.X.X_merged.bin`：串口完整刷写镜像。

## 最近版本

- `v1.6.16`
  - app sha256: `345a6f87faa95820a3fa0129a0cc10303efd1df149adde56a2fb6f860ba6f05b`
  - merged sha256: `745900bbfe7dd7036b8f8d47b5b7fec6b94e43acc1b7f1a1a8af7356675c7e7e`
- `v1.6.15`
  - app sha256: `da57f99486317667e9e8f1df32eb20b599f251dcfde73fb6b39ed8f03d6c9b6e`
  - merged sha256: `5af1a27ed597a9c91c447a69951b9cf6853962adde59f1fa3828197312637968`
- `v1.6.14`
  - app sha256: `89bbaf7cf5c88390479ec0659f76364b3bd09963cb6dd4f9639a6a04de22d5bb`
  - merged sha256: `c371a641dc19c95b3403243c31e0ac2adbda019001567f6b1d955e6a06c12226`
- `v1.6.13`
  - app sha256: `d019bcc6f2f4edb4ddf80de7f73f64f692599f02aa9536728906aee957a966d3`
  - merged sha256: `1afbcc6a9535b8860cbdfb66b84ae4410d346084dba9722650f19766321fa3f0`
- `v1.6.12`
  - app sha256: `c6b7b00979805749050348c39754e8f0708e13ee2d1bd674d5e0f3d480d50023`
  - merged sha256: `b4bec35e7218e512788f0e418dc6ae82a5b133d319bddd6b994d8a6896b27ad3`
- `v1.6.11`
  - app sha256: `de28a3f41883570c7d44135806dfce3a2c948fd40aa91391e4ebf76f64a2ec80`
  - merged sha256: `c39254004cf19bdd351eb35496ff714c18970f4b5adee137c898fd40299c41fa`
- `v1.6.10`
  - app sha256: `78f9930da268b078ca1c72094ac02d162d39ed573cfcd6a6ea759dd99c91b10a`
  - merged sha256: `a81e0258d4e472a4c55e167aaaca4cd391eb54e5a23926d0d6c316171eb5c784`
- `v1.6.9`
  - app sha256: `981766b25ca914654d92c44ce216463dbf6c82ac798b25a6ed75e069314eb3f4`
  - merged sha256: `612108130a5412f88f448bf8751f4b99b6fbcec4b9df22083f8a5692e67cc4e0`
- `v1.6.8`
  - app sha256: `7c322e8a300f4e7bf28cf0f57835be85cae7af21b4c6be5ef247e8bec16b64bf`
  - merged sha256: `f24d50cc216694c09040757c3dadb3ef8d6533a7b3a0ddff15b5206dd6c11d2c`
- `v1.6.7`
  - app sha256: `4c214b6e6f82a6c22bc79cd9c60fb3f5bf456eaa82e15a3f8879c85556959572`
  - merged sha256: `7182d99710c89774d3c01a47585e4449f07df08fee1c12f034a70c04c6def246`
