# 每日发现记录 — 2026-08-03（周一）

## 领域
- 机械/CAD/CAM
- 电气/PCB/EDA
- 材料/焊接/检测

## 搜索概况
- 查询数: 27（11 机械/CAD/CAM + 10 电气/PCB/EDA + 6 材料/焊接/检测）
- 候选总数: 198（搜索 API 初筛）→ 178 唯一
- API 验证: 20 个候选（star>=20 + README 去重 + 噪音过滤）
- 新增收录: 5

## 新增

### Skills 表

| Skill | 描述 | 来源 | Star |
|-------|------|------|------|
| [OpticalModeler](https://github.com/k-telux/OpticalModeler) | Evidence-gated agent skill：2D 光子学原理图重建为可物理审计的 Blender 光学平台（CAD、光束路径、机械、渲染验证） | k-telux | 212 |
| [veriflow-cc](https://github.com/bjwanneng/veriflow-cc) | Claude Code 驱动 RTL 设计 pipeline：架构→综合（iVerilog/Yosys）全流程，零 Python 依赖 | bjwanneng | 41 |
| [PCB-Agent-Teams](https://github.com/Zane456/PCB-Agent-Teams) | KiCad 10 多智能体 PCB 设计工作区：10 skills 驱动 Phase 0-5 流水线 | Zane456 | 26 |
| [cad-skills](https://github.com/delancy827/cad-skills) | AutoCAD 自动化设计技能包：pyautocad/AutoLISP/中望/浩辰 + GB/T 国标规范 | delancy827 | 23 |

### MCP Servers 表 — 电气 / PCB / EDA

| MCP Server | 描述 | 来源 | Star |
|-----------|------|------|------|
| [easyeda-mcp-pro](https://github.com/oaslananka/easyeda-mcp-pro) | EasyEDA Pro MCP server：PCB 检查、BOM 选料、制造导出、AI 辅助硬件审查 | oaslananka | 26 |

## 收录理由

1. **OpticalModeler ★212** — 高星 + last week 活跃（5 commits, 1 tag）。光学/光子学工程新细分方向（2D 原理图→3D 光学平台），skills/thorlabs-blender-optical-path 真实 SKILL.md，MIT。Skills 表首个光学工程条目。
2. **veriflow-cc ★41** — 86 commits、last month 活跃、6 forks。Claude Code 驱动的 RTL 设计 pipeline（spec→codegen→verify→lint/synth），多个 SKILL.md（vf-spec-golden/vf-coder/vf-linter 等 15+ 技能）。与 verilog-generator（RTL 生成）互补：veriflow-cc 侧重全流程编排。**注意**：2026-07-22 曾被 Pitfall #29 记录为 404，但 Individual Repo API + browser 均确认现存活跃——疑为当时误判或短暂下线，已复苏。
3. **PCB-Agent-Teams ★26** — 17 commits、last week 活跃。KiCad 10 多智能体设计工作区（10 skills，Phase 0-5：拓扑→原理图→PCB→DRC→Gerber），SPICE/DRC 脚本把关。与 kicad-happy（★878 通用技能集）互补：侧重多 agent 流水线编排。
4. **cad-skills ★23** — 2 个高质量 SKILL.md（cad-automation 834 行 + cad-designer 466 行），6 commits、pushed 53 天前（90 天内）。AutoCAD/pyautocad/win32com/AutoLISP + 中望/浩辰国产 CAD 兼容 + GB/T 国标制图规范。Skills 表首个 AutoCAD 专属 skill（MCP 表已有 Easy-MCP-AutoCad ★225）。
5. **easyeda-mcp-pro ★26** — 422 commits、57 tags、4 days ago 极活跃，CI/Scorecard 完备。与已有 easyeda-copilot（★97，原理图生成侧重）互补：PCB 检查/BOM/制造导出方向。同作者 oaslananka 已有 kicad-mcp-pro（★42）——Pitfall #58 同作者互补正面信号。

## 跳过候选

### 机械/CAD/CAM
| Repo | Stars | 原因 |
|------|-------|------|
| ForgeCAD/forgecad-public-kit | ★911 | **已在 README**（KoStard/forgecad-public-kit 同一项目，clone URL 仍指向 KoStard，org 更名） |
| microsoft/Resource2Skill | ★348 | 通用框架（多模态资源→可执行技能蒸馏），非工程专用 |
| rawwerks/VibeCAD | ★102 | 不活跃（pushed 2026-01-05，>90 天），上周已跳过 |
| ArchimedesCrypto/fusion360-mcp-server | ★82 | 不活跃（1 commit/90d，仅 badge 更新），skill 笔记已记录 |
| alisamsam/Solidworks-MCP | ★79 | 2 commits，功能被现有 SolidWorks MCP 覆盖（上周已跳过） |
| JustusBraitinger/Autodesk-Fusion-360-MCP-Server | ★53 | 192 commits 但 last commit 2 个月前；Fusion 360 已有 2 条目（AuraFriday ★113 + faust-machines ★65），功能重叠 |
| Joelalbon/Fusion-MCP-Server | ★37 | 不活跃（pushed 2025-06-12） |
| OctoEverywhere/mcp | ★35 | 不活跃（pushed 2025-07-03），3D 打印已被 mcp-3D-printer-server 覆盖 |
| arthurle3210/swapi-pilot-solidworks-mcp | ★27 | 功能极窄（SolidWorks API 文档搜索），SolidWorks 已有 3 条目 |
| sina-salim/AI-SolidWorks | ★25 | 不活跃（pushed 2025-04-20） |
| delancy827/cad-skills | ★23 | **已收录** |

### 电气/PCB/EDA
| Repo | Stars | 原因 |
|------|-------|------|
| embedded-society/altium-designer-mcp | ★31 | 功能极窄（Altium 元件库管理），Altium 已有 3 实现。**增长趋势向好**：★23→★31（+35% 月增长），758+ commits 仍极活跃，继续跟踪 |
| oaslananka/easyeda-mcp-pro | ★26 | **已收录** |
| ezrover/ESP32-AI-Agent-Skill | ★25 | 不活跃（2 commits、pushed 2026-04-14，111 天 >90 天边界），嵌入式领域 ESP32 已有覆盖 |
| circuit-synth/mcp-kicad-sch-api | ★20 | 不活跃（pushed 2025-08-20） |

### 材料/焊接/检测
| Repo | Stars | 原因 |
|------|-------|------|
| patsnap/skills | ★32 | PatSnap 公司数据驱动的专利情报/R&D 分析技能目录（类似 NVIDIA/skills 产品目录变体，Pitfall #64），非纯工程技能；engineering/ 下 TRIZ 等通用 R&D 分析，绑定商业平台数据 |

材料领域：welding/NDT/metallurgy 查询仍几乎无结果（welding MCP 6 结果、NDT 0、metallurgy 0），连续第 9 周无合格材料工程 MCP/server；materials science agent skill 查询命中 patsnap/skills（产品目录，跳过）和已收录的 materials-simulation-skills。

## 统计
- README 当前: 31 个 Skills（4 新增）+ 102 个 MCP Servers（1 新增）= 132 条（127 前 + 5 新增）
- 查询效果：机械/CAD/CAM Way D（agent skill）产出 4/5 新增——再次确认该领域 MCP 表饱和后 Way D 是主要来源
