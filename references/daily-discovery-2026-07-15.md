# Daily Discovery — 2026-07-15（周三）

## 领域
土木/结构/BIM + 化工/流程模拟 + 半导体/VLSI/FPGA

## 搜索概况
- 总查询数: 20（MCP 搜索 14 + Skill 搜索 6）× 去重后约 18 个独特查询
- 候选总数: 221（含重复交叉结果）
- 新增收录: 2（均为 Skills 表）

## 新增收录

### 社区精选 Skills

1. **xilinx-skill** (★360) — [QingquanYao/xilinx-skill](https://github.com/QingquanYao/xilinx-skill)
   - 领域: 半导体/VLSI/FPGA
   - 描述: Xilinx/AMD FPGA & MPSoC Vivado 设计 skill — Block Design、IP 配置、XDC 约束、综合、实现、Bitstream 生成、Vitis HLS、PetaLinux 全流程
   - 类型: Agent skill（SKILL.md 集合）
   - 质量: ★360, 26 commits, pushed 2026-04-25（81 天前，在 90 天内）, 31 forks
   - 收录理由: ★ ≥ 100，自动收录。与现有 verilog-generator（★187, RTL only）和 hls-generator（★20, HLS only）互补，覆盖完整的 Vivado/Vitis/PetaLinux 工具链
   - 发现方式: 方式 D — `FPGA skill` 关键词查询

2. **veriloga-skills** (★24) — [Arcadia-1/veriloga-skills](https://github.com/Arcadia-1/veriloga-skills)
   - 领域: 半导体/VLSI/FPGA — 模拟/混合信号 IC 设计
   - 描述: Agent skills for Verilog-A analog/mixed-signal IC design — Cadence Virtuoso conventions, 12 circuit categories, 1809 design pattern references
   - 类型: Agent skill（3 个 SKILL.md：veriloga核心、evas-sim 验证、openvaf 仿真）
   - 质量: ★24, pushed 2026-05-18（58 天前）, 良好 README + 完整参考文档
   - 收录理由: 20-100★ 需领域高度相关 + 近期活跃 + 有实质内容。Verilog-A 是现有 FPGA/RTL 类型（digital + HLS）中完全未被覆盖的模拟/混合信号子方向，3 个 SKILL.md 质量高
   - 发现方式: 方式 D — `Verilog agent skill` 关键词查询

## 主要跳过候选及原因

### 土木/结构/BIM
- **LuDattilo/revit-mcp-server** (★29) — 已有 mcp-servers-for-revit 组织同名项目（★237, ★147），此为个人 fork，Low Star + 功能重叠
- **Demolinator/revit-mcp-server** (★20) — pyRevit Revit MCP，已有 mcp-server-for-revit-python（★147, pyRevit）和 RevitMCP（★49, pyRevit），Low Star + 功能重叠
- **kaitpw/Rvt_Docs_MCP** (★31) — Revit API docs MCP server，pushed 2025-08-15（11 个月前），不活跃
- **Soljourner/claude-engineering-skills** (★37) — 通用工程 skill 集合，pushed 2025-11-07（8 个月前），不活跃，非专属于土木
- **Mibayy/token-savior** (★1066) — token 优化的通用 MCP，非工程专用
- **ozgurcd/gograph** (★198) — Go 静态分析 MCP，非土木/结构
- 其余 80+ 结果为通用代码工具/非工程项目/个人学习仓库

### 化工/流程模拟
- **Augmented-Nature/ChEMBL-MCP-Server** (★88) — ChEMBL 化学数据库 MCP，非流程模拟，pushed 2025-12-21（不活跃）
- **Augmented-Nature/PubChem-MCP-Server** (★44) — PubChem 数据库 MCP，非流程模拟，pushed 2025-12-21（不活跃）
- **brack101/AspenPlus-MCP-Server** (★24) — Aspen Plus MCP server，pushed 2025-10-09（9 个月前），不活跃
- 化工领域 MCP 生态持续空白，连续多周无新增

### 半导体/VLSI/FPGA
- **The-OpenROAD-Project/OpenROAD-MCP** (★11) — 官方组织 MCP，Star 过低，标记为低星候补
- **adeleempurpled290/FPGA-Agent-skills** (★25) — 8 个 Vivado/Vitis skill，10 commits 内容少，被 xilinx-skill（★360 全流程覆盖）覆盖
- **bjwanneng/veriflow-cc** (★36) — RTL 设计流水线，更接近 pipeline 框架非独立 SKILL.md 集合

## 查询效果统计

| 类型 | 查询数 | 命中 | 合格 |
|------|--------|------|------|
| 土木/结构/BIM MCP | 5 | 50 | 0 |
| 土木/结构/BIM Skill | 5 | 39 | 0 |
| 化工/流程模拟 MCP | 5 | 34 | 0 |
| 化工/流程模拟 Skill | 5 | 32 | 0 |
| 半导体/VLSI/FPGA MCP | 5 | 29 | 0 |
| 半导体/VLSI/FPGA Skill | 6 | 43 | 2 |

**关键观察**:
- 方式 D（agent skill 搜索）再次证明比方式 B（MCP server）更有效，尤其在半导体/FPGA 领域
- 半导体/VLSI/FPGA 的 Skills 生态持续壮大，xilinx-skill（★360）是本周最大亮点
- 化工/流程模拟连续多周零新增，该领域 MCP + Skill 生态几乎空白
- 土木/结构/BIM 的 MCP 关键词搜索被通用代码结构工具严重污染（"structural" → 代码静态分析）

## 当前 README 统计
- 社区精选 Skills: 19 → 21
- 社区精选 MCP Servers: 各领域总数不变
