# Daily Discovery — 2026-07-09 (周四)

## 搜索领域
- 油藏/石油/地质
- 汽车/自动驾驶
- 船舶/海洋工程

## 查询统计
| 领域 | 查询数 | ≥20★候选 | 新增 |
|------|--------|---------|------|
| 油藏/石油/地质 | 13 | 0 | 0 |
| 汽车/自动驾驶 | 8 | 1 (NVIDIA/elements ★25, 非工程) | 0 |
| 船舶/海洋工程 | 9 | 0 | 0 |
| **合计** | **30** | **1** | **0** |

## 新增收录
无

## 候选详情

### 油藏/石油/地质
| 仓库 | Star | pushed_at | 跳过原因 |
|------|------|-----------|----------|
| ameyxd/petromcp | 2 | 2026-05-08 | Star 过低（石油数据格式 MCP） |
| gabrielserrao/pyrestoolbox-mcp | 43 | 2026-03-11 | 已在 README |
| andresjbf/tnavigator-mcp | 2 | 2026-04-10 | Star 过低（tNavigator 油藏仿真） |
| SeequentEvo/evo-mcp | 7 | 2026-07-08 | Star 过低（Seequent 地学公司官方 MCP，但仅 ★7） |
| cyanheads/eia-energy-mcp-server | 1 | 2026-06-20 | Star 过低（EIA API，归能源领域） |
| blake365/macrostrat-mcp | 7 | 2025-08-26 | Star 过低 + 不活跃 |
| ojaogezi/opm-mcp | 0 | 2026-06-10 | Star 过低（OPM 油藏仿真） |
| fesp21/petro-mcp | 0 | 2026-03-31 | Star 过低 |
| 其余结果 | <5 | 不一 | 非石油工程（水权、火山、古生物、一般地质 API），或关键词噪音匹配 |

### 汽车/自动驾驶
| 仓库 | Star | pushed_at | 跳过原因 |
|------|------|-----------|----------|
| NVIDIA/elements | 25 | 2026-07-09 | 非工程 MCP — NVIDIA Design System + UI Agent Harness，含 .agents/.claude/.codex 目录但为通用 UI 框架，非自动驾驶工程 MCP |
| kingdoja/autonomous-driving-rag-mcp | 0 | 2026-04-20 | Star 过低 |
| CSOAI-ORG/autonomous-vehicles | 0 | 2026-06-13 | Star 过低 |
| ariekogan/ateam-mcp | 1 | 2026-07-06 | Star 过低（ADAS 命名但通用 multi-agent） |
| drivly/auto-dev-skill | 14 | 2026-04-08 | Star 过低（Automotive Data for AI Agents） |
| pangzhenying2025/hermes-automotive-skills | 1 | 2026-05-19 | Star 过低 |
| robertquant/automotive-wiki-skill | 0 | 2026-04-16 | Star 过低 |
| ADAS MCP 搜索结果 | 0-17 | 不一 | 全部是 Ada 编程语言/ADA Creative 等 false positive，无一是 Advanced Driver-Assistance Systems |

### 船舶/海洋工程
| 仓库 | Star | pushed_at | 跳过原因 |
|------|------|-----------|----------|
| weather-mcp/weather-mcp | 22 | 2026-07-07 | 通用天气 MCP，非海洋工程（已有 weather-mcp-server ★246 在 README） |
| lucasinocencio1/mcp-surf-forecast | 18 | 2026-02-11 | Star 过低 + 冲浪预报，非工程级 |
| cyanheads/noaa-marine-mcp-server | 1 | 2026-07-03 | Star 过低（潮位/浮标数据） |
| sailingnaturali/signalk-mcp | 1 | 2026-06-29 | Star 过低（SignalK 船舶数据） |
| tools-mcp/vessel-traffic-mcp | 1 | 2026-07-07 | Star 过低（AIS 船舶跟踪） |
| contextkits/naval-shipbuilding-standards | 0 | 2026-02-10 | Star 过低（NAVSEA 标准） |
| maritimeconnectivity/* | 1-23 | 不一 | **Maritime Connectivity Platform** — 这是海事通信平台（Java 项目），与 Model Context Protocol 完全无关。纯关键词歧义 |
| 其余结果 | <1 | 不一 | 「ship」关键词被「ship product/UI/websites」语境严重污染 |

## 低星复查（上周 July 2 候选）
| 仓库 | 上次 Star | 当前 Star | 变化 | 备注 |
|------|----------|----------|------|------|
| ameyxd/petromcp | 2 | 2 | +0 | 无增长 |
| andresjbf/tnavigator-mcp | 2 | 2 | +0 | 无增长 |
| ojaogezi/opm-mcp | 0 | 0 | +0 | 无增长 |
| kingdoja/autonomous-driving-rag-mcp | 0 | 0 | +0 | 无增长 |
| CSOAI-ORG/autonomous-vehicles | 0 | 0 | +0 | 无增长 |
| lucasinocencio1/mcp-surf-forecast | 18 | 18 | +0 | 无增长，>120天不活跃 |

## 关键观察

1. **这三个领域持续零产出** — 连续多月确认无合格 MCP server 或 agent skill 候选。所有候选 Star<20（或为关键词噪音匹配）。
2. **油藏领域唯一达标项目**仍然是 pyrestoolbox-mcp (★43)，已有在 README。Seequent 官方 MCP (evo-mcp) 仅 ★7，远不达标。OPM/Open Porous Media 的 MCP (opm-mcp) 为 ★0。
3. **汽车/自动驾驶领域 MCP 生态持续为零** — MCP2515 CAN 芯片污染已被有效过滤，但真实自动驾驶工程 MCP server 完全不存在。NVIDIA/elements (★25) 是唯一高星结果，但为 UI 设计系统非工程 MCP。
4. **船舶/海洋工程** — 「maritime」关键词搜索被「Maritime Connectivity Platform」（Java 海事通信协议）严重污染。真正的海洋工程 MCP server 仍为零。「ship」关键词噪音极高。
5. **低星复查无增长** — 所有上周候选 Star 无任何变化，petropt/petro-mcp 已删除 (404)。确认这些领域不值得每周常规搜索，推荐月度检查。
6. **NVIDIA/elements** 是本周四唯一值得注意的非工程发现——NVIDIA 设计系统含 .agents/.claude/.codex/.cursor 多平台 agent 配置，但定位为 UI Agent Harness 非工程工具。可列为综合资源备选，但当前不在收录范围。

## README 当前状态
- 原创 Skills: 3
- 社区精选 Skills: 10
- 社区精选 MCP Servers: ~91（不变）
