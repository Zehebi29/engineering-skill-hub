# 每日发现记录 — 2026-08-06（周四）

## 领域
- 油藏/石油/地质（周四常规）
- 汽车/自动驾驶（周四常规）
- 船舶/海洋工程（周四常规）
- **补充**：08-04（周二）/08-05（周三）无 daily-discovery 记录（cron 未执行），本周补扫 航空航天/CFD + 机器人/ROS + 能源/电力/电池 + 土木/结构/BIM + 化工/流程模拟 + 半导体/VLSI/FPGA

## 搜索概况
- 查询数: 49（方式 B + 方式 D，9 个领域）
- 候选深入分析: 8（Individual Repo API 验证）
- 新增收录: 1（Skills 表）

## 新增收录

### 半导体/VLSI/FPGA（Skills 表）
| 仓库 | Star | pushed_at | 说明 |
|------|------|-----------|------|
| Zhujian-Liang/verilog-design-skill | 21 | 2026-05-23 | Claude Code skill：Verilog 设计规范/流水线模式/FPGA 优化笔记 → 本地可查询知识库，带出处引用的实现建议与示例代码。真实 SKILL.md + references/ 结构（3 个参考文档），与 verilog-generator（RTL 生成）和 veriflow-cc（RTL pipeline）功能互补：本条目是设计知识检索，非代码生成。★21 ≥ 20 门槛 + 活跃（75 天内推送）+ 领域高度相关 |

## 跳过详情

### 机器人/ROS
| 仓库 | Star | 原因 |
|------|------|------|
| ros-claw/rosclaw | 178 | Physical AI 执行 runtime/控制平面平台，MCP 只是 southbound 协议之一；.agents/skills 是自身产品技能（Pitfall #64 模式）。非纯 MCP server 也非 skill 集合，类型不符（平台/运行时） |
| NVIDIA/skills | 2798 | 公司产品技能目录（Pitfall #64），非工程领域技能 |
| manykarim/rf-mcp | 109 | Robot Framework（通用测试自动化），非物理机器人（Pitfall #38） |
| telekinesis-ai/telekinesis-examples | 63 | Python SDK/库（PyPI 包），"Skills" 指算法模块非 SKILL.md（Pitfall #55 SDK≠MCP） |
| kakimochi/ros2-mcp-server | 84 | pushed 2025-06-27 不活跃 |
| IliaLarchenko/robot_MCP | 81 | pushed 2025-08-12 不活跃（已在复苏候补） |
| AI-FanGe/RobotArm-MCP-P340 | 36 | pushed 2025-07-10 不活跃 |
| Yutarop/ros-mcp | 35 | pushed 2025-08-19 不活跃（已在复苏候补） |
| gotoolkits/mcp-wecombot-server | 38 | 企业微信机器人消息，非物理机器人 |
| jeremyruppel/claude-collider | 51 | SuperCollider 音乐合成，非机器人 |
| ltlhuuu/PSEC | 65 | ICLR 2025 论文代码，非 skill 集合 |
| 其余 ros2-mcp / RoboRun / amazing-ros2-mcp | <15 | Star 过低 |

### 能源/电力/电池
| 仓库 | Star | 原因 |
|------|------|------|
| walkererik1991/energyplus-idf-mcp-server | 38 | 功能重叠：README 已有 LBNL-ETA/EnergyPlus-MCP ★107（官方项目） |
| content-designer/ux-writing-skill | 139 | UX 写作技能，非能源工程（关键词误匹配） |
| ElmatadorZ/MoneyAtlas-ClaudeSkill-Agent | 53 | 金融，非能源 |
| aloth/PowerSkills | 29 | PowerShell M365 工具，非电力系统（与已收录 Power-Agent/PowerSkills ★57 同名不同物） |
| haorui-harry/agent-harness | 36 | 通用 LangChain 框架 |

### 土木/结构/BIM
| 仓库 | Star | 原因 |
|------|------|------|
| LuDattilo/revit-mcp-server | 35 | 描述即 mcp-servers-for-revit（已在 README ★170/★120），疑似同源/迁移（Pitfall #69） |
| kaitpw/Rvt_Docs_MCP | 30 | pushed 2025-08-15 不活跃 |
| Demolinator/revit-mcp-server | 23 | Revit MCP 功能重叠（已有 RevitMCP/多个 revit-mcp） |
| schauh11/revit-mcp-server | 20 | 功能重叠 + pushed 2026-02-05 |
| 其余 Revit MCP（bimwright 11/RevitCortex 8/aps-sample 9/ArchSmarter 9） | <15 | Star 过低 + 重叠 |

