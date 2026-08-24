# Daily Discovery — 2026-08-24（周一）

## ⚠️ CRON 缺口报告（严重）

**08-18（周二）~ 08-23（周日）连续 6 天无 daily-discovery 记录，git log 最后提交停在 08-17。**
- 缺失文件：08-18, 08-19, 08-20, 08-21, 08-22, 08-23 全部缺失
- 最后提交：`00de5ca`（08-17 的 star sync），之后 cron 静默失败，无任何告警
- **用户需检查 cron job f2cc259c3af0 状态**（08-04/05 曾发生过同类静默失败）
- 本次已按优先级补扫：机器人/ROS、半导体/VLSI/FPGA（高）> 能源/电力、土木/BIM、化工、航空航天/CFD（中）> 生物医学/医疗、油藏、船舶、汽车、环境（低/月度）
- 周六/周日任务（awesome-mcp-servers 综合扫描 + 补漏）也已降级执行：
  - awesome-mcp-servers 行数 3822（08-15 为 3821，增量 1 行 <10）→ 跳过全量扫描（Pitfall #44）

## 执行背景

- 常规周一轮换：机械/CAD/CAM + 电气/PCB/EDA + 材料/焊接/检测
- 补扫 6 天缺失领域（见上）
- 共 47 个查询（Way B + Way D），间隔 2s

## 新增收录：2

