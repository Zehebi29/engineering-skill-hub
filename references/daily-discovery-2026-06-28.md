# Daily Discovery — 2026-06-28 (周日)

## 搜索类型
补漏 — 本周缺失领域综合检查 + 上周低星候选复查 + Saturday-style awesome-mcp-servers 综合扫描

## 本周覆盖状态（2026-06-22 ~ 2026-06-28）
**全部 15 个领域均未覆盖。** 本周没有任何 daily-discovery 文件。

## 执行内容

### 1. Saturday 综合扫描 — awesome-mcp-servers 反向提取
- 解析 3230 行 README，提取 1528 个 bullet 条目
- 关键词初筛 → 259 个命中 → 244 个不在 README 的新候选
- 按 sections 精筛：Aerospace & Astrodynamics（2）、Art & Culture（55）、Architecture & Design（10）、Biology/Medicine/Bioinformatics（28）、Embedded System（12）、Environment & Nature（4）
- API 查星验证 20+ 个最有希望的候选
- **结果：0 个新增收录。** OctoEverywhere/mcp（★34，3D 打印，pushed 2025-07-03 不活跃）。adancurusul/serial-mcp-server（★67，串口工具，非工程专用）。其他均为低星或不活跃。

### 2. 优先级领域搜索（本周缺失的 15 个领域）

#### 生物医学/医疗（10 个精确查询）
- 搜索：pubmed、fhir、dicom、clinical trial、genomics、healthcare、FDA、biomedical、medical、drug discovery
- 121+ 候选，API 验证 20 个 star≥20 候选
- **0 个新增收录。** 主要发现：
  - u9401066/pubmed-search-mcp（★20，活跃）— PubMed 多源搜索，与已有 3+ 条目功能重叠
  - sunanhe/awesome-medical-mcp-servers（★68）— awesome list，非 MCP server
  - bakhtiersizhaev/openevidence-mcp（★28，活跃）— 临床医学证据 MCP，非工程领域
  - 其他候选均为不活跃、低星或通用工具

#### 工业制造/QA（6 个精确查询）
- cadugrillo/s7-mcp-bridge（★20，pushed 2026-03-20，~100 天前不活跃）— Siemens S7 PLC MCP，领域相关但不活跃
- slalaure/korelate（★23）— 通用 UNS 运维中心，非工程 MCP server
- **0 个新增收录**

#### 环境/水利/污染（7 个精确查询）
- 天气/气象类为主：ezh0v/weather-mcp-server（★246）已在 README（2026-06-26 新增）
- Zhonghao1995/agentic-swmm-workflow（★14，活跃）— SWMM 暴雨管理 MCP，值得持续观察
- **0 个新增收录**

### 3. 低星候选复查

从上周（Jun 15-21）discovery 文件中提取低星候选，按规则只复查「因 Star < 20 被跳过且类型正确/领域相关/未归档」的候选：

| 仓库 | 上次 Star | 当前 Star | 变化 | 判断 |
|------|----------|----------|------|------|
| pzfreo/build123d-mcp | 18 (Jun 21) | **25** | +7 | ✅ **收录** — build123d 参数化 CAD MCP，360 commits，3 天前活跃 |
| asmith26/jupytercad-mcp | 19 (Jun 21) | 19 | 0 | ❌ 无增长，不活跃 |
| blwfish/freecad-mcp | 9 (Jun 15) | 10 | +1 | ❌ 增长微弱，已有 4 个 FreeCAD 条目 |
| GLechevalier/OpenGalatea | 14 (Jun 15) | 14 | 0 | ❌ 无增长 |
| petropt/petro-mcp | 1 (Jun 18) | 1 | 0 | ❌ 无增长 |
| ojaogezi/opm-mcp | 0 (Jun 18) | 0 | 0 | ❌ 无增长 |
| andresjbf/tnavigator-mcp | 2 (Jun 18) | 2 | 0 | ❌ 无增长 |
| CliDyn/copernicus-mcp | 11 (Jun 21) | 11 | 0 | ❌ 无增长 |
| midhunxavier/OPCUA-MCP | 15 (Jun 21) | 15 | 0 | ❌ 无增长 |
| publu/RoboRun | 14 (Jun 21) | 14 | 0 | ❌ 无增长 |
| kimimgo/viznoir | 15 (Jun 21) | 15 | 0 | ❌ 无增长 |

## 新增收录

| Repo | Star | 领域 | 描述 |
|------|------|------|------|
| [build123d-mcp](https://github.com/pzfreo/build123d-mcp) | 25 | 机械/CAD/CAM | build123d 参数化 CAD MCP server。360+ commits，60 版本，活跃维护。STEP/STL/GLB 导入导出，几何度量。与 agentcad（build123d+CadQuery）互补。 |

## 跳过条目

| Repo | Star | 原因 |
|------|------|------|
| OctoEverywhere/mcp | 34 | 3D 打印 MCP，pushed 2025-07-03，不活跃 >11 个月 |
| adancurusul/serial-mcp-server | 67 | 串口调试通用工具，非工程专用 |
| u9401066/pubmed-search-mcp | 20 | PubMed 搜索，与已有 3+ 条目功能重叠 |
| sunanhe/awesome-medical-mcp-servers | 68 | awesome list，非 MCP server |
| bakhtiersizhaev/openevidence-mcp | 28 | 临床医学证据 MCP，非工程领域 |
| the-momentum/apple-health-mcp-server | 219 | 消费者健康数据，pushed 2026-02-10 不活跃 |
| cadugrillo/s7-mcp-bridge | 20 | Siemens S7 PLC MCP，pushed 2026-03-20 不活跃 |
| slalaure/korelate | 23 | 通用 UNS 运维面板，非工程 MCP |
| Zhonghao1995/agentic-swmm-workflow | 14 | SWMM 暴雨管理 MCP，领域相关但 Star 过低（★14 < 20） |
| ArsMedicaTech/arsmedicatech | 22 | 通用临床 Web 应用，非 MCP server |

## 备注
- build123d-mcp 是本周唯一新增，从低星候选（★18）在 7 天内增长到 ★25，且维护非常活跃
- 机械/CAD/CAM 领域现有 17 个 MCP server，build123d 子领域形成 agentcad（★49 通用）+ build123d-mcp（★25 专注）互补格局
- 本周 15 个领域完全未覆盖，但域名搜索确认大多数领域生态无新增
- 生物医学/医疗领域 PubMed/FHIR 方向已被充分覆盖，政府健康数据集成（us-gov-open-data-mcp）是新方向

## README 当前状态
- Skills: 6（3 原创 + 6 社区）
- MCP Servers: 约 78+（含本次新增 1 条）
