# 工程 MCP/Skill 发现记录 — 2026-06-13（周六）

## 搜索类型
周六综合扫描 — awesome-mcp-servers 反向提取

## 执行概况
- awesome-mcp-servers 版本：3046 行（~2552 个 bullet list 条目）
- 关键词初筛命中：426 条（含大量 false positive）
- 严格过滤后候选：39 条
- API 验证后通过：2 条
- 新增收录：2 条

## 新增收录

| 仓库 | Star | 领域 | 描述 |
|------|------|------|------|
| ChristianHinge/dicom-mcp | 96 | 生物医学/医疗 | DICOM MCP server：连接 PACS 等 DICOM 服务器，查询/读取/移动医学影像和报告 |
| OHNLP/omop_mcp | 35 | 生物医学/医疗 | OMOP 临床术语映射 MCP server：用 LLM 将临床术语映射到 OMOP CDM 概念 |

## 跳过的候选

### Star 不达标（<20）
- asmith26/jupytercad-mcp ★19 — JupyterCAD MCP（CAD in Jupyter），不活跃（pushed 2025-10-07）
- pzfreo/build123d-mcp ★13 — build123d parametric CAD MCP，活跃但星低
- NyxToolsDev/dicom-hl7-mcp-server ★3 — DICOM+HL7+FHIR bridge，太新
- musharna/plant-genomics-mcp ★0 — 植物基因组学 MCP
- vitorpavinato/ncbi-mcp-server ★10 — NCBI/PubMed MCP，不活跃
- wise-vision/mcp_server_ros_2 ★0 — ROS2 MCP
- yusong652/yade-mcp ★9 — YADE DEM MCP（已在上周收录 pfc-mcp ★59 覆盖该领域）
- aliafsahnoudeh/wildfire-mcp-server ★0 — 野火监测 MCP
- jagan-shanmugam/climatiq-mcp-server ★8 — 碳排放计算 MCP

### 不活跃（>90天无代码更新）
- OctoEverywhere/mcp ★34 — 3D 打印 MCP，pushed 2025-07-03（近1年未更新）
- the-momentum/fhir-mcp-server ★86 — FHIR MCP，pushed 2025-10-23（8个月未更新）
- Yutarop/ros-mcp ★34 — ROS2 MCP，pushed 2025-08-19（10个月未更新）

### False positive（关键词误匹配）
- askbudi/roundtable — "ndt" 匹配 "unified"，非无损检测
- AliKarami/MikroMCP — "ros" 匹配 RouterOS，非机器人 ROS
- ezyang/codemcp — "asic" 匹配 "basic"，非芯片设计
- saurav61091/mcp-openapi — "asic" 匹配 "basic"，非芯片设计
- ndthanhdev/mcp-browser-kit — "ndt" 匹配 "browser" 子串
- awwaiid/mcp-server-taskwarrior — "asic" 匹配 "basic"
- giskard09/argentum-core — "ros" 匹配 "across" 子串
- 大量 weather MCP — 通用天气 API wrapper，非工程级气象数据

## 观察
- 生物医学领域继续是最活跃的工程 MCP 生态，本次又新增 2 个条目
- DICOM 方向出现专门化的 MCP server（之前只有 healthcare-mcp-public 作为综合型覆盖 DICOM）
- OMOP CDM 方向是新细分——面向临床数据标准化，不同于 PubMed/临床试验等文献方向
- 机械/CAD/CAM 方向的候选（jupytercad-mcp、build123d-mcp、OctoEverywhere）均因 Star 或活跃度不达标被跳过
- ROS2 方向的候选（wise-vision、Yutarop）均因 Star 过低被跳过，现有 ros-mcp-server（★1254）仍为主力
- awesome-mcp-servers 规模从上次扫描（~2800 行）增长到 3046 行，增速放缓
