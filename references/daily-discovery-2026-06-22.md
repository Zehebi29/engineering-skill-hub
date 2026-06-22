# Engineering Skill Hub — Daily Discovery
**Date**: 2026-06-22 (Monday)  
**Domains**: 机械/CAD/CAM, 电气/PCB/EDA, 材料/焊接/检测

## Search Summary

| Domain | Queries | Candidates | Added |
|--------|---------|------------|-------|
| 机械/CAD/CAM | 13 | 25 | 2 |
| 电气/PCB/EDA | 11 | 12 | 0 |
| 材料/焊接/检测 | 8 | 0 | 0 |
| **Total** | **32** | **37** | **2** |

## New Entries Added

1. **[OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)** ★158 — OpenSCAD MCP server：文本/图像生成多视图 3D 模型，CUDA 重建+参数化导出
2. **[openscad-mcp](https://github.com/quellant/openscad-mcp)** ★104 — OpenSCAD MCP server：AI 驱动 3D 建模渲染，FastMCP 实现，300+ 测试

## Key Skips

### 机械/CAD/CAM
- **camoufox-reverse-mcp** ★292 — 反检测浏览器，非 CAD/CAM（Pitfall #30: "CAM" 关键词匹配 Camoufox）
- **camofox-browser** ★279 — 同上
- **camofox-mcp** ★77 — 同上
- **esp32-cam-ai** ★27 — ESP32-CAM 硬件，非 CAD
- **zakahan/auto-slicing** ★24 — 视频切片工具，非 3D 打印切片
- **eyfel/mcp-server-solidworks** ★104 — 已收录（SolidworksMCP-TS 覆盖），不活跃 >1 年
- **ArchimedesCrypto/fusion360-mcp-server** ★78 — 已有 Fusion-360-MCP-Server (★101)，功能重叠
- **pzfreo/build123d-mcp** ★18 — Star 过低（<20），build123d 生态萌芽中，观察
- **armpro24-blip/cad-cae-copilot** ★17 — Star 过低（<20），CAD/CAE 新项目
- **bertvanbrakel/mcp-cadquery** ★16 — Star 过低
- **GLechevalier/OpenGalatea** ★14 — Star 过低，Prusa 打印机控制
- **rishigundakaram/cadquery-mcp-server** ★14 — Star 过低
- **Charleslotto/klipper-mcp** ★14 — Star 过低
- **format37/openscad-mcp** ★12 — Star 过低

### 电气/PCB/EDA
- **moltis-org/moltis** ★2747 — 通用个人 agent server，非 EDA 专用
- **mapleleavessssssss-wq/vivado-mcp** ★61 — 已在 README
- **circuit-synth/kicad-sch-api** ★40 — KiCad API 库，非 MCP server
- **Finerestaurant/kicad-mcp-python** ★37 — 已有多个 KiCad MCP 覆盖
- **timoncool/telegram-api-mcp** ★23 — Telegram bot，非 EDA
- **IntelligentElectron/universal-netlist** ★22 — Star 偏低，Cadence/Altium 网表读取
- **embedded-society/altium-designer-mcp** ★21 — Star 偏低，Altium 库管理，今日创建（太新）
- **circuit-synth/mcp-kicad-sch-api** ★20 — Star 偏低
- **gtnoble/ngspice-mcp** ★16 — Star 过低，已有 spicebridge 覆盖
- **xuio/ltspice-mcp** ★13 — Star 过低，已有 ltspice-mcp (★15) 覆盖
- **QuincySx/easyeda-agent-mcp-server** ★13 — Star 过低，已有 easyeda-copilot (★60) 覆盖

### 材料/焊接/检测
- 无候选。该领域 MCP 生态持续空白。

## Notes
- 冲突解决：与 star-sync cron (beb6907c6614) 在 README.md 上冲突，程序化合并（保留 HEAD 的更新 star 数 + 添加新条目）
- OpenSCAD MCP 生态形成双实现格局：jhacksman（多视图重建，★158）+ quellant（FastMCP 直接建模，★104）
- 材料/焊接/检测领域连续多周无新候选，该领域 MCP 生态空白
