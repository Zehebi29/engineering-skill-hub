# 每日工程发现 — 2026-07-20（周一）

## 搜索领域
机械/CAD/CAM + 电气/PCB/EDA + 材料/焊接/检测

## 查询统计

| 领域 | 查询数 | 候选总数 | 新增收录 |
|------|--------|---------|---------|
| 机械/CAD/CAM | 5 Way B + 4 Way D | 88 | 1 (Skills) |
| 电气/PCB/EDA | 5 Way B + 3 Way D | 78 | 0 |
| 材料/焊接/检测 | 4 Way B + 3 Way D | 33 | 0 |
| **合计** | **24** | **199** | **1** |

## 新增收录

### Skills 表
- [cad-skill](https://github.com/flowful-ai/cad-skill) (★451) — Claude Code skill for CadQuery parametric 3D-printable model generation. 21 commits, pushed last week, 24 forks. Way D 搜索 (`CAD skill` 查询) 发现。大于 ★100 直接收录。

## 跳过候选及原因

### 机械/CAD/CAM — MCP Server
| 仓库 | Star | 原因 |
|------|------|------|
| ATOMI-Ming/FreeCAD-MCP | ★93 | 404 Not Found (仓库已删除) |
| armpro24-blip/cad-cae-copilot | ★40 | 工作台平台型项目，非纯 MCP server；★<100，低于收录阈值 |
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | ★53 | Fusion 360 MCP 第 3 个实现，与已有 AuraFriday ★108 和 faust-machines ★55 功能重叠 |
| ArchimedesCrypto/fusion360-mcp-server | ★80 | 仅 2 commits，最后一次代码提交超过 1 年，实际不活跃 |
| alisamsam/Solidworks-MCP | ★67 | 已有 3 个 SolidWorks MCP 实现（TS ★203, Python ★39, C# ★156） |
| blwfish/freecad-mcp | ★11 | Star 过低 |
| zackpeters93/ugs-mcp | ★3 | Star 过低 |
| jupytercad-mcp | ★20 | 不活跃（pushed >90天前） |

### 机械/CAD/CAM — Agent Skills (Way D)
| 仓库 | Star | 原因 |
|------|------|------|
| wzyn20051216/solidworks-automation-skill | ★539 | 主要是 Python 自动化工具包，非纯 agent skill 集合；agents/ 和 mcp-server/ 为辅 |
| flowful-ai/cad-skill | ★451 | ✅ 已收录 |
| VibeCAD | ★98 | 不活跃（pushed 2026-01-05，>90天） |
| delancy827/solidworks-skills | ★40 | ★<100，且已有 text-to-cad 和 forgecad-public-kit 覆盖 CAD Skills 方向 |
| delancy827/cad-skills | ★16 | Star 过低 |
| earthtojake/cad-skill | ★39 | 同作者更全面的 text-to-cad (★8364) 已收录 |
| OpticalModeler | ★21 | 光子学极细分方向，★过低 |
| almightyshui/Mechanical-AI-Skill | ★10 | Star 过低 |

### 电气/PCB/EDA — MCP Server
| 仓库 | Star | 原因 |
|------|------|------|
| Finerestaurant/kicad-mcp-python | ★39 | 不活跃（pushed 2025-07-15） |
| oaslananka/easyeda-mcp-pro | ★13 | Star 过低 |
| RFingAdam/mcp-cst-studio | ★12 | Star 过低 |
| embedded-society/altium-designer-mcp | ★27 | 活跃但 ★<20（★27），继续观察 |
| Netlist-Studio/kicad-mcp | ★11 | Star 过低 |

### 电气/PCB/EDA — Agent Skills (Way D)
| 仓库 | Star | 原因 |
|------|------|------|
| Arcadia-1/analog-agents | ★42 | ★<100；同作者已有 veriloga-skills (★24) 在 Skills 表，互补但 Star 过低 |
| Keitark/pcba-design-skills | ★6 | Star 过低 |
| nickkraakman/skidl-skills | ★13 | Star 过低 |
| Seahan1/hardware-agency-agents | ★7 | Star 过低 |

### 材料/焊接/检测
| 仓库 | Star | 原因 |
|------|------|------|
| materials-simulation-skills | ★59 | 已在 Skills 表 |
| cooleava1-gif/Materials-Science-Skills | ★29 | 主要是学术论文写作工作流，非工程材料科学；★<100 |
| Hongyu-yu/matsci-ai-skills | ★15 | Star 过低 |
| kumagallium/e4m-mcp | ★0 | Star 过低 |
| bioteam/claude-science-hpc-integrations | ★3 | 通用 HPC 技能集，非材料专精 |

## 备注
- 材料/焊接/检测领域 MCP 生态连续多周无合格候选，符合 skill 中"月度检查频率"评估
- 电气/PCB/EDA 表已非常饱和（15 个 MCP Server 条目），新候选多为低星或不活跃
- 机械/CAD/CAM 表 20 个 MCP Server 条目已覆盖主流 CAD 工具，新增空间有限
- Way D 搜索仍然是机械/CAD 方向主要发现来源（cad-skill ★451）
- 今日无 MCP Server 新增，1 个 Skills 新增
