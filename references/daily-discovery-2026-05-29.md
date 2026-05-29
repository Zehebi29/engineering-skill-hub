# Daily Discovery — 2026-05-29 (Friday)

## 搜索领域
- 工业制造/QA
- 生物医学/医疗
- 环境/水利/污染

## 查询统计

| 领域 | 查询数 | 候选数 | 新增收录 |
|------|--------|--------|----------|
| 工业制造/QA | 10 | 49 | 0 |
| 生物医学/医疗 | 10 | 63 | 2 |
| 环境/水利/污染 | 10 | 38 | 0 |
| **合计** | **30** | **150** | **2** |

## 新增收录

| 仓库 | Star | 领域 | 说明 |
|------|------|------|------|
| wso2/fhir-mcp-server | 121 | 生物医学/医疗 | FHIR MCP server，WSO2 官方项目，将任意 FHIR Server 暴露为 MCP Server |
| cyanheads/pubmed-mcp-server | 101 | 生物医学/医疗 | PubMed/Europe PMC 搜索、全文获取（PMC/EPMC/Unpaywall）、MeSH 术语、引用查询，STDIO/Streamable HTTP |

## 领域观察

### 工业制造/QA
该领域 MCP 生态仍处于极早期。最佳候选 `cadugrillo/s7-mcp-bridge` ★19 接近阈值但未达标（Siemens S7 PLC MCP server，最近更新 2026-03-20）。已收录的 `thingsboard-mcp`（★97）、`opcua-mcp`（★26）等仍是该领域主力。

低星新兴候选：
- `cadugrillo/s7-mcp-bridge` ★19 — Siemens S7 PLC MCP（潜力大，活跃）
- `midhunxavier/OPCUA-MCP` ★12 — OPC UA MCP（与已有 opcua-mcp 功能重叠）
- `vogler75/winccua-mcp-server` ★11 — Siemens WinCC Unified SCADA MCP
- `vogler75/winccv8-mcp-server` ★10 — Siemens WinCC V8 SCADA MCP
- `gangsterke/Tia-Portal-MCP-server` ★8 — TIA Portal MCP（2026-05-28 更新）
- `litmusautomation/litmus-mcp-server` ★9 — Litmus 配置 MCP
- `nonead/Nonead-Universal-Robots-MCP` ★6 — Universal Robots 协作机器人 MCP
- `Nodeblue-AI/ignition-mcp-server` ★4 — Ignition SCADA MCP
- `Nodeblue-AI/studio5000-mcp-server` ★4 — Rockwell/Allen-Bradley Studio 5000 MCP

注意：搜索噪音主要来自 "manufacturing" 匹配 "production-ready" 通用工具，以及 "quality" 匹配代码质量工具。

### 生物医学/医疗
该领域 MCP 生态最成熟，本次找到两个达标候选：

**已收录：**
- `wso2/fhir-mcp-server` ★121 — WSO2 官方 FHIR MCP server，Python，Apache-2.0，42 forks，活跃维护
- `cyanheads/pubmed-mcp-server` ★101 — 来自 cyanheads（同 clinicaltrialsgov-mcp-server 作者），TypeScript，277 commits，76 tags，18h 前更新

**未达标候选（Star < 100 但值得关注）：**
- `ChristianHinge/dicom-mcp` ★95 — DICOM/PACS MCP server，Python，但最后 push 2025-12-15（>90 天无更新）
- `the-momentum/fhir-mcp-server` ★85 — 另一个 FHIR MCP，但最后 push 2025-10-23（>90 天），与 wso2 版功能重叠
- `dermatologist/pyomop` ★64 — OHDSI 临床数据 MCP，Python，GPL-3.0，活跃，但更像 Python 包+LLM 支持而非纯 MCP server
- `langcare/langcare-mcp-fhir` ★38 — 企业级 FHIR MCP
- `biocontext-ai/skill-to-mcp` ★26 — AI Skills 转 MCP 工具
- `biocontext-ai/knowledgebase-mcp` ★23 — 生物医学知识库 MCP
- `pascalwhoop/medical-mcps` ★21 — 生物医学数据库 MCP 工具集

### 环境/水利/污染
该领域 MCP 生态依然极稀少。P&ID 查询返回 6000 万结果（全是包含 "P" 和 "ID" 的不相关项目）。"environmental MCP server" 查询结果大多是通用工具碰巧匹配。

低星候选：
- `CliDyn/copernicus-mcp` ★8 — Copernicus 环境数据 MCP（欧洲哥白尼计划），最近活跃（2026-05-22 push），值得关注
- `jcholly/geotap-developer` ★6 — GeoTap 环境/基础设施数据 MCP
- `offtrailstudio/speak-for-the-trees-mcp` ★5 — 生态系统健康 MCP

