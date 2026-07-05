# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA / 上位机固件镜像仓库，不保存固件源码。

## 当前版本

- 最新版本：`v1.4.48`
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

- `v1.4.48`：`v1.4.48`：1. 修复温湿时钟秒级刷新偶发跳秒：温湿时钟页面活动时使用更短的 UI 轮询上限，秒牌仍保持秒值变化时局部刷新，不改变页面布局。<br>2. 修正状态栏 Wi-Fi 图标显示条件：天气时钟和所有工作页统一改为 Wi-Fi 已连接并获取 IP 后显示，断开后立即隐藏。<br>3. 完整验证并发布：同步更新固件、SDL、Gitea Release、Cloudflare R2 OTA 和 GitHub 源码仓库。
  - app sha256: `aa03a5b7d6f4dfc253de6e2fb012effdad927c8d3e0437b3dcf7d0712e564b78`
  - merged sha256: `022df528c5d6e65d90bec5135cd27740b81cb93ae486e79be4c510373edaa6a3`
- `v1.4.47`：`v1.4.47`：1. 调整页面命名：翻页时钟更名为温湿时钟，温度历史更名为温湿历史，用户侧页面名称与当前功能更一致。2. 重排默认页面顺序：默认顺序改为天气时钟、图片时钟、天气看板、温湿时钟、日历、温湿历史，并让设置显示页与默认 BOOT 顺序保持一致。3. 重排内部页面编号：页面编号改为天气时钟0、图片时钟1、天气看板2、温湿时钟3、日历4、温湿历史5，同时使用 page_mask_v4/page_order_v4 保存页面启用和排序；不维护旧编号兼容层。4. 升级注意：由于页面编号已调整，最佳方式是完整串口刷机；如果选择 OTA 升级，也可以在升级成功后执行恢复出厂设置并重新配网，让旧页面设置数据恢复到新编号默认状态。5. 维护整理：继续累积近期低风险优化，包括天气预警标题、OTA 文本、设置反馈、UI 同步状态、网络检测、每日文字、天气看板、温湿历史和多处临时 buffer/日志/helper 收口，固件功能、OTA 协议和分区表保持不变。
  - app sha256: `3b0bdefbded5d196a1abba56c5bd2068372aa50e65fd577326bd2585f2b57bb1`
  - merged sha256: `50e83f43868ca93ad4a101664024c7a196dfc339dbfa01e815eb7882d944c528`
- `v1.4.46`：`v1.4.46`：完整维护发布：继续推进低风险代码优化和可维护性收敛，温湿度小时历史加载新增单槽位读取 helper，统一处理 NVS key 生成、blob 长度校验、最新时间戳更新和读取错误日志，保持新格式优先、旧格式回退和缺失 key 静默策略不变；网络检测等待态初始化改为固定表驱动并增加覆盖断言，新增或调整诊断行时更容易发现漏初始化问题。固件运行逻辑、页面 UI、OTA 协议、分区表、NVS 数据格式和用户操作流程保持不变。
  - app sha256: `87536a8a620aaf42f63fa0ae3b7577b73a424fea66872d72ceace965cc8a8037`
  - merged sha256: `7c039a1cba18c46f08d12fa44b1cda4da6096b49b2648816adab6555a821b8b1`
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
