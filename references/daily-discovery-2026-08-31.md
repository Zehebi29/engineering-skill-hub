# Daily Discovery — 2026-08-31（周一）

## ⚠️ CRON 缺口报告（严重 — 连续第 2 轮 6 天缺失）

**08-25（周二）~ 08-30（周日）连续 6 天无 daily-discovery 记录。**
- 缺失文件：08-25, 08-26, 08-27, 08-28, 08-29, 08-30 全部缺失
- 最后提交：`df9ed63`（08-24 discovery）→ 之后仅今天 `7bdd0a0`（star sync）运行
- **这是 08-18~23 之后第二次连续 6 天静默失败**（08-04/05 也曾缺失两天）。cron job f2cc259c3af0 反复间歇性失效，无告警。**用户必须检查 job 状态**（PM2/cron 服务日志），建议加失败告警机制
- 本次已按优先级补扫：机器人/ROS、半导体/VLSI/FPGA（高）> 电气/PCB/EDA（今日常规）> 材料/焊接/检测（今日常规）
- 周六任务降级执行：awesome-mcp-servers 行数 **3937**（08-24 为 3822，增量 +115 >50）→ 本应全量 section 扫描，因时间约束以 API 初筛 + browser 验证替代（wave-mcp/mcp-cst-studio 等新条目已覆盖主要增量方向）

## 执行背景

- 常规周一轮换：机械/CAD/CAM + 电气/PCB/EDA + 材料/焊接/检测
- 补扫缺失领域（高优先级）：机器人/ROS、半导体/VLSI/FPGA
- 共 39 个查询（Way B + Way D），间隔 2s

## 新增收录：5（Skills 2 + MCP 3）

