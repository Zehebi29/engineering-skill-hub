# Daily Discovery — 2026-07-08 (周三)

## 搜索领域
- 土木/结构/BIM
- 化工/流程模拟
- 半导体/VLSI/FPGA

## 查询统计
| 领域 | 查询数 | ≥20★候选 | 新增 |
|------|--------|---------|------|
| 土木/结构/BIM | 8 | ~10 | 0 |
| 化工/流程模拟 | 8 | 1 (★24, >270d 不活跃) | 0 |
| 半导体/VLSI/FPGA | 12 | ~8 | 1 |
| **合计** | **28** | **~19** | **1** |

## 新增收录

### 社区精选 Skills

| Skill | Star | 描述 |
|-------|------|------|
| [hls-generator](https://github.com/Eriemon/hls-generator) | 20 | Agent skill for AMD/Xilinx Vitis HLS C/C++ high-level synthesis workflows. 24 commits, 13 tags, pushed 2 days ago. Has root-level SKILL.md with YAML frontmatter, proper agents/, evals/, references/, scripts/ structure. Same author as verilog-generator (★191, already in README). Complements the RTL-focused verilog-generator with Vitis HLS workflow. |

## 跳过的候选及原因

### 土木/结构/BIM
| 仓库 | Stars | 原因 |
|------|-------|------|
| LuDattilo/revit-mcp-server | ★27 | latest commit 3 months ago (per browser on 07-05), ★<100, and already 6 Revit entries in README |
| Demolinator/revit-mcp-server | ★19 | Star < 20, another Revit implementation with existing 6 entries |
| kaitpw/Rvt_Docs_MCP | ★31 | pushed 2025-08-15 (>10 months), Revit API docs index, not MCP server |
| louistrue/ifcx-mcp | ★18 | Star < 20 |
| veoery/GH_mcp_server | ★31 | pushed:2025-10-05 (>9 months inactive), cordyceps (★80) already covers Grasshopper |
| ferdinandobons/brand-docs | ★209 | False positive — Word/PowerPoint template generator, not civil engineering |
| schauh11/revit-mcp-server | ★17 | Star < 20 |
| tanishqbhattad/rhino-mcp | ★8 | Star < 20 |
| DDC_Skills_for_AI_Agents_in_Construction | ★229 | Already in README |
| ArchSightLabs/archsight-aios | ★6 | Star < 20 |

### 化工/流程模拟
| 仓库 | Stars | 原因 |
|------|-------|------|
| brack101/AspenPlus-MCP-Server | ★24 | pushed:2025-10-09 (>270 days), inactive |
| 其余所有 | <10 | Star < 10, 绝大多数为非工程或不相关工具 |
| ddtlxc001/aspen-mcp | ★1 | Star < 20 |
| thirakorn-mokkawes-59/aspen-mcp | ★0 | Star < 20 |
| sinagilassi/mozichem-mcp | ★4 | Star < 20, pushed 2025-09-14 |

该领域持续确认 MCP 生态空白。Aspen Plus/DWSIM 均只有低星或不活跃项目。

### 半导体/VLSI/FPGA
| 仓库 | Stars | 原因 |
|------|-------|------|
| adeleempurpled290/FPGA-Agent-skills | ★21 | 学习指南/教程，非 agent skill（SKILL.md 格式）。topics 混乱（inherit from template）。10 commits。质量不足。 |
| bjwanneng/veriflow-cc | ★34 | Claude Code RTL pipeline 项目，非通用 agent skill 合集。3 周前最后一次提交。无 SKILL.md 格式。 |
| Arcadia-1/veriloga-skills | ★24 | Verilog-A 模拟仿真 skills，71 commits。最后提交 2 个月前，接近活跃边界。功能过于 niche（Verilog-AMS）。 |
| coreyhahn/vivado_mcp | ★52 | pushed:2026-02-19 (>130 days), inactive |
| Eriemon/hls-generator | ★20 | ✅ 已收录 |
| Eriemon/verilog-generator | ★191 | 已在 README |
| ariklapid/pyslang-mcp | ★18 | Star < 20 |
| The-OpenROAD-Project/OpenROAD-MCP | ★11 | Star < 20 (活跃，值得观察) |
| 其余 | <20 | 均为低星或不相关 |

## 低星观察
| 仓库 | Star | 趋势 | 备注 |
|------|------|------|------|
| The-OpenROAD-Project/OpenROAD-MCP | ★11 | +0 | OpenROAD 官方 MCP，活跃但 star 低 |
| Arcadia-1/veriloga-skills | ★24 | +0 | Verilog-A skills，活跃度下降 |
| bjwanneng/veriflow-cc | ★34 | +0 | Claude Code RTL pipeline |

## 关键观察
1. **半导体/VLSI/FPGA 领域 agent skill 生态在活跃增长** — 同作者 Eriemon 从 verilog-generator (RTL) 扩展到 hls-generator (Vitis HLS)，两个 skills 互为补充覆盖 FPGA 全流程。
2. **土木/结构/BIM 领域无新候选** — Revit MCP 生态已饱和（6 个实现），Grasshopper 有 cordyceps 覆盖，IFC 有 ifc-lite + ifc-bonsai-mcp。
3. **化工/流程模拟领域持续空白** — 连续多周确认无合格 MCP server 或 agent skill。
4. **hls-generator** 虽然 ★20 为最低收录星数，但作为 Vitis HLS 专用 agent skill 填补了 FPGA 设计工作流中一个重要细分方向（从 C/C++ HLS 到 RTL 的桥接）。

## README 当前状态
- 原创 Skills: 3
- 社区精选 Skills: 10 (+1)
- 社区精选 MCP Servers: ~91（不变）
