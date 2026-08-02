# Daily Discovery — 2026-08-02 (Sunday 补漏)

## 本周执行状态
- 2026-07-27（周一）✅ 机械/CAD/CAM + 电气/PCB/EDA + 材料/焊接/检测
- 2026-07-28（周二）✅ 航空航天/CFD + 机器人/ROS + 能源/电力/电池
- 2026-07-29（周三）✅ 土木/结构/BIM + 化工/流程模拟 + 半导体/VLSI/FPGA
- 2026-07-30（周四）✅ 油藏/石油/地质 + 汽车/自动驾驶 + 船舶/海洋工程
- 2026-07-31（周五）✅ 工业制造/QA + 生物医学/医疗 + 环境/水利/污染
- 2026-08-01（周六）✅ 综合扫描（awesome-mcp-servers）
- **结论：本周 15 个领域全部覆盖，无缺失日期 → 执行四阶段补漏流程**

## 阶段一：awesome-mcp-servers 增量差异检查
- 当前行数：3820（与 08-01 记录一致，**增量 = 0 行**）
- 判定：增量 <10 行 → 跳过全量扫描（阶段四不执行）

## 阶段二：低星候选复查（11 个）
| 候选 | 之前 | 现在 | pushed_at | 结论 |
|------|------|------|-----------|------|
| ffffffffelix/automotive-functional-safety | ★6 | **404** | — | 已删除 → 记录到 deleted-repos.md |
| Zhonghao1995/Agentic-MIKE-Plus | ★5 | ★5 | 2026-07-07 | 无增长，继续观察 |
| mikan-atomoki/text-to-model | ★6 | ★6 | 2026-03-16 | 无增长 + 不活跃 |
| sandraschi/freecad-mcp | ★14 | ★14 | 2026-07-28 | 无增长，活跃 |
| ksterx/srunx | ★16 | ★16 | 2026-07-25 | 无增长，活跃 |
| The-OpenROAD-Project/OpenROAD-MCP | ★12 | ★12 | 2026-07-30 | 无增长，活跃 |
| adityakamath/ros2-skill | ★13 | ★13 | 2026-07-16 | 无增长 |
| Nodeblue-AI/ignition-mcp-server | ★10 | ★10 | 2026-06-12 | 无增长 |
| Nodeblue-AI/studio5000-mcp-server | ★12 | ★12 | 2026-06-12 | 无增长 |
| embedded-society/altium-designer-mcp | ★31 | ★31 | 2026-07-30 | 稳定活跃，仍未达 ★40 收录目标 |
| erebusnz/rigol-mcp | ★21 | ★22（+1） | 2026-07-19 | 缓慢增长，仍未达 ★30 收录目标 |

**结论：0 个跨过 ★20 收录阈值**

## 阶段三：复活候选检查（7 个）
| 候选 | 之前 | 现在 | pushed_at | 判定 |
|------|------|------|-----------|------|
| hedless/onshape-mcp | ★117 | ★125（+8） | 2026-03-04（未变） | Star 增长但代码未恢复活跃 → 不复活 |
| rawwerks/VibeCAD | ★98 | ★102（+4） | 2026-01-05（未变） | Star 增长但 7 个月无更新 → 不复活 |
| wzyn20051216/ros-robotics-skill | ★50 | ★51 | 2026-03-09（未变） | 不复活 |
| Soljourner/claude-engineering-skills | ★41 | ★44 | 2025-11-07（未变） | 不复活 |
| RoboSafe-Lab/ad-safety-research-skills | ★26 | ★27 | 2026-03-27（未变） | 不复活 |
| jinwx/weather-data-skills | ★36 | ★36 | 2026-04-06（未变） | 不复活 |
| cadugrillo/s7-mcp-bridge | ★20 | ★20 | 2026-03-20（未变） | 不复活 |

**结论：0 个复苏**。onshape-mcp（★125）和 VibeCAD（★102）Star 已超阈值但 pushed_at 无改善——按规则（需 Star + pushed_at 双指标改善）不收录。

## 阶段四：404 仓库确认（5 个）
全部确认 404（与 07-31 记录一致）：
- LNC/robot_MCP（另 IliaLarchenko/robot_MCP 拼写）
- cyrilschumacher/ros2-mcp-server
- kingtutt/RobotArm-MCP-P340
- LaplaceYoung/mechanical-mcp
- LaplaceYoung/hfss-mcp

已全部写入新建的 `references/deleted-repos.md`。

## 新增收录
**0 个**（本周补漏无新增）

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 76（无变化）
- 社区精选 MCP Servers: 185+（无变化）

## 备注
- 连续第 2 个周日四阶段补漏零新增（07-26 同样 0 新增）
- onshape-mcp ★125 / VibeCAD ★102 保持复苏候补跟踪：两者 Star 已超阈值，若 pushed_at 恢复活跃即可收录（机械/CAD/CAM Skills/MCP 表）
- altium-designer-mcp ★31 是 EDA 领域最稳定增长的低星候选（连续 3 周 +8/+1/+0），继续跟踪
- deleted-repos.md 为本次新建（skill 引用的 404 清单此前缺失），已收录全部已知删除案例
