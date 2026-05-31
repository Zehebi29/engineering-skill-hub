# Daily Discovery — 2026-05-31（周日）

## 补漏策略

周日补漏日，主要任务：
1. 补充本周缺失的周二领域（航空航天/CFD、机器人/ROS、能源/电力/电池）
2. 复查上周低星候选增长情况

## 搜索领域
- 航空航天 / CFD
- 机器人 / ROS
- 能源 / 电力 / 电池

## 查询统计

| 领域 | 查询数 | 候选数 | 新增收录 |
|------|--------|--------|----------|
| 航空航天/CFD | 12 | 3 | 0 |
| 机器人/ROS | 14 | 8 | 0 |
| 能源/电力/电池 | 10 | 0 | 0 |
| **合计** | **36** | **11** | **0** |

## 新增收录

| 仓库 | Star | 领域 | 说明 |
|------|------|------|------|
| wjc9011/COMSOL_Multiphysics_MCP | 306 | 综合资源 | COMSOL Multiphysics MCP server：AI 驱动多物理场仿真（热传导、流体、静电、固体力学），含知识库检索。Python，MIT，32 forks，活跃维护 |

## 领域观察

### 航空航天/CFD
该领域 MCP 生态仍然非常稀少。已收录的 openfoam-mcp-server（★99）和 stk-mcp（★32）仍是主力。新发现的 COMSOL_Multiphysics_MCP（★306）是通用多物理场仿真平台，涵盖 CFD 等多个物理场，归入综合资源而非航空航天专属。

低星候选：
- `knewnothing-git/ansys-mcp-server` ★23 — ANSYS MCP server（综合，非纯 CFD），last push 2025-09-14（>90 天无更新）
- `kimimgo/viznoir` ★12 — VTK 可视化 MCP（AI-Ready VTK），last push 2026-05-28（活跃但 Star 过低）

COMSOL 相关发现：
- `777gegewu/comsol-mcp` ★97 — 非官方 COMSOL MCP 学习项目，功能与 COMSOL_Multiphysics_MCP 重叠
- `Suzy-Sa/COMSOL-Multiphysics-MCP` ★22 — COMSOL MCP，Star 过低

### 机器人/ROS
该领域 MCP 生态已较成熟。ros-mcp-server（★1241）是绝对主力。本次搜索未发现新的达标候选。

关键发现：
- `nvidia-isaac/isaac_mission_dispatch` ★98 — 虽有 `mcp` topic 标签，但实际是 VDA5050 协议的 fleet mission dispatch 服务（REST API + MQTT），并非 Model Context Protocol server。**跳过**。
- `jackccrawford/reachy-mini-mcp` ★27 — Reachy Mini 机器人 MCP server，7 工具，活跃维护（pushed 2026-05-04）。Star 介于 20-100 之间，领域高度相关，但 Star 偏低（27），暂不收录，后续关注。
- `IliaLarchenko/robot_MCP` ★79 — SO-ARM100 机器人控制 MCP，但 last push 2025-08-12（>90 天无更新）
- `lpigeon/unitree-go2-mcp-server` ★79 — Unitree Go2 机器人 MCP，但 last push 2025-05-12（>1 年无更新）

### 能源/电力/电池
该领域搜索结果噪音极大（与历史记录一致）。"battery"、"solar"、"wind" 等关键词命中大量无关项目。仅有的 MCP server（PowerMCP ★143、EnergyPlus-MCP ★93）均已在 README 中。未发现新候选。

## 低星候选复查

上周（05-25 至 05-30）因 Star 过低被跳过的候选：

| 候选 | 当时 Star | 当前 Star | 最近 Push | 结论 |
|------|-----------|-----------|-----------|------|
| cadugrillo/s7-mcp-bridge | 19 | 19 | 2026-03-20 | 无增长，>90 天无更新，仍跳过 |
| gangsterke/Tia-Portal-MCP-server | 8 | 8 | 2025-10-12 | 无增长，仍跳过 |
| ChristianHinge/dicom-mcp | 95 | 96 | 2025-12-15 | 微增 1★，但 >90 天无更新，仍跳过 |
| the-momentum/fhir-mcp-server | 85 | 86 | 2025-10-23 | 微增 1★，但 >90 天无更新，仍跳过 |
| dermatologist/pyomop | 64 | 64 | 2026-05-29 | 无增长，Python 包非纯 MCP server |
| AI-FanGe/RobotArm-MCP-P340 | 34 | 34 | 2025-07-10 | 无增长，>90 天无更新，仍跳过 |

## 跳过的候选及原因

| 候选 | Star | 跳过原因 |
|------|------|----------|
| nvidia-isaac/isaac_mission_dispatch | 98 | 非 MCP server（Model Context Protocol），是 VDA5050 fleet dispatch REST API |
| 777gegewu/comsol-mcp | 97 | 功能与已收录 COMSOL_Multiphysics_MCP 重叠 |
| IliaLarchenko/robot_MCP | 79 | last push 2025-08-12（>90 天无更新） |
| lpigeon/unitree-go2-mcp-server | 79 | last push 2025-05-12（>1 年无更新） |
| jackccrawford/reachy-mini-mcp | 27 | Star 20-100 区间但偏低，暂不收录，后续关注 |
| knewnothing-git/ansys-mcp-server | 23 | Star 20-100 区间但偏低 + last push 2025-09-14（>90 天无更新） |
| Suzy-Sa/COMSOL-Multiphysics-MCP | 22 | Star 过低，功能与已收录 COMSOL_Multiphysics_MCP 重叠 |
| kimimgo/viznoir | 12 | Star < 20 |

## 统计

- 搜索查询数：36
- 去重候选数：11
- 新增收录数：1
- 低星复查数：6
- README 当前：8 Skills + 54 MCP Servers（新增 1 个 COMSOL_Multiphysics_MCP）
- Git: commit + push successful
