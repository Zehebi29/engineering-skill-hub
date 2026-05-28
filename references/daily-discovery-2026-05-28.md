# Daily Discovery — 2026-05-28 (Thursday)

## 搜索领域
- 油藏/石油/地质
- 汽车/自动驾驶
- 船舶/海洋工程

## 查询统计

| 领域 | 查询数 | 候选数 | 新增收录 |
|------|--------|--------|----------|
| 油藏/石油/地质 | 15 | 27 | 0 |
| 汽车/自动驾驶 | 14 | 18 | 0 |
| 船舶/海洋工程 | 14 | 0 | 0 |
| **合计** | **43** | **45** | **0** |

## 领域观察

### 油藏/石油/地质
该领域 MCP 生态仍然非常稀少。最有价值的发现：
- `ameyxd/petromcp` ★2 — 真正的石油数据格式 MCP server（LAS, DLIS），但 Star 极低
- `andresjbf/tnavigator-mcp` ★1 — tNavigator 油藏模拟 MCP server，最近更新（2026-05-26）
- `blake365/macrostrat-mcp` ★7 — Macrostrat 地质数据 MCP server
- `raghujayan/openvds-mcp-server` ★1 — Bluware OpenVDS 地震数据 MCP server
- `wolfram-laube/clarissa` ★0 — 油藏模拟对话式 AI agent（CLARISSA）
- `h4r1yzz/mcp_langchain` ★0 — 测井分析 MCP

已存在的 `gabrielserrao/pyrestoolbox-mcp`（★41）仍是该领域唯一的中等星数条目。

### 汽车/自动驾驶
搜索结果被 MCP2515 CAN 控制器芯片的硬件驱动库严重污染：
- `Longan-Labs/Arduino_CAN_BUS_MCP2515` ★167 — Arduino CAN 库（硬件驱动，非 MCP server）
- `adamczykpiotr/pico-mcp2515` ★104 — Pico CAN 接口库（硬件驱动）
- `crycode-de/mcp-can-boot` ★40 — AVR CAN 引导加载程序（硬件工具）
- `adafruit/Adafruit_CircuitPython_MCP2515` ★29 — CircuitPython CAN 库

注意：这些仓库中的 "MCP" 指的是 Microchip MCP2515 CAN 控制器芯片，与 Model Context Protocol 完全无关。

真正的汽车/自动驾驶 MCP server 生态几乎为零：
- `CSOAI-ORG/autonomous-vehicles` ★0 — 声称是自动驾驶 MCP server，但无 Star
- `hifriendbot/cogmemai-mcp` ★6 — 提到 autonomous robots/self-driving，但主要功能是认知记忆

### 船舶/海洋工程
该领域 MCP 生态完全空白。所有查询（marine, ship, naval, offshore, ocean, maritime, ROV, subsea, underwater）均返回 0 个相关结果。唯一沾边的是 `ttlappalainen/NMEA2000_mcp` ★21（NMEA2000 船舶电子协议库），但它是硬件驱动库而非 MCP server。

## 跳过的候选及原因

| 候选 | Star | 跳过原因 |
|------|------|----------|
| Longan-Labs/Arduino_CAN_BUS_MCP2515 | 167 | 硬件驱动库，MCP 指 MCP2515 芯片非 Model Context Protocol |
| adamczykpiotr/pico-mcp2515 | 104 | 同上，Pico CAN 接口库 |
| Xingsandesu/CarrotAI | 83 | 非汽车领域，"car" 关键词误匹配 |
| maqi1520/md2card-mcp-server | 79 | Markdown 转卡片工具，非汽车工程 |
| crycode-de/mcp-can-boot | 40 | AVR CAN 引导加载程序，硬件工具 |
| yasir-shahzad/MCP2515-CAN-Bus-Module | 34 | MCP2515 硬件模块文档 |
| trnila/rp2040-can-mcp2515 | 34 | RP2040 CAN 固件，硬件项目 |
| talvinder/carrot-ai-pm | 30 | 产品管理 MCP server，非汽车 |
| adafruit/Adafruit_CircuitPython_MCP2515 | 29 | CircuitPython CAN 库，硬件驱动 |
| ttlappalainen/NMEA2000_mcp | 21 | NMEA2000 库，硬件驱动非 MCP server |
| ameyxd/petromcp | 2 | Star 过低（<20），石油数据格式 MCP |
| blake365/macrostrat-mcp | 7 | Star 过低（<20），地质数据 MCP |
| OilpriceAPI/mcp-server | 2 | Star 过低，石油价格 API 非工程工具 |
| andresjbf/tnavigator-mcp | 1 | Star 过低，油藏模拟 MCP（潜力大但太新） |
| raghujayan/openvds-mcp-server | 1 | Star 过低，地震数据 MCP |
| CSOAI-ORG/autonomous-vehicles | 0 | Star 为零 |
| wolfram-laube/clarissa | 0 | Star 为零，油藏模拟 agent |
| h4r1yzz/mcp_langchain | 0 | Star 为零，测井分析 |

## 总结

今日 3 个领域（油藏/石油/地质、汽车/自动驾驶、船舶/海洋工程）的 MCP 生态均处于极早期或空白状态。汽车/自动驾驶的搜索结果被 MCP2515 CAN 芯片硬件驱动库严重污染（占 90%+ 结果），需要更精准的过滤策略。油藏/石油/地质有少量萌芽项目但 Star 均低于 10。船舶/海洋工程完全空白。

README 当前: 53 个 MCP Servers（无新增）
