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

| Skill                                                     | 描述                                                   | 来源                                          | Star |
| --------------------------------------------------------- | ------------------------------------------------------ | --------------------------------------------- | ---- |
| [text-to-cad](https://github.com/earthtojake/text-to-cad) | Agent skills 合集：CAD、机器人、硬件设计的自然语言驱动 | [earthtojake](https://github.com/earthtojake) | 2754 |

### 社区精选 MCP Servers

工程领域的 MCP server，为 AI agent 提供工程工具能力。按领域分组，组内按 Star 排序。

#### 机械 / CAD / CAM

| MCP Server                                                                   | 描述                                            | 来源                                            | Star |
| ---------------------------------------------------------------------------- | ----------------------------------------------- | ----------------------------------------------- | ---- |
| [freecad-mcp](https://github.com/neka-nat/freecad-mcp)                       | FreeCAD MCP server：AI 驱动参数化 CAD 建模      | [neka-nat](https://github.com/neka-nat)         | 942  |
| [CAD-MCP](https://github.com/daobataotie/CAD-MCP)                            | CAD MCP server：AI 驱动 CAD 绘图操作            | [daobataotie](https://github.com/daobataotie)   | 334  |
| [freecad-ai](https://github.com/ghbalf/freecad-ai)                           | FreeCAD AI 工作台：自然语言生成 3D 模型         | [ghbalf](https://github.com/ghbalf)             | 219  |
| [freecad_mcp](https://github.com/bonninr/freecad_mcp)                        | FreeCAD MCP：连接 Claude/Cursor，参数化设计     | [bonninr](https://github.com/bonninr)           | 182  |
| [Easy-MCP-AutoCad](https://github.com/zh19980811/Easy-MCP-AutoCad)           | AutoCAD MCP server：自然语言操控 AutoCAD        | [zh19980811](https://github.com/zh19980811)     | 159  |
| [jarvis-onshape-mcp](https://github.com/ReshefElisha/jarvis-onshape-mcp)     | Onshape MCP server：Claude Code 驱动云 CAD 建模 | [ReshefElisha](https://github.com/ReshefElisha) | 114  |
| [Fusion-360-MCP-Server](https://github.com/AuraFriday/Fusion-360-MCP-Server) | Fusion 360 MCP server：AI 控制 Fusion 360       | [AuraFriday](https://github.com/AuraFriday)     | 94   |

#### 电气 / PCB / EDA

| MCP Server                                                   | 描述                                                 | 来源                                          | Star |
| ------------------------------------------------------------ | ---------------------------------------------------- | --------------------------------------------- | ---- |
| [kicad-mcp](https://github.com/lamaalrajih/kicad-mcp)        | KiCad MCP server：跨平台 PCB 设计自然语言交互        | [lamaalrajih](https://github.com/lamaalrajih) | 451  |
| [kicad-mcp-pro](https://github.com/oaslananka/kicad-mcp-pro) | KiCad MCP server：PCB 和原理图自动化，DFM/SI/PI 辅助 | [oaslananka](https://github.com/oaslananka)   | 125  |
| [MCP4EDA](https://github.com/NellyW8/MCP4EDA)                | EDA MCP server：LLM 驱动 EDA 工具链（论文配套）      | [NellyW8](https://github.com/NellyW8)         | 88   |

#### 机器人

| MCP Server                                                     | 描述                                            | 来源                                          | Star |
| -------------------------------------------------------------- | ----------------------------------------------- | --------------------------------------------- | ---- |
| [ros-mcp-server](https://github.com/robotmcp/ros-mcp-server)   | ROS MCP server：连接 LLM 与机器人，支持 ROS 1/2 | [robotmcp](https://github.com/robotmcp)       | 1220 |
| [ros2_mcp](https://github.com/wise-vision/ros2_mcp)            | ROS 2 MCP server：AI agent 直连机器人系统       | [wise-vision](https://github.com/wise-vision) | 77   |
| [nav2_mcp_server](https://github.com/ajtudela/nav2_mcp_server) | ROS 2 Nav2 MCP server：AI 控制导航栈            | [ajtudela](https://github.com/ajtudela)       | 73   |

#### 航空航天 / CFD

| MCP Server                                                            | 描述                                           | 来源                                  | Star |
| --------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------- | ---- |
| [openfoam-mcp-server](https://github.com/webworn/openfoam-mcp-server) | OpenFOAM MCP server：LLM 驱动 CFD 流体仿真教学 | [webworn](https://github.com/webworn) | 95   |
| [stk-mcp](https://github.com/alti3/stk-mcp)                           | Ansys STK MCP server：数字任务工程仿真         | [alti3](https://github.com/alti3)     | 28   |

#### 能源 / 电力 / 电池

| MCP Server                                                              | 描述                                                          | 来源                                              | Star |
| ----------------------------------------------------------------------- | ------------------------------------------------------------- | ------------------------------------------------- | ---- |
| [PowerMCP](https://github.com/Power-Agent/PowerMCP)                     | 电力系统 MCP 服务器集合：PowerWorld、PSSE、OpenDSS 等仿真工具 | [Power-Agent](https://github.com/Power-Agent)     | 139  |
| [EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP)           | EnergyPlus 建筑能耗模拟 MCP，LBNL 官方项目                    | [LBNL-ETA](https://github.com/LBNL-ETA)           | 90   |

#### 油藏 / 石油

| MCP Server                                                            | 描述                                 | 来源                                              | Star |
| --------------------------------------------------------------------- | ------------------------------------ | ------------------------------------------------- | ---- |
| [pyrestoolbox-mcp](https://github.com/gabrielserrao/pyrestoolbox-mcp) | 油藏工程 MCP server：AI 驱动油藏计算 | [gabrielserrao](https://github.com/gabrielserrao) | 41   |

#### 工业自动化

| MCP Server                                             | 描述                                                            | 来源                                    | Star |
| ------------------------------------------------------ | --------------------------------------------------------------- | --------------------------------------- | ---- |
| [thingsboard-mcp](https://github.com/thingsboard/thingsboard-mcp) | ThingsBoard MCP server：连接工业 IoT 平台，设备管理、遥测数据查询 | [thingsboard](https://github.com/thingsboard) | 97   |
| [opcua-mcp](https://github.com/kukapay/opcua-mcp)      | OPC UA MCP server：连接工业自动化系统，实时监控和控制运行数据   | [kukapay](https://github.com/kukapay)   | 26   |
| [modbus-mcp](https://github.com/kukapay/modbus-mcp)    | Modbus MCP server：标准化工业 Modbus 数据，供 AI agent 调用     | [kukapay](https://github.com/kukapay)   | 23   |
| [twincat-mcp](https://github.com/eponce00/twincat-mcp) | TwinCAT MCP server：连接 Beckhoff PLC，构建/部署/监控自动化项目 | [eponce00](https://github.com/eponce00) | 20   |

#### 嵌入式 / 硬件

| MCP Server                                                                           | 描述                                                                 | 来源                                                  | Star |
| ------------------------------------------------------------------------------------ | -------------------------------------------------------------------- | ----------------------------------------------------- | ---- |
| [esp-mcp](https://github.com/horw/esp-mcp)                                           | ESP32 开发 MCP server：集中管理 ESP-IDF 命令，简化嵌入式开发入门     | [horw](https://github.com/horw)                       | 148  |
| [embedded-debugger-mcp](https://github.com/Adancurusul/embedded-debugger-mcp)        | 嵌入式调试 MCP server：支持 ARM Cortex-M、RISC-V 的 probe-rs 调试    | [Adancurusul](https://github.com/Adancurusul)         | 85   |

#### 半导体 / VLSI / FPGA

| MCP Server                                                                            | 描述                                                    | 来源                                                        | Star |
| ------------------------------------------------------------------------------------- | ------------------------------------------------------- | ----------------------------------------------------------- | ---- |
| [vivado-mcp](https://github.com/mapleleavessssssss-wq/vivado-mcp)                     | Vivado MCP Server：AI 驱动 FPGA 开发，CRITICAL WARNING 诊断 | [mapleleavessssssss-wq](https://github.com/mapleleavessssssss-wq) | 41   |

#### 生物医学 / 医疗

| MCP Server                                                                  | 描述                                                                        | 来源                                        | Star |
| --------------------------------------------------------------------------- | --------------------------------------------------------------------------- | ------------------------------------------- | ---- |
| [biomcp](https://github.com/genomoncology/biomcp)                           | BioMCP：单查询多源生物医学数据搜索（PubMed、临床试验、变异信息、本地分析）  | [genomoncology](https://github.com/genomoncology) | 507  |
| [mcp-simple-pubmed](https://github.com/andybrandt/mcp-simple-pubmed)        | PubMed MCP server：搜索和查询医学文献数据库                                 | [andybrandt](https://github.com/andybrandt) | 165  |
| [healthcare-mcp-public](https://github.com/Cicatriiz/healthcare-mcp-public) | Healthcare MCP server：访问 FDA、PubMed、临床试验、ICD-10、DICOM 等医疗数据 | [Cicatriiz](https://github.com/Cicatriiz)   | 115  |

#### 环境 / 水利

| MCP Server                                                | 描述                                                                     | 来源                                          | Star |
| --------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------- | ---- |
| [autocad-mcp](https://github.com/puran-water/autocad-mcp) | AutoCAD MCP server：面向水处理工程的 P&ID 图纸自动化，支持 AutoLISP 执行 | [puran-water](https://github.com/puran-water) | 249  |

#### 综合资源

| MCP Server                                                  | 描述                                             | 来源                                  | Star |
| ----------------------------------------------------------- | ------------------------------------------------ | ------------------------------------- | ---- |
| [awesome-ai-cae](https://github.com/kimimgo/awesome-ai-cae) | 113 个 AI-ready CAE 工具精选：CFD、FEA、SPH、DEM | [kimimgo](https://github.com/kimimgo) | 26   |

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
