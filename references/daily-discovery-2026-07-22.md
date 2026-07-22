# 每日发现记录 — 2026-07-22（周三）

## 搜索领域
- 土木/结构/BIM
- 化工/流程模拟
- 半导体/VLSI/FPGA

## 查询统计
| 类型 | 查询数 | 候选数（初筛） | 候选数（验证后） | 新增收录 |
|------|--------|----------------|------------------|----------|
| MCP Server 搜索（Way B） | 10 | 0 | 0 | 0 |
| Agent Skill 搜索（Way D） | 9 | 6 | 0 | 0 |
| 补充工具名搜索 | 8 | 0 | 0 | 0 |
| **合计** | **27** | **6** | **0** | **0** |

## 候选详情

### 跳过候选

| 仓库 | Star | 来源 | 跳过原因 |
|------|------|------|----------|
| topoteretes/brand-docs | 222★ | construction agent skill | 404 Not Found（仓库已删除） |
| Atelier-Arkitect/FPGA-Agent-skills | 25★ | FPGA agent skill | 404 Not Found |
| yuen-charles/veriflow-cc | 36★ | chip design agent skill | 404 Not Found |
| ChipOnChain/ccfoundry-agent-kit | 24★ | chip design agent skill | 404 Not Found |
| retentioneering/retentioneering-tools | 907★ | process simulation MCP/skill | 点击流分析工具，非化工/流程模拟，领域不相关 |
| The-OpenROAD-Project/OpenROAD-MCP | 12★ | OpenROAD MCP | Star < 20，虽然官方项目且活跃但不达阈值 |
| vicquick/vwx-mcp | 10★ | IFC MCP | Vectorworks MCP，Star < 20 不达阈值 |

## 领域状态评估

### 土木/结构/BIM
- MCP 表 9 个条目（ifc-lite, revit x3, cordyceps, ifc-bonsai, RevitMCP, tekla, Autodesk-Revit, RevitMCPBridge）
- Skills 表 1 个条目（DDC_Skills_for_AI_Agents_in_Construction 246★）
- 本周 MCP 搜索零新增。construction MCP server 搜索中 pyp6xer-mcp（12★, Primavera P6）和 procore-mcp-server（6★）为低星工程 MCP，但 star 不达标
- 土木/BIM 生态趋于稳定，低星候补（ifcx-mcp 18★, ifcMCP 34★已不活跃）短期内突破概率低

### 化工/流程模拟
- README 无此领域 section（因无任何条目）
- 连续多周确认：DWSIM 最高 3★，Aspen 最高 1★（除已不活跃的 AspenPlus-MCP-Server 25★）
- 该领域 MCP 生态持续空白，无新候选达到任何阈值

### 半导体/VLSI/FPGA
- MCP 表 2 个条目（vivado-mcp 76★, SynthPilot 52★）
- Skills 表 5 个条目（xilinx-skill 364★, verilog-generator 201★, veriloga-skills 26★, hls-generator 21★, SynthPilot 52★）
- 值得关注的低星候补：**The-OpenROAD-Project/OpenROAD-MCP**（12★, 官方项目，130 commits, 17 branches, 12 tags, pushed 4天前，24 open issues 活跃开发）。虽因 Star < 20 暂不收录，但作为 OpenROAD 官方的 MCP server，增长潜力大，建议下一轮复查优先检查
- gowin_mcp_server（2★）和 fpga-mcp-servers（6★）均星数过低

## 查询效果评估
- **土木/BIM**: `BIM MCP server` 查询最有效（10 个结果均为 BIM 相关），但已有条目已覆盖所有达标候选
- **化工**: `process simulation MCP server` 查询误匹配 retentioneering-tools（907★, 用户点击流分析），`chemical engineering MCP` 仅返回 2 个低星
- **半导体/FPGA**: `FPGA MCP server` 和 `Verilog MCP server` 查询结果基本被现有条目覆盖，新候选均为 < 13★
- **Way D（agent skill）**：对半导体领域有一定潜力（FPGA agent skill 找到 4 个候选），但 3 个已验证为 404

## 备注
- 多仓库 404 现象值得注意：brand-docs（222★, 之前存在于搜索结果中）、FPGA-Agent-skills（25★）、veriflow-cc（36★）、ccfoundry-agent-kit（24★）均已于近期删除
- retentioneering-tools（907★）的误匹配表明"process simulation"关键词在 GitHub 搜索中存在语义歧义
