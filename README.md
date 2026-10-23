# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.6.19`
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

- `v1.6.19`
  - app sha256: `8953eb4052c0e83cde34ce328822c8b75a0ebeba99a19b1759a879cf9f547d72`
  - merged sha256: `b196d8ea1a98190f6cb17efcd44b496ec98b46cba514b7783e50003ddfad4a52`
- `v1.6.18`
  - app sha256: `9ca2c5982fce0c435c0463f32ac1bf3882ea903cfc6837bc32d891bcdaa37138`
  - merged sha256: `a0016cbfb1cfab8b7d0c9b8efd5e1f1d70b05139356be1624a72348926f94556`
- `v1.6.17`
  - app sha256: `39636e7faecf4da977440f2e266365a8b3bf62a5c4b28a3a08bdf7c3010fb9bb`
  - merged sha256: `be55b91d62bc67ce34ad0d11f0000835e80ec6139cec672aeea163fbbab9e3f7`
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
