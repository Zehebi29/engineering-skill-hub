# 每日发现记录 — 2026-07-04（周六）

## 今日策略

周六综合扫描：从 awesome-mcp-servers（3230 行）反向提取工程相关 MCP server。

## 处理流程

1. 下载 awesome-mcp-servers README（3230 行，2725 个 bullet 条目）
2. 初级关键词过滤 → 643 个候选
3. 精炼关键词过滤 → 133 个工程相关候选
4. GitHub API 批量查星验证 → 确认最有可能的 33 个候选
5. Browser 深度验证部分候选

## 查询效果

精炼关键词过滤后仍有大量噪音，但 133 个候选已可通过手动检查筛选。最大噪音源：句子中包含 engineering 相关单词子串的通用工具（如 "ros" 子串在大量非机器人工具中出现）。

## 候选验证结果

### 通过 GitHub API 检查的候选（按结果）

| 仓库 | Star | pushed_at | 结果 |
|------|------|-----------|------|
| IO-Aerospace-software-engineering/mcp-server | ★0 | — | 无数据 |
| asmith26/jupytercad-mcp | ★19 | 2025-10-07 | ★不达标+不活跃 |
| mikan-atomoki/text-to-model | ★4 | 2026-03-16 | ★不达标 |
| OctoEverywhere/mcp | ★34 | 2025-07-03 | 不活跃(>1年)，且已有 mcp-3D-printer-server 覆盖 |
| zackpeters93/ugs-mcp | ★2 | 2026-06-12 | ★太低 |
| ksterx/srunx | ★15 | 2026-07-02 | ★不达标，但活跃(566 commits) |
| HanSur94/matlab-mcp-server-python | ★3 | 2026-04-03 | ★太低 |
| TylerIlunga/procore-mcp-server | ★2 | 2026-06-04 | ★太低 |
| yoelbassin/gnuradioMCP | ★0 | — | 无数据 |
| Zhonghao1995/agentic-swmm-workflow | ★16 | 2026-07-03 | ★不达标，但非常活跃(449 commits, 4h前) |
| bruno-portfolio/agrobr-mcp | ★25 | 2026-03-12 | 不活跃(~114天) |
| cobanov/teslamate-mcp | ★132 | 2026-06-23 | 非工程专用（Tesla 车主数据） |
| lodordev/mcp-teslamate-fleet | ★0 | 2026-03-23 | ★太低 |
| vessel-api/vesselapi-mcp | ★0 | 2026-05-23 | ★太低 |
| tools-mcp/vessel-traffic-mcp | ★0 | 2026-06-30 | ★太低 |
| Perufitlife/aviation-mcp | ★0 | 2026-06-18 | ★太低 |
| jagan-shanmugam/climatiq-mcp-server | ★9 | 2025-03-28 | 不活跃 |
| aliafsahnoudeh/wildfire-mcp-server | ★0 | 2025-12-27 | ★太低+不活跃 |
| Patent-PreCheck/patent-precheck-mcp | ★0 | 2026-06-18 | ★太低 |
| smythmyke/patent-search-mcp-server | ★1 | 2026-06-08 | ★太低 |
| tushariitr-19/patents-mcp | ★2 | 2026-06-19 | ★太低 |
| longevity-genie/gget-mcp | ★29 | 2025-10-27 | 不活跃(>8月) |
| vitorpavinato/ncbi-mcp-server | ★11 | 2025-06-28 | 不活跃 |
| musharna/plant-genomics-mcp | ★0 | 2026-06-29 | ★太低 |
| PantelisGeorgiadis/dicomweb-mcp-server | ★2 | 2026-05-16 | ★太低 |
| lpigeon/ros-mcp-server | ★0 | — | 无数据 |
| qinisolabs/icdwise | ★0 | 2026-06-22 | ★太低 |
| MyMedi-AI/mymedi-ai-mcp-server | ★1 | 2026-06-11 | ★太低 |
| kimimgo/viznoir | ★15 | 2026-07-01 | ★不达标，活跃(289 commits)，同作者已有 awesome-ai-cae 在 README |
| the-momentum/fhir-mcp-server | ★90 | 2025-10-23 | 不活跃(>8月)，且已有 wso2/fhir-mcp-server |
| Lukaris/framedeck-mcp | ★0 | 2026-04-08 | ★太低 |
| catallo/misterclaw | ★5 | 4月前 | ★太低+不活跃，MiSTer FPGA MCP |

## 新增收录

**0 个** — 无候选同时满足 star >= 20 + 活跃 + 非重复 + 工程相关。

## 未来复查候选（★< 20 但活跃）

| 仓库 | Star | 活跃度 | 领域 | 备注 |
|------|------|--------|------|------|
| Zhonghao1995/agentic-swmm-workflow | ★16 | 449 commits, 4h 前推送 | 环境/水利 - SWMM 暴雨管理 | 已有记录，等待 ★20 |
| ksterx/srunx | ★15 | 566 commits, 2天前推送 | HPC/SLURM 集群管理 | 新出现候选 |
| kimimgo/viznoir | ★15 | 289 commits, 2周前推送 | CFD/FEA 科学可视化 | 同作者已有 awesome-ai-cae |

## 备注

- awesome-mcp-servers 规模保持 ~3230 行，与上周一致
- 本周六无新增收录，主要原因为候选不满足 star 阈值或活跃度要求
- 最值得关注的新兴项目：agentic-swmm-workflow（SWMM 水文模拟）和 srunx（SLURM HPC 集群管理）
