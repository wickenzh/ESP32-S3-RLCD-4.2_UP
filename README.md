# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA / 上位机固件镜像仓库，不保存固件源码。

## 当前版本

- 最新版本：`v1.4.45`
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

- `v1.4.45`：`v1.4.45`：完整维护发布：翻页时钟底部 UI 完成一轮整理，温湿度改为覆盖小时与分钟区域的黑底反显面板，支持上下排列和舒适度表情，秒牌下方新增独立日期/农历反显框；优化记录按日期拆分，优化流水线增加中文发布说明校验、提交字段常量和候选扫描误报过滤；继续收敛 OTA、QWeather、每日文字、HTTP、NTP、网络检测、配网、音频、电池、电源管理、温湿度历史、自定义资源、按键、启动入口、设置页和 UI 主循环中的固定文案、日志文本、NVS key、表单字段、页面编号与布局常量校验，后续新增页面、接口或文案时更容易在编译期发现漏维护问题，固件运行逻辑、OTA 协议、分区表和用户操作流程保持不变。
  - app sha256: `4587708dcd8667c9972375ad716d99f5726909c5f47889991358a6cc8c7de7dc`
  - merged sha256: `77e969d4c193ebb67656d5555f3702e06bde63b7d2aca056e4fadaca1eff1691`
- `v1.4.44`：`v1.4.44`：v1.4.44: Wi-Fi portal fixed text guard and low-risk maintenance
  - app sha256: `55645904a8aae4b56af9191476c7f43945a67543335d1fd9865e91c1447c2fb5`
  - merged sha256: `13aa13a6fa1ebb4dd01df37318426cf092bd69e90d967d66ea162b6318b45ddc`
- `v1.4.43`：`v1.4.43`：v1.4.43: OTA status string guard and low-risk maintenance
  - app sha256: `a8c3b2cd3f8a7a10e42662110e97d1e001064ce5d04f6f482b0464cedd8af138`
  - merged sha256: `edfef015c3217199439db9d1e05db99f5db677c2c8637158f79bc1ac6158a9fc`
- `v1.4.42`：`v1.4.42`：v1.4.42: Low-risk maintenance optimizations
  - app sha256: `b912184f5ccda05437e40ca895b01b179117eecce7d271c2530f9700b3b48c8f`
  - merged sha256: `0a8c3e5f5703e1280f1ba421e9c99863a22f22b8bafeb0d5af508547c8eca179`
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
