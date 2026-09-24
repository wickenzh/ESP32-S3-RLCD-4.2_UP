# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.6.11`
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
- `v1.6.6`
  - app sha256: `b626e618ae7e14cb9fcc7cb36ce943719402edb645be815b554d96c45ab65c4c`
  - merged sha256: `4d284641765cd4be90b5fa4440db3130d931452a914246a6b7c0cbc9eb7923b8`
- `v1.6.5`
  - app sha256: `bf997cb9f218099a26576353c124ef83548b95e912cf2b0b093c7f05f55bcc5b`
  - merged sha256: `a26bf0bc7505dd5628e9f615ce0ee9c0ffc45ca083b775cde434a856ea174818`
- `v1.6.4`
  - app sha256: `9e65b3d4f006638103088eab86538bb9f7be6c53b16dcd75fea6be1d26e28db1`
  - merged sha256: `0eb3c694b64a37069b10babfb3a3913fca2801faa65a58f4940b99da6e9f63f0`
- `v1.6.3`
  - app sha256: `7210008ba77e7b50a5edb2246ff2d40c6e43b7a3990c00256911a150cd670ff8`
  - merged sha256: `d62c596eb158aa695e746e62c02fc499e486a3e284d5af410919d2062ec7efcc`
- `v1.6.2`
  - app sha256: `bff1d67dd0d3569a44f60099baf80d6481d5ab56936bb3ce19a4f6a9acce0082`
  - merged sha256: `4cafa94836060bbf2589ab803933001bfac86fa1659d14a58bff8996bb107280`
