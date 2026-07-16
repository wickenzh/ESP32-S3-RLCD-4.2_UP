# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.5.18`
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

- `v1.5.18`
  - app sha256: `29e656e7140e94eb253412765b0a80171998e3382cc816a933547d4cc185877e`
  - merged sha256: `aff348dcdbf13014ed6dba9349543e59ecabf3a6265b1b53b1ba401caeb36a5f`
- `v1.5.17`
  - app sha256: `de726a7db96fe7782e525b89487174ae127e94e469a681f4bb34d423f1863cbf`
  - merged sha256: `f397985ca5b0f840480541e53f3eea2b05dac67902424559a0b1b1c002a7719e`
- `v1.5.16`
  - app sha256: `41066715b97faf7ea8cde0241224326e7c852be20082a214f97f6e90792bd567`
  - merged sha256: `0f41e567c6ac0c9f0a4f160b6626a152e7fada30152ba1027973da15664917b8`
- `v1.5.15`
  - app sha256: `ecd3b8295960572d0a695fdd2342c4d2fa5b72afd80fe37d5feefd9a22213811`
  - merged sha256: `2a2c3fb988536894ce2c1912790f711ef6c0507df5f330daa05fea39909876f8`
- `v1.5.14`
  - app sha256: `f68ce32bedbc6cc1a18876800f04a0320946ea5a8e80346add681a113d7546bb`
  - merged sha256: `6c6c5c2bbe3f29bd4ace8f964bd4f57686a594cb353f0822673269661b841383`
- `v1.5.13`
  - app sha256: `92efc3f22507da45f0b85c90e0280ef26cc37903d33fe5c1c35e0f6d69a462ea`
  - merged sha256: `20581c036e2f7d50e3f7a25f24b783c032e26d30e449d12102f96a6d84297285`
- `v1.5.12`
  - app sha256: `9b39646030565555a2762ae86d3763d0e46c6729ffc149d89bdf5406149031b7`
  - merged sha256: `a4c5edab18af57f5f25c6153762f184115dd503a7b7c2e7fb8a1ee0010e521e6`
- `v1.5.11`
  - app sha256: `b487ea38a4ddff2cd7c9bb491a08eb2ac2f78298e2bc65a019f05e0b3fe69863`
  - merged sha256: `2be5cc0c6bda26d125516477d58ae6f8acd79089241abb412c9c6fe1e8d70ea5`
- `v1.5.10`
  - app sha256: `e0d963141b7910fa14f06f5db0eaf666a99ec62c6fd32b671501ff7e4dfb1426`
  - merged sha256: `f560e7fd69210353f6bb4b7f26cadffe806b6bf3ff9c0aef98b7fe6fb88ebf2f`
- `v1.5.9`
  - app sha256: `cd21709fd9ac0ea232563b56f0f7db9093a59ccc40824d568d2c22dcb7b9f942`
  - merged sha256: `4411a1aebb13423a2b0f5cbeca6cdd87825ecf8a0ea6d654a0857d44dbd3bde3`
