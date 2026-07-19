# Daily Discovery — 2026-07-19（周日补漏）

**搜索策略**: 补漏日 — 本周全部 15 个领域均已覆盖（07-13 至 07-18 均有 daily-discovery 记录），执行低星候选复查 + 增量扫描。

## 低星候选复查

从上周（07-12）和本周的观察清单中提取 6 个低星候选，GitHub Individual Repo API 批量验证：

| 仓库 | 上次 Star | 当前 Star | 变化 | pushed_at | 判断 |
|------|----------|----------|------|-----------|------|
| Zhonghao1995/agentic-swmm-workflow | ★19 (07-12) | **★20** | **+1** | 2026-07-16 | ✅ **跨过★20门槛**，活跃维护（479 commits, 23 tags, 105 branches），最新 commit 2 天前。首个 EPA SWMM 暴雨管理 MCP server，填补环境/水利领域 SWMM 子方向。收录至 环境/水利。 |
| kvgork/gazebo-mcp | ★16 | ★16 | +0 | 2026-07-10 | ❌ 活跃但无增长 |
| ariklapid/pyslang-mcp | ★18 | ★18 | +0 | 2026-06-14 | ❌ 无增长，35天未推送 |
| The-OpenROAD-Project/OpenROAD-MCP | ★11 | ★11 | +0 | 2026-07-18 | ❌ 远低于门槛 |
| embedded-society/altium-designer-mcp | ★23→★27 | ★27 | +0 | 2026-07-18 | ❌ 活跃但★27过低 + altium-mcp(★110)+eda-agent(★86)已覆盖 Altium 生态 |
| Zhonghao1995/Agentic-MIKE-Plus | ★5 | ★5 | +0 | 2026-07-07 | ❌ 远低于门槛 |

**新增收录**: 1

### 新增

#### 环境 / 水利 — MCP Server

| [agentic-swmm-workflow](https://github.com/Zhonghao1995/agentic-swmm-workflow) | Agentic SWMM MCP server：EPA SWMM 暴雨管理模型自动化，QGIS 集成、可复现水文模拟、校准支持、MCP 接口 | [Zhonghao1995](https://github.com/Zhonghao1995) | ★20 |

收录理由：★20（刚过门槛）、479 commits、105 branches、23 tags、pushed 2026-07-16（3 天前，活跃）。Agentic SWMM 连接 AI agent 与 EPA SWMM，支持 QGIS 集成、可复现水文模拟、校准工作流、provenance 追踪。与现有 autocad-mcp（P&ID 水处理）、weather-mcp-server（天气数据）、foehn（气象数据）互补，首次覆盖 SWMM/暴雨管理子方向。仓库名不含 -mcp 但明确有 MCP 接口实现。持续从 ★18→★19→★20 稳定增长（约 +1/周），值得关注。

## 跳过原因统计

| 原因 | 数量 | 说明 |
|------|------|------|
| Star 无增长 (<20) | 5 | gazebo-mcp, pyslang-mcp, OpenROAD-MCP, altium-designer-mcp, Agentic-MIKE-Plus |
| 功能覆盖 | 1 | altium-designer-mcp — 已被 altium-mcp + eda-agent 覆盖 |

## 下周优先复查清单

- **Zhonghao1995/agentic-swmm-workflow** (★20, +1/周) — 刚收录，已观察
- **kvgork/gazebo-mcp** (★16) — 活跃，缓慢增长，复查
- **ariklapid/pyslang-mcp** (★18) — 接近门槛但 35 天无推送

## README 当前统计

- **原创 Skills**: 3（不变）
- **社区精选 Skills**: 74（不变）
- **社区精选 MCP Servers**: 180+（+1）
- **总计表格行**: ~112（+1）
