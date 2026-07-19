# ESP32-S3 RLCD Weather Clock OTA

这个仓库是设备 OTA 与上位机固件备用镜像，不保存固件源码。

## 当前版本

- 最新版本：`v1.5.25`
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

- `v1.5.25`
  - app sha256: `c94da86157b7018818253806db40ba4498c8dd925e11a2f2ebfade5d115a6ab1`
  - merged sha256: `fd442befdbe47613278a05c14d4cddf4c5b6480a2ba7154bd2444432973be3d5`
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
- `v1.5.17`
  - app sha256: `de726a7db96fe7782e525b89487174ae127e94e469a681f4bb34d423f1863cbf`
  - merged sha256: `f397985ca5b0f840480541e53f3eea2b05dac67902424559a0b1b1c002a7719e`
- `v1.5.16`
  - app sha256: `41066715b97faf7ea8cde0241224326e7c852be20082a214f97f6e90792bd567`
  - merged sha256: `0f41e567c6ac0c9f0a4f160b6626a152e7fada30152ba1027973da15664917b8`
