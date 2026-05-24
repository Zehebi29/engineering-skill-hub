# 工程 Skill/MCP 发现日报 — 2026-05-24（周日）

## 搜索策略
周日：补漏 — 本周未覆盖的领域 + 上周低星候选复查

### 本周覆盖情况
- 周一 ✅ 机械/CAD/CAM, 电气/PCB/EDA, 材料/焊接/检测 — 10 条新增
- 周二 ✅ 航空航天/CFD, 机器人/ROS, 能源/电力/电池 — 0 条新增
- 周三 ✅ 土木/结构/BIM, 化工/流程模拟, 半导体/VLSI/FPGA — 2 条新增
- 周四 ✅ 油藏/石油/地质, 汽车/自动驾驶, 船舶/海洋工程 — 1 条新增
- 周五 ❌ 工业制造/QA, 生物医学/医疗, 环境/水利/污染 — **未执行（本次补漏）**
- 周六 ✅ 综合扫描（awesome-mcp-servers） — 1 条新增

## 查询统计

### 未覆盖领域搜索（3 个领域 x 6-8 个查询）
| 领域 | 查询数 | 唯一候选（★≥5） | 新增收录 |
|------|--------|-----------------|---------|
| 生物医学/医疗 | 9 | 47 (32 with ★≥5) | 2 |
| 工业制造/QA | 7 | 62 (26 with ★≥5) | 0 |
| 环境/水利/污染 | 6 | 36 (14 with ★≥5) | 0 |
| **合计** | **22** | **145** | **2** |

### 低星候选复查（36 个仓库）
大部分仓库 Star 数未见显著增长。关键发现：
- **JamesANZ/medical-mcp**: ★90→★93（小幅增长，但与 healthcare-mcp-public 重叠）
- 其他候选均未跨越收录门槛
- `petropt/petro-mcp` 和 `williamhoracek/unitree-go2-mcp-server` 已被删除（404）
- `kingtutt/RobotArm-MCP-P340` 已被删除（404）

## 新增条目

### 生物医学 / 医疗

| MCP Server | 来源 | Star | 领域 |
|------------|------|------|------|
| [clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server) | cyanheads | 75 | 生物医学/医疗 |
| [m3](https://github.com/rafiattrach/m3) | rafiattrach | 71 | 生物医学/医疗 |

#### clinicaltrialsgov-mcp-server（★75）
- **描述**: ClinicalTrials.gov v2 API MCP server：577K 临床试验搜索、高级字段过滤、患者匹配、研究详情详解
- **Star 判断**: ★75（20-100 范围内需领域高度相关 + 活跃维护）
- **活性验证**: ✅ 287 commits, 55 tags, v2.4.12 发布，最新提交 10 小时前（2026-05-23）。**极其活跃**
- **领域相关性**: ✅ 完全专注 ClinicalTrials.gov 临床试验数据，专为医疗/生物医学研究设计
- **类型判断**: ✅ 真实 MCP server（TypeScript，`@cyanheads/mcp-ts-core` 框架，10+ 工具 + resources + prompts）
- **独特性**: ✅ 与现有 healthcare-mcp-public（★115）不同——该 server 深度集成 ClinicalTrials.gov v2 API，支持高级过滤条件、字段值发现、患者匹配等，远比通用工具的临床试验功能深入

#### m3（★71）
- **描述**: MIMIC-IV 医疗数据 MCP server：自然语言查询重症监护数据库（支持 DuckDB/BigQuery）
- **Star 判断**: ★71（20-100 范围内需领域高度相关 + 活跃维护）
- **活性验证**: ✅ 183 commits, 8 tags, CI workflows，最新提交 1 个月前（2026-04-24）
- **领域相关性**: ✅ MIMIC-IV 是世界上最著名的开放重症监护医学数据库，是全球医学研究的基础资源
- **类型判断**: ✅ 真实 MCP server（Python FastMCP，自然语言→SQL 转换）
- **独特性**: ✅ 完全独特——现有条目没有任何 MIMIC-IV/MIMIC 数据库支持

## 跳过条目及原因

### 生物医学/医疗
| 仓库 | Star | 原因 |
|------|------|------|
| JamesANZ/medical-mcp | 93 | 与 healthcare-mcp-public 功能重叠（均覆盖 FDA、PubMed、多源医学数据） |
| jmandel/health-record-mcp | 78 | 最后提交 9 个月前，超过 90 天无更新 |
| rafiattrach/physionet-mcp | 10 | Star < 20 |
| u9401066/pubmed-search-mcp | 13 | Star < 20，且功能被 mcp-simple-pubmed 覆盖 |
| sunanhe/awesome-medical-mcp-servers | 67 | Awesome list（列表/合集），非 MCP server |

### 工业制造/QA（无合格候选）
| 仓库 | Star | 原因 |
|------|------|------|
| yvgude/lean-ctx | 2118 | "Lean" 指 Lean Theorem Prover，非精益制造 |
| tavily-ai/tavily-mcp | 2004 | 通用搜索 MCP，非工程专用 |
| nixopus/nixopus | 1438 | 通用基础设施平台 |
| golf-mcp/golf | 826 | 通用 MCP 框架 |
| Svetlana-DAO-LLC/cad-agent | 20 | CAD 3D 打印但 Star 刚达标，需进一步验证 |
| OctoEverywhere/mcp | 33 | 3D 打印 MCP，但仓库只有文档无代码实现 |

### 环境/水利/污染（无合格候选）
| 仓库 | Star | 原因 |
|------|------|------|
| puran-water/mathcad-mcp | 7 | Star < 20 |
| Zhonghao1995/agentic-swmm-workflow | 7 | Star < 20，且 SWMM 水文模拟 MCP 极早期 |
| jcholly/geotap-developer | 6 | Star < 20 |
| CliDyn/copernicus-mcp | 5 | Star < 20 |

### 低星复查：标记为已删除（404）的仓库
- petropt/petro-mcp — 404 Not Found
- williamhoracek/unitree-go2-mcp-server — 404 Not Found
- kingtutt/RobotArm-MCP-P340 — 404 Not Found

## 统计
- 今日查询数：22 (API) + 36 (recheck)
- 候选数：145
- 新增收录：2（均为 MCP Servers）
- README 当前：4 个 Skills + 48 个 MCP Servers（增 2）
- 生物医学/医疗：3 → 5 条
