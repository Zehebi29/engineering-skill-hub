# Daily Discovery — 2026-07-14 (周二)

## 搜索领域
航空航天/CFD + 机器人/ROS + 能源/电力/电池

## 查询
**方式 B (MCP server):**
- aerospace MCP server, CFD MCP server, aerodynamics MCP server, OpenFOAM MCP server, flight simulation MCP server, ANSYS MCP server
- "robotics" MCP, "ROS" MCP server, "ROS2" MCP server, "motion planning" MCP, "manipulator" MCP
- "power system" MCP, "power grid" MCP, "EnergyPlus" MCP, "OpenDSS" MCP

**方式 D (Agent skill):**
- aerospace agent skill, aerospace skill, CFD agent skill, CFD skill, aerodynamics agent skill
- robotics agent skill, robotics skill, ROS agent skill, ROS2 agent skill
- power system agent skill, power system skill, energy engineering agent skill, energy agent skill

## 统计
- 查询总数: 28
- 候选总数: 171
- Star >= 20 候选: 68
- 新增收录: 2

## 新增条目

### 社区精选 Skills 表

1. **[robotics-skills-suite](https://github.com/jherrodthomas/robotics-skills-suite)** (★259)
   - 描述: 76 audit-ready Claude skills for industrial robot, cobot, AMR, ROS2, V&V, AI/ML, and IEC 62443 lifecycle
   - 领域: 机器人/ROS
   - 验证: 有 skills/ 目录，38 commits，活跃维护（latest commit last week），ISO 标准锚定
   - 查询: robotics agent skill (way D)

2. **[PowerSkills](https://github.com/Power-Agent/PowerSkills)** (★55)
   - 描述: Agent Skills for power system analysis using PowerWorld, PSSE, OpenDSS 
   - 领域: 能源/电力/电池
   - 验证: 同 PowerMCP 作者（Power-Agent 组织），17 commits，last month 推送，有 .claude-plugin 和 powerskills-engineering 目录
   - 查询: power system agent skill (way D)

## 跳过候选

### 航空航天/CFD
- knewnothing-git/ansys-mcp-server (★41, pushed 2025-09-14, >90d 不活跃)
- Soljourner/claude-engineering-skills (★37, pushed 2025-11-07, >90d 不活跃)
- devideamax/aerospace-team (★16, star 过低)
- cavoiie/fluent-cfd-skill (★14, star 过低)

### 机器人/ROS
- ros-claw/rosclaw (★161, pushed 2026-07-12) — 运行时基础设施，非 SKILL.md 集合
- telekinesis-ai/telekinesis-examples (★60, pushed 2026-07-03) — Python 库，非 SKILL.md 集合
- kisaragi-mochi/stackchan-mcp (★87, pushed 2026-07-12) — StackChan MCP gateway，已有 stack-chan 条目
- lpigeon/ros-skill (★24, pushed 2026-02-27, >90d 不活跃)
- ManiSkill (★3100) — 机器人仿真/基准测试平台，非 agent skill
- ASAP (★2066) — RSS 2025 论文代码，非 agent skill
- motion_imitation (★1443) — 论文代码，非 agent skill
- RoboGen (★1212) — 机器人 agent 框架，非 SKILL.md 集合
- bagel (★387) — 机器人/drone/IoT 数据聊天，非 MCP/agent skill
- rf-mcp (★107) — Robot Framework MCP，非物理机器人
- nvidia-isaac/isaac_mission_dispatch (★101) — VDA5050 fleet dispatch，topic mcp 误匹配
- 其他: xcodeproj-mcp, illustrator-mcp, vs-claude, mcp-browser-agent, HarmonyOS-mcp 等均为通用工具，非工程相关

### 能源/电力/电池
- ai-evos/agent-skills (★21, pushed 2026-02-25, >90d 不活跃)
- content-designer/ux-writing-skill (★124) — UX writing，非工程
- staskh/trading_skills (★289) — 期权交易，非工程
- aloth/PowerSkills (★27) — Windows PowerShell，非电力系统
- 其余低星 (<20) 候选全部跳过

## MCP Server 生态观察
- 航空航天/CFD: openfoam-mcp-server (★110) 和 stk-mcp (★40) 仍然只有这两个条目。ANSYS MCP 生态持续不活跃。
- 机器人/ROS: Skills 生态活跃（robotics-skills-suite ★259 是高质量新增），MCP 生态已饱和（8 个已有条目覆盖全面）
- 能源/电力/电池: PowerSkills (★55) 是首个进入 Skills 表的电力系统 agent skill，与已有 PowerMCP (MCP server) 互补
