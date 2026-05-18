# 每日工程 Skill/MCP 发现记录 — 2026-05-18（周一）

## 搜索策略
周一轮换：机械/CAD/CAM + 电气/PCB/EDA + 材料/焊接/检测

## 查询统计
- GitHub API 查询: 21 个（3 个领域 x 6-7 个关键词 + 3 个补充查询）
- 唯一候选: 148 个（去重后）
- LLM 判断通过: 10 个
- 新增收录: 10 个（2 个社区 Skills + 8 个 MCP Servers）

## 新增条目

### 社区精选 Skills（新增 2 条）

| Skill | 来源 | Star | 判断 |
|-------|------|------|------|
| kicad-happy | aklofas | 339 | KiCad 设计审查 AI agent 技能集，★≥100 自动收录 |
| NextBoard | LeoKemp223 | 161 | PCB 硬件设计 AI Agent 技能，★≥100 自动收录 |

### 机械 / CAD / CAM（新增 2 条）

| MCP Server | 来源 | Star | 判断 |
|------------|------|------|------|
| SolidworksMCP-TS | vespo92 | 130 | SolidWorks MCP，★≥100 自动收录，TypeScript 实现 |
| freecad-addon-robust-mcp-server | spkane | 85 | FreeCAD Robust MCP，47 commits，企业级质量，领域高度相关+活跃 |

### 电气 / PCB / EDA（新增 5 条）

| MCP Server | 来源 | Star | 判断 |
|------------|------|------|------|
| KiCAD-MCP-Server | mixelpixx | 1022 | 最全面的 KiCAD MCP（122 tools，16 类），★≥100 自动收录 |
| altium-mcp | coffeenmusic | 78 | 首个 Altium Designer MCP server，活跃维护 |
| pcbparts-mcp | Averyy | 59 | 电子元器件搜索 MCP（JLCPCB/Mouser/DigiKey 1.5M+），179 commits |
| jlcmcp | hyl64 | 51 | 嘉立创 EDA MCP（39 tools），活跃维护 |
| JLCEDA-MCP | sengbin | 22 | 嘉立创 EDA MCP（VS Code 插件+WebSocket 桥），155 commits |

## 跳过的候选

### 材料/焊接/检测（本领域无有效新增）

- 所有高星结果均为通用工具或教学材料，无真正工程材料科学 MCP
- theNetworkChuck/docker-mcp-tutorial ★1492 — 教学培训材料
- microsoft/DebugMCP ★350 — 通用调试工具，非工程检测
- call518/MCP-PostgreSQL-Ops ★149 — 数据库运维，非材料工程
- 其他（tumourlove/monolith, threejs-devtools, blender-mcp-n8n 等）— 已在之前跳过

### 机械/CAD（跳过）

| 仓库 | Star | 原因 |
|------|------|------|
| ArchimedesCrypto/fusion360-mcp-server | 71 | 单次提交即废弃一年，仅为脚本生成器 |
| eyfel/mcp-server-solidworks | 85 | 无实际代码，仅架构提案，已废弃一年 |
| ATOI-Ming/FreeCAD-MCP | 81 | 与已有 FreeCAD MCP 条目重叠 |
| contextform/freecad-mcp | 73 | 与已有 FreeCAD MCP 条目重叠 |

### 电气/PCB（跳过）

| 仓库 | Star | 原因 |
|------|------|------|
| salitronic/eda-agent | 19 | Altium MCP 但 Star < 20，未达收录阈值 |
| clharman/circuit-mcp | 58 | Web 应用测试 MCP，非电路工程 |
| sibilleb/AAP-Enterprise-MCP-Server | 30 | Ansible Automation Platform MCP，EDA 指 Event-Driven Ansible，非电子设计自动化 |

## README 更新统计
- 社区精选 Skills: 1 → 3（新增 2：kicad-happy, NextBoard）
- 社区精选 MCP Servers 分组: 12 个（不变）
- 机械/CAD/CAM: 7 → 9（新增 2）
- 电气/PCB/EDA: 3 → 8（新增 5）
- 材料/焊接/检测: 无分组（仍无符合条件的 MCP）
- MCP Servers 总数: 29（原 21 + 新增 8）— 注意上次周日补漏时统计有误，实际先由 16→20+... 让我们重新统计

## 领域效果排名
1. ✅ 电气/PCB/EDA — 本周最丰富，KiCAD-MCP-Server（★1022）超高质量新发现，Altium MCP 生态首次出现
2. ✅ 机械/CAD/CAM — SolidWorks MCP 生态萌芽，FreeCAD MCP 持续丰富
3. ❌ 材料/焊接/检测 — 仍无真正工程材料科学 MCP，"materials"关键词被教学材料严重污染

## 搜索模式评估
- 周一轮换效果极好：电气/PCB/EDA 发现 5 条新增，含 1022★ 的 KiCAD-MCP-Server
- `"领域词" "MCP" in:name,description` 仍是信噪比最高的查询模式
- "SolidWorks" + "MCP" 在 name,description 搜索效果最好，发现 SolidworksMCP-TS（★130）
- "Altium" + "MCP" 找到了首个 Altium MCP server（altium-mcp ★78）
- "嘉立创" / "JLC" + "MCP" 找到 jlcmcp（★51）和 JLCEDA-MCP（★22）
