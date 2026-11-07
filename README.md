# mohang-assets

墨航网站静态资源。当前资源版本为 `v1.0.1`，生产引用使用固定标签，须推送标签后再部署应用：

```text
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/logo/logo.webp
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/favicon/favicon.ico
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/fonts/home-serif.woff2
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/fonts/home-mono.woff2
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/fonts/monitor-sans.woff2
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/fonts/monitor-mono.woff2
https://cdn.jsdelivr.net/gh/guoyiwen/mohang-assets@v1.0.1/monitor/brands/openai.svg
```

## 资源

- `logo/logo.png`：2026-11-03 从当前网站 `https://www.mohang.cc/logo.png` 迁移的原始品牌图。
- `logo/logo.webp`：原图无损转换，用于网页 Logo。
- `favicon/favicon.ico`：16/32/48/64/128/256 多尺寸图标。
- `favicon/favicon-32.png`、`favicon/favicon-192.png`：原图等比例缩放并居中填充，未裁剪或拉伸。
- `fonts/home-serif.woff2`：现有首页 Noto Serif SC 字体，600 字重；附 `NotoSerifSC-OFL.txt`。
- `fonts/home-mono.woff2`：现有首页 Geist Mono 可变字体，100–900 字重；附 `Geist-OFL.txt`。
- `fonts/monitor-sans.woff2`、`fonts/monitor-mono.woff2`：监控页 Geist / Geist Mono 可变字体，100–900 字重；遵循 `fonts/Geist-OFL.txt`。
- `monitor/brands/`：监控页使用的 Claude、OpenAI、Gemini、Grok、DeepSeek、Kimi、GLM 平台图标，从应用本次新增静态资源原样同步。
- `monitor/lucide-LICENSE`：监控页内联 Lucide 图标的许可证副本。

没有墨航矢量源文件，因此未将旧 Sub2API SVG 当成品牌 Logo，也未把 PNG 伪装成 SVG。没有独立的 regular/medium/bold 字体源文件，因此不创建占位字体。

## 更新

1. 更新资源。图标可通过 `python scripts/build_icons.py` 从原始 PNG 重建，需要 Pillow。
2. 检查内容、尺寸以及字体许可证，提交并推送。
3. 发布新标签（下次例如 `v1.0.2`），不要移动或覆盖旧标签。
4. 确认对应 CDN 地址可用后，更新应用内的版本引用。

字体遵循各自附带的 SIL OFL 许可证；这些许可证不覆盖品牌图标。第三方平台图标及商标归各自权利人所有。

## 版本记录

- `v1.0.1`（2026-11-07）：新增监控页的 2 个字体、7 个平台图标及 Lucide 许可证；保留 `v1.0.0` 所有资源路径。
- `v1.0.0`：墨航品牌图片、站点图标与首页字体。
