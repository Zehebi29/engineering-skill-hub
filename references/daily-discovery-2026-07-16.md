# 每日发现记录 — 2026-07-16（周四）

## 领域
- 油藏/石油/地质
- 汽车/自动驾驶
- 船舶/海洋工程

## 搜索概况
- 查询数: 20（方式 B + 方式 D + 具体工具名补充查询）
- 候选数: 约 80 (含低星)
- 新增收录: 1

## 新增

### 社区精选 Skills
| Skill | 描述 | 来源 | Star |
|-------|------|------|------|
| [automotive-skills-suite](https://github.com/jherrodthomas/automotive-skills-suite) | 152+ Claude skills for automotive engineering: ISO 26262 functional safety, ISO/SAE 21434 cybersecurity, ISO 21448 SOTIF, AIAG-VDA quality (APQP/PPAP/FMEA), Automotive SPICE, AUTOSAR, CAN/LIN/Ethernet | [jherrodthomas](https://github.com/jherrodthomas) | 2144 |

### 收录理由
- ★2144 (远超 ★100 门槛)
- pushed 2026-07-15 (14 小时前), 59 commits, 7 tags, 109 forks
- 真正的 agent skill 集合：`skills/` 目录含数百个 `.skill` 文件（builder + reviewer 配对模式）
- 覆盖汽车工程完整生命周期：功能安全(ISO 26262)、网络安全(ISO/SAE 21434)、SOTIF(ISO 21448)、质量(AIAG-VDA APQP/PPAP/FMEA)、ASPICE、AUTOSAR、车载通信(CAN/LIN/Ethernet)
- 同作者 jherrodthomas 的 robotics-skills-suite(★259) 已在 README。两者互补——汽车 vs 机器人，不同工程细分方向（Pitfall #58 适用）

## 跳过

### 油藏/石油/地质
| 仓库 | Star | 原因 |
|------|------|------|
| kucherenko/petropowers | 8 | Star 过低 (<20)，石油工程 AI skills 框架 |
| ameyxd/petromcp | 2 | Star 过低，石油数据格式 MCP |
| OilCoder/petro-agent | 2 | Star 过低，petrophysical reports MCP |
| 其余 | 0-1 | 无关项目或 Star 过低 |

### 汽车/自动驾驶
| 仓库 | Star | 原因 |
|------|------|------|
| NVIDIA/elements | 26 | Design System/UI Agent Harness，伪装为自动驾驶（Pitfall #31b），Skip |
| agrathwohl/carla-mcp-server | 13 | CARLA audio plugin host，非 CARLA 自动驾驶模拟器 MCP |
| Sma1lboy/autonomous | 6 | Star 过低，自驱动 agent 项目 |
| CSOAI-ORG/* | 0 | Star 为零 |
| kingdoja/autonomous-driving-rag-mcp | 0 | Star 过低的 demo 项目 |

### 船舶/海洋工程
| 仓库 | Star | 原因 |
|------|------|------|
| — | — | 所有查询均无合格候选 |

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 22 (+1)
- 社区精选 MCP Servers: 现有数维持

## 备注
- 三个周四领域中有两个（油藏/石油/地质、船舶/海洋工程）MCP 生态持续空白
- 汽车/自动驾驶领域虽 MCP 搜索为零，但方式 D（agent skill 搜索）成功发现 automotive-skills-suite ★2144
- automotive-skills-suite 与现有的 robotics-skills-suite 同作者互补，jherrodthomas 成为 README 中第一个跨领域双条目作者
