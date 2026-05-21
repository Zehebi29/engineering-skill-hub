# Daily Discovery — 2026-05-21 (Thursday)

## 搜索领域
- 油藏/石油/地质 (Petroleum / Reservoir / Geology)
- 汽车/自动驾驶 (Automotive / Autonomous Driving)
- 船舶/海洋工程 (Marine / Ship / Offshore / Ocean Engineering)

## 查询统计
- 总查询数: 39 (石油 11 + 汽车 16 + 船舶/海洋 12)
- 候选数: ~120 唯一仓库扫描
- 新增收录: 1 (Skills 表)
- Merge artifact 清理: 3 行

## 新增条目

### 社区精选 Skills
| Skill | 描述 | Star | 来源 | 领域 |
|-------|------|------|------|------|
| [geoscience-skills](https://github.com/SteadfastAsArt/geoscience-skills) | 30 AI-powered geoscience skills for Claude Code/Cursor/Copilot | 26★ | SteadfastAsArt | 油藏/石油/地质 |

**评星理由**: 26★ (< 100 但 >= 20), 领域高度相关 (地震/测井/3D 建模/地统计), 最后提交 2026-03-15 (< 90 天), README 有实质内容, 未归档.

## 跳过条目及原因

### 油藏/石油/地质
- `pyrestoolbox-mcp` (41★) — 已收录
- `ameyxd/petromcp` (2★) — Star 太低
- `petropt/petro-mcp` (1★) — Star 太低
- `blake365/macrostrat-mcp` (7★) — Star 太低 (< 20)
- `luskB/GeoSchlor-MCP` (4★) — Star 太低
- `OilpriceAPI/mcp-server` (2★) — 油价 API, 非工程 MCP
- `zzhonglei/GeoCode-Release` (32★) — 桌面 AI 应用, 非 MCP/agent skill 模板; 有自己的 skill 生态而非通用格式
- `tolenonetwork/toleno-mcp` (153★) — 加密货币挖矿, 非地质工程
- `owenloh/3D-Software-MCP-Server` (2★) — Star 太低
- `SeequentEvo/evo-mcp` (5★) — Star 太低

### 汽车/自动驾驶
- `agrathwohl/carla-mcp-server` (12★) — Carla 音频插件主机, 非 CARLA 模拟器; Star < 20
- `SofianeAlla/carla-mcp` (1★) — CARLA 模拟器 MCP 连接器, Star 太低
- `petrpatek/obd2-mcp-server` (1★) — OBD-II MCP, Star 太低
- `hakuturu583/autoware_claw` (5★) — Autoware MCP 桥, Star 太低
- `kingdoja/autonomous-driving-rag-mcp` (0★) — Star 太低
- `Ansvar-Systems/Automotive-MCP` (1★) — Star 太低
- `carla-simulator/carla` (13969★) — CARLA 模拟器本身, 非 MCP/agent skill
- `soda-auto/soda-sim` (130★) — 车辆模拟器, 非 MCP/agent skill

### 船舶/海洋工程
- `mansurjisan/ocean-mcp` (5★) — 海岸海洋学 MCP, Star 太低
- `AQUAVIEW-DAH/mcp` (3★) — 海洋大气数据 MCP, Star 太低
- `weather-mcp/weather-mcp` (12★) — 通用天气 MCP, 非海洋专用; Star < 20
- `reyemb/oss-aisexplorer` (34★) — 船舶跟踪 Web 工具, 非 MCP 或 agent skill
- `JuliaOcean/AIBECS.jl` (40★) — Julia 库, 非 MCP 或 agent skill
- `unmodeled-tyler/vessel-browser` (80★) — "Vessel" 是品牌名, 非船舶工程

## 额外修复
- 清理了 3 行来自之前 cron 冲突的 merge artifact: `(feat: add 10 engineering entries (mon daily scan - CAD/PCB))`

## 领域生态观察
- **油藏/石油/地质**: 地学 agent skill 生态开始萌芽 (geoscience-skills 26★, GeoCode-Release 32★), 但 MCP server 仍只有 pyrestoolbox-mcp (41★)
- **汽车/自动驾驶**: CARLA 模拟器 MCP 连接器处于极早期 (1★), OBD-II MCP (1★), Autoware MCP 桥 (5★); 均未达到收录阈值
- **船舶/海洋工程**: 海洋 MCP 生态几乎空白; weather-mcp (12★) 有海洋天气功能但不专注于此领域
