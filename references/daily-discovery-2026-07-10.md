# 每日发现记录 — 2026-07-10（周五）

## 搜索领域
- 工业制造/QA（搜索量：10 个 MCP 查询 + 24 个 MCP 查询 + 10 个 Skill 查询）
- 生物医学/医疗（搜索量：21 个 MCP 查询 + 10 个 Skill 查询）
- 环境/水利/污染（搜索量：22 个 MCP 查询 + 7 个 Skill 查询）

## 搜索结果

### 生物医学/医疗
MCP 查询候选：216 个（去重后），Skill 查询候选也已融合

#### 新增收录（Skills 表）

| 条目 | Star | 类型 | 理由 |
|------|------|------|------|
| aipoch/medical-research-skills | 1337 | Skill | ★≥100, 201 commits, active (2 weeks ago), 真实的 agent skill 集合 |
| ClawBio/ClawBio | 1032 | Skill | ★≥100, "first bioinformatics-native AI agent skill library", 1127 commits, active (16h ago) |
| GPTomics/bioSkills | 1002 | Skill | ★≥100, "a set of SKILLS.md for doing bioinformatics", 220 commits, active (5d ago) |
| jaechang-hits/SciAgent-Skills | 229 | Skill | ★≥100, 197 bioinformatics skills, 110 commits, active (last month) |
| ajhcs/healthcare-agents | 44 | Skill | ★44 但在 20-100 范围内，非常活跃（6h ago），115 commits, SKILL.md pack for US healthcare admin |

#### 跳过的候选（MCP Servers）
- KatherLab/STAMP (★124) — ML research codebase, 不是 MCP server
- healthchainai/HealthChain (★211) — SDK for healthcare AI (Pitfall #55)
- the-momentum/fhir-mcp-server (★93) — pushed 2025-10, 不活跃
- jmandel/health-record-mcp (★81) — pushed 2025-08, 不活跃
- lynnlangit/precision-medicine-mcp (★21) — MCP server 但 ★21 偏低, pushed 2026-07-10（活跃）。功能与现有 biomcp(★544) 和 medical-mcp(★102) 重叠。不收录。
- aks129/HealthClawGuardrails (★25) — guardrails 工具非 MCP server
- u9401066/pubmed-search-mcp (★20) — PubMed MCP，与现有多个 PubMed MCP 重叠
- 其余候选均 ★<20 或非真正工程 MCP Server

### 工业制造/QA
- MCP 搜索：绝大部分命中已收录条目（thingsboard-mcp, opcua-mcp, modbus-mcp, twincat-mcp）或通用工具
- Skill 搜索：addyosmani/agent-skills(★75k) 是通用 skill 集合非工程专用。muxuuu/serenity-skill(★3325) 是供应链 skill 但与工程制造不直接相关。其余均 <★20
- 新增收录：0

### 环境/水利/污染
- MCP 搜索：weather-mcp/weather-mcp(★22) 是另一个天气 MCP（不同于已收录的 ezh0v/weather-mcp-server），但 ★22 偏低且功能重叠
- Zhonghao1995/Agentic-MIKE-Plus(★5) 星数太低
- CliDyn/copernicus-mcp(★11) 星数太低
- NOAA-OWP/gval(★26) 是 geospatial evaluation framework 非 MCP server
- cyanheads 系列(★1-2) 星数太低
- pipeworx-io 系列(★0) 星数太低
- 新增收录：0

## 统计
- 总查询数：74（MCP + Skill）
- 总候选（未去重）：~700
- 新增收录：5（全部为 Skills 表）
- README 当前 Skills：15（5 新增 + 10 原有）
- README 当前 MCP Servers：不变

## 低星观察（下次优先复查）
- lynnlangit/precision-medicine-mcp (★21) — 活跃维护，如果持续增长可能值得收录
- aks129/HealthClawGuardrails (★25) — 非典型但活跃，关注方向
