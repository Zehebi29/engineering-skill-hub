# Daily Discovery — 2026-05-26 (Tuesday)

## Search Domains
- 航空航天/CFD
- 机器人/ROS
- 能源/电力/电池

## Search Queries Run

### 航空航天/CFD (3 queries)
| Query | Results | Stars ≥10 |
|-------|---------|-----------|
| aerospace+MCP+server | 5 | aerospace-mcp ★4, outgassing-mcp ★1 |
| CFD+AI+agent+tool | 1 | (none) |
| aerodynamics+LLM+integration | 0 | — |

### 机器人/ROS (3 queries)
| Query | Results | Stars ≥10 |
|-------|---------|-----------|
| robotics+MCP+server | 10 | ros-mcp-server ★1241, rf-mcp ★95, robot_MCP ★79, unitree-go2-mcp-server ★78, ros2_mcp ★78, nav2_mcp_server ★73, RobotArm-MCP-P340 ★34, ros-mcp ★32 |
| ROS+AI+agent+tool | 8 | RobotecAI/rai ★513 |
| motion+planning+LLM+tool | 2 | AutoTAMP ★75 |

### 能源/电力/电池 (10 additional targeted queries)
| Query | Results | Stars ≥10 |
|-------|---------|-----------|
| power+system+MCP | 10 | (All noise except existing PowerMCP ★145) |
| power+grid+AI+agent | 10 | (none ≥10 relevant) |
| energy+LLM+tools | 10 | PowerMCP ★145 (already in README) |
| solar+energy+MCP+server | 7 | pge-energy-mcp ★1, victron-vrm-mcp ★0 |
| renewable+energy+MCP | 6 | (none ≥10) |
| energy+system+MCP | 10 | PowerMCP ★145 (existing), smartEMS ★6 |
| battery+MCP+server | 10 | All "batteries-included" false positives |
| energy+simulation+MCP | 8 | PowerMCP ★145, EnergyPlus-MCP ★93 (both existing) |
| smart+grid+MCP+server | 0 | — |
| electric+power+MCP | 0 | — |

## Candidates Evaluated

### 航空航天/CFD
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| aerospace-mcp (cheesejaguar) | ★4 | Skip | <20 stars, no substance |
| outgassing-mcp-server | ★1 | Skip | <20 stars |
| factory-os-mcp | ★0 | Skip | <20 stars |
| cfd-ai-agent-optimizer | ★0 | Skip | <20 stars, demo project |

### 机器人/ROS
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| ros-mcp-server | ★1241 | Already in README | — |
| RobotecAI/rai | ★513 | Skip | Framework/library, not MCP server or agent skill. "vendor agnostic agentic framework" |
| rf-mcp (manykarim) | ★95 | Skip | Robot Framework (test automation), not engineering robotics |
| robot_MCP (IliaLarchenko) | ★79 | Skip | Last push 287 days ago. Same candidate evaluated 2026-05-19 — still inactive. |
| unitree-go2-mcp-server (lpigeon) | ★78 | Skip | Last push 379 days ago. Same candidate evaluated 2026-05-19 — still inactive. |
| ros2_mcp (wise-vision) | ★78 | Already in README | — |
| nav2_mcp_server | ★73 | Already in README | — |
| AutoTAMP | ★75 | Skip | Academic research project, not MCP server or reusable agent skill |
| RobotArm-MCP-P340 | ★34 | Skip | Last push 2025-07-10, inactive >6 months. Same as 2026-05-19 eval. |
| ros-mcp (Yutarop) | ★32 | Skip | Already covered by ros-mcp-server in README. |

### 能源/电力/电池
| Repo | Stars | Decision | Reason |
|------|-------|----------|--------|
| PowerMCP | ★145 | Already in README | — |
| EnergyPlus-MCP | ★93 | Already in README | — |
| pge-energy-mcp | ★1 | Skip | <20 stars |
| victron-vrm-mcp | ★0 | Skip | <20 stars |
| energyplus-mcp-server (RainerGaier) | ★0 | Skip | <20 stars |
| idfkit-mcp | ★0 | Skip | <20 stars |
| All "battery" results | various | Skip | "batteries-included" noise |
| All "wind" results | various | Skip | Windows ecosystem noise |

## Notable Observations
- Same pattern as 2026-05-19 (last Tuesday). No new qualifying candidates in any of the three domains.
- The robotics MCP server ecosystem is well-covered (ros-mcp-server ★1241, isaac-sim-mcp ★169, ros2_mcp ★78, nav2_mcp ★73).
- Energy/power domain has the same persistent keyword pollution issues (battery→"batteries-included", wind→Windows ecosystem).
- No new agent skills (prompt templates) found for any domain.
- Existing entries stable: openfoam-mcp-server ★99 (+0 from README), stk-mcp ★33 (+1), PowerMCP ★145 (+2).

## Final Result
**New entries added: 0**
**README modifications: None needed**
