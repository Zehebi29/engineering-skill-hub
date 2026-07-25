# 每日发现记录 — 2026-07-25（周六）

## 领域
- 综合扫描 — awesome-mcp-servers 反向提取工程相关条目

## 搜索概况
- awesome-mcp-servers 规模: 3722 行
- 工程 section 候选: 214 条（覆盖 Aerospace, Art & Culture, Architecture, Biology, Embedded, Environment, Industrial & IoT, Transportation 等）
- GitHub API 验证: 13 个最有前景的候选
- 新增收录: 1

## 新增

### MCP Servers 表 — 土木 / 结构 / BIM

| MCP Server | 描述 | 来源 | Star |
|-----------|------|------|------|
| [opentakeoff](https://github.com/Kentucky-ai/opentakeoff) | Construction plan takeoff MCP：AI agent 驱动 PDF 取量引擎，图纸集 MCP resources，一键房间检测、材料量化 | [Kentucky-ai](https://github.com/Kentucky-ai) | 32 |

### 收录理由
- ★32（超过 ★20 阈值）
- 368 commits, 9 tags, pushed 2 hours ago（极活跃）
- 真正的 MCP server：独立 `mcp/` 目录，`npx opentakeoff-mcp` 在官方 MCP registry 发布
- Stdio transport + MCP resources（sheet、title-block、rendered pages）
- Apache 2.0 许可证
- Construction plan takeoff 是建筑/土木工程特有的工程计量工具，填补了 BIM 分组中施工取量的空缺
- 与现有 Revit/IFC/Tekla 等设计/建模 MCP 互补——opentakeoff 覆盖的是施工前的材料估算环节

## 已验证但跳过的候选

### Aerospace & Astrodynamics
| Repo | Stars | 原因 |
|------|-------|------|
| IO-Aerospace-software-engineering/mcp-server | 404 | 仓库不存在（可能已删除或重命名） |
| viventine-space/orbit-sentinel-mcp | ★1 | Star 过低 |

### Embedded System
| Repo | Stars | 原因 |
|------|-------|------|
| yoelbassin/gnuradioMCP | ★0 | Star 过低 |
| catallo/misterclaw | ★6 | Star 过低（MiSTer FPGA） |
| turbyho/fw-context-mcp | ★5 | Star 过低 |
| adancurusul/serial-mcp-server | 未验证 | 通用串口工具，非工程专用 |

### Industrial & IoT
| Repo | Stars | 原因 |
|------|-------|------|
| FoundryNet/forge-mcp | ★0 | Star 过低（14 协议工业 AI 平台，有潜力但太新） |

### Environment
| Repo | Stars | 原因 |
|------|-------|------|
| Zhonghao1995/Agentic-MIKE-Plus | ★5 | Star 过低（MIKE Plus 水文模拟，已有 agentic-swmm-workflow 在 README） |
| aliafsahnoudeh/wildfire-mcp-server | ★1 | Star 过低 |
| atmospore/atmospore-mcp | ★1 | Star 过低 |

### Transportation
| Repo | Stars | 原因 |
|------|-------|------|
| vessel-api/vesselapi-mcp | ★1 | Star 过低（船舶追踪） |
| Perufitlife/aviation-mcp | ★1 | Star 过低 |

### Biology
| Repo | Stars | 原因 |
|------|-------|------|
| musharna/plant-genomics-mcp | ★3 | Star 过低 |

## 备注
- 本周全领域覆盖情况：Mon-Thu + Fri 均已完成，无遗漏
- 上周六（Jul 18）awesome-mcp-servers 扫描也无新增
- awesome-mcp-servers 新增条目多在 Aggregate/General 类别，工程 section 新增条目普遍低星
- opentakeoff 是今天唯一星数达标的候选，且质量不错（活跃维护 + 真正 MCP server）

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 76（周五 +1）
- 社区精选 MCP Servers: 184+（周五 +3，周六 +1）

## 后续关注
- FoundryNet/forge-mcp ★0 — 概念完整（14 协议、18 厂商），但刚发布，如 Star 增长可复查
- cadugrillo/s7-mcp-bridge ★20 — 周五补充搜索发现的 Siemens PLC MCP，已接近 ★20 阈值，下周复查
