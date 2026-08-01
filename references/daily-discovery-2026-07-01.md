# Daily Discovery — 2026-07-01 (周三)

## 搜索领域
- 土木/结构/BIM
- 化工/流程模拟
- 半导体/VLSI/FPGA

## 查询统计
- 土木/结构/BIM: 16 queries → 94 candidates → 2 new
- 化工/流程模拟: 14 queries → 32 candidates → 0 new
- 半导体/VLSI/FPGA: 16 queries → 54 candidates → 1 new

**总查询数**: 46 | **总候选数**: 180 | **新增收录**: 3

## 新增

### 社区精选 Skills
| Repo | Star | 描述 |
|------|------|------|
| [Eriemon/verilog-generator](https://github.com/Eriemon/verilog-generator) | 185 | Agent skill for Verilog-2001 RTL generation and FPGA design workflows. 含接口模板、验证门控、CLI 运行时。13 Tags, 20 commits, 3 周前活跃。类型：agent skill（有 SKILL.md）。 |

### 土木 / 结构 / BIM — MCP Servers
| Repo | Star | 描述 |
|------|------|------|
| [brookstalley/cordyceps](https://github.com/brookstalley/cordyceps) | 80 | Grasshopper MCP Bridge。Claude 控制 Rhino/Grasshopper 参数化设计画布和渲染工具。128 commits, 11 tags, 4 天前活跃。C# 实现。 |
| [Show2Instruct/ifc-bonsai-mcp](https://github.com/Show2Instruct/ifc-bonsai-mcp) | 52 | IFC BIM MCP server。50+ 工具，连接 AI 与 Blender Bonsai 插件，自然语言创建/编辑 IFC 元素。RAG 知识检索。Python 实现。 |

## 跳过的候选及原因

### 土木/结构/BIM
- Sam-AEC/aec-model-bridge (39★) — 与已有 Sam-AEC/Autodesk-Revit-MCP-Server (★38) 同作者功能重叠
- LuDattilo/revit-mcp-server (23★) — 与已有 mcp-servers-for-revit 功能重叠
- Demolinator/revit-mcp-server (17★) — Star 过低
- Aitology/Navisworks_MCP (12★) — Star 过低
- shuotao/REVIT_MCP_study (79★) — 学习教程，非 MCP server（Pitfall #40）
- DTDucas/chm-converter (79★) — topics 含 revit-mcp 但实际是 CHM 转 Markdown（Pitfall #41）
- alfredatnycu/grasshopper-mcp (90★) — pushed:2025-03-22, >90天不活跃
- smartaec/ifcMCP (33★) — pushed:2025-06-08, >90天不活跃
- kaitpw/Rvt_Docs_MCP (31★) — Revit API 文档索引，非 MCP server 实现
- gramaziokohler/lamcp (13★) — Star 过低
- louistrue/ifcx-mcp (16★) — Star 过低
- mako-357/archicad-mcp (2★) — Star 过低
- JardiMargalefAgusti/bSDD-mcp (3★) — Star 过低

### 化工/流程模拟
- brack101/AspenPlus-MCP-Server (24★) — pushed:2025-10-09, >90天不活跃
- nckugese/Aspen_Co-pilot (10★) — Star 过低
- sinagilassi/mozichem-mcp (3★) — Star 过低
- OntoLedgy/ol_dwsim_interop_services (3★) — Star 过低
- gsi-lab/APS-Agent (2★) — Star 过低
- ddtlxc001/aspen-mcp (0★) — Star 过低
- defnalk/aspen-copilot (0★) — Star 过低
- smslavin/waterworks-ai (0★) — 工业水处理 demo，Star 过低

### 半导体/VLSI/FPGA
- coreyhahn/vivado_mcp (50★) — pushed:2026-02-19, >90天不活跃
- adeleempurpled290/FPGA-Agent-skills (20★) — Star 刚好 20，但 topics 混乱（inherit from template），质量不足
- Eriemon/hls-generator (20★) — Star 刚好 20，与同作者 verilog-generator 功能相近但 Star 过低
- The-OpenROAD-Project/OpenROAD-MCP (11★) — Star 过低（★11），虽然活跃（pushed:今天），OpenROAD MCP 有潜力
- ariklapid/pyslang-mcp (18★) — Star 过低（SystemVerilog 语义分析）
- WangErShao/SynthAid_quartus_mcp (1★) — Star 过低（Intel Quartus FPGA）
- jgpeiro/gowin_mcp_server (1★) — Star 过低（Gowin FPGA）

## 领域生态总结

### 土木/结构/BIM
该领域持续保持活跃。新增 Grasshopper MCP（cordyceps ★80）填补了参数化建筑设计工具的 MCP 空白。IFC 生态方面，ifc-bonsai-mcp（★52）补充了 Blender Bonsai 工作流的 IFC MCP，与 ifc-lite（通用 IFC 工具包）互补。Revit MCP 生态已趋饱和（6 个不同实现）。

### 化工/流程模拟
持续空白。Aspen Plus MCP 只有低星（★0-24）且不活跃的项目。DWSIM MCP ★3。该领域 MCP 生态几乎不存在。

### 半导体/VLSI/FPGA
生态在 agent skill 层面有亮点。verilog-generator（★185）是优质 FPGA 设计 agent skill。MCP server 层面，vivado-mcp（★61）和 SynthPilot（★47）已在 README。OpenROAD-MCP（★11）有增长潜力但目前 Star 过低。

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 7（+1）
- MCP Servers:
  - 机械/CAD/CAM: 17
  - 电气/PCB/EDA: 15
  - 机器人: 6
  - 航空航天/CFD: 2
  - 土木/结构/BIM: 9（+2）
  - 能源/电力/电池: 2
  - 油藏/石油: 1
  - 工业自动化: 4
  - 嵌入式/硬件: 2
  - 半导体/VLSI/FPGA: 2
  - 生物医学/医疗: 15
  - 环境/水利: 3
  - 综合资源: 4
