# Daily Discovery — 2026-08-08 (Saturday)

## 搜索领域
综合扫描 — awesome-mcp-servers 反向提取（工程 section 白名单过滤）

## 查询数 / 候选数 / 新增收录
- awesome-mcp-servers: 3821 行（08-01 为 3820，+1 行/周，增量极小）
- 工程 section bullet items: 173 去重后候选（Aerospace 3 / Art & Culture 64 / Architecture 19 / Biology 38 / Embedded 16 / Environment 5 / Industrial 1 / Travel 45，去重后剩 173）
- 手工 LLM 筛选工程相关候选（API 验证）: 24 个
- 新增收录: 1 个（MCP Servers 表）

## 新增条目

### 1. [serial-mcp-server](https://github.com/Adancurusul/serial-mcp-server) ★83 → 嵌入式 / 硬件
- Rust MCP server + CLI for serial/UART 设备：JSON 宏 DSL 定时流程自动化（send→delay→expect）、无硬件仿真验证、宏计划/回放，含 `skills/serial-debug` agent skills 目录
- pushed 2026-07-07（活跃），17 commits，2 tags，MIT license，README 中英双语
- 收录理由：★83 ≥ 20，90 天内活跃，嵌入式串口调试领域高度相关。**与同作者 embedded-debugger-mcp（★137，ARM Cortex-M/RISC-V probe-rs 调试）互补**（Pitfall #58：同作者互补为正面信号）——一个管调试器，一个管串口通信，无功能重叠

## 已跳过候选及原因

| 候选 | Star | 跳过原因 |
|------|------|----------|
| ByteAsk/ByteAsk-Embedded-MCP | 23 | 核心检索引擎+语料库闭源（依赖托管端点 mcp.byteask.ai），开源部分仅 API 外壳（公司数据驱动模式，Pitfall #64 变体 2） |
| 0x1abin/matter-controller-mcp | 8 | 智能家居 Matter 协议，★8 过低 |
| octoco-ltd/sheetsdata-mcp | 9 | 元件 datasheet 查询，★9 过低 |
| turbyho/fw-context-mcp | 7 | 嵌入式固件语义索引，★7 过低 |
| JannLeo/telinksdk-builder-mcp | 1 | ★1 过低 |
| adancurusul/serial-mcp-server | 83 | ✅ 已收录 |
| aidc2026ai-melon/aidc-ai-mcp | 3 | 数据中心设计，★3 过低 |
| smaniches/uniprot-mcp | 3 | ★3 过低 |
| smaniches/alphafold-sovereign-mcp | 4 | ★4 过低 |
| hlydecker/ucsc-genome-mcp | 6 | ★6 过低 + pushed 2025-11 不活跃 |
| dnaerys/onekgpd-mcp | 2 | ★2 过低 |
| longevity-genie/gget-mcp | 30 | pushed 2025-10-27 不活跃（>90 天） |
| longevity-genie/biothings-mcp | 33 | pushed 2025-11-03 不活跃（>90 天） |
| atmospore/atmospore-mcp | 1 | 花粉预报，★1 过低 |
| nalediym/touch-grass | 2 | ★2 过低 |
| FoundryNet/forge-mcp | 0 | Industrial IoT，★0 过低 |
| Perufitlife/aviation-mcp | 1 | 航空数据，★1 过低 |
| IO-Aerospace-software-engineering/mcp-server | — | 404 Not Found（2026-08-01 已确认，本周再次确认，已在 deleted-repos.md） |
| yoelbassin/gnuradioMCP | — | Moved Permanently → 即已收录的 gr-mcp（更名） |

## 上周低星复查（2026-08-01 跳过候选）

| 候选 | 上周 | 现在 | 状态 |
|------|------|------|------|
| Zhonghao1995/Agentic-MIKE-Plus | 5 | 5 | 仍过低（MIKE+ 水动力 MCP，作者同 agentic-swmm-workflow） |
| mikan-atomoki/text-to-model | 6 | 6 | 仍过低（Fusion 360 文本转模型） |
| FoundryNet/forge-mcp | 0 | 0 | 仍过低 |
| asmith26/jupytercad-mcp | 20 | 20 | pushed 2025-10-07 不活跃 |
| OctoEverywhere/mcp | 35 | 35 | pushed 2025-07-03 不活跃 |

## 观察
- 本周 awesome-mcp-servers 增量仅 +1 行，周六综合扫描收益趋近零（延续 08-01 的 +98 行/周回落趋势）
- Embedded 领域本周唯一实质新增（serial-mcp-server），与上周 gr-mcp/pyslang-mcp 形成嵌入式+半导体工具链的持续积累
- Biology section 大量新条目但全部低星（<10）或 longevity-genie 系列不活跃，无一达标
