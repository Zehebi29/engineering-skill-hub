# 每日发现记录 — 2026-08-09（周日补漏）

## 执行背景
- 本周 15 领域全部已覆盖（08-04/05 周二三缺失已于 08-06 补扫，无新缺口）
- 周日补漏四阶段执行：无缺失日期模式

## 阶段一：awesome-mcp-servers 增量差异检查
- 当前行数: 3821（08-08 周六为 3821，**增量 +0 行/周**）
- 增量 < 10 → 跳过全量扫描，不做 section 过滤（延续 08-01 以来增量回落趋势：+98 → +1 → +0）

## 阶段二/三：低星候选 + 复苏候补 API 批量复查（Individual Repo API，16 个候选）

### 新增收录（1）
| 仓库 | Star | pushed_at | 说明 |
|------|------|-----------|------|
| ScottDuncanAI/claude-manufacturing-skills | 34 | 2026-08-06 | Claude Skills 编码化学制造工程实践：pfd-generator 从工艺描述生成概念 PFD（editable SVG + Python 脚本），含蒸馏塔/控制回路工程规范审查。真实 SKILL.md 结构（skills/pfd-generator + .claude-plugin + templates/），18 commits、3 contributors、1 release、MIT、pushed 2 天前。**★7→34 四天暴增**（08-07 刚创建时 ★7 记为观察对象，browser 验证非刷星：内容真实、结构完整、有 release 下载），填补 Skills 表**化工/流程模拟方向首个 agent skill**（该领域此前仅 ChEMBL/PubChem 数据库 MCP，流程模拟 MCP 生态空白） |

### 低星复查（未跨过阈值，继续观察）
| 仓库 | 上周 | 现在 | pushed_at | 状态 |
|------|------|------|-----------|------|
| kimimgo/viznoir | 18 | 18 | 2026-08-05 | VTK 科学可视化 MCP，仍活跃（289+ commits），接近 ★20 门槛 |
| Nodeblue-AI/studio5000-mcp-server | 17 | 18 | 2026-06-12 | 品牌级 PLC MCP，★12→17→18 持续增长，接近阈值 |
| CliDyn/copernicus-mcp | 12 | 12 | 2026-08-05 | Copernicus 环境数据 MCP，活跃但星低 |
| The-OpenROAD-Project/OpenROAD-MCP | 12 | 12 | 2026-08-06 | OpenROAD 官方组织 MCP，活跃，官方组织信号（Pitfall #56） |
| lcapossio/hdldiagZero | 17 | 17 | 2026-08-04 | HDL 诊断，活跃但星低 |
| sandraschi/freecad-mcp | 15 | 15 | 2026-07-28 | 活跃但星低 |
| kucherenko/petropowers | 9 | 10 | 2026-04-07 | 石油工程 AI skills，不活跃（pushed >90 天），★仅 +1 |
| Zhonghao1995/Agentic-MIKE-Plus | 5 | 5 | 2026-07-07 | 仍过低 |
| mikan-atomoki/text-to-model | 6 | 6 | 2026-03-16 | 仍过低 + 不活跃 |
| londey/claude-skill-verilog | 18 | 18 | 2026-04-21 | 不活跃（>90 天） |

### 复苏候补复查（均未复苏，继续候补）
| 仓库 | Star | pushed_at | 状态 |
|------|------|-----------|------|
| brack101/AspenPlus-MCP-Server | 30 (31) | 2025-10-09 | 未复苏。Aspen Plus MCP 化工领域空白仍待填补 |
| Yutarop/ros-mcp | 36 (35) | 2025-08-19 | 未复苏 |
| cadugrillo/s7-mcp-bridge | 21 (21) | 2026-03-20 | 未复苏（08-07 刚复查过，一致） |

### 404 复查（保持 deleted-repos.md 记录）
- IO-Aerospace-software-engineering/mcp-server — 仍 404（第三度确认）
- RohanYashRaj/FPGA-Agent-skills — 仍 404

## 统计
- 新增收录: 1（Skills 表，化工/流程模拟方向首个 agent skill）
- 复查候选: 16（低星 10 + 复苏 3 + 404 复查 2 + 已收录 1）
- README 当前: 社区精选 Skills 77（+1）、MCP Servers 185+

## 备注
- **claude-manufacturing-skills 是本周第二个通过"新建→观察→快速收录"路径的候选**（08-07 创建时 ★7，四天后 ★34）——低星观察机制有效，新建但质量高的 skill 仓库可快速爆发
- 化工/流程模拟 Skills 表首次有条目，该领域 MCP 生态空白但 agent skill 方向开始出现苗头
- 下周继续观察：kimimgo/viznoir（★18 活跃）、Nodeblue-AI/studio5000-mcp-server（★18 增长中）
