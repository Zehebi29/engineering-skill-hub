# 每日发现记录 — 2026-07-29（周三）

## 搜索领域
土木/结构/BIM + 化工/流程模拟 + 半导体/VLSI/FPGA

## 查询统计
| 领域 | 查询数 | 初筛候选 | 通过API验证 | 新增收录 |
|------|--------|----------|------------|---------|
| 土木/结构/BIM | 9 | 57 | 2 | 0 |
| 化工/流程模拟 | 8 | 30 | 4 | 0 |
| 半导体/VLSI/FPGA | 13 | 72 | 4 | 2 |
| **合计** | **30** | **159** | **10** | **2** |

## 新增收录

### 半导体 / VLSI / FPGA (MCP Servers 表)

| MCP Server | 描述 | 来源 | Star |
|------------|------|------|------|
| [xverif](https://github.com/BLANK2077/xverif) | 芯片验证调试 MCP 工具包：设计调试、波形分析、覆盖率、位计算、SVA 语义，387 commits 极活跃 | [BLANK2077](https://github.com/BLANK2077) | 69 |
| [pyslang-mcp](https://github.com/ariklapid/pyslang-mcp) | Verilog/SystemVerilog 分析 MCP server：基于 pyslang 编译器的语义分析、诊断、层次结构、设计单元查询 | [ariklapid](https://github.com/ariklapid) | 20 |

## 跳过候选详情

### 土木/结构/BIM
- **LuDattilo/revit-mcp-server** (33★, pushed 2026-07-03, last commit "3 months ago") — Fork of mcp-servers-for-revit (already in README). Functional overlap with existing entries. Skip.
- **Demolinator/revit-mcp-server** (21★, pushed 2026-06-09, active) — Another fork of mcp-servers-for-revit. Functional overlap. Skip.
- oakplank/RevitMCP (48★) — Already in README.
- All other candidates: low star (<20) or inactive (>90 days).

### 化工/流程模拟
- **retentioneering/retentioneering-tools** (910★) — Known false positive: clickstream analytics (process mining), NOT chemical process simulation. Skip per Pitfall.
- **techygarg/lattice** (166★, pushed 2026-07-06) — General engineering framework ("install engineering discipline"), not chemical/process engineering specific. Skip.
- **w95/awesome-claude-corporate-skills** (128★, pushed 2026-02-26) — General corporate skills collection, not engineering specific. Also inactive >90 days. Skip.
- **danderfer/Comp_Sci_Sem_2** (194★, pushed 2023-04-03) — Clearly a joke/university repo. Skip.
- AspenPlus-MCP-Server (27★, pushed 2025-10-09) — Inactive >90 days. Skip.
- All other candidates: low star or type mismatch.

### 半导体/VLSI/FPGA
- **BLANK2077/xverif** (69★, pushed 16 hours ago, 387 commits, active) → **已收录**
- **ariklapid/pyslang-mcp** (20★, active, MCP server for Verilog/SV analysis) → **已收录**
- **adeleempurpled290/FPGA-Agent-skills** (25★) — 404 Not Found (Search API ghost). Skip.
- **bjwanneng/veriflow-cc** (40★) — 404 Not Found (Search API ghost). Skip.
- **RohanYashRaj/FPGA-Agent-skills** (25★) — 404 Not Found. Skip.
- OpenROAD-MCP (12★) — Too low star, watch for future growth.
- Rvt_Docs_MCP (31★, pushed 2025-08-15) — Inactive. Skip.

## 备注
- xverif 同时包含 MCP server（xverif_mcp/）和 skills 目录，属于混合项目。因 MCP 入口是一等公民功能，归入 MCP Servers 表。
- pyslang-mcp (20★) 刚好跨过阈值门槛，活跃度好（last month 最新提交），填补 Verilog/SystemVerilog 纯分析工具的空白（与 Vivado 综合实现工具互补）。
- 化工/流程模拟领域连续多周零新增，继续呈现 MCP 生态空白状态。