| 仓库 | Star | 领域 | 说明 |
|------|------|------|------|
| [zhoushoujianwork/easyeda-agent](https://github.com/zhoushoujianwork/easyeda-agent) | 288 | 电气/PCB/EDA（Skills 表） | EasyEDA Pro 自动化：typed 原理图/PCB 动作，CLI / Agent Skill / stdio MCP 三形态融合，914 commits/44 tags/7 小时前提交极活跃，与官方 easyeda-api-skill(★545) 互补。browser 验证通过 |
| [Extelligence-ai/bagel](https://github.com/Extelligence-ai/bagel) | 395 | 机器人/ROS（MCP 组） | 机器人/无人机/IoT 数据查询 MCP server：自然语言查询 + 智能边缘数据缩减管线，654 commits/40 branches，5 天前提交，含 .claude-plugin + src/ 真实 MCP 实现 |

## 顺带修复

- **Skills 表 11 处历史 star 排序违规**（918→977、335→337、213→222、51→53、35→46、26→28/29/39、26→27/33、22→24 等）整表稳定重排 + CJK 重对齐（Pitfall #73），`git diff -w` = 12 对纯换位 + 2 新行 + 1 空行，零内容丢失
- **机器人组 reflow 修复**：bagel 来源列宽度恰等于 maxw 导致 pad=0 `)|` 粘连，改用 maxw+1 分隔空格逻辑

## 跳过（browser/API 验证后）

| 仓库 | Star | 原因 |
|------|------|------|
| kisaragi-mochi/stackchan-mcp | 114 | 真实 MCP（192 commits/36 tags/昨天提交），但 StackChan 平台已有 stack-chan(★1654, JavaScript 原版) 收录，同平台第 2 实现功能重叠；且 M5Stack 消费级机器人套件工程属性弱 → 跳过 |
| telekinesis-ai/telekinesis-examples | 72 | Telekinesis Agentic OS（通用机器人平台）的 examples 配套仓库，非独立 SKILL.md 集合（Pitfall #64 变体 3 平台型） |
| Impertio-Studio/Blender-Bonsai-ifcOpenshell-Sverchok-Claude-Skill-Package | 33 | 73 个 AEC/BIM Claude skills 真实，但默认分支最后提交 5 个月前（pushed_at 07-08 被非代码事件抬高，Pitfall #33）>90 天不活跃 |
| brack101/AspenPlus-MCP-Server | 32 | 复苏候补复查：pushed 仍 2025-10-09 >300 天不活跃，继续候补 |
| heyixuan2/bambu-studio-ai | 87 | 复苏候补复查：★85→87 增长但 pushed 07-03 仍不活跃（默认分支提交约 3 个月前） |
| NVIDIA-Omniverse/usd-convert-cad | 19 | 复查：★19 未跨线，pushed 07-30 活跃，继续观察 |
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | 54 | 复查：Fusion 已有 AuraFriday+faust-machines 两条目，继续观察 |
| zxkmm/kicad-footprint-generate | 28 | 复查：pushed 08-09 活跃但单用途，KiCad 生态 kicad-happy 覆盖，继续观察 |
| hanhuark/mechanical-engineering-research-skill | 15 | 复查：★15 未跨线但 pushed 08-23 极活跃，继续观察 |
| NeonGlay/inventor-mcp | 18 | 复查：★18 未跨线，继续观察 |
| lcapossio/hdldiagZero | 17 | 复查：★17 接近门槛，继续观察 |
| kimimgo/viznoir | 17 | 复查：★15→17 增长，仍 <20，继续观察 |
| ffffffffelix/automotive-functional-safety | 6 | **Individual Repo API 确认 404（第三次复查）**，从候选池移除，更新 deleted-repos.md |

## 跳过（API 初筛，未 browser）

- **机械/CAD/CAM**：blwfish/freecad-mcp(★32, FreeCAD 第 5+ 实现生态饱和判例)、Svetlana-DAO-LLC/cad-agent(★32, pushed 02-17 不活跃)、ppak10/RocketSmith(★21, hobby 非工程)、almightyshui/Mechanical-AI-Skill(★19, <20)、rishigundakaram/cadquery-mcp-server(★18, >1年不活跃)、bertvanbrakel/mcp-cadquery(★17, >1年不活跃)、pzfreo/cadgenbench-build123d(★5, 工具管线非独立skill)、fa-mc/vibe-cading(★5, <20)
- **电气/PCB/EDA**：moellere/WireStudio(★26, 平台型判例 08-17)、circuit-synth/kicad-sch-api(★50, API 库)、Finerestaurant/kicad-mcp-python(★40, 不活跃)、flaco-source/altium-mcp(★8, <20 + Altium 饱和)、nickkraakman/skidl-skills(★16, 观察)、Seahan1/hardware-agency-agents(★9, 观察)、2456018331lby-dev/embedded-engineering-skill(★10, <20)
- **材料/焊接/检测**（连续第 10 周零合格候选）：确认月度频率；patsnap/skills(★33, Pitfall #64 变体2)、GeoGeekLab/nature-reviewer-skills(★35, 通用学术非工程)
- **机器人/ROS**：NVIDIA/skills(★3080, Pitfall #64 变体1 公司产品目录)、huangjunsen0406/py-xiaozhi(★3450, 通用AI助手)、Genesis-Embodied-AI/RoboGen(★1223, ICLR研究框架)、ros-claw/rosclaw(★186, Pitfall #64 变体3 平台型)、nvidia-isaac/isaac_mission_dispatch(★104, Pitfall #36 topic误导)、manykarim/rf-mcp(★113, Pitfall #38 Robot Framework)、RobotLabLTH/SkiROS2(★232, 学术框架非MCP/skill)、wzyn20051216/ros-robotics-skill(★57, pushed 03-09 不活跃)、lpigeon/ros-skill(★26, pushed 02-27 不活跃)、varun29ankuS/shodh-memory(★275, 通用记忆工具)、Extelligence-ai 其他、verlab/hero_common(★75, G-code语言研究框架)
- **半导体/VLSI/FPGA**：Akashtailor-exe/30-days-of-verilog(★75, 学习repo)、ItzzInfinity/100-days-of-RTL(★39, 学习repo)、ic-star-tech/ccfoundry-agent-kit(★24, Pitfall #64 变体5)、londey/claude-skill-verilog(★18, 观察)、LNC0831/oh-my-fpga(★16, 观察)、simtenHQ/simten(★9, HDL工具链非MCP)
- **能源/电力/电池**：全部通用噪音（mcp-client-for-ollama ★805、innoshop ★655、atlas-mcp-server ★476、story-ui ★197、ux-writing-skill ★154 等均非工程）；aloth/PowerSkills(★30, PowerShell 工具包非能源领域)；Power-Agent/PowerSkills 已在 README ★61
- **土木/结构/BIM**：mcp-servers-for-revit 系列(★455/216/57, Revit 饱和判例)、Sam-AEC/aec-model-bridge(★50, Revit 饱和)、shuotao/REVIT_MCP_study(★101, Pitfall #40 教程)、DTDucas/chm-converter(★99, Pitfall #41 topics误导)、LuDattilo/revit-mcp-server(★48, Pitfall #33 pushed不可靠)、Soljourner/claude-engineering-skills(★60, 9月不活跃)
- **化工/流程模拟**：retentioneering-tools(★914, Pitfall 已记录 process mining 噪音)、vorobjewsen30-max/ansys-mcp-server(★8, 观察)、EPEL-SNU/Aspen_Plus_MCP(★6, 官方org观察)、jskherman/engg-skills(★6)、moldsim/moldsim-mcp(★6)、nckugese/Aspen_Co-pilot(★17)
- **航空航天/CFD**：sandraschi/freecad-mcp(★20, FreeCAD 饱和判例延伸)、isabecurtis023-lang/HarnessFOAM(★12, <20)、Ouscar-ou/AutoStar(★7, <20)、HNUVV/openfoam-CFD-codexskill(★6, <20)、hooyao/vortex-funnel-gen(★5, <20)
- **生物医学/医疗**（月度检查）：BioTender-max/awesome-bio-agent-skills(★160, awesome list 类型)、boheling/skillbench(★44, 通用benchmark)、yiyanli123/biorender-mechanism-figures-skill(★18, 观察)、chenxihuang1028-a11y/risk-management-specialist(★5, ISO 14971 观察)
- **油藏/石油/地质**（连续第 10 周零候选）：petroleum MCP 全部 <3★
- **汽车/自动驾驶**：ffffffffelix 404（见上）、duonghvu/automotive-syseng(★5, 观察)
- **船舶/海洋工程**：0 个 ★≥5 候选（连续第 10 周）
- **环境/水利/污染**：j03rul4nd/digital-twin-water(★7, demo 非 MCP)

## 观察/复查清单（下次补漏优先）

- NVIDIA-Omniverse/usd-convert-cad ★19（pushed 07-30 活跃，接近门槛）
- hanhuark/mechanical-engineering-research-skill ★15（pushed 08-23 极活跃）
- NeonGlay/inventor-mcp ★18、lcapossio/hdldiagZero ★17、kimimgo/viznoir ★17（15→17 增长）、lcapossio/fpgaZeroMCP ★5
- heyixuan2/bambu-studio-ai ★87（★85→87 增长，复苏候补）
- brack101/AspenPlus-MCP-Server ★32（复苏候补，>300 天不活跃）
- kisaragi-mochi/stackchan-mcp ★114（若 StackChan 生态继续分化可再评估）
- beiming183-cloud/AutoCAD-skills ★6（GB/T 国标方向，4→6 增长）、MP-AI-20/mechanical-engineering-skills ★5（647 模块）

## deleted-repos.md 更新

- ffffffffelix/automotive-functional-safety — 第三次确认 404（08-13 首次、本次 08-24），从候选池移除

## 统计

- 查询数：47（14 领域）| API 验证：21 | browser 验证：4
- 新增收录：2（Skills 1 + MCP 1）
- README 当前：社区精选 Skills 43、MCP Servers 104（+2，其中 easyeda-agent 入 Skills 表）

## 查询效果观察

- 机械/CAD/CAM：MCP 表饱和（FreeCAD 第 5+ 判例再次应用）；新方向是"三形态融合"（Skill+CLI+MCP），solidworks-automation-skill 同模式先例
- 电气/PCB/EDA：EasyEDA 生态 4 实现（官方 api-skill + copilot + mcp-pro + 本次 easyeda-agent 三形态差异化收录）
- 机器人/ROS：补扫有收获（bagel ★395 是 6 天缺失期间增长的高星 MCP）；多数候选不活跃或平台型
- 材料/焊接/检测、油藏、船舶、汽车：连续第 10 周零合格候选，维持月度频率
- 周六任务降级：awesome-mcp-servers 连续第 4 周零增量（3821→3822 仅 +1 行），增量 <10 行跳过全量扫描