| 仓库 | Star | 领域 | 说明 |
|------|------|------|------|
| [Tencent/wave-mcp](https://github.com/Tencent/wave-mcp) | 120 | 半导体/VLSI/FPGA（MCP 组） | RTL 波形调试 MCP server（腾讯蓬莱实验室）：FST 波形 + SystemVerilog 网表分析，27 工具含预仿真静态分析、X 态根因追踪，MIT 免 License，生产级验证（OpenTitan/香山 225 万信号、310 万工具调用）。1 个月 120★，极活跃。与 vivado-mcp(综合)/pyslang-mcp(解析)/xverif(验证) 互补，新增波形调试子方向 |
| [Cai-aa/CAD-Agent-Hub](https://github.com/Cai-aa/CAD-Agent-Hub) | 23 | 机械/CAD/CAM（MCP 组） | **README 首个 CATIA MCP 条目**：多 CAD MCP server 合集（CATIA V5 建模/原生分析 + SolidWorks/NX 状态化 MCP + Fusion Electronics 写桥 + ANSYS Workbench skill）。CATIA V5R21 兼容修复由外部 contributor PR 合入，2 contributors，昨日提交极活跃 |
| [RFingAdam/mcp-cst-studio](https://github.com/RFingAdam/mcp-cst-studio) | 21 | 电气/PCB/EDA（MCP 组） | CST Studio Suite MCP server：天线设计、RF/微波仿真、PCB 布局，20 类工具（几何/材料/端口/网格/求解器/天线模板/PCB），Connected（Windows 直连）+ Offline（VBA 生成任意 OS）双模式，VBA 安全校验，AGPL-3.0 + tests + CLA。CST 为全新工具覆盖 |
| [NVIDIA-Omniverse/usd-convert-cad](https://github.com/NVIDIA-Omniverse/usd-convert-cad) | 24 | 机械/CAD/CAM（Skills 表） | CAD→OpenUSD 转换 agent skill（NVIDIA-Omniverse 官方）：pip 安装 usd-convert-cad 包，STEP/IGES 转 USD/USDA/USDC，多平台 .claude/.codex/.cursor/.agent SKILL.md 工作流契约，无需 Omniverse Kit。08-24 观察清单 ★19 → 24 跨过阈值 |
| [lcapossio/hdldiagZero](https://github.com/lcapossio/hdldiagZero) | 20 | 半导体/VLSI/FPGA（Skills 表） | Claude Code agent skill：HDL/RTL/SoC 架构描述→SVG 框图，CDC 分块着色、快照回归校验，SKILL.md+plugin+CI+10 tags 结构完整。08-24 观察清单 ★17 → 20 跨过阈值，填补 Skills 表 HDL 可视化空白 |

## 顺带修复

- **Skills 表 + 4 个 MCP 表块 star 排序违规整表重排**（Pitfall #73）：
  - Skills 表：SciAgent-Skills/easyeda-agent、DDC/materials-simulation、tia-portal/cad-skills 等 6 处
  - 机械/CAD/CAM：mcp-3D-printer/freecad_mcp 等 4 处
  - 电气/PCB/EDA：jlcmcp/eda-agent/altium/easyeda-copilot/kicad-mcp-pro/easyeda-mcp-pro 6 处（历史积压最严重）
  - 土木/BIM 4 处、嵌入式 2 处、生物医学 6 处、综合资源 2 处（本轮顺带全部清零）
- 半导体组 pyslang-mcp 行错位（孤立空行 + 未对齐）修复
- `<summary>` 计数更新为真实值：Skills 45 个、MCP Servers 107 个（原 76/185+ 已严重过时）
- 全文件验证：License 节后 0 pipe 行、0 `)|` 粘连、0 双管道坍缩、全表块 order check 通过、`git diff -w` 无内容丢失（仅 5 新行 + 纯换位）

## 跳过（browser/API 验证后）

| 仓库 | Star | 原因 |
|------|------|------|
| vibeic/vibe-ic | 21 | AI-agent 自生成工作区（4,124 commits、19 分钟前提交、commit message 为 agent 消费设计），结构混乱非干净 MCP 产品，质量存疑 → 观察 |
| omnilink-tech/omnisim | 91 | 机器人仿真器平台（HTTP/JSON + MCP 控制），Pitfall #64 变体3 平台型（同 rosclaw 判例）→ 观察 |
| telekinesis-ai/telekinesis-examples | 81 | 08-24 已判平台型 examples 仓库，复查确认无变化（README 首段仍为 "Telekinesis Agentic OS" examples） |
| kisaragi-mochi/stackchan-mcp | 124 | ★114→124 增长，但 StackChan 平台已有 stack-chan(★1667) 收录，同平台第 2 实现重叠（08-24 同判） |
| ArchimedesCrypto/fusion360-mcp-server | 82 | Fusion 已有 AuraFriday+faust-machines 两条目，pushed 06-19 渐不活跃 → 继续观察 |
| ForgeCAD/forgecad-public-kit | 926 | Pitfall #69：ForgeCAD org = KoStard 已收录仓库（同 star 同描述），org 迁移别名 |
| alisamsam/Solidworks-MCP | 102 | SolidWorks 5 条目饱和；pushed 03-23 >150 天不活跃 |
| NVIDIA/skills | 3154 | Pitfall #64 变体1 公司产品目录 |
| NVlabs/ASPIRE | 105 | NVIDIA 研究框架（技能发现研究，非 SKILL.md 集合/MCP），同 RoboGen 判例 |
| microsoft/Resource2Skill | 508 | 通用多模态资源→skill 蒸馏研究框架，非工程领域专用 |
| earthtojake/step.parts | 343 | STEP 零件库（非 MCP/skill，类型不符） |
| ros-claw/rosclaw | 190 | Pitfall #64 变体3 平台型（08-24 已判） |
| manykarim/rf-mcp | 113 | Pitfall #38 Robot Framework 非物理机器人 |
| kakimochi/ros2-mcp-server | 84 | pushed 2025-06-27 >1 年不活跃（复苏候补复查无变化） |
| IliaLarchenko/robot_MCP | 83 | pushed 2025-08-12 >1 年不活跃 |
| AI-FanGe/RobotArm-MCP-P340 | 36 | pushed 2025-07-10 不活跃（07-31 曾 404，Search API 缓存脏数据复现） |
| ATOMI-Ming/FreeCAD-MCP | 97 | FreeCAD 生态饱和判例（第 5+ 实现，08-17 确立） |
| blwfish/freecad-mcp | 35 | 同上（第 5+ 实现） |
| patsnap/skills | 35 | Pitfall #64 变体2 公司数据驱动 |
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | 55 | Fusion 2 条目饱和 + ★52→55 仅微增，继续观察 |
| Soljourner/claude-engineering-skills | 62 | 9 个月不活跃（08-24 已判） |
| Moellere/WireStudio | 26 | 平台型判例（08-24 已判） |
| louistrue/ifcx-mcp | 25 | IFC5/IFCX 编辑 MCP，pushed 04-12 >4 个月不活跃；ifc-lite 已覆盖 IFC 生态 |
| Arcadia-1/awesome-ams-skills | 31 | awesome list 类型（非 skill 集合本身） |
| 其余 | — | 低星观察/通用噪音/类型不符（详见候选池 /tmp/candidates_20260831.json） |

## 观察/复查清单（下次补漏优先）

- vibeic/vibe-ic ★21（极活跃但结构存疑，若整理为正式 MCP 产品可收录）
- omnilink-tech/omnisim ★91（仿真器平台，若 MCP 成为一等公民可再评估）
- kimimgo/viznoir ★17（pushed 08-31 恢复极活跃，接近门槛）
- NeonGlay/inventor-mcp ★19（★18→19，接近门槛）
- hanhuark/mechanical-engineering-research-skill ★15（pushed 08-29 极活跃）
- tanishqbhattad/rhino-mcp ★17（Rhino 8 MCP，115 工具，pushed 08-20 活跃）
- DrYe1109/MS-MCP ★12（BIOVIA Materials Studio 材料仿真 MCP，新方向）
- zackpeters93/ugs-mcp ★5（CNC/Universal GCode Sender MCP，新方向）
- heyixuan2/bambu-studio-ai ★91（★87→91 增长，pushed 07-03 仍不活跃）
- brack101/AspenPlus-MCP-Server ★32（>300 天不活跃复苏候补）
- lcapossio/fpgaZeroMCP ★5、LNC0831/oh-my-fpga ★17、najaeda/naja-scope ★15、lhx66/RTL-Auto-sim-verify-skills ★11、Aryaman9999/open-verifier ★6（半导体低星观察）

## 统计

- 查询数：39（5 领域）| API 验证：21 | browser 验证：6
- 新增收录：5（Skills 2 + MCP 3）
- README 当前：社区精选 Skills 45、MCP Servers 107（+5）
- 全 README star 排序违规：0（本轮清零）

## 查询效果观察

- 半导体/VLSI/FPGA：补扫收获最大（wave-mcp ★120 腾讯官方 + hdldiagZero 跨线）——该领域 MCP 生态在验证/调试方向扩张（xverif→wave-mcp）
- 机械/CAD/CAM：CATIA 首次出现 MCP（CAD-Agent-Hub），此前完全空白；SolidWorks/FreeCAD/Fusion 饱和判例继续生效
- 电气/PCB/EDA：CST Studio（EM 仿真）新工具覆盖，与 ansys-aedt-mcp 形成电磁仿真双实现
- 机器人/ROS：无新增（平台型/不活跃为主）；omnisim ★91 值得跟踪
- 材料/焊接/检测：连续第 11 周零合格候选，维持月度频率
- 周六 awesome-mcp-servers 增量 +115 行（4 周零增后回升），下周六需全量 section 扫描
