# Daily Discovery — 2026-07-13（周一）

**搜索领域:** 机械/CAD/CAM, 电气/PCB/EDA, 材料/焊接/检测
**查询数:** 44 | **候选数:** 74 (star >= 20) | **新增收录:** 2

## 新增收录

### 社区精选 Skills

| Skill | Stars | 描述 | 收录理由 |
|-------|-------|------|---------|
| KoStard/forgecad-public-kit | ★898 | ForgeCAD agent skills: 10 SKILL.md files for parametric CAD | ★898 ≥ 100 阈值，10 个 SKILL.md 技能，pushed 2026-06-15（活跃），1295 commits，100 forks |
| HeshamFS/materials-simulation-skills | ★56 | Agent skills for computational materials science | ★56 在 20-100 区间但高度相关（计算材料科学）、活跃（pushed 2026-06-25）、8 个 SKILL.md 技能，结构完整（含测试、文档、Python 包） |

## 跳过候选

### 机械 / CAD / CAM

| 仓库 | Stars | 跳过原因 |
|------|-------|---------|
| Misterbra/fusion360-claude-ultimate | ★49 | 已有的 Fusion 360 条目已覆盖(AuraFriday ★108 + faust-machines ★47)，第三实现冗余，且 pushed 2026-04-20（约 85 天前，接近活跃度边界） |
| ajhcs/cameo-mcp-bridge | ★24 | CATIA Magic/Cameo Systems Modeler 的 SysML/UML MCP server，★24 过低，且属于系统工程/MBSE 领域非机械 CAD/CAM |
| KoStard/forgecad-public-kit | ★898 | 已收录至 Skills 表（非 MCP server） |
| Svetlana-DAO-LLC/cad-agent | ★27 | pushed 2026-02-17（>4月），不活跃，功能与 agentcad/build123d-mcp 重叠 |
| griches/bambu-mcp | ★32 | pushed 2026-03-08（>90天），另一 Bambu Lab 实现，被同作者 DMontgomery40 更全面的 mcp-3D-printer-server(★203) 覆盖 |
| asmith26/jupytercad-mcp | ★20 | pushed 2025-10-07（>6月），不活跃 |
| arthurle3210/swapi-pilot-solidworks-mcp | ★24 | SolidWorks API 文档搜索工具，非完整 MCP server |
| WhiteNightShadow/camoufox-reverse-mcp | ★346 | 反检测浏览器，非 CAD/CAM 工程 |
| redf0x1/camofox-browser | ★306 | 反检测浏览器，非 CAD/CAM 工程 |
| redf0x1/camofox-mcp | ★84 | 反检测浏览器，非 CAD/CAM 工程 |
| rzeldent/esp32-cam-ai | ★26 | ESP32 摄像头项目，非 CAD/CAM |

### 电气 / PCB / EDA

| 仓库 | Stars | 跳过原因 |
|------|-------|---------|
| embedded-society/altium-designer-mcp | ★27 | ★27 过低，且 altium-mcp(★110)+eda-agent(★86)已覆盖 Altium 生态 (从上周 ★23 增长到 ★27) |
| IntelligentElectron/universal-netlist | ★24 | Cadence/Altium 网表读取 MCP，★24 过低 |
| erebusnz/rigol-mcp | ★22 | 示波器控制 MCP（测试测量），★22 过低 |
| Arcadia-1/awesome-ams-skills | ★27 | AMS IC 设计技能集合，★27 偏低，仅 28 commits，Jekyll 网站形式而非 SKILL.md 集合 |
| nvsofts/jlcpcb-parts-mcp | ★32 | pushed 2025-04-20（>1年），不活跃 |
| ezrover/ESP32-AI-Agent-Skill | ★20 | ★20 刚好达标但 pushed 2026-04-14（约 90 天前），且 ESP32 属于嵌入式/硬件已有条目 |
| electerm/electerm | ★14468 | 终端客户端，非工程 EDA |
| remorses/spiceflow | ★164 | Web 框架，非工程 EDA |
| sibilleb/AAP-Enterprise-MCP-Server | ★30 | Ansible Automation Platform (AAP/Event-Driven Ansible)，非 Electronic Design Automation |

### 材料/焊接/检测

| 仓库 | Stars | 跳过原因 |
|------|-------|---------|
| 所有 MCP server 搜索结果 | 全部 < 20 | "inspection", "NDT", "welding", "materials science", "metallurgy" 关键词搜索结果均为软件代码检查工具、通用材料（教学材料/framework 描述）或 star 过低的项目 |
| patsnap/skills | ★25 | PatSnap 专利/工程分析官方技能集合，但其技能主要面向专利检索与分析，非材料/焊接/检测工程领域 |
| HeshamFS/materials-simulation-skills | ★56 | 已收录至 Skills 表（计算材料科学 agent skills，归入 Skills 表而非材料/焊接/检测 MCP 表） |

该领域连续多周确认 MCP 生态近乎空白。welding/NDT/metallurgy 搜索仍无合格 MCP server 候选。

## 搜索效果总结

| 领域 | 查询数 | ≥20★候选 | 新增 (Skills) |
|------|--------|---------|---------------|
| 机械/CAD/CAM | 19 | 32 | 1 (forgecad-public-kit) |
| 电气/PCB/EDA | 16 | 30 | 0 |
| 材料/焊接/检测 | 9 | 12 | 1 (materials-simulation-skills) |
| **合计** | **44** | **74** | **2** |

## 关键观察

1. **forgecad-public-kit (★898)**: 首个 JavaScript/TypeScript 参数化 CAD 的 SKILL.md 集。10 个 forgecad-* SKILL.md 覆盖模型构建、设计规格、检查、重建等完整工作流。其作者 KoStard 有 1295 commits，社区活跃（100 forks）。
2. **materials-simulation-skills (★56)**: 计算材料科学领域的 agent skill 集合，含 8 个 SKILL.md（core-numerical, simulation-workflow, verification-validation 等），结构完整（Python 包、测试、文档、CI）。★56 虽低但其领域（计算材料科学）在 Skills 表中尚无条目，填补了空白。
3. **材料/焊接/检测领域 MCP 生态仍为零**: 该领域连续多周无合格 MCP server 候选。"inspection" 关键词搜索结果被代码检查工具（Godot, Metro, Drain3, NDepend 等）严重污染。工程级的 NDT/welding MCP 仍未出现。
4. **Star 同步提醒**: 本次更新未同步现有条目的 Star 数（由周一 Star 同步 cron 处理）。如 Star 同步 cron 在本次推送前运行，git push 时可能出现冲突，需按 cron-conflict-resolution.md 处理。
