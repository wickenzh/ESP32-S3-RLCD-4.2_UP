# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA / 上位机固件镜像仓库，不保存固件源码。

## 当前版本

- 最新版本：`v1.4.54`
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

- `v1.4.54`：`v1.4.54`：
  1. 收拢版本同步脚本检查：版本同步脚本的依赖命令和目标版本文件改为集中清单维护，后续新增版本文件时更不容易漏改。
  2. 收拢 R2 OTA 发布检查：R2 发布脚本集中维护依赖命令、Worker 源文件和构建产物脚本路径，并在 Cloudflare secret 解析失败时提前给出明确错误。
  3. 收拢 GitHub OTA 备用源检查：GitHub OTA 发布脚本集中维护依赖命令和必要子脚本，减少备用源发布流程的重复检查代码。
  4. 收拢 OTA bin 归档检查：本地 OTA bin 归档脚本集中维护依赖命令、构建产物和保留数量校验，方便后续排查固件补传问题。
  5. 收拢 OTA manifest 生成检查：OTA manifest 脚本集中维护依赖命令、app bin 和发布说明 helper 路径，保持 `latest.json` 生成逻辑更清楚。
  6. 修复 Gitea Release 正文变量边界：附件文件名变量增加显式边界，避免中文标点触发 shell 变量解析错误。
  7. 完整验证并发布：重新构建固件和 SDL，生成发布产物、预览图、Gitea Release、Cloudflare R2 OTA，并同步 GitHub 源码仓库。
  - app sha256: `b0e52a4083abd278fe3623e2bc55d6480dc0c24c868dccbbfa45aee3ac26f7b0`
  - merged sha256: `e5053ecae340eced2ba61c5d7a470046a828600f7577f16fdfe3c3d4e7dc3bd7`
- `v1.4.53`：`v1.4.53`：
  1. 增强 Gitea Release 上传稳定性：Release 查询、创建/更新、附件列表、旧附件删除和新附件上传增加统一短重试，降低本地 Gitea 短暂抖动导致完整发布中断的概率。
  2. 收拢 Gitea Release curl 调用入口：所有 Gitea API 请求统一走同一个 helper，确保后续新增 Release 请求时不会漏用重试参数。
  3. 收拢 Gitea Release 依赖命令检查：上传脚本依赖命令改为集中清单维护，新增依赖时更容易检查和审阅。
  4. 收拢 Gitea Release 附件文件名：app bin、flash package 和 merged bin 的文件名集中为具名变量，路径、说明和上传调用复用同一份命名来源。
  5. 完整验证并发布：重新构建固件和 SDL，生成发布产物、预览图、Gitea Release、Cloudflare R2 OTA，并同步 GitHub 源码仓库。
  - app sha256: `5617bf247fc816ea10cc480140c66c946c420c16b90de1e88ef59fa9e03d171e`
  - merged sha256: `60284e5da57f7195fd3dc5180d5693da717e025b10a88ecc2353bda1b1fcb3de`
- `v1.4.52`：`v1.4.52`：
  1. 收拢发布入口依赖命令清单：完整发布脚本中的基础命令、Gitea Release、R2 OTA 和可选 GitHub OTA 依赖命令改为集中数组维护，后续新增发布目标时更不容易漏检命令。
  2. 收拢发布入口子脚本清单：构建产物、预览图、静态检查、Gitea Release、R2 OTA 和可选 GitHub OTA 子脚本改为集中声明，preflight 检查更清楚。
  3. 收拢发布布尔开关：发布目标、允许脏文件和允许白名单内新文件等 `0/1` 开关统一通过 helper 读取和校验，避免不同使用点默认值写散。
  4. 收拢 R2 发布验证参数：R2 发布后校验 `latest.json`、`versions.json` 和固件 bin 的超时、重试次数与间隔集中成常量，后续调整验证耐心时更容易维护。
  5. 收拢仓库路径拼接：发布入口调用仓库内脚本和 README release notes helper 时统一使用 `repo_path()`，减少重复手写 `$ROOT_DIR/...` 带来的维护风险。
  6. 完整验证并发布：重新构建固件和 SDL，生成发布产物、预览图、Gitea Release、Cloudflare R2 OTA，并同步 GitHub 源码仓库。
  - app sha256: `381eaafd4436817b6c3565908589a389e345b1b90fb226b763580ddbbb97c450`
  - merged sha256: `8ce4eec917644c301546c1de06d4b2daea68c75b1dfad9822c91139b7ced9772`
