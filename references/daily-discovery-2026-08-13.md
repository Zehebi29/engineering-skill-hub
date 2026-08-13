# Daily Discovery — 2026-08-13（周四）

**Cron 状态**：本周无新增缺失。08-10（周一）缺口已在 08-11 补扫并报告；08-12（周三）记录存在。cron `f2cc259c3af0` 本周运行正常（08-11/12/13 连续三天有提交）。

## 搜索领域（周四常规 3 个）
- 油藏/石油/地质
- 汽车/自动驾驶
- 船舶/海洋工程

## 执行统计
- 查询数：26（3 领域 × 8-9 关键词，方式 B MCP + 方式 D agent skill 各半；汽车领域按 skill 建议优先 `"ISO 26262" skill`、`automotive engineering skill`、`AUTOSAR skill`、`functional safety skill`、`automotive SPICE skill`）
- 候选数：124 原始 → README 去重后 124（无已在 README 条目）
- API 验证：12 个候选 Individual Repo API
- Browser 深度验证：0（无候选通过 ★20 门槛）
- 新增收录：**0**

## 跳过详情（重点候选及原因）

### 油藏/石油/地质
| 仓库 | Star | 原因 |
|------|------|------|
| lookfree/cc-harness | 46 | Claude Code 桌面工作台（subagent 拓扑/token 成本），通用工具非工程 |
| swati1024/torrents | 103 | 被 hack 的描述污染仓库（Skip to content），非工程 |
| kucherenko/petropowers | 10 | 石油工程 AI skills 框架（Superpowers 基础，领域空白唯一候选），★9→★10 缓慢增长，pushed 2026-04-07 已 4 个月；继续观察 |
| blake365/macrostrat-mcp | 8 | **复苏迹象**：pushed 2026-08-09（08-06 记录曾 2025-08-26 不活跃），Macrostrat 地质数据 MCP 恢复活跃；但 ★8 仍 <20，继续观察 |
| luskb/geoschlor-mcp | 5 | 地质/物探测井文献检索 MCP（CNKI/OnePetro/万方），★5 过低，观察 |
| wzhang3912/opendtect-mcp | 1 | **新方向**：OpendTect 地球物理 MCP（SEG-Y 导入、3D 地平线自动追踪）——真正的石油/地质专业工具 MCP，但 ★1 过低，观察 |
| cyanheads/eia-energy-mcp-server | 2 | EIA 能源数据 MCP（cyanheads 多产作者），★2 过低 |
| sanjaydasgupta/ai-skills-for-reservoir-engineering | 2 | 油藏工程 AI skills，★2 过低 |
| 其余 40+ 条 | 0-3 | 个人作品集/课程作业/ag2-mcp 自动生成/非工程 |

### 汽车/自动驾驶
| 仓库 | Star | 原因 |
|------|------|------|
| sfedfcv/redesigned-pancake | 255 | 被 hack 的描述污染仓库（Skip to content），非工程 |
| nvidia/elements | 78 | NVIDIA Design System + UI Agent Harness（React/CSS），描述含 Autonomous Vehicles 但非工程（Pitfall #31b） |
| enovella/r2con-prequals-rhme3 | 17 | 硬件 CTF，非工程 skill（08-06 已记录） |
| luna-system/ada | 16 | 聊天框架（ADAS 关键词误匹配，08-06 已记录） |
| fffffffffelix/automotive-functional-safety | — | **404 Not Found**（Search API 缓存脏数据，Pitfall #29；ISO 26262 Codex skill，2-4 周后用 Individual Repo API 复查） |
| duonghvu/automotive-syseng | 4 | 汽车系统工程 skill（INCOSE/EARS、MISRA-C、SAE J3），★4 过低 |
| pangzhenying2025/hermes-automotive-skills | 3 | 汽车 ADAS/AUTOSAR/BMS skills（Hermes 平台），★3 过低 |
| muhammed-salih-karademir/automotive-skills | 3 | 汽车软件 skills，★3 过低 |
| petrpatek/obd2-mcp-server | 2 | OBD-II 诊断 MCP，★2 过低 |
| ariekogan/ateam-mcp | 1 | ADAS MCP（08-06 已记录 ★0），仍过低 |
| 其余 30+ 条 | 0-3 | 个人项目/通用 MCP/非工程 |

### 船舶/海洋工程
| 仓库 | Star | 原因 |
|------|------|------|
| weather-mcp/weather-mcp | 36 | 通用天气数据 MCP（marine 只是工具之一），非船舶工程 + 与 weather-mcp-server 重叠（08-06 已记录） |
| lucasinocencio1/mcp-surf-forecast | 19 | 冲浪预报，非工程（08-06 已记录，★19 仍 <20 且 pushed 2026-02-11 不活跃） |
| cyreslab-ai/marinetraffic-mcp-server | 9 | pushed 2025-05-15 仍不活跃（08-06 已记录） |
| dungnotnull/rc-boat-hydrodynamics-design-agent-skill | 4 | RC 船水动力/船舶设计 Claude skill（新方向），★4 过低 |
| waterwawawa/china-offshore-wind-power | 1 | 海上风电产业链分析 Claude Skill，★1 过低 |
| sailingnaturali/signalk-mcp | 1 | SignalK 船舶数据 MCP，★1 过低 |
| 其余 20+ 条 | 0-1 | 个人作品集/招聘网站/非工程 |

## 查询效果观察
- **三个领域连续第 9 周无新增收录**（油藏/船舶 MCP 生态持续空白；汽车/自动驾驶 Way D 边际收益继续下降，与 08-06 结论一致）。
- 汽车领域 `"ISO 26262" skill` / `functional safety skill` 查询返回大量低星个人项目（★2-6），无 ★20+ 候选。
- 船舶领域 `shipbuilding skill` / `marine engineering skill` 查询被个人作品集、招聘网站严重污染。
- **复苏观察 1 例**：blake365/macrostrat-mcp 从 08-06 的不活跃状态恢复（pushed 2026-08-09），是油藏/地质领域少见的活跃维护 MCP。
- **新方向 2 个**：OpendTect 地球物理 MCP（wzhang3912/opendtect-mcp，SEG-Y/地平线追踪）、RC 船水动力设计 skill（dungnotnull）——均 ★<5，仅记录。
- **404 待复查**：fffffffffelix/automotive-functional-safety（ISO 26262 Codex skill 包，07-22 前无记录，今日 Search API 命中但 Individual Repo API 404），2-4 周后复查存在性（Pitfall #29/#57）。

## README 统计
- 社区精选 Skills：77（不变）
- MCP Servers：不变
