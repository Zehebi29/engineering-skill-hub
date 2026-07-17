# 工程 Skill/MCP 发现日报 — 2026-07-17（周五）

**搜索领域**: 工业制造/QA | 生物医学/医疗 | 环境/水利/污染

## 执行概况

| 指标 | 值 |
|------|-----|
| 查询总数 | 22（6 MCP + 5 Skills for 工业制造/QA, 6 MCP + 5 Skills for 生物医学/医疗, 6 MCP + 5 Skills for 环境/水利/污染） |
| 初筛候选 | ~130 |
| API 验证 | 18 个 >=20★ 候选 |
| 新增收录 | 2 |

## 新增

### [sap-engineering-skill](https://github.com/shrek-abaper/sap-engineering-skill) ★25
- **类型**: Agent Skill
- **领域**: 工业制造/QA（SAP ERP 工程）
- **描述**: SKILL-spec agent skills for SAP ABAP engineering: ADT-based code read/write, security & quality review, transport release gating
- **理由**: 25★, pushed 2026-06-19（活跃）, 27 commits, 含 `skills/` SKILL.md 目录。SAP ABAP 是工业 ERP 核心工程领域，填补 Skills 表中 SAP 工程空白。注意：★25 < 100 阈值，但其领域高度相关 + 活跃维护 + 真实 SKILL.md 集合。

### [meddev-agent-skills](https://github.com/AminAlam/meddev-agent-skills) ★24
- **类型**: Agent Skill
- **领域**: 生物医学/医疗
- **描述**: Modular SKILL.md files for AI coding agents working on medical device software — IEC 62304, architecture, CI/CD, firmware, connectivity, regulatory
- **理由**: 24★, pushed 2026-05-21（57天前，活跃）, 21 commits, 5 forks。IEC 62304 医疗设备软件合规是严格的工程领域，填补 Skills 表中医疗设备软件工程空白。注意：24★ < 100 阈值，但领域极其特殊+活跃维护+真实 SKILL.md 集合。

## 跳过原因统计

| 原因 | 数量 | 示例 |
|------|------|------|
| 低星 (<20) | ~90 | dgilford/ai-tools ★12, Zhonghao1995/Agentic-MIKE-Plus ★5 |
| 不活跃 (>90d) | 8 | jinwx/weather-data-skills ★36 (101d), biocontext-ai/knowledgebase-mcp ★28 (185d), ai-evos/agent-skills ★21 (142d), cadugrillo/s7-mcp-bridge ★20 (117d) |
| 通用/非工程 | 6 | quality-playbook (软件质量), design-farmer (UI设计), quality.md (通用), zebbern/skills (通用) |
| Awesome list | 1 | awesome-bio-agent-skills ★117 |
| 功能重复 | 1 | pubmed-search-mcp ★20 (已有 ★121 和 ★169 的 PubMed MCP) |
| 注册表/转换器 | 3 | biocontext-ai/registry, skill-to-mcp |
| 串口工具非MCP | 1 | SerialRUN ★25 |
| 低星+功能重叠 | ~15 | TealFlowMCP ★28 (不活跃), etc. |

## 环境/水利/污染领域状态

连续多周确认：该领域 MCP 生态仍然稀少。现有 autocad-mcp (★341) + weather-mcp-server (★246) + foehn (★42) 三个条目。hydrology/wastewater/water treatment 关键词搜索几乎无工程级 MCP 结果。jinwx/weather-data-skills (★36) 因 101 天未更新跳过。值得关注：Zhonghao1995/Agentic-MIKE-Plus (★5) 是首个 MIKE+ 水文模型 MCP/skill，若 Star 增长建议复查。

## 工业制造/QA 领域状态

制造业 MCP 生态以工业协议（OPC UA/Modbus/TwinCAT）为主，agent skill 类候选开始出现。sap-engineering-skill 是首个 SAP 工程 skill 候选。cadugrillo/s7-mcp-bridge (★20, 117d 不活跃) 仍是唯一 Siemens PLC MCP。注意：q = "production MCP server" 返回大量通用/框架工具（tavily-mcp、golf-mcp、cve-mcp-server 等），完全无法用于工程发现。

## 生物医学/医疗领域状态

Skills 生态仍在增长但趋于成熟（已有 medical-research-skills ★1337, ClawBio ★1032, bioSkills ★1002, SciAgent-Skills ★229）。MCP server 生态也饱和（biomcp ★547, pubmed-mcp-server ★121, fhir-mcp-server ★129 等）。meddev-agent-skills (★24) 首次覆盖医疗设备软件工程（IEC 62304）这一细分方向。biocontext-ai 系列（knowledgebase/skill-to-mcp/registry）全部不活跃或类型不符。

## README 当前统计

- **原创 Skills**: 3
- **社区精选 Skills**: 74（+2）
- **社区精选 MCP Servers**: 180+
