# Daily Discovery — 2026-07-05 (周日)

## 搜索类型
补漏 — 本周缺失领域搜索 + 低星候选复查

## 本周覆盖状态（2026-06-29 ~ 2026-07-05）

| 日期 | 星期 | 领域 | 状态 |
|------|------|------|------|
| 06-29 | 周一 | 机械/CAD/CAM, 电气/PCB/EDA, 材料/焊接/检测 | ❌ 缺失 |
| 06-30 | 周二 | 航空航天/CFD, 机器人/ROS, 能源/电力/电池 | ✅ Covered |
| 07-01 | 周三 | 土木/结构/BIM, 化工/流程模拟, 半导体/VLSI/FPGA | ❌ 缺失 |
| 07-02 | 周四 | 油藏/石油/地质, 汽车/自动驾驶, 船舶/海洋工程 | ✅ Covered |
| 07-03 | 周五 | 工业制造/QA, 生物医学/医疗, 环境/水利/污染 | ✅ Covered |
| 07-04 | 周六 | 综合扫描（awesome-mcp-servers） | ✅ Covered |

**需补漏领域**: 机械/CAD/CAM, 电气/PCB/EDA, 材料/焊接/检测, 土木/结构/BIM, 化工/流程模拟, 半导体/VLSI/FPGA

## 搜索统计
- **总查询数**: 30+ (含 all domains + low-star review)
- **总候选数**: ~100+
- **新增收录**: 2

## 新增收录

### 电气 / PCB / EDA

| Repo | Star | 描述 |
|------|------|------|
| [altium-designer-mcp](https://github.com/embedded-society/altium-designer-mcp) | 23 | Altium Designer 元器件库管理 MCP server（Rust 实现），728 提交，5 小时前推送，持续活跃。聚焦元器件库管理（原理图符号、PCB 封装），与现有 coffeenmusic/altium-mcp（原理图/PCB/库通用）和 salitronic/eda-agent（200+ 工具全流程）形成互补。 |

### 综合资源

| Repo | Star | 描述 |
|------|------|------|
| [cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot) | 36 | CAD/CAE 智能体工作台：AI 原生 build123d/OpenCASCADE 参数化建模、网格划分、仿真求解，含 MCP server 工具。827 提交，4 天前推送，31 branches。跨 CAD（机械）+ CAE（仿真）多领域平台 → 归入综合资源。 |

## 跳过的候选

### 机械 / CAD / CAM

| Repo | Star | 跳过原因 |
|------|------|----------|
| eyfel/mcp-server-solidworks | 129 | SolidPilot — SolidWorks MCP, 4 天前活跃（从之前的不活跃恢复）。但已有 2 个 SolidWorks 条目在 README（vespo92/SolidworksMCP-TS 和 andrewbartels1/SolidworksMCP-python），功能重叠，不收录 |
| ATOI-Ming/FreeCAD-MCP | 91 | 404 Not Found（之前已知删除） |
| ArchimedesCrypto/fusion360-mcp-server | 78 | 仅 2 commits，代码 last year 未更新。README badge 2 周前更新（非代码活动）→ 不活跃 |
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | 52 | Fusion 360 MCP，已有 2 个 Fusion 360 条目，功能重叠 |
| Misterbra/fusion360-claude-ultimate | 48 | Fusion 360，同上，功能重叠 |
| LuDattilo/revit-mcp-server | 25 | latest commit "3 months ago"， >90 天不活跃。推入由非代码活动引起 |
| arthurle3210/swapi-pilot-solidworks-mcp | 24 | SolidWorks API 文档搜索 MCP，非参数化建模，且已有 2 个 SolidWorks 条目 |
| OctoEverywhere/mcp | 34 | 3D 打印，pushed 2025-07-03，>1 年不活跃 |
| asmith26/jupytercad-mcp | 19 | Star 过低 (<20) |
| blwfish/freecad-mcp | 10 | Star 过低，已有 4 个 FreeCAD 条目 |
| all others | <20 | Star 过低或非工程工具 |

### 电气 / PCB / EDA

| Repo | Star | 跳过原因 |
|------|------|----------|
| oaslananka/kicad-mcp | 16 | Star 过低 (<20)。KiCad production-grade MCP，值得观察 |
| Finerestaurant/kicad-mcp-python | 39 | pushed 2025-07-15，不活跃 |
| circuit-synth/mcp-kicad-sch-api | 20 | pushed 2025-08-20，不活跃 |
| timoncool/telegram-api-mcp | 23 | Telegram Bot API，非 EDA |
| kicad-mcp (blwfish) | 4 | Star 过低 |
| all others | <23 | Star 过低或非工程工具 |

### 材料/焊接/检测
- **0 合格候选**。materials/welding/NDT 查询全部返回低星非工程工具或通用项目

### 土木 / 结构 / BIM
| Repo | Star | 跳过原因 |
|------|------|----------|
| LuDattilo/revit-mcp-server | 25 | 3 个月前推送，不活跃 |
| Demolinator/revit-mcp-server | 18 | Star 过低 |
| schauh11/revit-mcp-server | 18 | Star 过低 |
| 其余 | <18 | 低星或不相关 |

### 化工/流程模拟 / 半导体/VLSI/FPGA
- **0 合格候选**。两个领域 MCP 生态持续空白

## 低星候选复查

从 07-03, 07-04, 06-30 近日 discovery 文件中提取 7 个候选，全部低星无增长：

| 仓库 | 上次 Star | 当前 Star | 变化 | 判断 |
|------|----------|----------|------|------|
| Zhonghao1995/agentic-swmm-workflow | 16 | 16 | 0 | 持续观察（活跃，449 commits） |
| ksterx/srunx | 15 | 15 | 0 | 持续观察（566 commits，SLURM HPC） |
| kimimgo/viznoir | 15 | 15 | 0 | 持续观察（289 commits，VTK 可视化） |
| lynnlangit/precision-medicine-mcp | 19 | 19 | 0 | 差 1★ 达门槛，活跃（pushed 06-24），下周优先复查 |
| kvgork/gazebo-mcp | 16 | 16 | 0 | 活跃（pushed 07-04），Gazebo 仿真唯一候选 |
| asmith26/jupytercad-mcp | 19 | 19 | 0 | 不活跃（pushed 2025-10-07） |
| nickzren/opentargets-mcp | 19 | 19 | 0 | pushed 2026-05-15，接近活跃边界 |

## 备注
- **eyfel/mcp-server-solidworks** 从之前的不活跃状态恢复（129★，4 天前推送），但 SolidWorks MCP 已有 2 个条目覆盖，不因复苏再收录
- **embedded-society/altium-designer-mcp** 是本期最佳发现：728 提交，Rust 实现，专注元器件库管理细分方向，与现有 Altium 条目形成差异化
- **cad-cae-copilot** 作为跨 CAD/CAE 综合平台放入综合资源分组
- 低星候选中 **precision-medicine-mcp（★19）** 和 **gazebo-mcp（★16）** 距离门槛最近且活跃，下周优先复查
- MCP 生态持续稳定增长但增速放缓：本周补漏 2 个新增，主要来自活跃新项目而非既有条目复苏

## README 当前状态
- 原创 Skills: 3
- 社区精选 Skills: 6
- 社区精选 MCP Servers: ~91（含本次新增 2 条）
