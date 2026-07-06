# Daily Discovery — 2026-07-06（周一）

**搜索领域:** 机械/CAD/CAM, 电气/PCB/EDA, 材料/焊接/检测
**查询数:** 21 | **候选数:** 63 (star >= 20) | **新增收录:** 1

## 新增收录

### 机械 / CAD / CAM

| MCP Server | Stars | 描述 | 收录理由 |
|---|---|---|---|
| eyfel/mcp-server-solidworks | ★131 | SolidWorks MCP server：C# COM 互操，技术制图、模型几何回读 | ★131 ≥ 100 阈值，pushed 2026-06-30（5天前），4 commits/90天，从长期不活跃恢复维护 |

## 跳过候选

### 机械 / CAD / CAM

| 仓库 | Stars | 跳过原因 |
|---|---|---|
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | ★52 | 已有的 Fusion 360 条目已覆盖(AuraFriday ★108 + faust-machines ★47)，第三实现冗余 |
| ArchimedesCrypto/fusion360-mcp-server | ★78 | 90天内仅1个 commit (README badge 更新)，代码无实质更新 |
| armpro24-blip/cad-cae-copilot | ★36 | 工作台/平台型项目，非纯 MCP server，功能与 agentcad/build123d-mcp 重叠 |
| alisamsam/Solidworks-MCP | ★58 | pushed 2026-03-23（>90天），不活跃 |
| arthurle3210/swapi-pilot-solidworks-mcp | ★24 | SolidWorks API 文档搜索工具，非完整 MCP server，star 偏低 |
| ATOI-Ming/FreeCAD-MCP | ★91 | 仅1个 README 更新 commit/90天，代码无实质更新 |
| Joelalbon/Fusion-MCP-Server | ★32 | pushed 2025-06-12 (>1年)，不活跃 |
| OctoEverywhere/mcp | ★35 | pushed 2025-07-03 (>1年)，不活跃 |
| contextform/freecad-mcp | ★90 | pushed 2025-08-15 (>10月)，不活跃 |
| thepiruthvirajan/autocad-mcp-server | ★50 | pushed 2025-07-28 (>11月)，不活跃 |
| Svetlana-DAO-LLC/cad-agent | ★26 | pushed 2026-02-17 (>4月)，不活跃 |
| sina-salim/AI-SolidWorks | ★24 | pushed 2025-04-20 (>1年)，不活跃 |

### 电气 / PCB / EDA

| 仓库 | Stars | 跳过原因 |
|---|---|---|
| embedded-society/altium-designer-mcp | ★23 | 超活跃(758 commits, pushed today)但★23过低，且 altium-mcp(★108)+eda-agent(★79)已覆盖 Altium 生态 |
| Finerestaurant/kicad-mcp-python | ★39 | pushed 2025-07-15 (>1年) |
| circuit-synth/mcp-kicad-sch-api | ★20 | pushed 2025-08-20 (>10月) |
| sibilleb/AAP-Enterprise-MCP-Server | ★30 | Ansible Automation Platform，非工程 EDA |

### 材料/焊接/检测

该领域连续多周确认 MCP 生态近乎空白。所有查询均无合格候选：
- `welding MCP server`: 0 star >= 20 候选
- `NDT MCP server`: 0 结果
- `materials MCP server`: 全部 false positive（教学材料、Three.js 材质、Blender 素材）
- `metallurgy MCP`: 0 个相关结果
- `inspection MCP server`: 全部代码/Web 检查工具，非工程检测
- `materials science MCP`: 全部 < 5 star

## 搜索效果总结

| 领域 | 查询数 | ≥20★候选 | 新增 |
|---|---|---|---|
| 机械/CAD/CAM | 9 | 27 | 1 |
| 电气/PCB/EDA | 6 | 23 | 0 |
| 材料/焊接/检测 | 6 | 13 (全 false positive) | 0 |
| **合计** | **21** | **63** | **1** |

## 关键观察

1. **eyfel/mcp-server-solidworks 复苏确认**: 该仓库从2025年不活跃状态于2026年6月下旬恢复维护，★97→★131，15 commits，结构完整（solidworks-compiler、solidworks-execution等子模块），是 SolidWorks MCP 生态的重要补充（与现有 vespo92/SolidworksMCP-TS ★197 TypeScript 实现、andrewbartels1/SolidworksMCP-python ★33 Python 实现形成三实现格局）。
2. **Fusion 360 MCP 生态仍碎片化**: 多个实现均未持续更新，JustusBraitinger (★52, 192 commits, pushed Jul 2026) 是当前最活跃的实现但已有两个条目覆盖。
3. **armpro24-blip/cad-cae-copilot** (★36, 827 commits) 令人印象深刻但属于 workbench 平台型项目，非纯 MCP server。
4. **embedded-society/altium-designer-mcp** (★23, 758 commits, Rust) 虽活跃度极高但星数过低，作为低星观察对象值得以后复查。
