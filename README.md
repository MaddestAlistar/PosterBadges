# 良友影视海报角标库 · PosterBadges

由 **良哥看未来** 整理维护 · v1.0 · 2026-10-23

[返回良友资源中心](https://maddestalistar.github.io/LiangYou-ResourceHub/) · [查看全部角标预览](preview/index.html)

将常见的分辨率、片源、HDR、编码与音轨格式制作成统一风格的 **透明 PNG 和可编辑 SVG**。可叠加在影视海报、媒体库卡片或播放器展示图上。

## 目前已制作

**12 类角标 × 2 套配色 = 24 张透明 PNG + 24 个 SVG**，图像均为 **540 × 164 px**。PNG 的四角为透明（RGBA），中间的角标面板是不透明/半透明设计。

| 类型 | 角标 |
| --- | --- |
| 分辨率 | 4K、1080P |
| HDR | HDR10、HDR10+、Dolby Vision |
| 音频 | Atmos、TrueHD、DTS-HD MA |
| 编码与色深 | HEVC、10BIT |
| 片源 | REMUX、WEB-DL |

- [深色版全部素材](assets/dark/)：面向深色、黑色影视海报。
- [浅色版全部素材](assets/light/)：适合浅色背景。
- [角标数据目录](catalog.json)：包含文件名、类别、尺寸和配色信息。
- [使用说明与叠加位置](docs/usage.md)。
- [自定义展示配置示例](templates/poster-config.example.json)。
- [离线预览页](preview/index.html)。
- [PNG 重建脚本](scripts/build_badges.py)：可在本地调整颜色、尺寸或标签后生成。

### 单张素材示例

**深色 4K PNG**：https://raw.githubusercontent.com/MaddestAlistar/PosterBadges/main/assets/dark/4k.png  
**浅色 Dolby Vision PNG**：https://raw.githubusercontent.com/MaddestAlistar/PosterBadges/main/assets/light/dolby-vision.png  
**深色 Atmos SVG**：https://raw.githubusercontent.com/MaddestAlistar/PosterBadges/main/assets/dark/atmos.svg

请先看完整预览并根据海报背景选配色；不是所有海报软件都接受远程 PNG URL，有的需要先下载文件再上传。

## 重新生成

在电脑上安装 Python 3 与 Pillow：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_badges.py
python3 scripts/validate.py
```

新增角标或修改样式时，编辑生成脚本开头的 `BADGES` 表和 `make_png / make_svg` 参数后再生成。

## 重要说明

- 本仓库的角标均为**良友原创排版**，并非 Dolby、DTS 或任何格式标准组织的官方认证 Badge。文字仅用于客观说明媒体属性；Dolby Vision、Atmos、TrueHD、DTS、HDR10+ 等名称归其各自权利人所有。
- **不能通过文件名保证影片真的拥有所标规格**：角标应以播放器/媒体库读取的实际视频及音频流信息为准，不要对不具备该属性的片源贴标。
- 一张海报不建议叠加太多标记：可优先选择「分辨率 + HDR + 核心音轨 + 片源类型」，通常 2–4 枚即可。
- 不含媒体资源、电影海报图片或未经许可的官方图样，也**不是** Jellyfin、Emby、Radarr 可直接导入的配置文件；第三方海报工具接入需要适配。
