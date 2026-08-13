# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.5.36`
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

- `v1.5.36`
  - app sha256: `4c0e1f6b9f34922f931d70ec7cc3031b753257efe773622de86bc2f23ebce58f`
  - merged sha256: `ffc683afa70bc05c79366e08b067a34277acc9c01e2eb0d4b41953bd095cb5ea`
- `v1.5.35`
  - app sha256: `2b437a4d96bfa913940e1d4726bb7bbe3c73643377047903c4fe81a9bdf43463`
  - merged sha256: `0a9aafd67eed59cfb0e416322a3b5d8e7ae5bdb364313133543085dd9e6a143b`
- `v1.5.34`
  - app sha256: `b1ff52463e6892b67a21f52a6543b80612272e577491a24cb2ddc04d1285dcee`
  - merged sha256: `281f556204ed8c977443d71199e4a89e0bc81e0b542dc5537db4d56a25266356`
- `v1.5.33`
  - app sha256: `d2f667b041163311097df4438787608367f77e302fd5b8ce369c97d8c863ad26`
  - merged sha256: `fa2d91882d18bad85e0b6a5cca89f867094dfc0244b57437149ec5191c0a3ace`
- `v1.5.32`
  - app sha256: `913e0b9f24ba2be3fffe82c2045ae6799bdc524aa1989571b15551a0b7f1e53b`
  - merged sha256: `21da71e102ad3ec08cc7354d91908063b6db25dbb10ef60cf424f30098508eb5`
- `v1.5.31`
  - app sha256: `17912f5a1b6da734d46acfb1acd94657ef02d996e07666330ba2cf7983843363`
  - merged sha256: `ea238d4095709cb09b830ba50ef0edc4a27f673ec5658208f94d518b2b19e32f`
- `v1.5.30`
  - app sha256: `e36e60c05353d9212683a6986667ebd18447b98213e17176df45ed90a332dcc7`
  - merged sha256: `feb97f7d178e7c5bd44332ca6dd27ca06d346e454bea499b0b444966af8832c1`
- `v1.5.29`
  - app sha256: `d82b7c66531e1354560d5e4e92266b6b93c2f0b06e43bfdf432c9252f4be2baa`
  - merged sha256: `70a8bf33df19f118fa57481feaae96af1a04b1ffbf0a25856c58ece63263cdf8`
- `v1.5.28`
  - app sha256: `238c6cafe273375a7adfcc4bc0c72043f78c7e58f30bde9ea68a4313b3fdbeca`
  - merged sha256: `c361880d913935c02d78f0855df369ca9f2d0da87ae99c478ae48f6c53cfa630`
- `v1.5.27`
  - app sha256: `26e1390f1054f33055d22e8b808382c8282d2d33a6f4179f5a2b07399e1b4db7`
  - merged sha256: `0411182ea2aa15b5537ccf32d15bbeb752c495090d2e2b9040bdb81e780779ac`
