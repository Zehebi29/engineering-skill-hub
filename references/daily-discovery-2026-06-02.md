# 工程 MCP Server 发现记录 — 2026-06-02（周二）

## 搜索领域
- 航空航天 / CFD
- 机器人 / ROS
- 能源 / 电力 / 电池

## 查询统计
- 查询数: 30（首轮 14 + 补充 16）
- 候选数: 21（首轮）+ 7（补充）+ 0（第三轮）
- 新增收录: 0

## 领域搜索结果

### 航空航天 / CFD
- 查询: aerospace MCP server, CFD MCP server, aerodynamics AI agent, OpenFOAM MCP, flight simulation MCP, ANSYS MCP server, CFD simulation MCP, SU2 MCP CFD, XFOIL MCP server, aerospace simulation MCP, Fluent MCP ANSYS, CFD AI agent tool
- Topic 查询: openfoam+mcp, openfoam+ai, computational-fluid-dynamics+ai, openfoam+llm
- 结果: 仅 1 个候选 `knewnothing-git/ansys-mcp-server` ★25，但 pushed_at=2025-09-14（>90 天不活跃），跳过
- 评估: 航空航天/CFD 领域 MCP 生态仍由 openfoam-mcp-server（★100）和 stk-mcp（★34）主导，无新增

### 机器人 / ROS
- 查询: robotics MCP server, ROS2 MCP server, motion planning MCP, robot manipulator AI agent, kinematics MCP server, manipulator MCP server, industrial robot MCP, UR5 MCP robot, robot simulation MCP, ROS MCP robot arm, humanoid robot MCP, drone UAV MCP server, Isaac Sim MCP server
- Topic 查询: ros+mcp, robotics+mcp, ros2+ai-agent, ros2+mcp-server
- 结果:
  - `manykarim/rf-mcp` ★98 — Robot Framework MCP server（测试自动化），非物理机器人控制，不归入"机器人"分组
  - `kakimochi/ros2-mcp-server` ★82 — pushed_at=2025-06-27（>90 天不活跃），跳过
  - `IliaLarchenko/robot_MCP` ★79 — SO-ARM100 控制，pushed_at=2025-08-12（>90 天不活跃），跳过
  - `lpigeon/unitree-go2-mcp-server` ★79 — Unitree Go2 控制，pushed_at=2025-05-12（>90 天不活跃），跳过
  - `RobotecAI/agentic-mobile-manipulator` ★28 — 仓库机器人 demo，非 MCP server（README 无 MCP 内容），跳过
  - `robotmem/robotmem` ★24 — 机器人记忆系统，太小且非核心机器人控制，跳过
- 评估: 机器人领域 MCP 生态成熟但稳定，ros-mcp-server（★1254）、isaac-sim-mcp（★172）仍为主力。低星候选多但活跃度不足

### 能源 / 电力 / 电池
- 查询: power system MCP, power grid MCP, EnergyPlus MCP, power simulation MCP server, OpenDSS MCP, PowerWorld MCP, PSSE MCP server, energy management MCP, electric grid MCP server
- Topic 查询: energy+mcp, power-systems+ai
- 结果: "power system" 查询返回大量通用工具（mcp-client-for-ollama ★720、atlas-mcp-server ★474 等），全部是关键词误匹配（描述含"power"但与能源工程无关）
- 评估: 能源领域搜索噪音仍然极高。精确查询（power system/grid MCP）只能命中已有条目（PowerMCP、EnergyPlus-MCP），无新增

## 跳过的候选详情

| 候选 | Star | 域 | 跳过原因 |
|------|------|----|---------|
| knewnothing-git/ansys-mcp-server | 25 | 航空航天 | pushed_at=2025-09-14，>90 天不活跃 |
| kakimochi/ros2-mcp-server | 82 | 机器人 | pushed_at=2025-06-27，>90 天不活跃 |
| IliaLarchenko/robot_MCP | 79 | 机器人 | pushed_at=2025-08-12，>90 天不活跃 |
| lpigeon/unitree-go2-mcp-server | 79 | 机器人 | pushed_at=2025-05-12，>90 天不活跃 |
| manykarim/rf-mcp | 98 | 机器人 | 通用测试自动化（Robot Framework），非工程机器人控制 |
| RobotecAI/agentic-mobile-manipulator | 28 | 机器人 | README 无 MCP 内容，非 MCP server |
| robotmem/robotmem | 24 | 机器人 | 通用记忆系统，非核心机器人工具 |

## 总结
今日三个领域（航空航天/CFD、机器人/ROS、能源/电力/电池）均未发现符合条件的新 MCP server。搜索结果主要问题：
1. 航空航天/CFD 和能源/电力生态稳定但增长缓慢
2. 机器人领域有多个候选但大多 >90 天不活跃
3. 能源领域关键词噪音极高（"power system" 匹配大量通用工具）
