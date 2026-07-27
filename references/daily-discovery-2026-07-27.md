# 每日发现记录 — 2026-07-27（周一）

## 领域
- 机械/CAD/CAM
- 电气/PCB/EDA
- 材料/焊接/检测

## 搜索概况
- 查询数: 34（14 机械/CAD/CAM + 11 电气/PCB/EDA + 9 材料/焊接/检测）
- 候选总数: 242（搜索 API 初筛）
- API 验证: 74 个非重复候选
- 新增收录: 1

## 新增

### MCP Servers 表 — 机械 / CAD / CAM

| MCP Server | 描述 | 来源 | Star |
|-----------|------|------|------|
| [cad-cae-copilot](https://github.com/armpro24-blip/cad-cae-copilot) | CAD/CAE Copilot：AI-native CAD/CAE/CAX 工作台 + MCP server，文本→build123d/OpenCASCADE 几何→STEP/STL→CAE 全流程 | [armpro24-blip](https://github.com/armpro24-blip) | 42 |

### 收录理由
- ★42（超过 ★20 阈值）
- 830 commits, 31 branches, pushed 2 周前（极活跃）
- AI-native CAD/CAE/CAX 工作台，含 MCP server 表面（.mcp.json 配置、MCP Setup 文档）
- 与现有 agentcad（★79, build123d/CadQuery CLI + MCP）互补：agentcad 侧重建模 CLI，cad-cae-copilot 侧重 CAD→CAE 全流程（拓扑优化、FEA 设置、确定性批评）
- 含独立 aieng-agent-skills 技能目录，覆盖工程技能
- 已在 2026-07-06 技能笔记中记录（当时 ★36），持续增长至 ★42（+6/3 周）
- Topics: 20 个工程标签（build123d, opencascade, cad, cae, calculix, generative-design, topology-optimization 等）

## 跳过候选

### 机械/CAD/CAM
| Repo | Stars | 原因 |
|------|-------|------|
| ATOMI-Ming/FreeCAD-MCP | 404 | 此前已标记为 404（2026-05），仍不存在 |
| camoufox-reverse-mcp | ★346 | CAM 关键词噪音（反检测浏览器），非工程 |
| camofox-browser | ★306 | CAM 关键词噪音（反检测浏览器），非工程 |
| camofox-mcp | ★84 | CAM 关键词噪音（反检测浏览器），非工程 |
| hedless/onshape-mcp | ★117 | 不活跃（pushed 2026-03-04，>90天无更新） |
| rawwerks/VibeCAD | ★98 | 不活跃（pushed 2026-01-05） |
| bambu-printer-mcp (DMontgomery40) | ★77 | 同作者 mcp-3D-printer-server（★207）已覆盖 Bambu 打印——Pitfall #51 |
| alisamsam/Solidworks-MCP | ★70 | 较少提交（2 commits），功能被现有 SolidWorks MCP 覆盖 |
| armpro24-blip/cad-cae-copilot | ★42 | **已收录** |
| earthtojake/cad-skill | ★40 | 已归档（archived） |
| AJ-Chen0810/FreeCAD-MCP | — | (重复验证) |
| veoery/GH_mcp_server | ★31 | 不活跃（pushed 2025-10-05） |
| arthurle3210/swapi-pilot-solidworks-mcp | ★27 | SolidWorks API 文档搜索 MCP，功能极窄，SolidWorks 已有 3 个条目 |
| rzeldent/esp32-cam-ai | ★26 | ESP32-CAM 嵌入式摄像头，非 CAD/CAM |
| Ajhcs/cameo-mcp-bridge | ★29 | Cameo Systems Modeler/SysML，属系统建模非 CAD/CAM |

### 电气/PCB/EDA
| Repo | Stars | 原因 |
|------|-------|------|
| electerm | ★14468 | EDA 关键词噪音（终端/SSH 客户端），非工程 |
| spiceflow | ★164 | "spice" 关键词噪音（React API 框架），非 SPICE 仿真 |
| Finerestaurant/kicad-mcp-python | ★40 | 不活跃（pushed 2025-07-15），KiCad 已有多个条目 |
| circuit-synth/kicad-sch-api | ★48 | 不活跃（pushed 2025-12-05） |
| embedded-society/altium-designer-mcp | ★30 | ★30 略高于阈值但功能极窄（Altium 元件库管理），Altium 已有 3 个 MCP 实现 |
| Arcadia-1/awesome-ams-skills | ★28 | Awesome list（非 SKILL.md 集合），同作者 veriloga-skills（★26）已在 Skills 表 |
| IntelligentElectron/universal-netlist | ★25 | Cadence/Altium 网表阅读器，功能极窄 |
| erebusnz/rigol-mcp | ★21 | Rigol 示波器 MCP，极端小众但活跃——标记候补 |
| oaslananka/easyeda-mcp-pro | ★22 | 低星，EasyEDA 已有 2 个条目 |
| zxkmm/kicad-footprint-generate | ★27 | KiCad 焊盘生成工具，非 MCP server |
| circuit-synth/mcp-kicad-sch-api | ★20 | 低星 + 不活跃（pushed 2025-08-20） |

### 材料/焊接/检测（全部跳过 — 无工程候选）
| Repo | Stars | 原因 |
|------|-------|------|
| godot-devtool | ★88 | Godot 游戏引擎，非材料科学 |
| metro-mcp | ★63 | React Native 调试，非工程 |
| drain_mcp | ★54 | Log 模板挖掘，非材料 |
| NDepend.MCP.Server | ★41 | .NET 代码分析，非工程 |
| mcp-server-zotero-dev | ★36 | Zotero 插件开发，非工程 |
| roslyn-codelens-mcp | ★29 | .NET 代码分析，非工程 |
| skills (patsnap) | ★25 | 通用 AI 技能，非材料/焊接专用 |
| windows-computer-use-mcp | ★22 | 桌面自动化，非工程 |
| materials-simulation-skills | ★58 | 已在 Skills 表 |

## 备注
- 材料/焊接/检测领域连续 8 周无任何合格 MCP server 或 agent skill 候选（之前已建议降为月度检查）
- 机械/CAD/CAM 领域新增 cad-cae-copilot 作为平台型 MCP 项目，补充了 CAD→CAE 全流程缺口
- 电气/PCB/EDA 领域本周无新增——现有条目已覆盖全面，新候选多为低星/不活跃
- 材料/焊接/检测领域 skill 搜索（"materials science" agent skill）仅返回已收录的 materials-simulation-skills（★58）和 general academic skills（非工程专用）

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 76（无变化）
- 社区精选 MCP Servers: 185+（+1）

## 后续关注
- **erebusnz/rigol-mcp** ★21 — Rigol 示波器 MCP，活跃，电气工程细分方向，如达 ★30 可收录（电气/PCB/EDA）
- **embedded-society/altium-designer-mcp** ★30 — Rust 实现 Altium MCP，极活跃（875 commits），如达 ★40 可收录
- **armpro24-blip/cad-cae-copilot** ★42 — 已收录，继续关注增长
- The-OpenROAD-Project/OpenROAD-MCP ★12 — 增长至 ★12，下次复查优先
