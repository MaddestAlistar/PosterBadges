# 良友影视海报角标库 · PosterBadges

[← 良友资源中心](https://maddestalistar.github.io/LiangYou-ResourceHub/) · 2026-10-23

首批 **12 种技术标签 × 深浅两套样式**。透明 PNG 便于影视海报直接叠加，SVG 矢量版适合无损缩放。

## 角标分类
4K、1080P、HDR10、HDR10+、Dolby Vision、Atmos、TrueHD、DTS-HD MA、HEVC、REMUX、WEB-DL、10BIT。

- [深色版 PNG / SVG](assets/dark/)：深底和发光边缘。
- [浅色版 PNG / SVG](assets/light/)：亮底和克制的彩色标识。
- [在线图文预览](preview/index.html)（GitHub 上可直接查看 HTML 文件；如启用 GitHub Pages 则可预览交互页面）。
- [全部标签及颜色定义](badges.json)。

**PNG 输出尺寸 320×100 px，四周带透明 Alpha；高清制作用同名 SVG。** 可在 Photoshop、Canva、影像海报工具里作为叠加图层。需要重生成 PNG，可运行 `python3 -m pip install Pillow`，然后 `python3 scripts/build_png.py`；不必上传自己设备的字体文件。

此库角标为**良友原创视觉样式**，文字仅描述常见媒体格式，并非 Dolby、DTS 等第三方厂商的官方商标徽章或质量认证。使用前先核实影片技术参数，勿因文件名推断真实内容。
