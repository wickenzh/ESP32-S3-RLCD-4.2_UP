# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA / 上位机固件镜像仓库，不保存固件源码。

## 当前版本

- 最新版本：`v1.4.27`
- Manifest：`firmware/latest.json`
- 版本清单：`firmware/versions.json`

## 文件用途

- `firmware/latest.json`：设备端检查 OTA 时读取的最新版本清单。
- `firmware/versions.json`：上位机读取最近版本列表，包含 app bin 和 merged bin 的 URL、大小和 SHA256。
- GitHub Release 附件 `weather_clock_vX.X.X.bin`：设备 OTA 升级用 app 固件。
- GitHub Release 附件 `weather_clock_vX.X.X_merged.bin`：串口完整刷写镜像，包含 bootloader、分区表、OTA data 和 app。

## 同步来源

本仓库由 GitHub Actions 自动从 Cloudflare R2 OTA 存储同步。

- R2 是设备默认 OTA 下载源。
- GitHub Release 是备份、历史下载和上位机读取的镜像。
- 每次同步最多保留最近 `10` 个版本。

## 最近版本

- `v1.4.27`：`v1.4.27`：降低未充电状态电池采样频率，低刷新页面空闲按键轮询放宽到 500ms，并增加 RLCD 局部/全屏刷新诊断日志。
  - app sha256: `1d7759c892282efa49c874b761e60ab816b5f11dfb7b75532834fa93415a6ae5`
  - merged sha256: `291b1775860c93d2cf47b87773faf09ee7b760ebff0d4266adbc8d47c456901b`
