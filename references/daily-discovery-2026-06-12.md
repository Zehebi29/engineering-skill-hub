# 每日发现记录 — 2026-06-12（周五）

## 搜索领域
- 工业制造/QA
- 生物医学/医疗
- 环境/水利/污染

## 查询统计
- 第一轮查询：22 个（7 工业 + 8 生物医学 + 7 环境）
- 第二轮扩展查询：26 个（7 工业 + 7 生物医学 + 6 环境 + 6 通用）
- 第三轮深度查询：19 个（6 生物医学 + 6 环境 + 5 工业 + 2 通用）
- 总查询数：67
- 唯一候选数：93（第一轮）+ 11（第二轮）+ 1（第三轮）= 105
- 过滤后（非已有、非归档、star>=20）：5 + 11 + 1 = 17
- 最终收录：3

## 新增收录

### 社区精选 Skills
| 名称 | Star | 描述 |
|------|------|------|
| [night_owl_research_agent](https://github.com/GRIND-Lab-Core/night_owl_research_agent) | 88 | NORA：地学/遥感/GIS 全自动 AI 研究 Agent，含 GeoBenchmark、期刊模板、MCP server |

### MCP Servers — 生物医学 / 医疗
| 名称 | Star | 描述 |
|------|------|------|
| [medical-mcps](https://github.com/pascalwhoop/medical-mcps) | 21 | 生物医学 MCP server：100+ 工具，集成 Reactome/KEGG/UniProt/ChEMBL/PubMed/OpenFDA 等 14 个数据库 |

### MCP Servers — 环境 / 水利
| 名称 | Star | 描述 |
|------|------|------|
| [foehn](https://github.com/kayhendriksen/foehn) | 41 | MeteoSwiss 气象数据 MCP server：20+ 数据集（站点、雷达、冰雹、预报、气候），Python API/CLI/MCP |

## 跳过的候选

### 因类型不符跳过
| 名称 | Star | 原因 |
|------|------|------|
| ForestHubAI/edge-agents | 75 | 边缘 AI agent 运行时，非 MCP server，是通用框架 |
| CheMiguel23/MemoryMesh | 343 | 通用知识图谱 MCP server，非工程领域专用 |
| carterlasalle/mac_messages_mcp | 298 | iMessage MCP server，完全无关 |
| mr-tbot/mesh-api | 153 | Meshtastic 网状网络 AI 路由器，非工程 MCP |
| gensecaihq/pfsense-mcp-server | 72 | 防火墙 MCP，网络安全非工程 |
| pasie15/meshy-ai-mcp-server | 37 | Meshy AI 3D 模型生成，通用工具 |
| agentic-ops/real-estate-mcp | 41 | 房地产 MCP demo，非工程 |
| Md-Emon-Hasan/MediGenius | 34 | 医疗 AI 助手（LangGraph），非 MCP server |

### 因 Star 不足或不活跃跳过
| 名称 | Star | 原因 |
|------|------|------|
| biocontext-ai/knowledgebase-mcp | 24 | 生物医学知识库 MCP，但 >90 天未更新（2026-01-12） |
| biocontext-ai/skill-to-mcp | 26 | 技能转 MCP 工具，非 MCP server，>90 天未更新 |
| biocontext-ai/registry | 20 | 生物医学 MCP 注册表，是目录工具非 MCP server |
| Appsilon/TealFlowMCP | 27 | 临床试验 Teal R Shiny MCP，但 >90 天未更新（2026-03-01） |

### 因领域不相关跳过
| 名称 | Star | 原因 |
|------|------|------|
| heurist-network/heurist-mesh-mcp-server | 64 | 无描述，无法验证相关性 |
| Aryia-Behroziuan/References | 61 | AI 参考文献集合，2022 年最后更新 |

## 领域搜索效果评估

### 工业制造/QA
- 查询效果差，与历史记录一致
- "manufacturing"、"quality"、"production" 关键词噪音极高
- "OPC UA"、"Modbus"、"PLC"、"SCADA" 返回结果极少
- "CNC machining" 基本无 MCP server
- 该领域 MCP 生态持续空白，建议降为月度检查

### 生物医学/医疗
- 查询效果好，该领域 MCP 生态最丰富
- 新增 medical-mcps（★21）：首个集成 14 个生物医学数据库的统一 MCP server
- biocontext-ai 系列（knowledgebase-mcp、skill-to-mcp、registry）活跃但 star 低或类型不符
- Appsilon/TealFlowMCP（★27）临床试验 Teal MCP 有价值但不活跃

### 环境/水利/污染
- 查询效果一般，该领域 MCP 生态仍然稀少
- 新增 foehn（★41）：首个气象数据 MCP server（MeteoSwiss），填补气候/天气数据空白
- "water treatment"、"wastewater"、"hydrology"、"pollution" 查询几乎无结果
- "environmental" 查询返回大量通用工具误匹配
- GIS/遥感方向有 night_owl_research_agent（归入 Skills）

## 总结
- README 当前：6 Skills + 约 65 MCP Servers
- 今日新增：1 Skill + 2 MCP Servers
- 工业制造领域持续空白，环境/水利仅有少量新增
