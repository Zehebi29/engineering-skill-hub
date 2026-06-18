# 每日发现记录 — 2026-06-18（周四）

## 搜索领域
- 油藏/石油/地质
- 汽车/自动驾驶
- 船舶/海洋工程

## 查询统计
- 主查询：8 + 7 + 7 = 22 个 GitHub API 查询
- 补充查询：11 个（petroleum LLM, reservoir AI, seismic AI, well log, CARLA MCP, autonomous vehicle simulation, ADAS testing, naval shipbuilding, marine engineering, AIS vessel, ocean engineering simulation）
- 总计：33 个查询

## 油藏/石油/地质（8 查询）

### 候选（全部不达标）
| 仓库 | Star | pushed_at | 跳过原因 |
|------|------|-----------|----------|
| petropt/petro-mcp | 1 | 2026-06-10 | Star 过低（需 ≥20） |
| ojaogezi/opm-mcp | 0 | 2026-06-10 | Star 过低 |
| andresjbf/tnavigator-mcp | 2 | 2026-04-10 | Star 过低 |
| OilpriceAPI/mcp-server | 3 | 2026-03-29 | Star 过低 |
| blake365/macrostrat-mcp | 7 | 2025-08-26 | Star 过低 + 不活跃 |
| raghujayan/openvds-mcp-server | 1 | 2026-02-23 | Star 过低 |
| FizziksRU/oilgas-rag-mcp | 1 | 2026-04-29 | Star 过低 |

### 备注
该领域 MCP 生态持续极度稀少。已有条目 pyrestoolbox-mcp（★42）仍是唯一达标项目。petro-mcp 和 opm-mcp 均为 2026-06 新建项目，值得低星复查。

## 汽车/自动驾驶（7 查询）

### 候选
| 仓库 | Star | pushed_at | 跳过原因 |
|------|------|-----------|----------|
| cobanov/teslamate-mcp | 130 | 2026-05-21 | 类型不符：TeslaMate 是车辆数据追踪/日志工具，非自动驾驶/ADAS |
| petrpatek/obd2-mcp-server | 2 | 2026-05-16 | Star 过低（OBD-II 诊断，非自动驾驶） |
| kingdoja/autonomous-driving-rag-mcp | 0 | 2026-04-20 | Star 过低 |
| CSOAI-ORG/autonomous-vehicles | 0 | 2026-06-13 | Star 过低，描述模糊 |
| RFingAdam/mcp-emc-regulations | 1 | 2026-05-13 | Star 过低（EMC 法规查询，非自动驾驶） |

### 备注
真正的自动驾驶 MCP server 生态持续为零。teslamate-mcp（★130）是该领域唯一高星项目，但它是 TeslaMate 数据库查询工具（车辆追踪/能耗日志），不是自动驾驶仿真或 ADAS 开发工具，不收录。

## 船舶/海洋工程（7 查询）

### 候选（全部不达标）
| 仓库 | Star | pushed_at | 跳过原因 |
|------|------|-----------|----------|
| lucasinocencio1/mcp-surf-forecast | 18 | 2026-02-11 | Star 过低 + 不活跃（>90 天） |
| Cyreslab-AI/marinetraffic-mcp-server | 10 | 2025-05-15 | Star 过低 + 不活跃（>1 年） |
| tools-mcp/vessel-traffic-mcp | 0 | 2026-06-16 | Star 过低（AIS 船舶追踪，非船舶工程） |
| BharathChowdary43/maritime_mcp_package | 1 | 2026-06-16 | Star 过低 |
| contextkits/naval-shipbuilding-standards | 0 | 2026-02-10 | Star 过低 + 不活跃 |
| contextkits/shipbuilding-specs | 0 | 2026-02-10 | Star 过低 + 不活跃 |

### 备注
船舶/海洋工程 MCP 生态持续空白。所有候选均为 <20 Star，且多数已不活跃。该领域不值得常规搜索投入。

## 新增收录
无

## 跳过汇总
- 全部 33 个查询结果不达标
- 油藏/石油/地质：生态极度稀少，所有候选 Star < 5
- 汽车/自动驾驶：唯一高星项目（teslamate-mcp ★130）为车辆追踪工具，非自动驾驶
- 船舶/海洋工程：生态完全空白

## 低星复查候选（下周日补漏）
- petropt/petro-mcp（★1, 2026-06-10）— 石油工程 MCP，活跃
- ojaogezi/opm-mcp（★0, 2026-06-10）— 油藏仿真 MCP，活跃
- andresjbf/tnavigator-mcp（★2, 2026-04-10）— tNavigator 油藏仿真
- kingdoja/autonomous-driving-rag-mcp（★0, 2026-04-20）— 自动驾驶 RAG
- contextkits/naval-shipbuilding-standards（★0, 2026-02-10）— 海军造船标准