- `v1.4.51`：`v1.4.51`：
  1. 统一发布说明解析：发布脚本新增统一的 README 版本说明提取入口，Gitea Release 和 OTA manifest 现在复用同一份解析结果，减少多处 shell 解析规则不一致的风险。
  2. 支持多行中文发布说明：正式版本记录可以继续使用分点换行格式，发布脚本会完整提取多行内容，不再把说明压成一整行。
  3. 兼容旧版单行记录：历史版本如果仍是单行写法，补传 Release 或重新生成 manifest 时也能读取原有说明，不会轻易退回兜底文案。
  4. 收拢发布说明兜底文案：缺少版本记录时的默认说明统一由 helper 维护，避免 OTA manifest 和 Gitea Release 缺省文案分叉。
  5. 收拢发布入口版本检查：固件、SDL 和 CMake 版本号读取与比对逻辑集中到 release pipeline helper，缺失或不一致时输出更明确。
  6. 收拢 README 版本记录预检查：完整发布前会复用统一 release notes helper 检查当前版本记录，确保预检查规则和实际发布说明生成规则一致。
  7. 收拢发布白名单：dirty 范围检查和发布暂存路径复用同一份白名单，继续避免 `host_web/`、本地归档、密钥等非固件发布内容被误带入。
  8. 完整验证并发布：重新构建固件和 SDL，生成发布产物、预览图、Gitea Release、Cloudflare R2 OTA，并同步 GitHub 源码仓库。
  - app sha256: `da3821848803a49a3df32380189be64e4a7c7e25959fca98e344ac00ce200d25`
  - merged sha256: `9bac443f379b75003474deb060b9e1c2caeffd5c59efc45fc9bc7065a4630ab2`
- `v1.4.50`：`v1.4.50`：
  1. 收拢启动页面配置恢复路径：把页面启用 mask、页面顺序归一化、主页选择等启动恢复逻辑集中到 helper，后续调整页面排序或主页兜底更容易维护。
  2. 收拢联网请求清理事件位：把离线模式、恢复出厂和配置切换时需要清理的联网、网络检测和 OTA 请求位集中管理，降低后续新增请求位时漏清理的风险。
  3. 收拢设置页互斥确认态清理：恢复出厂、离线模式关闭和手动天气城市清除的二次确认 pending 状态统一由 helper 清理，避免切换设置项后旧确认态残留。
  4. 完整验证并发布：重新构建固件和 SDL，生成发布产物、预览图、Gitea Release、Cloudflare R2 OTA，并同步 GitHub 源码仓库。
  - app sha256: `0b6870b29182a0f0130432097af5365946b493bdc3d53ac83439d164e26dafe7`
  - merged sha256: `ecf5c909a1f8821a50a8cda16d9d7ba13fb925e0dbdb5a8a8f546bff294c1895`
- `v1.4.49`：`v1.4.49`：<br>1. 修复设置页页面顺序排序时偶发误返回工作页的问题：设置页 30 秒无操作超时改为使用最新 tick 和有符号差值判断，避免按键任务刚刷新活动时间后被 UI 主循环旧 tick 误判超时。<br>2. 补强设置页 KEY 短按活动计时：页面顺序模式下切换选择项也会刷新最后活动时间，确保用户正在操作时不会被当作无操作。<br>3. 继续同步维护文档和优化日志：补充设置页跨任务超时判断规则，后续调整按键或设置页状态机时避免回退到旧判断方式。<br>4. 完整验证并发布：重新构建固件和 SDL，生成发布产物、预览图、Gitea Release、Cloudflare R2 OTA，并同步 GitHub 源码仓库。
  - app sha256: `6498da64a30a9492784f621623536a4bca3aa3b725fe95e1f153178db04d116c`
  - merged sha256: `4044358c34b4c034b6083162f2aa758e698cbb8bb1eb7b8978cd2d6d3e67077a`
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
