# Daily Discovery — 2026-08-17（周一）

## 执行背景
- 本周无新缺口：08-10（周一）已由 08-11 补扫，08-14（周五）已由 08-15 补扫，08-16 周日确认 15 领域全覆盖
- 常规周一轮换：机械/CAD/CAM + 电气/PCB/EDA + 材料/焊接/检测
- 共 35 个查询（Way B MCP 20 + Way D agent skill 15），间隔 2s

## 新增收录：1（MCP Servers）

| 仓库 | Star | 领域 | 说明 |
|------|------|------|------|
| [U-C4N/Autocad-MCP](https://github.com/U-C4N/Autocad-MCP) | 53 | 机械/CAD/CAM | 生产级 AutoCAD MCP server：122 工具，双引擎（实时 COM + 无头 ezdxf，无需运行中 AutoCAD），ISO GD&T 尺寸公差校验；50 commits / v1.5.1 / 16 forks / 每周提交 / 对抗性安全审计。与已有 Easy-MCP-AutoCad(★241) 架构互补，插入 SolidworksMCP-python(★60) 之后 |

## 顺带修复
- **机械/CAD/CAM 表块 6 处历史 star 排序违规**（Easy-MCP-AutoCad 241 排在 freecad_mcp 218 后等）整表稳定重排 + CJK 重对齐（Pitfall #73），`git diff -w` = 1 新行 + 6 对纯换位，零内容丢失
- **deleted-repos.md 更新**：ATOMI-Ming/FreeCAD-MCP 复苏确认存在（05-25/07-27 两度 404 记录 → 08-17 Individual Repo API 确认 ★97, pushed 2026-06-17, archived=False），但 FreeCAD 生态饱和（README 已有 neka-nat ★1825/ghbalf ★427/bonninr ★218/spkane ★186 四条目）不收录，按 08-16 sandraschi ★20 判例延伸

## 跳过（browser 验证后）

| 仓库 | Star | 原因 |
|------|------|------|
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | 54 | 真实 MCP（192 commits），但 README 自我定位"assistive/educational project, not replacement for professional CAD workflows"；最后提交 2 个月前；Fusion 已有 AuraFriday(★118)+faust-machines(★72) 两条目且 faust-machines 08-03 更活跃 → 观察 |
| heyixuan2/bambu-studio-ai | 85 | Bambu Lab 3D 打印 OpenClaw skill（SKILL.md 完整、137 commits），但浏览器默认分支最后提交约 3 个月前（pushed_at=07-03 被 tag 推送抬高，Pitfall #33）>90 天 → 不活跃跳过，复苏候补 |
| ezrover/ESP32-AI-Agent-Skill | 27 | ESP32 9 变体 Claude Code 插件（内容真实），但仅 2 commits、最后提交 4 个月前 + 含 LISTING-SUBMISSION 营销提交 → 不活跃跳过 |
| moellere/WireStudio | 26 | 极活跃（558 commits/33 tags/昨天提交）但类型为"agent-driven design studio"独立应用（web UI + wirestudio 包），非 MCP server 也非 SKILL.md 集合（Pitfall 平台型判例）→ 不收录，值得观察方向 |
| zxkmm/kicad-footprint-generate | 28 | 真实 SKILL.md（datasheet→KiCad footprint），活跃（上周提交），但 0 forks/1 contributor/20 commits 单用途，KiCad 生态已有 kicad-happy(★974) 综合覆盖 → 观察 |
| ATOI-Ming/FreeCAD-MCP | 97 | 复苏存在确认，FreeCAD 第 5 实现，生态饱和跳过 |

## 跳过（API 初筛，未 browser）

- **机械/CAD/CAM**：OctoEverywhere/mcp(★35, >1年不活跃)、ArchimedesCrypto/fusion360-mcp-server(★82, 仅badge更新不活跃)、Misterbra/fusion360-claude-ultimate(★55, pushed 04-20)、alisamsam/Solidworks-MCP(★92, pushed 03-23 不活跃 + SolidWorks 饱和)、sina-salim/AI-SolidWorks(★24, 16月不活跃)、Xuan-BOMS/soildworks-mcp(★20, SolidWorks 饱和)、Soljourner/claude-engineering-skills(★50, 9月不活跃)、delancy827/solidworks-skills(★61, 同作者 cad-skills 已在 README + SolidWorks 饱和)、microsoft/Resource2Skill(★469, 通用框架非工程)、ForgeCAD/forgecad-public-kit(★918, 与 KoStard 同仓库 org 迁移, Pitfall #69)、unnir/CadenceSKILL-Python(★83, Cadence SKILL 语言非 agent skill + 2016 年)、NVIDIA-Omniverse/usd-convert-cad(★19, <20 + CAD→USD 非工程技能)
- **电气/PCB/EDA**：device-context-protocol/dcp(★55, 协议/框架非 MCP server)、Finerestaurant/kicad-mcp-python(★40, >1年不活跃)、circuit-synth/kicad-sch-api(★50, API 库非 MCP server)、moellere/WireStudio 见上、juulsA/exportJson(★35, Cadence SKILL 脚本语言非 agent skill)、DIVESH8/IIT-madras-PCB-Design-workshop(★25, 课程材料)、tonylofgren/aurora-smart-home(★102, 智能家居非工程)、captainluzik/oh-my-embedded(★20, pushed 03-04 不活跃)、Abhishekvlsi/108-RTL-Projects(★62, RTL 项目集非 agent skill)、Arcadia-1/awesome-ams-skills(★31, awesome list + 作者已有 analog-agents/veriloga-skills)
- **材料/焊接/检测**（连续第 9 周零合格候选）：welding/NDT/metallurgy 全部 <6★；patsnap/skills(★33, Pitfall #64 变体2 商业数据驱动跳过)、GeoGeekLab/nature-reviewer-skills(★35, 通用学术非工程)、Hongyu-yu/matsci-ai-skills(★16, <20)、SFETNI/Deep-Matter-Chem-Skills(★5, <20)

## 观察/复查清单（下次补漏优先）
- NVIDIA-Omniverse/usd-convert-cad ★19（CAD→OpenUSD 官方 skill，接近门槛）
- JustusBraitinger/Autodesk-Fusion-360-MCP-Server ★54（若 faust-machines 转不活跃则成 Fusion 主候选）
- heyixuan2/bambu-studio-ai ★85（复苏候补：若恢复代码提交即达收录线）
- zxkmm/kicad-footprint-generate ★28（KiCad footprint 细分，fork 增长观察）
- NeonGlay/inventor-mcp ★16、BenCaunt/SynthCAD ★15、nickkraakman/skidl-skills ★15、Midstall/claude-for-hardware ★15、hanhuark/mechanical-engineering-research-skill ★15（pushed 08-16 极活跃）、Keitark/pcba-design-skills ★9、Seahan1/hardware-agency-agents ★9、beiming183-cloud/AutoCAD-skills ★4（GB/T 国标 CAD skill 方向）、MP-AI-20/mechanical-engineering-skills ★4（647 个机械工程 skill 模块）

## 统计
- 查询数：35（机械 15 + EDA 14 + 材料 6）| API 验证：20 | browser 验证：6
- 新增收录：1（MCP Servers）
- README 当前：社区精选 Skills 42、MCP Servers 103

## 查询效果观察
- 机械/CAD/CAM：MCP 表继续饱和，Way B 大部分命中已有条目；本次唯一收录来自 Way B 的 `CAD MCP server` 查询。SolidWorks/Fusion/FreeCAD 生态全部饱和，AutoCAD 尚有余量（U-C4N 双引擎差异化）
- 电气/PCB/EDA：KiCad/Altium/EasyEDA 均饱和，新候选集中在窄细分（footprint 生成、SKiDL、ESP32）且低星
- 材料/焊接/检测：连续第 9 周零合格候选，确认月度频率正确；`welding skill`/`NDT skill` 关键词几乎无 agent skill 生态
- 本日 3 个 browser 验证候选（bambu-studio-ai/ESP32-AI-Agent-Skill/JustusBraitinger）pushed_at 均被非代码事件抬高，实际默认分支提交 >90 天——Pitfall #33 再次验证，browser 检查不可省
