# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA / 上位机固件镜像仓库，不保存固件源码。

## 当前版本

- 最新版本：`v1.4.31`
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

- `v1.4.31`：`v1.4.31`：OTA 检查和安装支持 Cloudflare R2 与 GitHub OTA 双路径备份，发布流程默认同步两个 OTA 源。
  - app sha256: `f234ebc1cd7a3b2d0b4b5db52191641a6d807371238c2a5be9e3b3606f1ae6de`
  - merged sha256: `8cb4d2b808fc35b0ff74c259fb646e879d83176de5adc7dacb3da036d7c8aa5f`
- `v1.4.30`：`v1.4.30`：增强预览生成脚本参数校验，并补强发布/自动化入口的本机工具和子脚本前置检查，避免发布流程静默忽略异常输入或在后期才暴露环境问题。
  - app sha256: `b86559e9b5cbed05f72b6bd894ecc9d42620acd6a027d9cb3a05005891aa8227`
  - merged sha256: `3d2ec410882f62b224175accbcafc195d361d73ca679711bc3eac1bfae4bd2af`
- `v1.4.29`：`v1.4.29`：增强 SDL 页面预览生成流程，默认适配无人值守环境，并在截图转换成功后再替换目标预览图。
  - app sha256: `a8bf3d8db239ef004f80fb7f6f8f8ae66312846d0ac85fa2d2fcdef15b6f88f9`
  - merged sha256: `eb5f0a9b0fc273ed51f0704a9d9898a607aa9e161ba5d49719e74e05d7bf94d5`
- `v1.4.28`：`v1.4.28`：低风险代码维护优化，集中电池百分比常量、NTP/HTTP/诊断配置常量，并增强发布脚本环境检查。
  - app sha256: `14131624e7f7831968664a2817c04fe8c76544e6e24d698a2687861c21ce6bf2`
  - merged sha256: `b8cd6ebadc82d39c85c6f637ddba79e37c2b6383284adc5e9d6ca5d3bb939809`
- `v1.4.27`：`v1.4.27`：降低未充电状态电池采样频率，低刷新页面空闲按键轮询放宽到 500ms，并增加 RLCD 局部/全屏刷新诊断日志。
  - app sha256: `1d7759c892282efa49c874b761e60ab816b5f11dfb7b75532834fa93415a6ae5`
  - merged sha256: `291b1775860c93d2cf47b87773faf09ee7b760ebff0d4266adbc8d47c456901b`
- `v1.4.26`：`v1.4.26`：低风险收敛功耗与稳定性，降低翻页时钟温湿度刷新频率，补强联网同步失败收尾，并保留 OTA 下载期 RAM/DMA 保护策略。
  - app sha256: `b7c445dd400eb73c24afb89c1bac36b22df3056365c2a0394959c064f575b839`
  - merged sha256: `cb828a73b4b59f6164e8ae28e23a9c1cd122b0ddea47e3708b5767af5f187c27`
- `v1.4.25`：`v1.4.25`：取消翻页时钟铰链/折线显示，保留圆角黑底数字牌，并整理数字居中与顶部温湿度显示。
  - app sha256: `41f6e78b53041ed4608d007da9f79e79a073330e081c4ee9c81d82d1a9f68f9c`
  - merged sha256: `a637e1a0db277edd3febd2b01b4f48e498e0ec4106a800056baa1955c1c9da0b`
- `v1.4.24`：`v1.4.24`：微调翻页时钟铰链位置，取消翻页动画并保留稳定秒级局部刷新。
  - app sha256: `a9623dd4b06e99f5cf5b2a1e2cd28ba1c77466aaf464f776628445b932a49a1f`
  - merged sha256: `9f382d25418e6dd2e044389a38071e0fa295829bd7637ccf2249b0a8201009eb`
- `v1.4.23`：`v1.4.23`：新增翻页时钟页面，修正工作页状态栏对齐，并接入 6 页面顺序管理。
  - app sha256: `5f0878e94dd0a380288ea41a0ad908d408cdf97f11ceab550aaa1dc7194133a4`
  - merged sha256: `8aa4b33c8b679e3108dc7a21f24b4c9449a1f6fbb1fdc42f699083d4574ad897`
- `v1.4.22`：`v1.4.22`：统一非天气时钟工作页顶部状态栏，增加分钟时间并在所有工作页显示声音/Wi-Fi 状态图标。
  - app sha256: `9549992fdeeecbb6471994fcc17aef3f91cf57d99a579665d05ed03e829202bc`
  - merged sha256: `2fea3697d04471aebb8dec493e4a60c23d614983e7b02b8f767921f3c5f4a997`
