# 每日发现记录 — 2026-08-07（周五）

## 领域
- 工业制造/QA（周五常规）
- 生物医学/医疗（周五常规）
- 环境/水利/污染（周五常规）
- 本周无缺失天数（08-04/05 已于昨日 08-06 补扫）

## 搜索概况
- 查询数: 24（方式 B + 方式 D，3 个领域）
- 候选深入分析: 10（Individual Repo API 验证）
- Browser 深度验证: 2（edgeCore、tia-portal-openness-ai）
- 新增收录: 1（Skills 表）

## 新增收录

### 工业制造/QA（Skills 表）
| 仓库 | Star | pushed_at | 说明 |
|------|------|-----------|------|
| huahaizo/tia-portal-openness-ai | 47 | 2026-05-24 | Claude Code/Agent skill for Siemens TIA Portal Openness V15-V21：自然语言 → PLC 项目操作（打开/列设备/导出块/导入 SCL/编译/归档），C# Openness 控制器执行。真实 SKILL.md 结构（SKILL.md + references/openness-patterns.md + scripts/new-openness-controller.ps1 + agents/）。★47 ≥ 20 + 活跃（75 天内推送）+ 领域高度相关（工业 PLC 工程自动化），填补 Skills 表西门子 PLC 工程空白（此前仅 sap-engineering-skill 覆盖 ERP 方向） |

## 跳过详情

### 工业制造/QA
| 仓库 | Star | 原因 |
|------|------|------|
| anviod/edgeCore | 109 | 工业边缘网关平台产品（Go 完整边缘计算网关：Modbus/BACnet/OPC-UA/S7 采集 + 边缘计算 + 云端连接），MCP 只是其 AI 特性之一，非 MCP server 也非 skill 集合（Pitfall #64 变体 3 平台型） |
| YaoIsAI/SerialRUN | 35 | 串口调试助手附带 Modbus/PLC 支持（SerialRUN 模式噪音，Pitfall 已记录） |
| cadugrillo/s7-mcp-bridge | 21 | ★21 跨过阈值但 pushed 2026-03-20（>90 天不活跃）。品牌级 PLC MCP 复苏候补，继续观察 |
| Nodeblue-AI/studio5000-mcp-server | 17 | ★17 < 20 不达标，品牌级 PLC 观察对象 |
| MarcelRoozekrans/roslyn-codelens-mcp | 42 | .NET 代码理解 MCP，非工业制造（"quality inspection" 关键词误匹配） |
| ai-evos/agent-skills | 24 | 物流/制造/零售/能源运营经验 skills，pushed 2026-02-25 不活跃（>90 天） |
| npatel221/PLC_Projects | 24 | 个人 PLC 学习项目集合，非 agent skill/MCP |
| ScottDuncanAI/claude-manufacturing-skills | 7 | 太新（created 2026-08-05）+ ★7 过低，但化学过程/制造工程实践方向值得观察 |
| 其余（mattmohandiss/cad-mcp-server 2、MIGO-OvO/plc-skill 10、PENG111LIN/industrial-vision-skills 3 等） | <15 | Star 过低 |

### 生物医学/医疗（连续第 5 周 MCP 零新增）
| 仓库 | Star | 原因 |
|------|------|------|
| LeonChaoX/qinyan-academic-skills | 770 | 通用学术 skills 噪音（Pitfall 已记录，跨领域非工程专用） |
| BioTender-max/awesome-bio-agent-skills | 139 | awesome list 类型（分类目录），非 skill 集合本身 |
| AlterLab-IEU/AlterLab-Academic-Skills | 58 | 通用学术噪音，跨 17 个研究领域非工程专用 |
| Nexgene-Research/nexonco-mcp | 64 | pushed 2025-08-12 不活跃（>1 年） |
| boheling/skillbench | 44 | agent skill 基准测试框架，非医学工程 |
| Appsilon/TealFlowMCP | 28 | Teal R Shiny 临床试验数据分析，pushed 2026-03-01 不活跃 |
| biocontext-ai/registry | 21 | registry 类型（Pitfall #48），非 MCP server |
| Augmented-Nature/OpenFDA-MCP-Server | 21 | pushed 2025-12-21 不活跃 |
| u9401066/pubmed-search-mcp | 24 | PubMed MCP 功能重叠（已有 mcp-simple-pubmed/pubmed-mcp-server/medical-mcp） |
| AminAlam/meddev-agent-skills | 25 | 已在 README |

### 环境/水利/污染
| 仓库 | Star | 原因 |
|------|------|------|
| CliDyn/copernicus-mcp | 12 | Copernicus 环境数据 MCP，★12 < 20 不达标，活跃值得观察 |
| cyanheads/usgs-water-mcp-server | 1 | Star 过低 |
| cyanheads/epa-mcp-server | 1 | Star 过低 |
| malkreide/swiss-environment-mcp | 1 | Star 过低 |
| dungnotnull/*-agent-skill 系列 | 3-4 | Star 过低（fog-water-harvester/emergency-water-filter 等） |
| 其余 | <10 | Star 过低 |

## 低星/复苏复查（本周轮换内完成）
- cadugrillo/s7-mcp-bridge：★20→21（微增），pushed 仍 2026-03-20，未复苏 → 继续候补
- Nodeblue-AI/studio5000-mcp-server：★12→17（+5 增长中），仍 <20 → 继续观察
- brack101/AspenPlus-MCP-Server：★31，pushed 仍 2025-10-09，未复苏 → 继续候补（化工领域空白）
- ScottDuncanAI/claude-manufacturing-skills：新建 2 天 ★7，制造工程实践，列入下轮观察

## 查询效果备注
- 工业制造/QA：`PLC MCP server`、`manufacturing agent skill` 是有效查询；`quality inspection MCP server` 被 .NET/代码质量工具污染；`production` 已确认无用（未用）
- 生物医学/医疗：方式 D 连续多周仅学术噪音/awesome list，MCP 连续 5 周零新增，确认降为月度检查频率
- 环境/水利：生态仍空白，copernicus-mcp 是唯一值得跟踪的新苗头
