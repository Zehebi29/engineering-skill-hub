# Daily Discovery — 2026-06-11 (Thursday)

## 搜索领域
- 油藏/石油/地质 (9 queries + 6 refined)
- 汽车/自动驾驶 (9 queries + 6 refined)
- 船舶/海洋工程 (8 queries + 5 refined)
- Topic searches: 5 queries (all returned 0)

## 总计
- 查询数: 24 (first pass) + 17 (second pass) + 5 (topic) = 46
- 候选数: 76 (raw) → 5 (after dedup/archive/star filter) → 0 (after LLM domain judgment)
- 新增收录: 0

## 领域分析

### 油藏/石油/地质
- **SeequentEvo/evo-mcp** (★5) — Seequent Evo MCP server for geoscience data access. Genuine geoscience MCP, but star too low (5). 12 forks suggests organizational adoption. Created 2026-02-02, last pushed 2026-06-09. **Watch candidate** — may grow given Seequent/Bentley backing.
- **blake365/macrostrat-mcp** (★7) — MCP server for Macrostrat geology API. Genuine geology MCP but inactive since 2025-08-26 (>9 months). Below star threshold.
- No other petroleum/reservoir/drilling MCP servers found.
- 仅 pyrestoolbox-mcp (★42) + geoscience-skills (★28) 已在 README。

### 汽车/自动驾驶
- 搜索结果 90%+ 被 MCP2515 CAN 控制器芯片驱动库污染（Pitfall #31）
- agrathwohl/carla-mcp-server (★13) 是 CARLA **音频插件宿主**的 MCP，非 CARLA 自动驾驶仿真器，完全无关
- 自动驾驶 MCP server 生态持续为零（自 2026-05-28 以来第 4 次确认）

### 船舶/海洋工程
- marine engineering / ship simulation / offshore engineering / naval architecture / subsea MCP 搜索全部返回 0 结果
- ttlappalainen/NMEA2000_mcp (★21) 是硬件驱动库（MCP2515 芯片），非 MCP server
- navado/ESP32MCPServer (★46) 是 ESP32 传感器 MCP server（含 NMEA2000），属嵌入式/硬件领域，非船舶工程专用
- 该领域 MCP 生态完全空白（自 2026-05-28 以来第 4 次确认）

## Topic 搜索结果
所有 5 个 topic 查询返回 0 结果：
- topic:geology AND topic:mcp → 0
- topic:geoscience AND topic:mcp → 0
- topic:petroleum AND topic:mcp → 0
- topic:ocean AND topic:mcp → 0
- topic:maritime AND topic:mcp → 0

确认 Pitfall 结论：topic 搜索对所有工程领域均不可靠。

## 低星候选复查（Watch List）
以下候选 Star 不达标但有增长潜力：
- SeequentEvo/evo-mcp (★5) — Seequent/Bentley 背景的 geoscience MCP，12 forks
- blake365/macrostrat-mcp (★7) — 地质数据 MCP，但已不活跃 >9 个月

## 结论
**三个领域 MCP 生态持续空白，无新增候选。** 这是连续第 4 次周四搜索无结果。建议：
- 油藏/石油/地质：降为月度检查频率，关注 SeequentEvo/evo-mcp 增长
- 汽车/自动驾驶：降为月度检查频率，生态无变化
- 船舶/海洋工程：降为月度检查频率，生态完全空白

## README 当前状态
- 69 个 MCP Servers（无新增）
- 多个领域分组，周四三个领域均为极低活跃
