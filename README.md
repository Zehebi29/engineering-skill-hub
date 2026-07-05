<p align="center">
  <img src="docs/logo.svg" alt="Engineering Skill Hub" width="600">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Engineering-Skills-3b82f6?style=flat-square&labelColor=1e293b" alt="Engineering">
  <img src="https://img.shields.io/badge/AI_Agent-Skills-22c55e?style=flat-square&labelColor=1e293b" alt="AI Agent">
  <img src="https://img.shields.io/badge/License-MIT-3b82f6?style=flat-square&labelColor=1e293b" alt="MIT License">
  <img src="https://img.shields.io/badge/Compatible-Hermes%20%7C%20OpenClaw-a855f7?style=flat-square&labelColor=1e293b" alt="Compatible">
</p>

<p align="center">
  工程领域的 AI Agent 技能库<br>
  面向工程师和研究人员的可复用技能集合
</p>

<p align="center">
  每个 skill 都是独立的 <code>SKILL.md</code> 文件<br>
  兼容 <a href="https://github.com/nousresearch/hermes-agent">Hermes Agent</a> 和 <a href="https://github.com/openclaw/openclaw">OpenClaw</a>
</p>

---

## Skills

### 原创 Skills

| Skill                                                                | 描述                                                                     | 标签                                      | 兼容              |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------ | ----------------------------------------- | ----------------- |
| [engineering-lit-review](skills/engineering-lit-review/SKILL.md)     | 工程领域文献综述自动化：多数据库检索、三级去重、BibTeX 输出              | `research` `literature-review` `academic` | Hermes / OpenClaw |
| [engineering-paper-digest](skills/engineering-paper-digest/SKILL.md) | 工程论文速读：URL/DOI/标题 -> 结构化中文摘要（方法、结果、局限性）       | `research` `paper-reading` `digest`       | Hermes / OpenClaw |
| [patent-landscape](skills/patent-landscape/SKILL.md)                 | 工程领域专利态势分析：技术趋势、主要申请人、技术分类、代表性专利、空白点 | `research` `patent` `innovation`          | Hermes / OpenClaw |

### 社区精选 Skills

来自社区的高质量工程相关 agent skill（prompt 模板）。

