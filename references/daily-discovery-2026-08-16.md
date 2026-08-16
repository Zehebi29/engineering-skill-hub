# Daily Discovery — 2026-08-16（周日补漏）

## 执行背景
- 本周 15 领域**全部已覆盖**：08-10（周一）缺口已由 08-11 补扫，08-14（周五）缺口已由 08-15 补扫，无新缺口
- 周日补漏四阶段执行（无缺失日期模式）

## 阶段一：awesome-mcp-servers 增量差异检查
- 当前行数：**3821（连续第 3 周零增量：08-08/08-15/08-16 均为 3821）**
- 增量 < 10 → 跳过全量 section 扫描，直接做候选 API 验证

## 阶段二/三：低星候选 + 复苏候补 API 批量复查（Individual Repo API，26 个候选）
- 复查清单构建规则：只复查因「Star 过低」跳过且 ★≥5 的候选（类型正确、领域相关、未归档），加复苏候补（★≥20 因不活跃跳过）与 404 复查
- 数据源：本周记录（08-11/12/13/15）+ 上周 08-09 补漏记录

### 新增收录：0

### 低星复查（19 个，均未跨过 ★20 或有饱和问题）
| 仓库 | 上周 | 现在 | pushed_at | 状态 |
|------|------|------|-----------|------|
| sandraschi/freecad-mcp | 15 | **20** | 2026-07-28 | **跨线但 FreeCAD 生态饱和跳过**（README 已有 neka-nat ★1583 / ghbalf ★408 / bonninr ★210 / spkane ★167 四个 FreeCAD 条目，browser 验证为 FastMCP 自动化 server，CFD 扩展（FluidX3D/OpenFOAM）是唯一差异化，61 commits，3 周前活跃；按 Revit 饱和先例（08-12 IbrahimFahdah ★21 跳过）不收录，CFD 角度值得后续观察 |
| Nodeblue-AI/studio5000-mcp-server | 18 | **19** | 2026-08-13 | ★12→17→18→19 持续增长，最接近门槛的品牌级 PLC MCP，继续观察 |
| nodeblue-ai/ignition-mcp-server | 10 | 10 | 2026-08-13 | ★4→10 增长后稳定，活跃（pushed 3 天前），继续观察 |
| kimimgo/viznoir | 18 | 17 | 2026-08-11 | ★18→17 微降，仍活跃，接近门槛 |
| The-OpenROAD-Project/OpenROAD-MCP | 12 | 13 | 2026-08-12 | 官方 org +1，pushed 4 天前活跃，继续观察 |
| lcapossio/hdldiagZero | 17 | 17 | 2026-08-10 | 活跃，接近门槛 |
| midhunxavier/opcua-mcp | 16 | 16 | 2026-06-05 | 不变 |
| vibeic/vibe-ic | 16 | 16 | 2026-08-15 | 不变，活跃 |
| najaeda/naja-scope | 15 | 15 | 2026-08-05 | 不变 |
| paulieb89/pyp6xer-mcp | 12 | 12 | 2026-05-17 | 进度管理新方向，不变 |
| Nice3point/revit-skills | 11 | 11 | 2026-08-13 | 知名作者，活跃，仍 <20 |
| CliDyn/copernicus-mcp | 12 | 12 | 2026-08-05 | 不变 |
| kucherenko/petropowers | 10 | 10 | 2026-04-07 | 不活跃（>4 个月），不再重点观察 |
| blake365/macrostrat-mcp | 8 | 8 | 2026-08-09 | 复苏迹象维持（pushed 08-09），★8 仍过低 |
| Zhonghao1995/Agentic-MIKE-Plus | 7 | 7 | 2026-07-07 | 不变 |
| EPEL-SNU/Aspen_Plus_MCP | 5 | 5 | 2026-07-27 | 官方 org 活跃，仍过低 |
| lcapossio/fpgaZeroMCP | 5 | 5 | 2026-08-09 | 不变 |
| zackpeters93/ugs-mcp | 5 | 5 | 2026-06-12 | 不变 |
| luskb/geoschlor-mcp | 5 | 5 | 2026-04-29 | 不变 |

### 复苏候补复查（4 个，均未复苏）
| 仓库 | Star | pushed_at | 状态 |
|------|------|-----------|------|
| brack101/AspenPlus-MCP-Server | 30 | 2025-10-09 | **未复苏**（>300 天）。Aspen Plus MCP 化工领域空白仍待填补，继续候补 |
| Yutarop/ros-mcp | 36 | 2025-08-19 | 未复苏 |
| cadugrillo/s7-mcp-bridge | 21 | 2026-03-20 | 未复苏（>150 天） |
| kakimochi/ros2-mcp-server | 84 | 2025-06-27 | 未复苏（>1 年），存在性再确认（非 404） |

### 404 复查（3 个，全部确认 404，已更新 deleted-repos.md）
- ffffffffelix/automotive-functional-safety — 三度确认（08-02/08-13/08-16），保持 404 记录
- RohanYashRaj/FPGA-Agent-skills — 两度确认（07-29/08-16），保持 404 记录
- IO-Aerospace-software-engineering/mcp-server — 多度确认，保持 404 记录
- **修正**：deleted-repos.md 中 adeleempurpled290/FPGA-Agent-skills 与 bjwanneng/veriflow-cc 两行标注过时——两仓库均已复苏收录（08-12/08-03），本次更新为「勿再当 404」

## 统计
- 新增收录: **0**
- API 复查: 26（低星 19 + 复苏 4 + 404 3）
- README 当前: 社区精选 Skills 42、MCP Servers 102（与 08-15 一致）

## 查询效果观察
- 周日补漏已连续多周 0 新增；低星复查的价值在于**确认增长趋势**而非立即收录——studio5000-mcp-server（★19）和 ignition-mcp-server（★10）是品牌级 PLC 生态最接近门槛的两条线，建议下次补漏优先复查
- freecad-mcp（sandraschi）跨线但生态饱和的判例说明：★20 达标 ≠ 可收录，去重/饱和检查优先级更高（呼应 Pitfall #51）
- awesome-mcp-servers 连续 3 周零增量，周六/周日扫描的边际收益接近零；下周起建议周六仅做行数检查
