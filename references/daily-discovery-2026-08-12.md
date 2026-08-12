# Daily Discovery — 2026-08-12（周三）

**Cron 状态**：08-10（周一）缺口已在 08-11 补扫并报告；08-04/05 已在 08-06 补扫。本周无新增缺失。⚠️ 提示：cron `f2cc259c3af0` 近期连续缺口（08-04/05、08-10），建议用户检查 job 状态。

## 搜索领域（周三常规 3 个）
- 土木/结构/BIM
- 化工/流程模拟
- 半导体/VLSI/FPGA

## 执行统计
- 查询数：32（3 领域 × 5-6 关键词，方式 B MCP + 方式 D agent skill 各半）
- 候选数：281 原始 → 去重后 218（土木 97 + 化工 39 + 半导体 82）
- API 验证：20 个候选 Individual Repo API
- Browser 深度验证：2 个（FPGA-Agent-skills、ccfoundry-agent-kit）
- 新增收录：**1**（Skills 表）

## 新增条目（1）

### Skills 表
| 条目 | Star | 领域 | 理由 |
|------|------|------|------|
| [FPGA-Agent-skills](https://github.com/adeleempurpled290/FPGA-Agent-skills) | 28 | 半导体/VLSI/FPGA | 8 个 Vivado/Vitis 分步引导 skill（HLS 综合、RTL、综合、约束、时序、仿真、调试、TCL），每目录 SKILL.md + REFERENCE.md + examples 结构完整；★28 ≥ 20 门槛 + pushed 2026-08-11（20 小时前）极活跃。**曾 404 复苏案例**：2026-07-22 被标记 404，今日 Individual Repo API + browser 双确认存在（Pitfall #29/#57 印证——Search API 404 是缓存脏数据，不应永久排除），10 commits、GPL-2.0 |

## 跳过详情（重点候选及原因）

### 半导体/VLSI/FPGA
| 仓库 | Star | 原因 |
|------|------|------|
| ic-star-tech/ccfoundry-agent-kit | 24 | 曾 404 复苏确认，但 browser 验证为平台框架：SDK + Dev Board + 商业 Foundry（foundry.cochiper.com）S2E 商业模式，非纯 MCP/skill 集合（Pitfall #64 变体 4 开源外壳/平台绑定） |
| The-OpenROAD-Project/OpenROAD-MCP | 12 | OpenROAD 官方 org（Pitfall #56 可放宽），但 ★12 仍 <20 且较 07-22 无增长（★12→★12）；pushed 2026-08-11 活跃，继续观察 |
| videGavin/serenity-analyst | 35 | 半导体供应链 chokepoint 分析（Serenity 投资人观点蒸馏），非工程设计 skill；同类仓库 4 个（serenity-analyst/serenity-skills×2/serenity-skill）均同主题，非工程方法论 |
| lcapossio/hdldiagZero | 17 | ★17 <20 接近门槛，pushed 2026-08-10 极活跃；HDL→SVG 框图生成，纳入下次复查 |
| londey/claude-skill-verilog | 18 | ★18 <20；单一 Verilog skill 与已收录 verilog-design-skill 功能重叠 |
| vibeic/vibe-ic | 16 | ★16 <20，IC 设计插件 MCP-EDA，观察 |
| najaeda/naja-scope | 15 | ★15 <20，SystemVerilog 网表探索 MCP，观察 |
| lcapossio/fpgaZeroMCP | 5 | ★5 过低，完整 FPGA 工具链 MCP，观察 |
| wangyuxin0707/vivado-mcp-agent | 4 | ★4 过低 |
| 14H034160212/serenity-skills 等 3 个 serenity 系 | 3 | ★3 过低 + 非工程方法论 |

### 土木/结构/BIM
| 仓库 | Star | 原因 |
|------|------|------|
| Sam-AEC/aec-model-bridge | 50 | Revit MCP 生态已饱和（已有 TS/Python/C# 多实现，同作者 Sam-AEC 已有 Autodesk-Revit-MCP-Server 收录），功能重叠 |
| Soljourner/claude-engineering-skills | 47 | 通用工程 skills（机械/航空/通用）非土木专用，且 pushed 2025-11-07 不活跃（>270 天） |
| IbrahimFahdah/revit-claude-mcp | 21 | Revit MCP 又一个实现，功能重叠（生态饱和） |
| Nice3point/revit-skills | 11 | Nice3point 是 Revit API 知名开发者，但 ★11 <20；pushed 2026-08-10 活跃，纳入下次复查 |
| paulieb89/pyp6xer-mcp | 12 | Primavera P6 XER 进度分析 MCP——新细分方向（进度管理），★12 <20，观察 |
| ArchSightLabs/archsight-aios | 11 | 建筑行业 AI skills（BIM/IFC/RAG），★11 <20，观察 |
| TylerIlunga/procore-mcp-server | 7 | ★7 过低 |
| yixuanzhong/PLAXIS-MCP | 5 | PLAXIS 岩土 MCP 新方向，★5 过低 |
| ferdinandobons/brand-docs | 243 | 文档模板生成 skills（Word/PPT/Excel），非工程 |
| sii-research/Legal-world | 18 | 法律 agent 环境，非工程 |
| 其余 70+ 条 | — | 个人作品集/课程作业/低星（<10）/类型不符 |

### 化工/流程模拟
| 仓库 | Star | 原因 |
|------|------|------|
| brack101/AspenPlus-MCP-Server | 31 | ★31 达标但 pushed 2025-10-09（>300 天不活跃）；Aspen Plus MCP 是流程模拟核心工具，纳入复苏候补列表（2-4 周复查） |
| nckugese/Aspen_Co-pilot | 15 | ★15 <20 |
| PhelanShao/orca-mcp-server | 19 | ★19 <20，ORCA 量子化学（计算化学）非流程模拟 |
| EPEL-SNU/Aspen_Plus_MCP | 5 | ★5 过低（但 pushed 2026-07-27 活跃，Aspen 官方组织 EPEL-SNU，观察） |
| jskherman/engg-skills | 4 | chemical engineering skills，★4 过低 |
| OntoLedgy/ol_dwsim_interop_services | 3 | DWSIM MCP，★3 过低 |
| sharique2004/dwsim-mcp | 1 | DWSIM MCP，★1 过低 |
| yuuyo-arobet/AspenHYSYS-MCP-Server | 3 | HYSYS MCP 51 工具，★3 过低，观察 |
| 其余 30+ 条 | — | 课程作业/个人项目/低星 |

## 查询效果观察
- **半导体/VLSI/FPGA**：Way D（agent skill）仍是主要来源。MCP 侧新出现完整工具链方向（fpgaZeroMCP ★5、vibe-ic ★16、naja-scope ★15）但全部低星。serenity 供应链分析类噪音 4 仓库同主题，建议搜索时语义过滤"supply chain/serenity/investor"
- **土木/结构/BIM**：Revit MCP 生态完全饱和（5+ 实现），新增方向在进度管理（pyp6xer Primavera P6 ★12）、岩土（PLAXIS ★5）、AEC skills 集（archsight ★11）——全部低星待复查
- **化工/流程模拟**：MCP 生态持续空白（Aspen/DWSIM 全部 <20 或不活跃），Skills 方向 claude-manufacturing-skills 仍是唯一条目。AspenPlus-MCP-Server ★31 不活跃是复苏候补首选

## 表修复记录
- 修复 Skills 表 star 排序错误：axi-compliance-skill（★29）原位于 sap-engineering-skill（★25）之后（08-11 插入遗留，Pitfall #72 场景），本次整表重排（42 数据行按 star 降序，稳定排序保持同星序）+ 单表块 CJK 对齐，`git diff -w` 后仅 1 条新行 + 纯换位

## 复苏候补（下次复查）
- brack101/AspenPlus-MCP-Server（★31，不活跃 >300 天）
- The-OpenROAD-Project/OpenROAD-MCP（★12，官方 org 活跃）
- lcapossio/hdldiagZero（★17）
- Nice3point/revit-skills（★11，知名作者）
- paulieb89/pyp6xer-mcp（★12，进度管理新方向）
- lcapossio/fpgaZeroMCP（★5）
- vibeic/vibe-ic（★16）
- najaeda/naja-scope（★15）
- EPEL-SNU/Aspen_Plus_MCP（★5，官方 org 活跃）

## 文件状态
- commit: `698ddff`
- push: `5f41364..698ddff main -> main` 成功
- README Skills 表：41 → 42 数据行
