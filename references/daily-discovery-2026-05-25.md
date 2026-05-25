# Daily Discovery — 2026-05-25（周一）

## 搜索领域
- 机械 / CAD / CAM
- 电气 / PCB / EDA
- 材料 / 焊接 / 检测

## 查询与结果

### 机械 / CAD / CAM（6 个查询 → 52 个候选，去重后 32 个唯一候选）

| 查询 | 结果数 | 有效候选 |
|------|--------|---------|
| "CAD" "MCP" server | 10 | 7 (3 known) |
| "3D printing" MCP server | 10 | 10 |
| SolidWorks MCP | 10 | 9 (1 known) |
| "Fusion 360" MCP | 10 | 9 (1 known) |
| CAM "MCP" server | 10 | 5 (1 known, 4 噪音) |
| CNC MCP server | 8 | 8 (全部 < 10★) |

### 电气 / PCB / EDA（6 个查询 → 52 个候选，去重后 ~25 个唯一候选）

| 查询 | 结果数 | 有效候选 |
|------|--------|---------|
| KiCad MCP server | 10 | 7 (2 known, 1 archived) |
| PCB design MCP | 10 | 10 |
| schematic MCP | 10 | 10 |
| EDA MCP server | 10 | 6 (3 known) |
| Altium MCP | 10 | 9 (1 known) |
| circuit MCP server | 10 | 9 (1 known) |

### 材料 / 焊接 / 检测（5 个查询 → 11 个候选，全部低星或无关）

| 查询 | 结果数 | 有效候选 |
|------|--------|---------|
| materials engineering MCP | 5 | 5 (全部无关：教育材料) |
| welding MCP server | 3 | 3 (全部 < 3★) |
| NDT inspection MCP | 0 | 0 |
| metallurgy AI agent tool | 0 | 0 |
| "materials science" MCP server | 3 | 3 (全部 < 1★) |

## 新增收录（5 个）

### 机械 / CAD / CAM
1. **[multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp)** ★36 — Multi-CAD MCP server：统一接口操控 AutoCAD、ZWCAD、BricsCAD、GstarCAD。Python FastMCP 实现，7 工具 55 指令。活跃维护（最后提交 2 个月前）。来源：[AnCode666](https://github.com/AnCode666)

2. **[fusion360-mcp-server](https://github.com/faust-machines/fusion360-mcp-server)** ★31 — Fusion 360 MCP server：84 工具覆盖草图、特征、CAM、钣金，PyPI 一键部署。含 CAM/制造工具，Mock Mode 测试支持。活跃维护。来源：[faust-machines](https://github.com/faust-machines)

### 电气 / PCB / EDA
3. **[circuitron](https://github.com/Shaurya-Sethi/circuitron)** ★96 — Agentic PCB Design Accelerator：多智能体系统（OpenAI Agents SDK），自然语言生成网表→布局→KiCad 输出，含 MCP RAG 知识图谱。546 commits，架构文档完善。来源：[Shaurya-Sethi](https://github.com/Shaurya-Sethi)

4. **[kicad-mcp-server](https://github.com/Seeed-Studio/kicad-mcp-server)** ★42 — KiCad MCP server（Seeed Studio）：KiCad 9.0+ 原理图/PCB 分析、网表追踪、DRC/ERC 自动化。来自知名开源硬件公司 Seeed Studio。最后提交 3 天前，活跃维护。来源：[Seeed-Studio](https://github.com/Seeed-Studio)

5. **[eda-agent](https://github.com/salitronic/eda-agent)** ★26 — Altium Designer MCP server：200+ 工具覆盖原理图、PCB、库管理，持久化 DelphiScript 桥接。含设计审查面板、SPICE 仿真工作流、原理图→PCB 交叉引用。最后提交 5 天前，活跃维护。来源：[salitronic](https://github.com/salitronic)

## 跳过说明

### 因功能重叠跳过
- **eyfel/mcp-server-solidworks** ★90 — SolidWorks MCP，但最后提交 > 1 年前（2025-04-12），不活跃
- **ArchimedesCrypto/fusion360-mcp-server** ★73 — Fusion 360 MCP，最后提交 > 1 年前
- **JustusBraitinger/Autodesk-Fusion-360-MCP-Server** ★45 — Fusion 360 MCP，最后提交 2026-02-19（> 90 天）
- **Misterbra/fusion360-claude-ultimate** ★43 — Fusion 360 MCP，功能与已有 Fusion-360-MCP-Server 重叠，且仅 5 commits
- **Joelalbon/Fusion-MCP-Server** ★29 — Fusion 360 MCP，最后提交 2025-06-12（不活跃）
- **alisamsam/Solidworks-MCP** ★25 — SolidWorks MCP，与已有的 SolidworksMCP-TS ★130 重叠，仅 2 commits
- **Finerestaurant/kicad-mcp-python** ★37 — KiCad MCP，最后提交 2025-07-15（不活跃）
- **circuit-synth/mcp-kicad-sch-api** ★20 — KiCad 原理图 MCP，最后提交 2025-08-20（不活跃）

### 因 Star 过低跳过（< 20）
- **sina-salim/AI-SolidWorks** ★19 — 最后提交 2025-04-20（不活跃）
- **asmith26/jupytercad-mcp** ★18 — 最后提交 2025-10-07
- **gNucleus/text-to-cad-mcp** ★16
- **rishigundakaram/cadquery-mcp-server** ★13
- **clanker-lover/spicebridge** ★19 — SPICE 仿真 MCP，有质量但 < 20★
- **Cognitohazard/ltspice-mcp** ★11
- **embedded-society/altium-designer-mcp** ★17
- **luarss/openroad-mcp** ★10 — OpenROAD VLSI MCP，有质量但 < 20★
- **ajhcs/cameo-mcp-bridge** ★14 — CATIA Magic/Cameo SysML MCP，有质量但 < 20★

### 因仓库不存在跳过
- **ATOMI-Ming/FreeCAD-MCP** — GitHub API 返回 404 Not Found（已删除）

### 材料/焊接/检测 — 全部跳过
该领域 MCP 生态几乎空白：materials 关键词被教育材料污染，welding/NDT/metallurgy 搜索结果为零或低星（< 3★）。记录在 deleted-repos.md 中的例外。

## 搜索结果统计
- **今日查询数**: 17
- **去重候选数**: ~68
- **Browser 验证数**: 9（全部确认真实 MCP server）
- **新增收录数**: 5
- **跳过总数**: 63

## README 当前统计
- 社区 Skills: 4 个（无变化）
- MCP Servers: 机械/CAD/CAM 11 个（+2），电气/PCB/EDA 11 个（+3），其他领域无变化
- 合计 MCP Servers: 42 → 47 个（+5）

## 备注
- 材料/焊接/检测领域连续多次搜索无收获，建议该领域搜索频率降低，重点关注 awesome-mcp-servers 反向提取
- 本周新增 cameo-mcp-bridge（★14）是 CATIA Magic/Cameo SysML MCP，虽 < 20★ 但为唯一覆盖 MBSE 的 MCP，未来可关注
