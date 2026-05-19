# Daily Discovery — 2026-05-19 (Tuesday)

## Search Domains
- 航空航天/CFD
- 机器人/ROS
- 能源/电力/电池

## Search Queries Run

### 航空航天/CFD (8 queries)
| Query | Results | Stars ≥10 |
|-------|---------|-----------|
| "CFD" "MCP" | 10 | openfoam-mcp-server ★98, awesome-ai-cae ★28 |
| "aerospace" MCP server | 5 | aerospace-mcp ★3 |
| "flight simulation" AI agent | 0 | — |
| "CFD" "agent" "tool" | 1 | (none) |
| "CFD" simulation MCP | 1 | awesome-ai-cae ★28 |
| "drone" MCP server | 10 | drone-mcp ★25, MAVLinkMCP ★16 |
| "satellite" MCP server | 10 | (none ≥10 relevant) |
| "aerodynamics" MCP | 0 | — |

### 机器人/ROS (5 queries)
| Query | Results | Stars ≥10 |
|-------|---------|-----------|
| "robotics" MCP server | 10 | ros-mcp-server ★1226, rf-mcp ★95, robot_MCP ★78, unitree-go2-mcp-server ★78 |
| "ROS 2" "MCP" | 10 | ros2-mcp-server ★81, ros2_mcp ★77, nav2_mcp_server ★73, ros-mcp ★32 |
| "motion planning" AI agent tool | 0 | — |
| "robot arm" MCP | 10 | RobotArm-MCP-P340 ★34 |
| "mobile robot" MCP | 5 | (none ≥10) |

### 能源/电力/电池 (4 queries)
| Query | Results | Stars ≥10 |
|-------|---------|-----------|
| "power grid" MCP server | 3 | ne_power_grid_mcp_server ★1 |
| "battery" AI agent tool | 9 | All "batteries-included" false positives |
| "solar energy" "MCP" | 0 | — |
| "wind" MCP server | 10 | All Windows/Microsoft false positives |
| "solar" MCP server | 10 | (none relevant) |
| "renewable" MCP | 3 | (none ≥10) |
| "power system" MCP | 10 | PowerMCP ★139 (already in README) |

## Candidates Evaluated

### 航空航天/CFD
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| openfoam-mcp-server | ★98 | Already in README | Listed as ★97, now ★98 |
| awesome-ai-cae | ★28 | Already in README | In 综合资源 section |
| drone-mcp (0xKoda) | ★25 | Skip | Push date 2025-04-09, >90 days inactive. Not actively maintained. |
| MAVLinkMCP | ★16 | Skip | <20 stars. Not maintained. |
| aerospace-mcp | ★3 | Skip | <20 stars, no substance |

### 机器人/ROS
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| ros-mcp-server | ★1226 | Already in README | — |
| ros2_mcp (wise-vision) | ★77 | Already in README | — |
| nav2_mcp_server | ★73 | Already in README | — |
| unitree-go2-mcp-server | ★78 | Skip | Last push 2025-05-12, >90 days inactive. Stars <100 requires active maintenance. |
| robot_MCP (IliaLarchenko) | ★78 | Skip | Last push 9 months ago, >90 days inactive. |
| RobotArm-MCP-P340 | ★34 | Skip | Last push 2025-07-10, >90 days inactive. |
| ros2-mcp-server (kakimochi) | ★81 | Skip | No description/topics. Cannot verify domain relevance. No active code pushes. |
| ros-mcp | ★32 | Skip | Already covered by ros-mcp-server in README. |
| rf-mcp (manykarim) | ★95 | Skip | Robot Framework = test automation framework, not engineering robotics. |
| unitree-go2-mcp-server | ★78 | Skip | Active topic tags but no code changes in >1 year. |

### 能源/电力/电池
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| PowerMCP | ★139 | Already in README | — |
| EnergyPlus-MCP | ★90 | Already in README | — |
| All "wind" results | various | Skip | "wind" matches Windows tools (windbg, windsurf), not wind energy |
| All "battery" results | various | Skip | "battery" matches "batteries-included" in AI framework descriptions |

## Notable Observations
- Drone-mcp (★25) is aerospace-relevant but inactive since April 2025. Worth re-checking if revived.
- Unitree Go2 MCP server (★78) has strong robotics relevance but no recent code maintenance. 
- "Battery" keyword heavily polluted by "batteries-included" AI framework descriptions.
- "Wind" keyword heavily polluted by Windows ecosystem tools.
- No new agent skills (prompt templates) found for any of the three domains.

## Final Result
**New entries added: 0**
**README modifications: None needed**
