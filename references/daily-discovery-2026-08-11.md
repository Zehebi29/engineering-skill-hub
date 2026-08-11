# Daily Discovery — 2026-08-11（周二）

**⚠️ Cron 缺口报告**：2026-08-10（周一）无 daily-discovery 文件，git log 最后提交停在 08-09（周日），**周一发现任务静默失败**。已按规范将周一领域（机械/CAD/CAM、电气/PCB/EDA、材料/焊接/检测）并入本次轮换补扫。请用户检查 cron job `f2cc259c3af0` 状态（连续第二次缺口：08-04/05 曾缺失，08-06 补扫过）。

## 搜索领域（6 个 = 周二常规 3 + 周一补扫 3）
- 补扫周一：机械/CAD/CAM、电气/PCB/EDA、材料/焊接/检测
- 常规周二：航空航天/CFD、机器人/ROS、能源/电力/电池

## 执行统计
- 查询数：28（6 领域 × 3-5 关键词，含 Way D agent skill 查询）
- 候选数：205（去重后）
- API 验证：19 个候选 Individual Repo API
- 新增收录：**11**（7 Skills + 4 MCP Servers）

## 新增条目（11）

### Skills 表（7）
| 条目 | Star | 领域 | 理由 |
|------|------|------|------|
| [solidworks-automation-skill](https://github.com/wzyn20051216/solidworks-automation-skill) | 701 | 机械/CAD/CAM | ★701 远超阈值；Skill+CLI+MCP 三入口，capabilities.yaml 能力边界声明，pushed 2026-08-03 活跃 |
| [easyeda-api-skill](https://github.com/easyeda/easyeda-api-skill) | 496 | 电气/PCB/EDA | 嘉立创官方 org AI SKILL（Agent Skills 标准），WebSocket 桥接 + API 文档索引，pushed 2026-08-07 |
| [VibeCAD](https://github.com/rawwerks/VibeCAD) | 106 | 机械/CAD/CAM | ★≥100；Claude Code skills 教 CAD 工具（build123d/render-glb/gltf-transform） |
| [analog-agents](https://github.com/Arcadia-1/analog-agents) | 49 | 电气/PCB/EDA | 12 agentic skills 模拟 IC 设计；与同作者 veriloga-skills（★28 已收录）互补（Pitfall #58 正面信号）；pushed 2026-07-02 |
| [Materials-Science-Skills](https://github.com/cooleava1-gif/Materials-Science-Skills) | 35 | 材料/焊接/检测 | 材料科学研究全流程 skill（14 skills/29 材料系统/17 期刊格式），与 materials-simulation-skills 互补；pushed 2026-08-09 |
| [axi-compliance-skill](https://github.com/RuihongY/axi-compliance-skill) | 29 | 半导体/VLSI/FPGA | AXI4-Stream 合规检查，RTL 验证细分（与现有 generator/knowledge 类 skills 不重叠）；pushed 2026-05-25 |
| [fluent-cfd-skill](https://github.com/cavoiie/fluent-cfd-skill) | 21 | 航空航天/CFD | **该领域 Skills 表首个条目**；Ansys Fluent/PyFluent 工作流，收敛诊断 + MCP 安全边界；pushed 2026-06-01 |

### MCP Servers 表（4）
| 条目 | Star | 分组 | 理由 |
|------|------|------|------|
| [pypsa-mcp](https://github.com/open-energy-transition/pypsa-mcp) | 70 | 能源/电力/电池 | PyPSA 官方组织（Pitfall #56 放宽）；电力系统建模 MCP，与 PowerMCP/EnergyPlus-MCP 互补 |
| [altium-designer-mcp](https://github.com/embedded-society/altium-designer-mcp) | 36 | 电气/PCB/EDA | 第 3 次复查（★23→★31→★36）；Rust 实现（唯一），758+ commits，pushed 2026-08-10 极活跃；与 altium-mcp(Pascal)/eda-agent(Python) 3 实现互补 |
| [universal-netlist](https://github.com/IntelligentElectron/universal-netlist) | 29 | 电气/PCB/EDA | 网表读取/设计审查型 MCP（分析而非操控），Cadence/Altium/KiCad；pushed 2026-08-08 |
| [swapi-pilot-solidworks-mcp](https://github.com/arthurle3210/swapi-pilot-solidworks-mcp) | 27 | 机械/CAD/CAM | SolidWorks API 文档导航 MCP（检索 docs/examples/enums），与建模型 SolidWorks MCP 互补；pushed 2026-07-05 |

## 跳过（重点候选及原因）
- ForgeCAD/forgecad-public-kit ★916 — **已在 README**（KoStard/forgecad-public-kit，org 迁移确认：KoStard 返回 301 Moved Permanently，Pitfall #69）
- kisaragi-mochi/stackchan-mcp ★108 — 功能重叠：机器人分组已有 stack-chan ★1630（M5Stack StackChan MCP 控制），此为同主题派生实现
- Extelligence-ai/bagel ★390 — 类型不符：机器人/无人机/IoT 数据分析工具（SQL+NL 查询），非 MCP server 非 skill 集合
- NVIDIA/skills ★2843、ros-claw/rosclaw ★179 — Pitfall #64 产品/平台自带 skills，跳过
- wzyn20051216/ros-robotics-skill ★52 — pushed 2026-03-09（>90 天不活跃）+ ROS Skills 已饱和（robotics-agent-skills/ros2-engineering-skills/robotics-skills-suite 均已收录）
- alisamsam/Solidworks-MCP ★88 — 仅 2 commits 历史记录确认不活跃（此前记录 ★35）
- moellere/WireStudio ★26 — 类型模糊：硬件设计工具平台（web UI + MCP client 之一），非纯 MCP/skill
- cooleava1-gif 相关：GeoGeekLab/nature-reviewer-skills ★34 — 通用学术审稿 skills，跳过（跨学科噪音）
- BeckhamLabsLLC/kicad-jlcpcb ★22 — pushed 2026-04-20（>90 天）
- kakimochi/ros2-mcp-server ★84 — 存在但 pushed 2025-06-27（>1 年不活跃）；注意：2026-07-31 记录曾标记 404，现 API 确认存在（Search API 缓存/误判案例，Pitfall #29）
- kimimgo/viznoir ★18 — 低星观察对象（★15→★18 增长中，继续跟踪）
- muhammadanas0716/Data-Science-Projects---EDA ★80 — EDA=Exploratory Data Analysis 非电子设计自动化
- yasir-shahzad/MCP2515-CAN-Bus-Module ★40 — MCP2515 芯片硬件（Pitfall #31）

## 查询效果观察
- 机械/CAD/CAM：Way D 仍是主要来源（CAD skill 类查询产出最多候选）。SolidWorks 生态出现第 4 个实现方向（swapi-pilot 文档导航型）
- 电气/PCB/EDA：今日丰收（easyeda 官方 skill + analog-agents + altium-designer-mcp + universal-netlist），EDA Skills 生态在扩展
- 材料/焊接/检测：连续第 9 周 MCP 零候选；Way D 连续 2 周产出 skill（上周 materials-simulation-skills 后，本周 Materials-Science-Skills 收录）
- 航空航天/CFD：Skills 表首个条目（fluent-cfd-skill）；MCP 生态仍稀少
- 机器人/ROS：候选多但大部分是论文代码/模拟器/平台，MCP 生态持续 inactive 状态
- 能源/电力/电池：pypsa-mcp（官方 org）是本周亮点

## 文件状态
- commit: `ce494b8`
- push: `9345b6e..ce494b8 main -> main` 成功
- README 计数：Skills 76→83，MCP Servers 185+→189+（sync_stars 周一自动同步）
