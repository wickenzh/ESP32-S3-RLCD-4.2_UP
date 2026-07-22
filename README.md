# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.5.27`
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

- `v1.5.27`
  - app sha256: `26e1390f1054f33055d22e8b808382c8282d2d33a6f4179f5a2b07399e1b4db7`
  - merged sha256: `0411182ea2aa15b5537ccf32d15bbeb752c495090d2e2b9040bdb81e780779ac`
- `v1.5.26`
  - app sha256: `b080c314aa55822da12bea6b8688b8355e6e231ed11500cf804878416b0e61d8`
  - merged sha256: `40a15665f700a39b14a186ddf8dbee7b0e0d2d78b251dd19b4d9da5805fad598`
- `v1.5.25`
  - app sha256: `abfd4c9eb5af3136ab63d40cf0c85e691eea576af26bfd29b59deab0e95ace6a`
  - merged sha256: `19b9919fd04d91ada7fd52f228d9042ebc4b07289e4f3c4866939f809713e858`
- `v1.5.24`
  - app sha256: `9bd56894e1bc6385f191a3e33cdaa153f40bf603d680170a3445e9df7236cc37`
  - merged sha256: `7dfdecaf22b9624ea7f5d1170ce62bfa460cd4d97087af99d40de708fd68d2a4`
- `v1.5.23`
  - app sha256: `78fc56a7489f90c930ac1ac462b161bf6a13a823cbb919fa61230f360309ab81`
  - merged sha256: `448652051e0dae3547facf693ea486d755a69bbc84dc05bb551592df8da88c6e`
- `v1.5.22`
  - app sha256: `c04fc2d08692cb923eb1e67f172f1dbbb91ad7a8c5d20796019b9c0d61d9605a`
  - merged sha256: `b16dd63cfc4adf75bb5f4ed867266252f3235659dd4507efefc8964bd35a9a74`
- `v1.5.21`
  - app sha256: `1b6ac0c7111f69bfb4e798db5331ebf083a6f06091e045cbf25c9d7a680c7e66`
  - merged sha256: `2c8d3ac97088644c5b10220eb7bf4f5b36a94a1d63097b3fb5cf5d31e197c24d`
- `v1.5.20`
  - app sha256: `2fadff3e491113e8770a722251ed33dbe05a1ba2a7d40bf1e43d6c38803821d6`
  - merged sha256: `68330904dc76b265b3602aed90ef6ae619971b780fdf4e4afc3f99600e3eeb4b`
- `v1.5.19`
  - app sha256: `c756e8a41fa07d23799de744afe487c6ae78ae09bda30c94c72b3e202ca2c140`
  - merged sha256: `8fdc4f1a5a19cca4e957c7766e49f2736df83d692024c511cf20ae637ab7f91a`
- `v1.5.18`
  - app sha256: `27cb4539b3b2ddad4ec7272aba1a6931d9182e17f0a4f9df698446e2bed6d3da`
  - merged sha256: `72e9d6dc52f3bdbd22ddb160f8076faf3d52a83630f609430db98ade3c89362c`
