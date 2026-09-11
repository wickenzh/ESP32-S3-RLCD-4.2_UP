# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.6.3`
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

- `v1.6.3`
  - app sha256: `7210008ba77e7b50a5edb2246ff2d40c6e43b7a3990c00256911a150cd670ff8`
  - merged sha256: `d62c596eb158aa695e746e62c02fc499e486a3e284d5af410919d2062ec7efcc`
- `v1.6.2`
  - app sha256: `bff1d67dd0d3569a44f60099baf80d6481d5ab56936bb3ce19a4f6a9acce0082`
  - merged sha256: `4cafa94836060bbf2589ab803933001bfac86fa1659d14a58bff8996bb107280`
- `v1.6.1`
  - app sha256: `8a8ac5d91fffa97a646943bab8c56f0f4fc3481a155a41a65db4620d480fe344`
  - merged sha256: `285d247c198f8d1bfe09fff10377d1ba0df1581cb00c3f0db354a14ce340d8b8`
- `v1.6.0`
  - app sha256: `67b00e2f571ab32ec0ae5f9c0cdefe10c711d60294934ed646b6471f7ad280eb`
  - merged sha256: `37843ab52555d7564221935a16db6782f140ff3e57771c190db2bc6af72fc39f`
- `v1.5.41`
  - app sha256: `20d7e5047890bf634a4e10aab003cb1953b18a7b9d2a0f2b8860891360f2cc48`
  - merged sha256: `91098e4343421f4430ab62cec0d77b86d7683049774fbc8e8c011300672bbed1`
- `v1.5.40`
  - app sha256: `5a968ac9246be47d8d239b349be9ebf81286e7866c1a81cef682799ab831f88b`
  - merged sha256: `6af9ef55bc2694547e8c3b0c57abd82a1ad1d6305d97f5d053f4dd48dc33687d`
- `v1.5.39`
  - app sha256: `95a0004a15e60f1aa8d0e64780a5d3baaadbdacd2a0ccf72ed45829783c7dff3`
  - merged sha256: `5a92448e7bf940dc0a790f614a22bfbfa115643ca56b6e721a70d944c72b3367`
- `v1.5.38`
  - app sha256: `ec771de44bbb001b891a0d5a69bfd6ec20037e92c3fb5db7c23cae7e75ff70ce`
  - merged sha256: `03c777128f44315234ae96183efe3ac4921e8bb52c695d4fd1c6d65252067812`
- `v1.5.37`
  - app sha256: `65b46b262c9354660e2b3f91ae6530c28d415e0c754d23c37c11fd327e29270f`
  - merged sha256: `ba086ac7365540141a9588ad68fd2c0afb17f09ba877ea771fe77510773a3a61`
- `v1.5.36`
  - app sha256: `4c0e1f6b9f34922f931d70ec7cc3031b753257efe773622de86bc2f23ebce58f`
  - merged sha256: `ffc683afa70bc05c79366e08b067a34277acc9c01e2eb0d4b41953bd095cb5ea`
