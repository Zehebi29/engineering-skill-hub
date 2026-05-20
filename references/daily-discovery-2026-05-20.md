# Daily Discovery Report — 2026-05-20（周三）

## 搜索领域
1. 土木/结构/BIM
2. 化工/流程模拟
3. 半导体/VLSI/FPGA

## 统计

| 领域 | 查询数 | 候选数（去重） | 新增收录 |
|------|--------|---------------|---------|
| 土木/结构/BIM | 5 | 41 | 2 |
| 化工/流程模拟 | 5 | 30 | 0 |
| 半导体/VLSI/FPGA | 5 | 24 | 0 |
| **合计** | **15** | **95** | **2** |

## 新增条目

### 土木 / 结构 / BIM（新分组）

1. **mcp-servers-for-revit/mcp-servers-for-revit** ★170
   - Revit MCP server（TypeScript）
   - 26+ 工具，支持 Revit 2020-2026
   - 来源：mcp-servers-for-revit
   - 已验证：真实 MCP server，活跃维护（最新提交 2026-04-05），v1.0.0 发布，CI/CD 自动化
   - 判断：领域高度相关（BIM/Revit），Star >= 100 ✅

2. **mcp-servers-for-revit/mcp-server-for-revit-python** ★120
   - Revit MCP server（Python/pyRevit）
   - pyRevit Routes REST API 桥接 Revit 与 AI agent，18 个工具
   - 来源：mcp-servers-for-revit
   - 已验证：真实 MCP server，78 commits，活跃维护（最新提交 2026-03-05）
   - 判断：领域高度相关（BIM/Revit），Star >= 100 ✅

## 跳过条目（含原因）

### 土木/结构/BIM
- **mcp-servers-for-revit/revit-mcp** ★413 — 已归档（archived），不收录
- **mcp-servers-for-revit/revit-mcp-plugin** ★214 — 已归档（archived），不收录
- **mcp-servers-for-revit/revit-mcp-commandset** ★53 — 已归档（archived），不收录
- **Show2Instruct/ifc-bonsai-mcp** ★42 — 领域高度相关（BIM/IFC），但 Star < 100 且 last commit 2025-11（超过 90 天）
- **oakplank/RevitMCP** ★44 — Revit MCP，Star < 100，活跃度一般
- **ZedMoster/revit-mcp** ★37 — Revit MCP，Star < 100，last push 2025-12
- **shuotao/REVIT_MCP_study** ★72 — 学习资料/教程，非工具型 MCP server
- **DTDucas/RevitMCPSDK** ★30 — Revit MCP SDK，低星 + 低活跃度
- **schauh11/revit-mcp-server** ★14 — 低星
- **bimwright/rvt-mcp** ★5 — 低星
- 其余 low-star BIM 相关：< 10★ 均跳过

### 化工/流程模拟
- **brack101/AspenPlus-MCP-Server** ★13 — Aspen Plus MCP server，Star < 20
- **nckugese/Aspen_Co-pilot** ★8 — Star < 20
- **sinagilassi/mozichem-mcp** ★3 — 化学工程 MCP 合集，Star 极低
- **OntoLedgy/ol_dwsim_interop_services** ★2 — DWSIM 流程模拟 MCP，Star 极低
- **moldsim/moldsim-mcp** ★2 — 注塑成型模拟 MCP，Star 极低
- **sinagilassi/PyMemSim-MCP** ★1 — 膜模拟 MCP，Star 极低
- **gsi-lab/APS-Agent** ★0 — Aveva Process Simulation MCP agent，Star 极低
- 其余：< 5★，全跳过

### 半导体/VLSI/FPGA
- **vivado-mcp** ★43 — 已在 README 中
- **fpgaZeroMCP** ★3 — Star 极低
- **fpga-mcp-servers** ★3 — Star 极低
- **gowin_mcp_server** ★1 — Star 极低
- **GateFlow** ★0 — Star 极低
- 其余 Verilog/RTL 相关项目：均为学术/框架类，非 MCP server，Star 极低

## 查询效果评价

### 土木/结构/BIM（优秀）
Revit MCP 生态蓬勃发展。虽然原 revit-mcp ★413 已归档，但 fork 版本 mcp-servers-for-revit ★170 仍在活跃维护。Python 版本 ★120 也在增长。此外还有 10+ 个 Revit MCP 项目在 10-72★ 区间等待成长。

### 化工/流程模拟（差）
该领域 MCP 生态极不成熟。最高星 AspenPlus-MCP-Server 仅 13★，无任何候选达到 20★ 收录门槛。DWSIM 和 MoziChem 的 MCP server 均 < 5★。与 skill 中记录的 Pitfall #25 一致（该领域 MCP 生态稀少）。

### 半导体/VLSI/FPGA（一般）
除了已在 README 中的 vivado-mcp ★43，其他 FPGA MCP 项目均 < 10★。Verilog 相关的 VLSI 项目多为学术研究工具或 LLM 代码生成项目，非 MCP server，不符合收录类型。

## 当前 README 状态
- 原创 Skills: 3
- 社区精选 Skills: 3
- MCP Servers 分组: 13（新增 土木/结构/BIM）
- MCP Servers 总数: 27（新增 2）
