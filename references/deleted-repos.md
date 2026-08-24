# 已删除（404）仓库清单

记录在 discovery 过程中发现已删除/设为 private 的仓库，避免后续复查浪费 API 额度。
规则：从 README 收录条目的 404 需从 README 移除；从未收录的 404 只需记录。

| 仓库 | 最后确认 | 领域 | 备注 |
|------|---------|------|------|
| petropt/petro-mcp | 2026-05-24 | 油藏/石油 | 石油数据 MCP，已删除 |
| williamhoracek/unitree-go2-mcp-server | 2026-05-24 | 机器人 | 宇树 Go2 MCP，已删除 |
| kingtutt/RobotArm-MCP-P340 | 2026-05-24 / 2026-07-31 / 2026-08-02 | 机器人 | 三度确认 404 |
| ATOMI-Ming/FreeCAD-MCP | 2026-05-25 / 2026-07-27 → **08-17 复苏确认存在** | 机械/CAD | 05-25/07-27 记录 404，08-17 Search API 返回 ★97 + Individual Repo API 确认存在（created 2025-08-26, pushed 2026-06-17, archived=False）。因 FreeCAD 生态饱和（README 已有 4 条目）未收录，勿再当 404 |
| faust-machines/mcp-fusion360 | 2026-07-11 | 机械/CAD | Fusion 360 MCP，已删除 |
| adeleempurpled290/FPGA-Agent-skills | 2026-07-29 → **08-12 复苏已收录** | 半导体/FPGA | 07-29 记录 404，08-12 API+browser 双确认存在并收录（Pitfall #29/#57 案例，勿再当 404） |
| bjwanneng/veriflow-cc | 2026-07-29 | 半导体/FPGA | Search API 幽灵候选，404（08-03 已确认存在并收录，勿再当 404） |
| RohanYashRaj/FPGA-Agent-skills | 2026-07-29 / 2026-08-16 | 半导体/FPGA | Search API 幽灵候选，两度确认 404（注意与 adeleempurpled290 复苏的 repo 不同 owner） |
| IO-Aerospace-software-engineering/mcp-server | 2026-08-01 / 2026-08-16 | 航空航天 | 已删除（上游 awesome-mcp-servers 链接失效，多度确认） |
| LNC/robot_MCP（又名 IliaLarchenko/robot_MCP） | 2026-07-31 / 2026-08-02 | 机器人 | 已删除，两拼写均 404 |
| cyrilschumacher/ros2-mcp-server | 2026-07-31 / 2026-08-02 | 机器人 | 已删除 |
| LaplaceYoung/mechanical-mcp | 2026-07-31 / 2026-08-02 | 航空航天 | ANSYS Mechanical gRPC MCP，已删除 |
| LaplaceYoung/hfss-mcp | 2026-07-31 / 2026-08-02 | 航空航天 | HFSS via PyAEDT MCP，已删除 |
| ffffffffelix/automotive-functional-safety | 2026-08-02 / 2026-08-13 / 2026-08-16 / 2026-08-24 | 汽车/自动驾驶 | ISO 26262 功能安全 skill，四度确认 404（08-24 再次 Individual Repo API 确认），从候选池移除 |

备注：2026-07-22 的 Way D（agent skill 搜索）4 个候选全部为 Search API 幽灵（返回名称/star 但仓库不存在）：
brand-docs ★222、FPGA-Agent-skills ★25、veriflow-cc ★36、ccfoundry-agent-kit ★24。agent skill 类仓库生命周期比 MCP server 短，Way D 结果必须用 Individual Repo API 验证存在性（见 Pitfall #29）。
