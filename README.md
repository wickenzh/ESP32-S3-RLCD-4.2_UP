# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA / 上位机固件镜像仓库，不保存固件源码。

## 当前版本

- 最新版本：`v1.4.41`
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

- `v1.4.41`：`v1.4.41`：v1.4.41: 翻页时钟底部温湿度改为黑底反显信息栏。
  - app sha256: `018b98fbb9a5d1b4ba27f704efa0479397714702cbd6f088faed3de79ac08fd3`
  - merged sha256: `46b435ea56adfa76f5202ed37a34ddb75f37965e2ea0e17f68c8546a1d0edc8d`
- `v1.4.40`：`v1.4.40`：低风险维护发布：继续集中设置页、网络检测和配网页 buffer/辅助控件维护路径，减少重复边界处理，保持功能、UI、协议和使用方式不变。
  - app sha256: `79170d05e487937c509f8066b1eb30e87d396aa594402e0475e22f72852a962a`
  - merged sha256: `d554c6ed9dea53bab43d9e08c370176dba3767ce48c0a1c7e4c622cad4391fc7`
- `v1.4.39`：`v1.4.39`：低风险维护发布：集中配网页、UI、OTA、自定义资源、GitHub 源码同步和预览脚本的 buffer/常量与资源释放细节，保持功能、UI、协议和使用方式不变。
  - app sha256: `251ae1adf4fc7460c64cc92d325df5d87ccfe1a7e6b6a24b26ecbd75f485c8ef`
  - merged sha256: `26a9528a3e6568a33828bc9b39b9eda3cdf9cf24dc2aae0eebb4a6630e06cf7f`
- `v1.4.38`：`v1.4.38`：低风险维护发布：整理配网页表单字段匹配与 URL 解码边界，并汇总近期 NTP、HTTP、网络诊断和每日文字解析 helper 化优化；功能、UI 和协议保持不变。
  - app sha256: `2ee09a2963b490c77f1bf422bbf307125bc288b84791ae99a331479cde4fa071`
  - merged sha256: `60374102e29a93897fad154833c290f2abc20ccf7ac01d677934f7efee48f413`
- `v1.4.37`：`v1.4.37`：低风险维护发布：继续整理设置页菜单索引，网络和声音设置改用命名常量，降低后续菜单扩展时误改风险，功能和 UI 行为保持不变。
  - app sha256: `40b0be29d8cef366f1340aa8e3d3477093d96a1e0230cb6840859868de4c66be`
  - merged sha256: `ee5ad3670c52d5a04a73b9078a2e8277233305abb51af32087bdcd259e946fff`
- `v1.4.36`：`v1.4.36`：低风险代码维护发布：集中工作页常量、页面名称、显示设置映射和系统设置索引，清理无用 include，保持现有功能和 UI 不变。
  - app sha256: `d086e63981a6cb3fdbc662dfa4c9a6c18408275ce1099f75060437fdf512b836`
  - merged sha256: `7a0a0c071042588d472b4c4c58e38a6da31b5a6ff7226bcd0dd8637b3ba60dad`
- `v1.4.35`：`v1.4.35`：合并手动天气城市配置；修复配网页中文城市输入与清除后同步逻辑；降低联网同步期间 RLCD SPI DMA 内存压力。
  - app sha256: `ec555c50b53317690ca7abf488519ba3380ed718c33e566833c85150ae5d9576`
  - merged sha256: `8ac1834ce2d24eac7e07a67e106d8936d20363b9fa6c2eb29553cede5eea1df3`
- `v1.4.34`：`v1.4.34`：低风险优化网络配置解析、每日文字失败日志、HTTP 响应预览和网络诊断日志。
  - app sha256: `3e5c097f0836753a46551dd06c6ad6f2140b8067ef0b296fd352828ef882c13e`
  - merged sha256: `475f3d93bed362b6e9682285687ab2b8046a4bf5d21a9a80a45aca708bc49e4a`
- `v1.4.33`：`v1.4.33`：补强 OTA 本地固件归档清理流程，旧归档文件异常时不影响当前版本发布。
  - app sha256: `94a094e75028b20b973a4b195a692c9c39248f5e2981f1818149066b9b10350c`
  - merged sha256: `895b38de1be95e8eb9100e9f30ad37be48b880156ff3fe7008ca6d3b207872b0`
- `v1.4.32`：`v1.4.32`：优化整点报时播放包络，降低首音炸音概率，并补强 OTA Worker 维护检查。
  - app sha256: `8cb5b42a1d22f8c8186d6880b7c5d04eac7515e88c6629a0865c9fcb9e5e6077`
  - merged sha256: `e37d3a642827a70a2da712c1476c60446d8b2e66652c52f28754a96f9d851f9d`
