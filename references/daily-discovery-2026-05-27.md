# Daily Discovery — 2026-05-27 (Wednesday)

## Search Domains
- 土木/结构/BIM (Civil / Structural / BIM)
- 化工/流程模拟 (Chemical / Process Simulation)
- 半导体/VLSI/FPGA (Semiconductor / VLSI / FPGA)

## Search Queries Run

### 土木/结构/BIM (9 queries)
| Query | Results | New Candidates |
|-------|---------|----------------|
| BIM MCP server | 10 | 7 |
| Revit MCP server | 10 | 7 |
| civil engineering MCP server | 1 | 1 |
| structural engineering AI agent tool | 1 | 1 |
| building information modeling LLM | 10 | 10 |
| Tekla MCP server | 5 | 5 |
| IFC MCP server | 10 | 8 |
| construction AI agent | 10 | 10 |
| BIM AI tool | 10 | 9 |

### 化工/流程模拟 (8 queries)
| Query | Results | New Candidates |
|-------|---------|----------------|
| chemical engineering MCP server | 1 | 1 |
| process simulation MCP server | 5 | 5 |
| Aspen Plus MCP server | 2 | 2 |
| chemical process AI agent tool | 0 | 0 |
| distillation MCP server | 6 | 6 |
| reactor simulation LLM | 0 | 0 |
| DWSIM MCP | 2 | 0 |
| chemical engineering LLM integration | 0 | 0 |

### 半导体/VLSI/FPGA (9 queries)
| Query | Results | New Candidates |
|-------|---------|----------------|
| FPGA MCP server | 10 | 9 |
| VLSI MCP server | 2 | 2 |
| semiconductor MCP server | 6 | 5 |
| Verilog MCP server | 4 | 3 |
| chip design AI agent tool | 2 | 2 |
| EDA semiconductor MCP | 1 | 1 |
| FPGA development LLM | 2 | 2 |
| Vivado MCP | 10 | 6 |
| Gowin FPGA MCP | 1 | 0 |

## Candidates Evaluated

### 土木/结构/BIM
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction | ★149 | **Added to Skills** | 221 construction AI skills (SKILL.md collection), BIM/cost estimation/scheduling, MIT license, active |
| teknovizier/tekla_mcp_server | ★35 | **Added to MCP** | Tekla Structures MCP server, very active (pushed today), GPL-3.0, substantial README with 7 tool modules |
| datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR | ★154 | Skip | Data/database tool (55K work items + n8n workflows), not MCP server or agent skill template |
| Sam-AEC/Autodesk-Revit-MCP-Server | ★25 | Skip | Functional overlap — already 2 Revit MCP servers in README (★177 + ★121) |
| smartaec/ifcMCP | ★32 | Skip | Inactive >90 days (last push 2025-06-08) |
| kaitpw/Rvt_Docs_MCP | ★29 | Skip | Inactive >90 days (last push 2025-08-15), docs-only MCP |
| LuDattilo/revit-mcp-server | ★19 | Skip | Star < 20 |
| louistrue/ifcx-mcp | ★15 | Skip | Star < 20 |

### 化工/流程模拟
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| brack101/AspenPlus-MCP-Server | ★15 | Skip | Star < 20, no description, inactive (last push 2025-10-09) |

### 半导体/VLSI/FPGA
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| coreyhahn/vivado_mcp | ★48 | Skip | Functional overlap with existing vivado-mcp ★46, inactive >90 days (last push 2026-02-19) |
| mfranzon/circuitiny | ★39 | Skip | Standalone circuit design tool/app, not MCP server or agent skill |
| ariklapid/pyslang-mcp | ★15 | Skip | Star < 20 |
| luarss/openroad-mcp | ★10 | Skip | Star < 20 |

## New Entries Added

### 社区精选 Skills
| Skill | Description | Source | Star | Domain |
|-------|-------------|--------|------|--------|
| [DDC-Skills-for-AI-Agents-in-Construction](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction) | 221 个建筑行业 AI 技能：BIM 分析、成本估算、进度管理、文档控制、自动化工作流 | datadrivenconstruction | 149 | 土木/结构/BIM |

### MCP Servers — 土木/结构/BIM
| MCP Server | Description | Source | Star | Domain |
|------------|-------------|--------|------|--------|
| [tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server) | Tekla Structures MCP server：工具化建模自动化，支持选择、组件插入、属性管理、视图操作 | teknovizier | 35 | 土木/结构/BIM |

## Notable Observations
- BIM/土木领域 MCP 生态持续增长：Revit MCP 有 2 个活跃主干（★177 + ★121），Tekla MCP 新增（★35），IFC MCP 生态开始萌芽（ifcMCP ★32, ifcx-mcp ★15）
- 化工/流程模拟领域仍然极不成熟：最高星 AspenPlus-MCP-Server 仅 ★15，无任何候选达到 20★ 门槛
- 半导体/VLSI/FPGA 除已有 vivado-mcp 外，其他 FPGA/EDA MCP 均 < 10★。OpenROAD MCP（★10）和 pyslang-mcp（★15）有潜力但尚未达标
- datadrivenconstruction 组织同时维护 Skills 集合（★149）和 CWICR 数据库（★154），后者为数据资源而非 agent skill，按规则不收录
- star sync cron 与发现 cron 同时执行导致 push reject，pull --rebase 无冲突解决

## Statistics
- Total queries: 26
- Total unique candidates scanned: ~102
- New entries: 2 (1 Skills + 1 MCP Server)
- README modifications: Yes (2 additions)
- Git: commit + push successful

## Current README Status
- 原创 Skills: 3
- 社区精选 Skills: 5 (added 1)
- MCP Servers 分组: 13
- MCP Servers 总数: 30 (added 1)
