# Engineering Skill Hub — 每日发现记录
日期: 2026-05-14 (周四)
搜索策略: v2 — 领域轮换搜索

## 今日搜索领域
周四轮换: 油藏/石油/地质 + 汽车/自动驾驶 + 船舶/海洋工程
额外跨域搜索: 机械/CAD, 电气/PCB, 航空航天/CFD, 机器人

## 搜索统计
- GitHub API 查询: 24 个（12 个成功，12 个被 403 限流）
- 策略: 每个领域关键词 + "MCP" 组合，in:name,description,readme
- 唯一仓库数: 139（去重后）
- MCP 相关仓库: 128
- LLM 判断通过: 19 个
- 最终收录: 9 个

## 新增收录

| 仓库 | Stars | 领域 | 描述 |
|------|------:|------|------|
| robotmcp/ros-mcp-server | 1219 | 机器人 | ROS 1/2 MCP，LLM-机器人双向通信 |
| lamaalrajih/kicad-mcp | 448 | 电气/PCB | KiCad 跨平台 PCB MCP |
| daobataotie/CAD-MCP | 333 | 机械/CAD | CAD 绘图 MCP |
| zh19980811/Easy-MCP-AutoCad | 158 | 机械/CAD | AutoCAD 自然语言 MCP |
| cobanov/teslamate-mcp | 127 | 汽车 | 跳过 — 个人用车追踪，非工程 |
| ReshefElisha/jarvis-onshape-mcp | 114 | 机械/CAD | Onshape 云 CAD MCP |
| webworn/openfoam-mcp-server | 94 | 航空航天/CFD | OpenFOAM CFD MCP |
| NellyW8/MCP4EDA | 87 | 电气/PCB | EDA 工具链 MCP（论文配套） |
| wise-vision/ros2_mcp | 77 | 机器人 | ROS 2 MCP |
| ajtudela/nav2_mcp_server | 73 | 机器人 | ROS 2 Nav2 导航 MCP |

## 跳过的高星候选

| 仓库 | Stars | 原因 |
|------|------:|------|
| 0x4m4/hexstrike-ai | 8719 | 通用 MCP server，碰巧匹配 "autonomous" |
| doobidoo/mcp-memory-service | 1835 | 通用记忆服务，非工程 |
| ascending-llc/jarvis-registry | 802 | 通用 MCP 注册表 |
| agentic-community/mcp-gateway-registry | 647 | 通用 MCP 网关 |

## 低星候选（待复查）

油藏/石油领域极小众，暂无 >10 star 的项目：
- ameyxd/petromcp (2★) — 石油数据格式 MCP
- petropt/petro-mcp (1★) — 石油工程数据 MCP
- QuentinCody/eia-mcp-server (0★) — EIA 能源数据 MCP

汽车/自动驾驶：
- emqx/sdv-mcp-demo (7★) — 软件定义汽车 demo
- Ansvar-Systems/Automotive-MCP (1★) — 汽车网络安全标准

船舶/海洋：
- Cyreslab-AI/marinetraffic-mcp-server (9★) — 船舶 AIS 追踪
- robderstadt/datalastic-mcp (1★) — 海洋 AIS 数据
- dorian-erkens/mcp-shom-wrecks (1★) — 法国海洋测绘数据
- contextkits/naval-shipbuilding-standards (0★) — 军舰建造标准

## 策略评估

v2 策略效果显著：
- v1（笼统关键词）: 每天找到 0-2 个新工程 MCP，大量不相关结果
- v2（领域轮换）: 今天一次找到 9 个新工程 MCP，相关性高

关键改进：
1. 用 `"领域词" "mcp" in:name,description` 比泛搜精准得多
2. 机器人领域（ROS）是工程 MCP 最成熟的方向，值得重点跟踪
3. 油藏/石油、船舶/海洋极小众，但有萌芽项目（petromcp 等）
4. GitHub API 限流是主要瓶颈 — 未认证 60 次/小时，需要加 token 认证

## Git 提交
- 5aaeddc: feat: add 9 engineering MCP servers (domain-driven search v2)
