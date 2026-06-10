# Daily Discovery — 2026-06-10 (Wednesday)

## 搜索领域
- 土木/结构/BIM (7 queries)
- 化工/流程模拟 (6 queries)
- 半导体/VLSI/FPGA (8 queries)

## 总计
- 查询数: 21
- 候选数: 15 (API 验证前) → 5 (API 验证后) → 2 (LLM 判断 + browser 验证)
- 新增收录: 2

## 新增收录

| Repo | Stars | Domain | Description |
|------|-------|--------|-------------|
| LNC0831/SynthPilot | 46 | 半导体/VLSI/FPGA | Vivado MCP server: 500+ tools for full FPGA flow, oh-my-fpga methodology layer, local execution, PyPI |
| Sam-AEC/Autodesk-Revit-MCP-Server | 31 | 土木/结构/BIM | Revit MCP server (C#/.NET): 100+ tools covering geometry, views, families, MEP, structures, Revit 2024-2026 |

## 跳过条目

| Repo | Stars | Reason |
|------|-------|--------|
| datadrivenconstruction/cad2data-Revit-IFC-DWG-DGN | 402 | Not MCP/agent skill - CAD file conversion workflow |
| ai-hpc/ai-hardware-engineer-roadmap | 183 | Not MCP/agent skill - learning roadmap |
| datadrivenconstruction/OpenConstructionEstimate-DDC-CWICR | 162 | Not MCP/agent skill - construction cost database |
| QuanZ827/zexus | 98 | Not MCP/agent skill - Revit AI agent with C# code execution |
| Show2Instruct/ifc-bonsai-mcp | 50 | Inactive 156 days (last push 2026-01-05) |
| coreyhahn/vivado_mcp | 48 | Inactive 111 days (last push 2026-02-19) - different from existing vivado-mcp |
| smartaec/ifcMCP | 33 | Inactive 367 days (last push 2025-06-08) |
| kaitpw/Rvt_Docs_MCP | 29 | Inactive 299 days (last push 2025-08-15) |
| brack101/AspenPlus-MCP-Server | 19 | Star below threshold (19), inactive 244 days |
| fdias78git/dwsim-claude-integration | 17 | Not MCP/agent skill - Python library + Claude Code agent |
| ariklapid/pyslang-mcp | 17 | Star below threshold (17) - Verilog/SystemVerilog analysis MCP |
| louistrue/ifcx-mcp | 16 | Star below threshold (16) - IFC5/IFCX authoring MCP |
| LuDattilo/revit-mcp-server | 21 | Fork of mcp-servers-for-revit (already in README at ★199), 138 tools |

## 候选详细分析

### SynthPilot (★46)
- Vivado MCP server with 500+ tools covering the entire FPGA development flow
- Includes oh-my-fpga methodology layer for turning tools into one-sentence outcomes
- Runs locally: RTL never leaves the machine
- Published on PyPI, supports Claude/Cursor/Cline
- Very active: pushed 2026-06-09 (yesterday), 6 commits
- Topics: ai, claude, cursor, eda, fpga, mcp, model-context-protocol, verilog, vivado, xilinx
- Complementary to existing vivado-mcp (★56, CRITICAL WARNING diagnosis focus)

### Sam-AEC/Autodesk-Revit-MCP-Server (★31)
- C#/.NET implementation of Revit MCP server
- 100+ Revit API tools (geometry, views, sheets, families, MEP, structures)
- Localhost HTTP bridge with sub-second response time
- Thread-safe ExternalEvent architecture
- Advanced reflection API for unlimited Revit access
- Supports Revit 2024-2026
- 114 commits, active (last commit 2 weeks ago)
- 10 forks, MIT license
- Complementary to existing mcp-servers-for-revit (TypeScript, 26+ tools)

## 化工/流程模拟领域
连续多周无新候选。本次搜索 6 个查询（chemical engineering MCP server, process simulation MCP, Aspen MCP server, DWSIM MCP server, chemical process AI agent, distillation simulation MCP）无新增。仅 brack101/AspenPlus-MCP-Server（★19）接近阈值但不活跃。

## 搜索领域效果备注
- 土木/结构/BIM: Revit MCP 生态持续活跃，多个独立实现并存
- 半导体/VLSI/FPGA: SynthPilot 是该领域首个超 500 工具的 MCP server
- 化工/流程模拟: MCP 生态持续空白

## README 当前状态
- 69 个 MCP Servers (2 新增)
- 多个领域分组: 机械/CAD/CAM, 电气/PCB/EDA, 机器人, 航空航天/CFD, 土木/结构/BIM, 能源/电力/电池, 油藏/石油, 工业自动化, 嵌入式/硬件, 半导体/VLSI/FPGA, 生物医学/医疗, 环境/水利, 综合资源
