# 每日发现记录 — 2026-07-11（周六）

## 今日策略

周六综合扫描：从 awesome-mcp-servers（3276 行，+46 vs 上周）反向提取工程相关 MCP server。

## 处理流程

1. 下载 awesome-mcp-servers README（3276 行，2745 个 bullet 条目）
2. 关键词初筛 → 782 个工程相关候选
3. 按 section 精筛（重点扫描：Aerospace & Astrodynamics, Art & Culture, Architecture & Design, Embedded System, Environment, Biology/Medicine, Research, Travel & Transportation, Data Science, Other Tools）
4. GitHub API 批量查星验证 ~30 个候选
5. Browser 深度验证 1 个通过候选

## 候选验证结果

| 仓库 | Star | pushed_at | 结果 |
|------|------|-----------|------|
| ahujasid/blender-mcp | ★23,701 | 2026-06-11 | ✅ 已在 README |
| genomoncology/biomcp | ★547 | 2026-07-10 | ✅ 已在 README |
| horw/esp-mcp | ★154 | 2025-12-27 | ✅ 已在 README（但已不活跃） |
| adancurusul/embedded-debugger-mcp | ★123 | 2026-06-24 | ✅ 已在 README |
| **yusong652/itasca-mcp** (原名 pfc-mcp) | **★121** | **2026-07-10** | **✅ 新增！** |
| ChristianHinge/dicom-mcp | ★99 | 2026-06-12 | ✅ 已在 README |
| PatrickPalmer/MayaMCP | ★87 | 2025-05-12 | ❌ 不活跃(>1年)，且非工程工具 |
| kukapay/modbus-mcp | ★25 | 2025-05-12 | ✅ 已在 README |
| Pradumnasaraf/aviationstack-mcp | ★24 | 2026-02-24 | ❌ 不活跃 |
| pzfreo/build123d-mcp | ★28 | 2026-07-10 | ✅ 已在 README |
| kvgork/gazebo-mcp | ★16 | 2026-07-10 | ❌ Star <20，持续观察 |
| kimimgo/viznoir | ★16 | 2026-07-01 | ❌ Star <20，持续观察(同作者 awesome-ai-cae 已在 README) |
| 其余所有 | <20 | — | ❌ Star <20 或不活跃 |

## 新增收录

### 综合资源

| MCP Server | Star | 描述 |
|------------|------|------|
| [itasca-mcp](https://github.com/yusong652/itasca-mcp) | 121 | ITASCA 数值模拟引擎 MCP server：PFC/FLAC/3DEC/MPoint/MassFlow，DEM/FEM 岩土与地质力学仿真。289 commits, 51 tags, 27 branches，yesterday 活跃。原仓库名 pfc-mcp（★59），近期已更名并扩展到覆盖全部 ITASCA 引擎。 |

## 关键观察

1. **yusong652/itasca-mcp 是重要发现**：原来在 DEM/岩土领域作为 pfc-mcp（★59）被追踪，本次发现已更名并扩展到 itasca-mcp（★121），从单一 PFC 扩展到支持全部 ITASCA 引擎（PFC、FLAC、3DEC、MPoint、MassFlow），star 大幅增长。作为活跃维护（yesterday 推送）、功能完整（289 commits, 51 tags, 27 branches）的项目，顺利收录至综合资源分组。
2. **awesome-mcp-servers 增长放缓**：仅从 3230 → 3276 行（+46 行/周），远低于 2025 年底到 2026 年初的高速增长期。
3. **已有条目覆盖率高**：绝大多数工程相关 MCP server 已被 README 收录。本次扫描确认的 ~30 个候选中有 ~8 个已在 README 中。
4. **Kimimgo 生态**：同作者 kimimgo 已有 awesome-ai-cae（★37, 在 README）和 viznoir（★16, 待复查），形成 CAE 工具生态。
5. **低星观察候选**：gazebo-mcp（★16, pushed yesterday 活跃）和 viznoir（★16, 同作者已有 README 条目）是最值得下次复查的低星候选。

## README 当前状态
- 原创 Skills: 3
- 社区精选 Skills: 10
- 社区精选 MCP Servers: ~92（含本次新增 1 条）
- 总计表格行: 102