### 化工/流程模拟
| 仓库 | Star | 原因 |
|------|------|------|
| brack101/AspenPlus-MCP-Server | 31 | **复苏候补**：pushed 2025-10-09 不活跃（>90天）。Aspen Plus MCP 领域空白 + 类型正确 + ★31，值得 2-4 周后复查 pushed_at |
| nckugese/Aspen_Co-pilot | 16 | Star <20 |
| retentioneering/retentioneering-tools | 911 | 点击流/流程挖掘，非化工（已知噪音） |

### 半导体/VLSI/FPGA
| 仓库 | Star | 原因 |
|------|------|------|
| adeleempurpled290/FPGA-Agent-skills | 27 | **07-22 曾标记 404，本次确认已复活**（Individual Repo API 存在，pushed 2026-07-27）。但内容为 Windows 下载教程/学习资源（Pitfall #40），且与 xilinx-skill ★382 功能重叠 → 不收录。验证了 Pitfall #29 的 404 非永久原则 |
| ic-star-tech/ccfoundry-agent-kit | 24 | **07-22 曾标记 404，本次确认已复活**。但为 SDK+开发板 demo（Skill-to-Earn 演示），类型不符 |
| The-OpenROAD-Project/OpenROAD-MCP | 12 | Star <20（官方组织，继续观察） |
| londey/claude-skill-verilog | 18 | Star <20 |
| lcapossio/hdldiagZero | 17 | Star <20 |
| Akashtailor-exe/30-days-of-verilog | 73 | 学习教程仓库（Pitfall #40），非 skill 集合 |
| ItzzInfinity/100-days-of-RTL | 39 | 同上 |
| ccfoundry-agent-kit | 24 | SDK/演示，类型不符 |

### 油藏/石油/地质
| 仓库 | Star | 原因 |
|------|------|------|
| kucherenko/petropowers | 9 | 真正的石油工程 AI skills 框架（Superpowers 基础），但 ★9 < 20。领域空白，值得观察 |
| blake365/macrostrat-mcp | 8 | Star <20 + pushed 2025-08-26 不活跃 |
| keros68/cugb-doctoral-thesis-format | 8 | 论文格式检查，非工程 |

### 汽车/自动驾驶
| 仓库 | Star | 原因 |
|------|------|------|
| luna-system/ada | 16 | 聊天框架（ADAS 关键词误匹配） |
| enovella/r2con-prequals-rhme3 | 17 | 硬件 CTF，非工程 skill |

### 船舶/海洋工程
| 仓库 | Star | 原因 |
|------|------|------|
| weather-mcp/weather-mcp | 33 | 通用天气数据 MCP（marine 只是工具之一），非船舶工程 + 与 weather-mcp-server 重叠 |
| lucasinocencio1/mcp-surf-forecast | 19 | 冲浪预报，非工程 |
| Cyreslab-AI/marinetraffic-mcp-server | 9 | Star <20 + pushed 2025-05-15 不活跃 |
| 所有 "ship MCP" 高星结果（rohitg00 ★46021 / PostHog ★37518 / ShipSwift / shippie 等） | — | "ship it" 软件交付语义噪音，与船舶工程无关 |

### 航空航天/CFD
| 仓库 | Star | 原因 |
|------|------|------|
| kimimgo/viznoir | 18 | Star <20（★15→★18 增长中，289+ commits 活跃，继续观察） |
| sandraschi/freecad-mcp | 15 | Star <20（已有观察） |
| Soljourner/claude-engineering-skills | 45 | pushed 2025-11-07 不活跃 |

## 备注
- **08-04/08-05 cron 缺失**：本周二、三的 daily-discovery 记录不存在（git log 最后提交为 08-03 周一）。本次已将周二/周三 6 个领域全部补扫，未发现漏掉的新候选。建议检查 cron f2cc259c3af0 状态。
- 周四三个领域连续第 8 周无新增（油藏/船舶 MCP 生态持续空白；汽车/自动驾驶 Way D 边际收益继续下降）。
- **复苏验证成功 2 例**：FPGA-Agent-skills 和 ccfoundery-agent-kit 均从 07-22 的 404 标记恢复存在，进一步验证 Pitfall #29（404 非永久）。但两者均因类型/内容问题不收录。
- **新复苏候补**：brack101/AspenPlus-MCP-Server ★31（化工/流程模拟领域空白，若恢复活跃即可收录）。
- README 统计：社区精选 Skills 77（+1）、MCP Servers 不变。
