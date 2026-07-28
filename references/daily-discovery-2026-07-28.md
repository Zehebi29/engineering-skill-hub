# 每日工程 Skill/MCP 发现记录 — 2026-07-28（Tuesday）

## 搜索领域
航空航天/CFD + 机器人/ROS + 能源/电力/电池

## 查询数
Way B (MCP): 12 个查询 | Way D (Agent Skill): 14 个查询 | 补充: 4 个查询 = 30 个总查询

## 候选数 → 新增收录
### MCP Servers
- 原始候选: 56 (但绝大多数 ★<20)
- 二次验证(★≥20): 5 个候选
  - 全部因 inactivity (pushed >90天前) 跳过
  - `robot_MCP` (★81, pushed 2025-08-12)
  - `RobotArm-MCP-P340` (★36, pushed 2025-07-10)
  - `ros-mcp` (★35, pushed 2025-08-19)
  - `ros2-mcp-server` (★84, pushed 2025-06-27)
  - `mcp-rosbags` (★27, pushed 2025-09-21)
- **新增收录: 0**

### Skills
- 原始候选: 42 (绝大多数 ★<20)
- 二次验证(★≥20): 4 个候选
  - `NVIDIA/skills` (★2695, 活跃) — 通用 NVIDIA 产品技能目录,非工程领域专用 → 跳过
  - `claude-engineering-skills` (★41, pushed 2025-11-07) → inactivity 跳过
  - `ros-robotics-skill` (★50, pushed 2026-03-09) → inactivity 跳过
  - `ros-skill` (★24, pushed 2026-02-27) → inactivity 跳过
- **新增收录: 0**

### 低星候选复查建议
- `ros-robotics-skill` (wzyn20051216, ★50, pushed 2026-03-09) — 领域高度相关(ROS1/2 engineering-grade skill),但 140+天未更新。如果复苏,值得收录。
- `claude-engineering-skills` (Soljourner, ★41, pushed 2025-11-07) — 机械/航空航天工程 skill 集合,但 260+天未更新。复苏后值得复查。

## 补充搜索发现

### ANSYS MCP 生态
- `ansys-mcp-server` (vorobjewsen30-max, ★43, pushed 2025-09-14) — 通用 ANSYS MCP,但 inactive
- `mechanical-mcp` (★10, pushed 2026-06-23) — ANSYS Mechanical gRPC MCP,活跃但 ★<20
- `hfss-mcp` (★12, pushed 2026-07-03) — HFSS MCP,活跃但 ★<20
- 结论:ANSYS MCP 生态正在萌芽(多个 active 但低星),值得每2-4周复查

## 重复/噪音提示
- `claude-collider` (★49) — SuperCollider 音乐合成,假阳性
- `mcp-wecombot-server` (★38) — 企业微信机器人,非物理机器人
- `MikroMCP` (★42) — MikroTik RouterOS 网络自动化,非工程机器人
- `mt5-trading-mcp` (★4) — MetaTrader 5 金融交易,因 topics 含 `cfd` (差价合约)误匹配

## 备注
- 机器人/ROS 领域现有 8 个 MCP Server 条目,生态成熟但活跃度普遍下降
- 航空航天/CFD 领域仅 2 个条目,生态持续稀少
- 能源/电力/电池 领域仅 2 个条目,新 candidates 均为 ★<20
- 三个领域今日均无新增收录