已收录的 `puran-water/autocad-mcp`（★280）仍是该领域唯一大型条目。

## 跳过的候选及原因

### 工业制造/QA

| 候选 | Star | 跳过原因 |
|------|------|----------|
| cadugrillo/s7-mcp-bridge | 19 | Star < 100，领域生态稀少不满足"高度相关+活跃"补充条件（last push 2026-03-20 >90天） |
| aws-samples/sample-manufacturing-automotive-ai-toolkit | 19 | AWS 样例集合，非独立 MCP server |
| midhunxavier/OPCUA-MCP | 12 | Star 过低，功能与已有 opcuc-mcp 重叠 |
| vogler75/winccua-mcp-server | 11 | Star 过低 |
| vogler75/winccv8-mcp-server | 10 | Star 过低 |
| litmusautomation/litmus-mcp-server | 9 | Star 过低 |
| gangsterke/Tia-Portal-MCP-server | 8 | Star 过低 |
| iunera/ypipe | 7 | 通用本地 AI 平台，非工业专用 |
| nonead/Nonead-Universal-Robots-MCP | 6 | Star 过低 |
| kmanditereza/mcp-server-for-industrial-data | 5 | Star 过低，无描述 |
| Nodeblue-AI/ignition-mcp-server | 4 | Star 过低 |
| Nodeblue-AI/studio5000-mcp-server | 4 | Star 过低 |
| intecrel/industrial-mcp | 3 | Star 过低，B2B 分析非工程制造 |
| Czarnak/tia-portal-mcp | 3 | Star 过低 |
| jeanlopezxyz/cncf-tech-advisor-mcp | 3 | CNCF 云原生技术顾问，非工业制造 |
| hlpsxc/video-quality-mcp | 5 | 视频质量分析，非工程 QA |

### 生物医学/医疗

| 候选 | Star | 跳过原因 |
|------|------|----------|
| ChristianHinge/dicom-mcp | 95 | Star < 100 且 last push 2025-12-15（>90 天无更新） |
| the-momentum/fhir-mcp-server | 85 | Star < 100 且 last push 2025-10-23（>90 天），与 wso2 版功能重叠 |
| Aryia-Behroziuan/References | 60 | 学术参考文献列表，非 MCP server |
| dermatologist/pyomop | 64 | Python 包+LLM 支持，非纯 MCP server |
| langcare/langcare-mcp-fhir | 38 | Star < 100 |
| Md-Emon-Hasan/MediGenius | 31 | 多 agent 医疗助手框架，非 MCP server |
| biocontext-ai/skill-to-mcp | 26 | AI Skills 转 MCP 工具，非工程医疗 MCP |
| biocontext-ai/knowledgebase-mcp | 23 | Star < 100 |
| pascalwhoop/medical-mcps | 21 | Star < 100 |
| biocontext-ai/registry | 20 | 注册表，非 MCP server |
| erikhoward/azure-fhir-mcp-server | 18 | Star < 100，Azure 特定 |
| eigenbau/mcp-snomed-ct | 18 | Star < 100 |
| rdmgator12/awesome-healthcare-mcp-servers | 8 | awesome list，非 MCP server |
| hherb/biomedmcp | 7 | Star 过低，proof of concept |

### 环境/水利/污染

| 候选 | Star | 跳过原因 |
|------|------|----------|
| public-apis/public-apis | 437666 | 通用 API 列表，非工程 MCP |
| EbookFoundation/free-programming-books | 389108 | 编程书籍列表，非 MCP |
| 1Utkarsh1/mcp-stdio-guard | 47 | MCP stdio 通用工具，非环境工程 |
| GSA-TTS/fed-data-mcp-registry | 14 | 政府数据 MCP 注册表，非环境专用 |
| CliDyn/copernicus-mcp | 8 | Star < 100 且 < 20（不满足补充条件） |
| jcholly/geotap-developer | 6 | Star 过低 |
| offtrailstudio/speak-for-the-trees-mcp | 5 | Star 过低 |
| AI-Hydro/aihydro-tools | 2 | Star 过低，水文工具 MCP |

## 总结

本次搜索 3 个领域共 30 个查询，150 个候选中筛出 2 个新增收录（均来自生物医学/医疗领域）。工业制造/QA 和环境/水利/污染的 MCP 生态仍处于极早期，最佳候选均 Star < 20。生物医学/医疗是 MCP 生态最成熟的工程领域，FHIR 和 PubMed 两个子方向均有高质量 server。

README 当前: 3 Skills + 55 MCP Servers（新增 2 个）
