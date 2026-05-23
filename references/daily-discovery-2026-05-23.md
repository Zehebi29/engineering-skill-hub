# 工程 Skill/MCP 发现日报 — 2026-05-23（周六）

## 搜索策略
周六：综合扫描 — awesome-mcp-servers + awesome-mcp-clients 反向提取工程相关

## 查询与结果

### 源数据
- awesome-mcp-servers README: 2628 行
- awesome-mcp-clients README: 已扫描，工程内容极少（如预期），跳过深度扫描

### 从 awesome-mcp-servers 提取的工程候选

| 仓库 | Star | 状态 | 说明 |
|------|------|------|------|
| omni-mcp/isaac-sim-mcp | 169 | ✅ 已收录 → 机器人 | NVIDIA Isaac Sim MCP，AI 驱动机器人仿真 |
| IO-Aerospace-software-engineering/mcp-server | 0 | ❌ Star 过低 | 航空航天 MCP server，但无人关注 |
| asmith26/jupytercad-mcp | 18 | ❌ Star 过低 + 7月未更新 | JupyterCAD MCP |
| mikan-atomoki/text-to-model | 2 | ❌ Star 过低 | Fusion 360 文本转模型 |
| OctoEverywhere/mcp | 33 | ❌ 近1年未更新 | 3D 打印 MCP server |
| catallo/misterclaw | 5 | ❌ Star 过低 | MiSTer FPGA MCP |
| yoelbassin/gnuradioMCP | 0 | ❌ Star 过低 | GNU Radio MCP |
| aliafsahnoudeh/wildfire-mcp-server | 0 | ❌ Star 过低 | 野火检测 MCP |
| octoco-ltd/sheetsdata-mcp | 6 | ❌ Star 过低 | 电子元器件 datasheet MCP |
| OFODevelopment/cerebrochain-mcp-server | 0 | ❌ Star 过低 | 供应链物流 MCP |
| stack-chan/stack-chan | 1486 | ❌ 非工程 MCP server | 玩具机器人产品，非工程工具 |

### 补充 GitHub API 搜索（18 个关键词查询）

| 查询 | 有趣候选 | 说明 |
|------|---------|------|
| "CAD" MCP server | AnCode666/multiCAD-mcp ★34 | 多 CAD 支持，但已有 AutoCAD MCP |
| "Fusion 360" MCP server | faust-machines/fusion360-mcp-server ★31 | 另一 Fusion 360 MCP，重复 |
| "PLCs" MCP server | cadugrillo/s7-mcp-bridge ★17 | < 20 stars 阈值 |
| "matlab" MCP server | HanSur94/matlab-mcp-server-python ★1 | < 20 stars |
| "circuit" MCP server | clanker-lover/spicebridge ★19 | < 20 stars |
| "finite element" MCP | ekstanley/ccFenics-plugin ★2 | < 20 stars |
| "power system" MCP | PowerMCP ★142 | 已收录 |

其他 11 个查询均未发现符合条件的候选（Star < 20 或不相关）。

### awesome-mcp-clients
工程内容极少，快速扫描后跳过。

## 新增收录

| 名称 | 来源 | Star | 领域 |
|------|------|------|------|
| isaac-sim-mcp | omni-mcp | 169 | 机器人 |

## 统计
- 今日查询数：1 (awesome-mcp-servers 扫描) + 18 (补充 API 搜索) = 19
- 候选数：13
- 新增收录：1
- README 当前：4 个 Skills + 46 个 MCP Servers (含新增)

## 查询效果分析
- awesome-mcp-servers 依然是工程 MCP 发现的最佳来源
- 补充关键词搜索质量和之前类似——信号噪音比低
- 周六综合扫描日找到的候选数量通常少于领域专项搜索日
