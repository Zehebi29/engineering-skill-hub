# 每日发现记录 — 2026-07-23（周四）

## 领域
- 油藏/石油/地质
- 汽车/自动驾驶
- 船舶/海洋工程

## 搜索概况
- 查询数: 36（方式 B + 方式 D）
- 候选数: 约 30 (含低星)
- 新增收录: 1

## 新增

### 社区精选 Skills
| Skill | 描述 | 来源 | Star |
|-------|------|------|------|
| [autonomousguy](https://github.com/ptsilivis/autonomousguy) | AI skill prompts for embedded automotive engineers — AUTOSAR Classic/Adaptive, MISRA C, ISO 26262 functional safety, ECU debugging, 10 mode-aware skills | [ptsilivis](https://github.com/ptsilivis) | 21 |

### 收录理由
- ★21（刚过 ★20 阈值）
- pushed 2026-07-06 (17 天前), 323 commits, 30 commits on master
- 真正的 agent skill 集合：`skills/` 目录下有 8 个子目录（autosar, change-management, code-quality, debugging, requirements, safety, testing, workspace），每个含 SKILL.md
- Way D 搜索命中（`"ISO 26262" skill` 查询）
- 覆盖嵌入式汽车工程特有的 AUTOSAR Classic/Adaptive、MISRA C:2025、ISO 26262 功能安全、ECU 调试等细分方向
- 与现有 automotive-skills-suite (★2333) 互补：后者更偏体系/法规层面，autonomousguy 专注于 ECU 软件开发实操
- 支持多平台：Claude Code, GitHub Copilot, Cursor, Codex, Gemini CLI
- npm 可安装（`npx skills add ptsilivis/autonomousguy -g`）
- MIT 许可证

## 跳过

### 油藏/石油/地质
| 仓库 | Star | 原因 |
|------|------|------|
| gabrielserrao/pyrestoolbox-mcp | 43 | **已在 README** |
| blake365/macrostrat-mcp | 7 | Star 过低 (<20), pushed 2025-08-26 (不活跃) |
| ttracx/oil-and-gas-claude-skills | 6 | Star 过低 (<20), 钻井 KPIs/总承包 skills |

### 汽车/自动驾驶
| 仓库 | Star | 原因 |
|------|------|------|
| jherrodthomas/automotive-skills-suite | 2333 | **已在 README** |
| NVIDIA/elements | 28 | Design System / UI Agent Harness，伪装为自动驾驶（Pitfall #31b） |
| ptsilivis/autonomousguy | 21 | ✅ **已收录** |
| Aryia-Behroziuan/References | 63 | 学术参考文献合集（计算机科学书单），非 automotive engineering skill |
| Aryia-Behroziuan/Other-sources | 41 | 学术参考文献合集，同上 |
| anantvignesh/Training-Self-Driving-Car-Using-Reinforcement-Learning | 17 | 强化学习教程课程项目，非 agent skill |
| agrathwohl/carla-mcp-server | 13 | CARLA audio plugin host，非 CARLA 自动驾驶模拟器 MCP |

### 船舶/海洋工程
| 仓库 | Star | 原因 |
|------|------|------|
| cporter202/agentic-ai-apis | 351 | 通用 API 集合，非船舶工程 |
| yantrikos/yantrikdb-server | 167 | 通用认知记忆数据库 |
| itechmeat/open-second-brain | 131 | 通用记忆工具 |
| mdowis/anansi | 100 | Web scraper |
| weather-mcp/weather-mcp | 28 | 通用天气 MCP（非海洋工程） |
| lucasinocencio1/mcp-surf-forecast | 19 | 冲浪预测（休闲用途，非工程） |
| Cyreslab-AI/marinetraffic-mcp-server | 9 | 船舶交通追踪 API，非工程 MCP |
| 其余 | 10-167 | 均与船舶/海洋工程无关的通用工具 |

## 备注
- 三个周四领域中有两个（油藏/石油/地质、船舶/海洋工程）MCP 生态持续空白
- 汽车/自动驾驶领域 MCP 搜索（方式 B）持续为零，但方式 D 再次产出一个合格候选
- autonomousguy ★21 与上月收录的 automotive-skills-suite ★2333 同领域互补——前者专注 ECU 级嵌入式开发，后者覆盖体系/法规/质量
- 两个 Skills 表条目均通过方式 D 搜索发现，证明 agent skill 搜索策略在低生态领域仍有效

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 26 (+1)
- 社区精选 MCP Servers: 现有数维持
