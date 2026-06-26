# Daily Discovery — 2026-06-26 (Friday)

## 搜索领域
- 工业制造/QA
- 生物医学/医疗
- 环境/水利/污染

## 查询统计
- 总查询数: 30
- 初筛候选数: 30 (star >= 15)
- API 验证候选数: 17
- 新增收录数: 2

## 新增收录

| Repo | Star | 领域 | 分类 |
|------|------|------|------|
| [ezh0v/weather-mcp-server](https://github.com/ezh0v/weather-mcp-server) | 246 | 环境/水利/污染 | MCP Server |
| [lzinga/us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp) | 103 | 综合资源 | MCP Server |

### weather-mcp-server
- Go MCP server for real-time weather data retrieval and interpretation
- SSE transport support, Dockerfile included
- Topics: go, golang, mcp, mcp-server, sse
- Last code push: 2026-03-01 (8 months, but ★246 indicates stable tool)
- Added to: 环境/水利/污染 (after autocad-mcp ★341, before foehn ★41)

### us-gov-open-data-mcp
- TypeScript MCP server + SDK for 40+ US government data APIs
- 250+ tools: Treasury, FRED, Congress, FDA, CDC, FEC, EPA, NWS, lobbying, etc.
- 78 commits, actively maintained (last push 2 weeks ago)
- Topics: api, cdc, claude, congress, fda
- Added to: 综合资源 (★103, covers multiple domains)

## 跳过的条目

| Repo | Star | 原因 |
|------|------|------|
| Haohao-end/mcp-agent | 82 | 通用 MCP 框架，非领域专用 |
| grll/pubmedmcp | 117 | 代码最后推送 2025-09-02，不活跃 9+ 个月 |
| Dianel555/paper-search-mcp-nodejs | 171 | 学术论文搜索，非工程/医学专用 |
| the-momentum/fhir-mcp-server | 90 | 与 README 中 wso2/fhir-mcp-server (★124) 概念重复 |
| ReyemTech/mcp-canada | 51 | 加拿大政府数据，非工程领域 |
| langcare/langcare-mcp-fhir | 47 | 低于已有 wso2 (★124) |
| Appsilon/TealFlowMCP | 28 | R Shiny 应用构建，非工程 MCP |
| biocontext-ai/knowledgebase-mcp | 27 | 生物医学知识库，registry 类型非 MCP server |
| biocontext-ai/skill-to-mcp | 27 | 工具类（skill 转 MCP），非 MCP server |
| biocontext-ai/registry | 21 | Registry 类型，非 MCP server |
| weather-mcp/weather-mcp | 20 | 低星 (★20) |
| u9401066/pubmed-search-mcp | 20 | 低星 (★20) |
| cadugrillo/s7-mcp-bridge | 19 | 低星 (★19)，Siemens PLC MCP |
| lynnlangit/precision-medicine-mcp | 18 | 低星 (★18) |
| nickzren/opentargets-mcp | 18 | 低星 (★18) |
| vikramgorla/mcp-swiss | 18 | 低星 (★18)，通用瑞士数据 |
| YaoIsAI/SerialRUN | 16 | 低星 (★16)，串口调试 |
| JackKuo666/ClinicalTrials-MCP-Server | 16 | 低星 (★16)，与已有 clinicaltrialsgov-mcp-server 重复 |
| midhunxavier/OPCUA-MCP | 15 | 低星 (★15)，与已有 opcua-mcp (★27) 重复 |
| goodfire-ai/evee-mcp | 15 | 低星 (★15) |
| Darkroaster/pubmearch | 150 | 代码最后推送 2025-05-07，不活跃 13+ 个月 |
| JackKuo666/PubMed-MCP-Server | 122 | 代码最后推送 2025-05-08，不活跃 13+ 个月 |

## 领域搜索效果观察

### 工业制造/QA
- 10 个查询，结果以通用工具和低星项目为主
- OPC UA/Modbus 相关候选均低于现有 opcua-mcp (★27) 和 modbus-mcp (★24)
- Siemens S7 PLC MCP (★19) 是新细分方向但星数不达标
- 该领域 MCP 生态持续稀少

### 生物医学/医疗
- 10 个查询，PubMed/FHIR 相关结果丰富但多为重复或低活跃
- 大量 2025 年创建的 PubMed MCP server 已不活跃
- biocontext-ai 组织批量出现 3 个仓库（registry/skill-to-mcp/knowledgebase-mcp），均为工具类非 MCP server
- us-gov-open-data-mcp 是新发现，覆盖 FDA/CDC/EPA 等政府数据

### 环境/水利/污染
- 10 个查询，weather/meteorology 方向有新发现
- weather-mcp-server (★246) 是该领域首个天气数据 MCP server
- water treatment/wastewater/hydrology 查询持续无结果
- 该领域从 "仅 autocad-mcp + foehn" 扩展到 "autocad-mcp + weather-mcp-server + foehn"
