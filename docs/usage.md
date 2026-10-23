# 海报角标排版与接入建议

1. 优先读取媒体库里的**实际媒体流**属性：宽度/高度、DV Profile / HDR 格式、音轨 codec、是否为 REMUX 等。
2. 深色海报使用 `assets/dark/`，浅色海报使用 `assets/light/`；不要在深浅版之间仅凭外观混用。
3. 角标放于海报左上或右上，保持四周安全距离；原生规格 540 × 164，建议在海报上缩放到相应比例，避免大面积覆盖人物。
4. 推荐显示顺序：**4K/1080P → Dolby Vision/HDR10+/HDR10 → Atmos/TrueHD/DTS-HD MA → REMUX/WEB-DL → HEVC/10BIT**。
5. 同类型不要同时显示互斥项，例如同一视频轨的 4K 与 1080P；真实情况下 DV 和 HDR10 可能兼容/共存，但不可直接假设双标都有效。
6. 如需高密度海报角标可使用 SVG 缩放。SVG 与 PNG 的基础样式一致，具体字体渲染受系统影响。为保证一致性，请在制作工具中自行转曲或导出位图。

## 透明图片叠加示例

网页：`<img src="./assets/dark/4k.png" alt="4K" width="135" height="41">`

其他编辑软件：先下载 PNG 再导入为贴纸图层，设置合适的透明度和坐标。

## 接入说明

`templates/poster-config.example.json` **只是跨工具示例结构**，不是 Emby、Jellyfin、MoviePoster 或其他特定平台的原生配置文件。使用前需按目标软件的 API/图层规则转换。

若需要播放器徽章配置，请查看 [良友 Apple TV 媒体徽章库](https://github.com/MaddestAlistar/liangyou-appletv-badges)；本仓库专注于**海报叠加素材**。
