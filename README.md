# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 专用仓库，不保存固件源码。

## 当前 OTA 版本

- 版本：`v1.4.7`
- OTA 固件：`weather_clock_v1.4.7.bin`
- 完整刷写镜像：`weather_clock_v1.4.7_merged.bin`
- Manifest：`firmware/latest.json`

## 文件用途

- `firmware/latest.json`：设备端检查更新时读取的清单文件。
- GitHub Release 附件 `weather_clock_v1.4.7.bin`：仅用于设备 OTA 升级，只包含 app 固件。
- GitHub Release 附件 `weather_clock_v1.4.7_merged.bin`：用于串口完整刷写，包含 bootloader、分区表、OTA data 和 app。

如果设备分区表发生变化，不能只刷 OTA app bin，需要使用完整刷写镜像或完整烧录包。

## v1.4.7 更新说明

`v1.4.7`：修复 GitHub OTA 长签名 URL 下载请求失败，并调整设置页显示/系统菜单按钮右侧对齐。

## 发布策略

- 历史 Release 附件会保留，方便回退和对比测试。
- `latest.json` 永远指向当前希望设备 OTA 获取的版本。
- 不向本仓库推送固件源码。
