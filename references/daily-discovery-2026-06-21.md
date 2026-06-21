# Daily Discovery — 2026-06-21 (周日)

## 搜索类型
补漏 — 本周未覆盖领域检查 + 低星候选复查 + 补充搜索

## 本周覆盖状态
所有 15 个领域本周均已覆盖（周一至周六均有 daily-discovery 记录），无缺失领域。

## 低星候选复查

### 复查清单（上周 Star < 20 但有增长潜力，类型正确，领域相关，未归档）

| 仓库 | 上次 Star | 本周 Star | 判断 |
|------|----------|----------|------|
| pzfreo/build123d-mcp | 18 | 18 | 无增长，活跃但 Star 仍不达标 |
| asmith26/jupytercad-mcp | 19 | 19 | 无增长，且不活跃（pushed 2025-10-07） |
| kimimgo/viznoir | 15 | 15 | 无增长，VTK 通用可视化工具 |
| publu/RoboRun | 14 | 14 | 无增长，ROS 管理 MCP |
| midhunxavier/OPCUA-MCP | 15 | 15 | 无增长，OPC UA 工业自动化 |
| CliDyn/copernicus-mcp | 11 | 11 | 无增长，Copernicus 气候数据 |

### 因其他原因跳过的候选（不复查）
- catallo/misterclaw (★5) — MiSTer FPGA MCP，Star 过低
- zackpeters93/ugs-mcp (★1) — CNC MCP，Star 过低
- RocketPy-Team/Infinity-API (★9) — RocketPy MCP，Star 过低
- petropt/petro-mcp (★1) — 石油工程 MCP，Star 过低
- ojaogezi/opm-mcp (★0) — 油藏仿真 MCP，Star 过低
- andresjbf/tnavigator-mcp (★2) — tNavigator MCP，Star 过低

## 补充搜索

### 查询及结果

对 20 个精确查询进行 GitHub API 搜索，筛选 Star ≥ 20、活跃（90 天内有更新）、未收录的候选。

#### 新增收录

| 仓库 | Star | 领域 | 原因 |
|------|------|------|------|
| [mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server) | 195 | 机械/CAD/CAM | 3D 打印 MCP server，支持 OctoPrint/Klipper/Bambu/Prusa/Creality/Duet/Repetier 7+ 打印机品牌，含 STL 操作+切片+可视化，195★ 达标 |
| [agentcad](https://github.com/jdilla1277/agentcad) | 48 | 机械/CAD/CAM | CAD CLI + MCP server，支持 build123d/CadQuery，STEP 导出+STL/GLB 网格+几何度量+浏览器预览，20 commits/14 branches/4 tags，非常活跃 |
| [Kiln](https://github.com/codeofaxel/Kiln) | 22 | 机械/CAD/CAM | 3D 打印全流程 MCP server：AI 驱动设计→切片→打印，支持 Bambu/Prusa/Creality/Klipper/Elegoo 等 15+ 品牌，1491 commits，非常活跃 |
| [LabVIEW-MCP-Server-Toolkit](https://github.com/JanGoebel/LabVIEW-MCP-Server-Toolkit) | 32 | 综合资源 | LabVIEW MCP server 工具包，从 LabVIEW VI 直接托管 MCP server，NI 测试测量集成 |
| [COMSOL-Multiphysics-MCP](https://github.com/Suzy-Sa/COMSOL-Multiphysics-MCP) | 28 | 综合资源 | COMSOL 多物理场 MCP server，建模工作流自动化+验证+RAG 辅助仿真 |

#### 跳过（领域相关但不收录）

| 仓库 | Star | 原因 |
|------|------|------|
| manykarim/rf-mcp | 103 | Robot Framework（测试自动化框架）MCP，非物理机器人（Pitfall #38） |
| ATOI-Ming/FreeCAD-MCP | 87 | FreeCAD MCP，功能与已有 4 个 FreeCAD 条目重叠 |
| DMontgomery40/bambu-printer-mcp | 59 | Bambu Lab 专属 MCP，被 mcp-3D-printer-server（★195）覆盖 |
| Haohao-end/mcp-agent | 82 | 通用 MCP 框架，非工程专用 |
| ReyemTech/mcp-canada | 51 | 加拿大政府数据 MCP，非工程领域 |
| connerlambden/bgpt-mcp | 32 | 通用学术论文搜索 API，非工程专用 |
| biocontext-ai/registry | 21 | MCP 注册表，非 MCP server 实现 |

## 统计
- README 当前：12 Skills + 73 MCP Servers（含本次新增 5 条）
- 复查候选：6 个（0 个达标，6 个未达标）
- 补充搜索：20 个查询，5 个新发现收录
- 低星观察列表：build123d-mcp(★18)、jupytercad-mcp(★19)、viznoir(★15)、RoboRun(★14)、OPCUA-MCP(★15)、copernicus-mcp(★11)
