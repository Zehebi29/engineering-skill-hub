# Daily Discovery — 2026-05-15 (Friday)

## Search Domains
- 工业制造/QA
- 生物医学/医疗
- 环境/水利/污染

## Queries

### 工业制造/QA (8 queries)
- `"manufacturing" "mcp" in:name,description` — lots of noise (production-ready generic tools)
- `"quality inspection" "mcp"` — no results
- `"manufacturing" "ai" "agent"` — mostly generic
- `"quality control" "llm"` — noise
- `"CNC" "mcp" in:name,description` — no results
- `"3D printing" "mcp" in:name,description` — found OctoEverywhere (33★, low activity)
- `"industrial" "mcp" "server"` — found industrial MCP servers (OPC UA, Modbus, TwinCAT)
- `"opcua" "mcp"` — confirmed opcua-mcp

### 生物医学/医疗 (7 queries)
- `"biomedical" "mcp" in:name,description` — strong results
- `"medical" "mcp" "server"` — strong results
- `"biomedical" "ai" "agent"` — Biomni (3081★, agent framework, not MCP)
- `"medical imaging" "mcp"` — no results
- `"healthcare" "mcp"` — healthcare-mcp-public (115★)
- `"clinical" "mcp"` — clinicaltrialsgov-mcp-server (71★, medical not environmental)
- `"medical" "llm" "agent"` — various

### 环境/水利/污染 (6 queries)
- `"environmental" "mcp" in:name,description` — noise
- `"water" "mcp" "server"` — found puran-water/autocad-mcp (247★)
- `"wastewater" "mcp"` — no results
- `"pollution" "mcp"` — no results
- `"hydrology" "mcp"` — no results
- `"environmental" "ai" "agent"` — noise

## New Entries Added (6)

### 工业自动化 (new section)
| Repo | Stars | Notes |
|------|-------|-------|
| [kukapay/opcua-mcp](https://github.com/kukapay/opcua-mcp) | 26 | OPC UA 工业自动化协议 MCP server |
| [kukapay/modbus-mcp](https://github.com/kukapay/modbus-mcp) | 23 | Modbus 工业数据 MCP server |
| [eponce00/twincat-mcp](https://github.com/eponce00/twincat-mcp) | 20 | TwinCAT/Beckhoff PLC MCP server, very active (47 commits) |

### 生物医学 / 医疗 (new section)
| Repo | Stars | Notes |
|------|-------|-------|
| [andybrandt/mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed) | 165 | PubMed 文献搜索 MCP server |
| [Cicatriiz/healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public) | 115 | 综合医疗数据 MCP server (FDA, ICD-10, DICOM) |

### 环境 / 水利 (new section)
| Repo | Stars | Notes |
|------|-------|-------|
| [puran-water/autocad-mcp](https://github.com/puran-water/autocad-mcp) | 247 | 水处理工程 P&ID 图纸自动化 MCP server |

## Skipped

| Repo | Stars | Reason |
|------|-------|--------|
| snap-stanford/Biomni | 3081 | Biomedical AI agent framework, not MCP server |
| NVIDIA-AI-Blueprints/biomedical-aiq-research-agent | 128 | NVIDIA agent blueprint, not MCP server |
| YUHAO-corn/manufacturing-agents | 162 | Multi-agent system, not MCP server |
| tavily-ai/tavily-mcp | 1965 | Generic search MCP, not engineering-specific |
| apecloud/ApeRAG | 1167 | Generic RAG system |
| golf-mcp/golf | 824 | Generic MCP framework |
| the-momentum/fhir-mcp-server | 80 | Medical (FHIR), below threshold |
| jmandel/health-record-mcp | 78 | Medical EHR, below threshold |
| cyanheads/clinicaltrialsgov-mcp-server | 71 | Clinical trials, below threshold |
| JamesANZ/medical-mcp | 89 | Medical, below threshold |

## Query Effectiveness Notes
- "industrial" + "mcp" + "server" was the best query for manufacturing domain
- "water" + "mcp" found puran-water (key: org name contains domain keyword)
- Biomedical domain has more MCP server ecosystem than environmental
- Environmental/water engineering MCP servers are very rare
- Most high-star results are generic tools that happen to match keywords — LLM filtering essential
- Adding `"in:name,description"` to queries reduces noise significantly

## README Stats After Update
- Skills: 1 community + 3 original
- MCP Servers: 9 sections (机械/CAD, 电气/PCB, 机器人, 航空航天, 油藏, 工业自动化, 生物医学, 环境/水利, 综合资源)
- Total MCP Server entries: 27