| Skill                                                                                                                          | 描述                                                                                 | 来源                                                                | Star |
| ------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ | ------------------------------------------------------------------- | ---- |
| [kicad-happy](https://github.com/aklofas/kicad-happy)                                                                          | AI 编码 agent 技能集：KiCad 原理图分析、PCB 审查、电路设计自动化                     | [aklofas](https://github.com/aklofas)                               | 630  |
| [NextBoard](https://github.com/LeoKemp223/NextBoard)                                                                           | 硬件 PCB 方案设计的 AI Agent：需求确认、器件选型、BOM 输出、原理图生成               | [LeoKemp223](https://github.com/LeoKemp223)                         | 264  |
| [text-to-cad](https://github.com/earthtojake/text-to-cad)                                                                      | Agent skills 合集：CAD、机器人、硬件设计的自然语言驱动                               | [earthtojake](https://github.com/earthtojake)                       | 7125 |
| [geoscience-skills](https://github.com/SteadfastAsArt/geoscience-skills)                                                       | 30 个 AI-powered 地学技能集合：地震、测井、3D 建模、反演、地统计学、空间回归、NetCDF | [SteadfastAsArt](https://github.com/SteadfastAsArt)                 | 31   |
| [DDC-Skills-for-AI-Agents-in-Construction](https://github.com/datadrivenconstruction/DDC_Skills_for_AI_Agents_in_Construction) | 221 个建筑行业 AI 技能：BIM 分析、成本估算、进度管理、文档控制、自动化工作流         | [datadrivenconstruction](https://github.com/datadrivenconstruction) | 207  |
| [verilog-generator](https://github.com/Eriemon/verilog-generator)                                                               | 代理技能：Verilog-2001 RTL 生成和 FPGA 设计工作流，含接口模板、验证门控、CLI 运行时   | [Eriemon](https://github.com/Eriemon)                               | 185  |
| [night_owl_research_agent](https://github.com/GRIND-Lab-Core/night_owl_research_agent)                                         | NORA：地学/遥感/GIS 全自动 AI 研究 Agent，含 GeoBenchmark、期刊模板、MCP server      | [GRIND-Lab-Core](https://github.com/GRIND-Lab-Core)                 | 92   |

### 社区精选 MCP Servers

工程领域的 MCP server，为 AI agent 提供工程工具能力。按领域分组，组内按 Star 排序。

#### 机械 / CAD / CAM

| MCP Server                                                                                   | 描述                                                                                             | 来源                                                | Star  |
| -------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | --------------------------------------------------- | ----- |
| [blender-mcp](https://github.com/ahujasid/blender-mcp)                                       | Blender MCP server：AI 驱动 3D 建模、渲染、动画，支持场景操作和脚本化                            | [ahujasid](https://github.com/ahujasid)             | 23265 |
| [freecad-mcp](https://github.com/neka-nat/freecad-mcp)                                       | FreeCAD MCP server：AI 驱动参数化 CAD 建模                                                       | [neka-nat](https://github.com/neka-nat)             | 1194  |
| [CAD-MCP](https://github.com/daobataotie/CAD-MCP)                                            | CAD MCP server：AI 驱动 CAD 绘图操作                                                             | [daobataotie](https://github.com/daobataotie)       | 423   |
| [freecad-ai](https://github.com/ghbalf/freecad-ai)                                           | FreeCAD AI 工作台：自然语言生成 3D 模型                                                          | [ghbalf](https://github.com/ghbalf)                 | 348   |
| [mcp-3D-printer-server](https://github.com/DMontgomery40/mcp-3D-printer-server)              | 3D 打印 MCP server：OctoPrint/Klipper/Bambu/Prusa/Creality 多品牌打印机控制+STL 操作+切片        | [DMontgomery40](https://github.com/DMontgomery40)   | 197   |
| [freecad_mcp](https://github.com/bonninr/freecad_mcp)                                        | FreeCAD MCP：连接 Claude/Cursor，参数化设计                                                      | [bonninr](https://github.com/bonninr)               | 200   |
| [Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)                           | AutoCAD MCP server：自然语言操控 AutoCAD                                                         | [zh19980811](https://github.com/zh19980811)         | 203   |
| [SolidworksMCP-TS](https://github.com/vespo92/SolidworksMCP-TS)                              | SolidWorks MCP：TypeScript 实现，COM 互操参数化建模                                              | [vespo92](https://github.com/vespo92)               | 192   |
| [jarvis-onshape-mcp](https://github.com/ReshefElisha/jarvis-onshape-mcp)                     | Onshape MCP server：Claude Code 驱动云 CAD 建模                                                  | [ReshefElisha](https://github.com/ReshefElisha)     | 136   |
| [OpenSCAD-MCP-Server](https://github.com/jhacksman/OpenSCAD-MCP-Server)                      | OpenSCAD MCP server：文本/图像生成多视图 3D 模型，CUDA 重建+参数化导出                           | [jhacksman](https://github.com/jhacksman)           | 162   |
| [Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server)                 | Fusion 360 MCP server：AI 控制 Fusion 360                                                        | [AuraFriday](https://github.com/AuraFriday)         | 105   |
| [openscad-mcp](https://github.com/quellant/openscad-mcp)                                     | OpenSCAD MCP server：AI 驱动 3D 建模渲染，FastMCP 实现，300+ 测试                                | [quellant](https://github.com/quellant)             | 108   |
| [freecad-addon-robust-mcp-server](https://github.com/spkane/freecad-addon-robust-mcp-server) | FreeCAD Robust MCP server：企业级 CAD 自动化，47 项工具+资源                                     | [spkane](https://github.com/spkane)                 | 131   |
| [agentcad](https://github.com/jdilla1277/agentcad)                                           | CAD CLI + MCP server：build123d/CadQuery 脚本执行、STEP 导出、STL/GLB 网格、几何度量、浏览器预览 | [jdilla1277](https://github.com/jdilla1277)         | 54    |
| [multiCAD-mcp](https://github.com/AnCode666/multiCAD-mcp)                                    | Multi-CAD MCP server：统一接口操控 AutoCAD、ZWCAD、BricsCAD、GstarCAD                            | [AnCode666](https://github.com/AnCode666)           | 49    |
| [fusion360-mcp-server](https://github.com/faust-machines/fusion360-mcp-server)               | Fusion 360 MCP server：84 工具覆盖草图、特征、CAM、钣金，PyPI 部署                               | [faust-machines](https://github.com/faust-machines) | 47    |
| [SolidworksMCP-python](https://github.com/andrewbartels1/SolidworksMCP-python)               | SolidWorks MCP server：Python 实现，COM 互操参数化建模，CI/测试完备                              | [andrewbartels1](https://github.com/andrewbartels1) | 30    |
| [build123d-mcp](https://github.com/pzfreo/build123d-mcp)                                     | build123d MCP server：AI 驱动参数化 CAD，360+ 提交/60 版本，STEP/STL/GLB 导入导出和几何度量      | [pzfreo](https://github.com/pzfreo)                 | 25    |
| [Kiln](https://github.com/codeofaxel/Kiln)                                                   | 3D 打印 MCP server：AI 驱动设计→切片→打印全流程，Bambu/Prusa/Creality/Klipper/Elegoo 15+ 品牌    | [codeofaxel](https://github.com/codeofaxel)         | 24    |

#### 电气 / PCB / EDA

| MCP Server                                                           | 描述                                                                                       | 来源                                              | Star |
| -------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ | ------------------------------------------------- | ---- |
| [KiCAD-MCP-Server](https://github.com/mixelpixx/KiCAD-MCP-Server)    | KiCAD MCP server：122 项工具，16 类 PCB 自动化（原理图、布局、DFM、Gerber）                | [mixelpixx](https://github.com/mixelpixx)         | 1379 |
| [kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)                | KiCad MCP server：跨平台 PCB 设计自然语言交互                                              | [lamaalrajih](https://github.com/lamaalrajih)     | 478  |
| [kicad-mcp-pro](https://github.com/oaslananka/kicad-mcp-pro)         | KiCad MCP server：PCB 和原理图自动化，DFM/SI/PI 辅助                                       | [oaslananka](https://github.com/oaslananka)       | 125  |
| [circuitron](https://github.com/Shaurya-Sethi/circuitron)            | Agentic PCB Design Accelerator：多智能体系统，自然语言生成网表→布局→KiCad 输出，含 MCP RAG | [Shaurya-Sethi](https://github.com/Shaurya-Sethi) | 106  |
| [MCP4EDA](https://github.com/NellyW8/MCP4EDA)                        | EDA MCP server：LLM 驱动 EDA 工具链（论文配套）                                            | [NellyW8](https://github.com/NellyW8)             | 91   |
| [altium-mcp](https://github.com/coffeenmusic/altium-mcp)             | Altium Designer MCP server：原理图、PCB、库管理自然语言操控                                | [coffeenmusic](https://github.com/coffeenmusic)   | 102  |
| [pcbparts-mcp](https://github.com/Averyy/pcbparts-mcp)               | 电子元器件搜索 MCP server：JLCPCB/Mouser/DigiKey 1.5M+ 器件库                              | [Averyy](https://github.com/Averyy)               | 69   |
| [jlcmcp](https://github.com/hyl64/jlcmcp)                            | 嘉立创 EDA MCP server：39 个 PCB 自动化工具，直接操控 JLC EDA                              | [hyl64](https://github.com/hyl64)                 | 130  |
| [kicad-mcp-server](https://github.com/Seeed-Studio/kicad-mcp-server) | KiCad MCP server（Seeed Studio）：KiCad 9.0+ 原理图/PCB 分析、网表追踪、DRC/ERC            | [Seeed-Studio](https://github.com/Seeed-Studio)   | 53   |
| [JLCEDA-MCP](https://github.com/sengbin/JLCEDA-MCP)                  | 嘉立创 EDA MCP：VS Code 插件+WebSocket 桥，原理图读写审查                                  | [sengbin](https://github.com/sengbin)             | 49   |
| [ansys-aedt-mcp](https://github.com/LaplaceYoung/ansys-aedt-mcp)     | Ansys AEDT MCP server：HFSS/Maxwell/Q3D/Icepak/Circuit 电磁仿真自动化，PyAEDT + 原生 API   | [LaplaceYoung](https://github.com/LaplaceYoung)   | 18   |
| [altium-designer-mcp](https://github.com/embedded-society/altium-designer-mcp) | Altium Designer MCP server（Rust）：AI 辅助元器件库管理，728 提交，持续活跃              | [embedded-society](https://github.com/embedded-society) | 23   |
| [eda-agent](https://github.com/salitronic/eda-agent)                 | Altium Designer MCP server：200+ 工具覆盖原理图、PCB、库管理，持久化 DelphiScript 桥接     | [salitronic](https://github.com/salitronic)       | 68   |
| [easyeda-copilot](https://github.com/biosshot/easyeda-copilot)       | EasyEDA Pro AI 助手 MCP：自然语言生成原理图、LCSC 器件搜索、SPICE 仿真                     | [biosshot](https://github.com/biosshot)           | 66   |
| [spicebridge](https://github.com/clanker-lover/spicebridge)          | NGspice 电路仿真 MCP server：AI 直连 ngspice，设计/仿真/验证电路                           | [clanker-lover](https://github.com/clanker-lover) | 23   |
| [ltspice-mcp](https://github.com/Cognitohazard/ltspice-mcp)          | LTspice/NGspice 电路仿真 MCP server：AI 驱动电路设计、仿真、蒙特卡洛分析、波形测量         | [Cognitohazard](https://github.com/Cognitohazard) | 16   |

#### 机器人

| MCP Server                                                                  | 描述                                                                               | 来源                                          | Star |
| --------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | --------------------------------------------- | ---- |
| [stack-chan](https://github.com/stack-chan/stack-chan)                      | Stack-chan MCP server：M5Stack 嵌入式机器人，JavaScript 驱动，MCP 自然语言控制     | [stack-chan](https://github.com/stack-chan)   | 1560 |
| [ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)                | ROS MCP server：连接 LLM 与机器人，支持 ROS 1/2                                    | [robotmcp](https://github.com/robotmcp)       | 1323 |
| [isaac-sim-mcp](https://github.com/omni-mcp/isaac-sim-mcp)                  | NVIDIA Isaac Sim MCP server：AI 驱动机器人仿真，自然语言控制 Isaac Sim/Lab/OpenUSD | [omni-mcp](https://github.com/omni-mcp)       | 179  |
| [agenticros](https://github.com/agenticros/agenticros)                       | ROS 2 机器人 AI agent 集成平台：MCP server + OpenClaw/Claude/Gemini 多平台适配，自然语言控制机器人感知、推理、动作 | [agenticros](https://github.com/agenticros)   | 106  |
| [ros2_mcp](https://github.com/wise-vision/ros2_mcp)                         | ROS 2 MCP server：AI agent 直连机器人系统                                          | [wise-vision](https://github.com/wise-vision) | 81   |
| [unitree-go2-mcp-server](https://github.com/lpigeon/unitree-go2-mcp-server) | Unitree Go2 四足机器人 MCP server，基于 ROS 2 控制运动/传感器                      | [lpigeon](https://github.com/lpigeon)         | 82   |
| [nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server)              | ROS 2 Nav2 MCP server：AI 控制导航栈                                               | [ajtudela](https://github.com/ajtudela)       | 81   |
| [robotmem](https://github.com/robotmem/robotmem)                            | Robot Memory：AI 机器人持久记忆系统，MCP Server + 混合搜索 + 空间检索，支持 ROS 2  | [robotmem](https://github.com/robotmem)       | 25   |

#### 航空航天 / CFD

| MCP Server                                                            | 描述                                           | 来源                                  | Star |
| --------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------- | ---- |
| [openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server) | OpenFOAM MCP server：LLM 驱动 CFD 流体仿真教学 | [webworn](https://github.com/webworn) | 106  |
| [stk-mcp](https://github.com/alti3/stk-mcp)                           | Ansys STK MCP server：数字任务工程仿真         | [alti3](https://github.com/alti3)     | 39   |

#### 土木 / 结构 / BIM

| MCP Server                                                                                          | 描述                                                                                          | 来源                                                              | Star |
| --------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- |
| [ifc-lite](https://github.com/LTplus-AG/ifc-lite)                                                   | IFC/AEC 工具包：解析、查询、编辑、导出 IFC/IDS/BCF/点云，含 MCP server 和 WebGPU 3D 查看器    | [LTplus-AG](https://github.com/LTplus-AG)                         | 256  |
| [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit)             | Revit MCP server（TypeScript）：26+ 工具，AI 驱动 Revit 建模自动化，支持 Revit 2020-2026      | [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit) | 222  |
| [mcp-server-for-revit-python](https://github.com/mcp-servers-for-revit/mcp-server-for-revit-python) | Revit MCP server（Python/pyRevit）：pyRevit Routes REST API 桥接 Revit 与 AI agent，18 个工具 | [mcp-servers-for-revit](https://github.com/mcp-servers-for-revit) | 138  |
| [cordyceps](https://github.com/brookstalley/cordyceps)                                                                          | Grasshopper MCP Bridge：Claude 控制 Rhino/Grasshopper 参数化设计画布和渲染工具               | [brookstalley](https://github.com/brookstalley)                   | 80   |
| [ifc-bonsai-mcp](https://github.com/Show2Instruct/ifc-bonsai-mcp)                                                              | IFC BIM MCP server：50+ 工具，连接 AI 与 Blender Bonsai 插件，自然语言创建/编辑 IFC 元素      | [Show2Instruct](https://github.com/Show2Instruct)                 | 52   |
| [RevitMCP](https://github.com/oakplank/RevitMCP)                                                                               | Revit MCP server（pyRevit）：模型查询、视图控制、元素操作，pyRevit Routes 桥接                | [oakplank](https://github.com/oakplank)                           | 48   |
| [tekla_mcp_server](https://github.com/teknovizier/tekla_mcp_server)                                 | Tekla Structures MCP server：工具化建模自动化，支持选择、组件插入、属性管理、视图操作         | [teknovizier](https://github.com/teknovizier)                     | 38   |
| [Autodesk-Revit-MCP-Server](https://github.com/Sam-AEC/Autodesk-Revit-MCP-Server)                   | Revit MCP server（C#/.NET）：100+ 工具覆盖几何、视图、族、MEP、结构，支持 Revit 2024-2026     | [Sam-AEC](https://github.com/Sam-AEC)                             | 38   |
| [RevitMCPBridge2026](https://github.com/WeberG619/RevitMCPBridge2026)                               | Revit MCP bridge（C#）：705+ MCP 端点，AI 全读写 Revit，BIM Ops Studio 开源项目               | [WeberG619](https://github.com/WeberG619)                         | 22   |

#### 能源 / 电力 / 电池

| MCP Server                                                   | 描述                                                          | 来源                                          | Star |
| ------------------------------------------------------------ | ------------------------------------------------------------- | --------------------------------------------- | ---- |
| [PowerMCP](https://github.com/Power-Agent/PowerMCP)          | 电力系统 MCP 服务器集合：PowerWorld、PSSE、OpenDSS 等仿真工具 | [Power-Agent](https://github.com/Power-Agent) | 171  |
| [EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | EnergyPlus 建筑能耗模拟 MCP，LBNL 官方项目                    | [LBNL-ETA](https://github.com/LBNL-ETA)       | 99   |

#### 油藏 / 石油

| MCP Server                                                            | 描述                                 | 来源                                              | Star |
| --------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------- | ---- |
| [pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp) | 油藏工程 MCP server：AI 驱动油藏计算 | [gabrielserrao](https://github.com/gabrielserrao) | 43   |

#### 工业自动化

| MCP Server                                                        | 描述                                                              | 来源                                          | Star |
| ----------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------- | ---- |
| [thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) | ThingsBoard MCP server：连接工业 IoT 平台，设备管理、遥测数据查询 | [thingsboard](https://github.com/thingsboard) | 98   |
| [opcua-mcp](https://github.com/kukapay/opcua-mcp)                 | OPC UA MCP server：连接工业自动化系统，实时监控和控制运行数据     | [kukapay](https://github.com/kukapay)         | 27   |
| [modbus-mcp](https://github.com/kukapay/modbus-mcp)               | Modbus MCP server：标准化工业 Modbus 数据，供 AI agent 调用       | [kukapay](https://github.com/kukapay)         | 25   |
| [twincat-mcp](https://github.com/eponce00/twincat-mcp)            | TwinCAT MCP server：连接 Beckhoff PLC，构建/部署/监控自动化项目   | [eponce00](https://github.com/eponce00)       | 21   |

#### 嵌入式 / 硬件

| MCP Server                                                                    | 描述                                                              | 来源                                          | Star |
| ----------------------------------------------------------------------------- | ----------------------------------------------------------------- | --------------------------------------------- | ---- |
| [esp-mcp](https://github.com/horw/esp-mcp)                                    | ESP32 开发 MCP server：集中管理 ESP-IDF 命令，简化嵌入式开发入门  | [horw](https://github.com/horw)               | 151  |
| [embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp) | 嵌入式调试 MCP server：支持 ARM Cortex-M、RISC-V 的 probe-rs 调试 | [Adancurusul](https://github.com/Adancurusul) | 115  |

#### 半导体 / VLSI / FPGA

| MCP Server                                                        | 描述                                                                               | 来源                                                              | Star |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ---- |
| [vivado-mcp](https://github.com/mapleleavessssssss-wq/vivado-mcp) | Vivado MCP Server：AI 驱动 FPGA 开发，CRITICAL WARNING 诊断                        | [mapleleavessssssss-wq](https://github.com/mapleleavessssssss-wq) | 62   |
| [SynthPilot](https://github.com/LNC0831/SynthPilot)               | Vivado MCP server：500+ 工具覆盖全流程 FPGA 开发，含 oh-my-fpga 方法论层，本地运行 | [LNC0831](https://github.com/LNC0831)                             | 47   |

#### 生物医学 / 医疗

| MCP Server                                                                                | 描述                                                                                            | 来源                                                | Star |
| ----------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---- |
| [biomcp](https://github.com/genomoncology/biomcp)                                         | BioMCP：单查询多源生物医学数据搜索（PubMed、临床试验、变异信息、本地分析）                      | [genomoncology](https://github.com/genomoncology)   | 532  |
| [mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)                      | PubMed MCP server：搜索和查询医学文献数据库                                                     | [andybrandt](https://github.com/andybrandt)         | 167  |
| [fhir-mcp-server](https://github.com/wso2/fhir-mcp-server)                                | FHIR MCP server：将任意 FHIR Server/API 暴露为 MCP server，WSO2 官方项目                        | [wso2](https://github.com/wso2)                     | 124  |
| [healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public)               | Healthcare MCP server：访问 FDA、PubMed、临床试验、ICD-10、DICOM 等医疗数据                     | [Cicatriiz](https://github.com/Cicatriiz)           | 117  |
| [pubmed-mcp-server](https://github.com/cyanheads/pubmed-mcp-server)                       | PubMed/Europe PMC MCP server：文献搜索、全文获取、引用分析、MeSH 术语，STDIO/HTTP               | [cyanheads](https://github.com/cyanheads)           | 116  |
| [medical-mcp](https://github.com/JamesANZ/medical-mcp)                                    | Medical MCP server：FDA/WHO/PubMed/RxNorm/Google Scholar 多源医疗数据聚合，本地运行零配置       | [JamesANZ](https://github.com/JamesANZ)             | 100  |
| [dicom-mcp](https://github.com/ChristianHinge/dicom-mcp)                                  | DICOM MCP server：连接 PACS 等 DICOM 服务器，查询/读取/移动医学影像和报告                       | [ChristianHinge](https://github.com/ChristianHinge) | 98   |
| [clinicaltrialsgov-mcp-server](https://github.com/cyanheads/clinicaltrialsgov-mcp-server) | ClinicalTrials.gov MCP server：577K 试验搜索、高级字段过滤、患者匹配、研究详情详解              | [cyanheads](https://github.com/cyanheads)           | 81   |
| [m3](https://github.com/rafiattrach/m3)                                                   | MIMIC-IV 医疗数据 MCP server：自然语言查询重症监护数据库（DuckDB/BigQuery）                     | [rafiattrach](https://github.com/rafiattrach)       | 72   |
| [pyomop](https://github.com/dermatologist/pyomop)                                         | OMOP CDM 数据管理 Python 包：SQLite/PostgreSQL/MySQL 支持，含 MCP server 和 LLM 集成            | [dermatologist](https://github.com/dermatologist)   | 64   |
| [ChatSpatial](https://github.com/cafferychen777/ChatSpatial)                              | 空间转录组学 MCP server：自然语言驱动的空间分析（Scanpy/Squidpy），含 bioRxiv 论文              | [cafferychen777](https://github.com/cafferychen777) | 40   |
| [encode-toolkit](https://github.com/ammawla/encode-toolkit)                               | ENCODE 基因组学 MCP server：搜索、下载、分析功能基因组实验数据                                  | [ammawla](https://github.com/ammawla)               | 35   |
| [openevidence-mcp](https://github.com/bakhtiersizhaev/openevidence-mcp)                     | OpenEvidence MCP：开源浏览器会话 MCP server，连接 OpenEvidence 医学证据平台，支持问诊、文章检索           | [bakhtiersizhaev](https://github.com/bakhtiersizhaev) | 28   |
| [omop_mcp](https://github.com/OHNLP/omop_mcp)                                             | OMOP 临床术语映射 MCP server：用 LLM 将临床术语映射到 OMOP CDM 概念，OHDSI 生态                 | [OHNLP](https://github.com/OHNLP)                   | 36   |
| [medical-mcps](https://github.com/pascalwhoop/medical-mcps)                               | 生物医学 MCP server：100+ 工具，集成 Reactome/KEGG/UniProt/ChEMBL/PubMed/OpenFDA 等 14 个数据库 | [pascalwhoop](https://github.com/pascalwhoop)       | 21   |

#### 环境 / 水利

| MCP Server                                                        | 描述                                                                                           | 来源                                              | Star |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---- |
| [autocad-mcp](https://github.com/puran-water/autocad-mcp)         | AutoCAD MCP server：面向水处理工程的 P&ID 图纸自动化，支持 AutoLISP 执行                       | [puran-water](https://github.com/puran-water)     | 364  |
| [weather-mcp-server](https://github.com/ezh0v/weather-mcp-server) | 轻量级天气数据 MCP server：AI 助手实时获取和解读天气数据，Go 实现，SSE 传输                    | [ezh0v](https://github.com/ezh0v)                 | 247  |
| [foehn](https://github.com/kayhendriksen/foehn)                   | MeteoSwiss 气象数据 MCP server：20+ 数据集（站点、雷达、冰雹、预报、气候），Python API/CLI/MCP | [kayhendriksen](https://github.com/kayhendriksen) | 41   |

#### 综合资源

| MCP Server                                                                            | 描述                                                                                     | 来源                                      | Star |
| ------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ----------------------------------------- | ---- |
| [us-gov-open-data-mcp](https://github.com/lzinga/us-gov-open-data-mcp)                | 美国政府开放数据 MCP server：40+ API、250+ 工具（FDA、CDC、EPA、NWS、Treasury、FRED 等） | [lzinga](https://github.com/lzinga)       | 103  |
| [awesome-ai-cae](https://github.com/kimimgo/awesome-ai-cae)                           | 113 个 AI-ready CAE 工具精选：CFD、FEA、SPH、DEM                                         | [kimimgo](https://github.com/kimimgo)     | 36   |
| [cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot)                   | CAD/CAE 智能体工作台：AI 原生 build123d 参数化建模+网格划分+仿真求解，含 MCP server，827 提交 | [armpro24-blip](https://github.com/armpro24-blip) | 36   |
| [LabVIEW-MCP-Server-Toolkit](https://github.com/JanGoebel/LabVIEW-MCP-Server-Toolkit) | LabVIEW MCP server 工具包：从 LabVIEW VI 直接托管 MCP server，NI 测试测量集成            | [JanGoebel](https://github.com/JanGoebel) | 34   |
| [COMSOL-Multiphysics-MCP](https://github.com/Suzy-Sa/COMSOL-Multiphysics-MCP)         | COMSOL 多物理场 MCP server：建模工作流自动化、验证、RAG 辅助仿真                         | [Suzy-Sa](https://github.com/Suzy-Sa)     | 30   |
| [data360-mcp](https://github.com/worldbank/data360-mcp)                                     | World Bank Data360 MCP server：搜索、验证、获取发展指标（GDP、贫困、性别平等、气候等）不含幻觉 | [worldbank](https://github.com/worldbank)            | 28   |

> 自动更新：每天 09:00 扫描 GitHub，发现新的高星工程 agent skill 自动添加到上表。

持续更新中。欢迎 [贡献新 skill](CONTRIBUTING.md)。

## 快速使用

### Hermes Agent

```bash
git clone git@github.com:Zehebi29/engineering-skill-hub.git
cp -r engineering-skill-hub/skills/engineering-lit-review ~/.hermes/skills/
```

### OpenClaw

```bash
git clone git@github.com:Zehebi29/engineering-skill-hub.git
cp -r engineering-skill-hub/skills/engineering-lit-review ~/.openclaw/.agents/skills/

# 或用软链接（推荐，方便更新）
ln -s $(pwd)/engineering-skill-hub/skills/engineering-lit-review ~/.openclaw/.agents/skills/
```

### 通用方式

每个 skill 的 `SKILL.md` 是一个自包含的 prompt 模板：

- 直接复制内容到任何支持 system prompt 的 LLM 对话中
- 用作 Claude / ChatGPT / Cursor 的自定义指令
- 集成到你自己的 agent 框架

## Skill 文件格式

每个 skill 使用标准 YAML frontmatter，兼容 Hermes 和 OpenClaw：

```yaml
---
name: "skill-name"
description: "一行描述"
author: "作者名"
tags: [tag1, tag2]
version: "1.0"
license: MIT
compatible_with: [hermes, openclaw]
metadata:
  hermes:
    tags: [research, literature-review]
  openclaw:
    requires:
      bins: [curl, python3]
---
```

详见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## 兼容平台

| 平台                                                         | 状态        | Skill 路径          |
| ------------------------------------------------------------ | ----------- | ------------------- |
| [Hermes Agent](https://github.com/nousresearch/hermes-agent) | 完全兼容    | `~/.hermes/skills/` |
| [OpenClaw](https://github.com/openclaw/openclaw)             | 完全兼容    | `.agents/skills/`   |
| Claude / ChatGPT / Cursor                                    | 通用 prompt | 直接复制使用        |

## License

MIT License — 自由使用、修改和分发。
