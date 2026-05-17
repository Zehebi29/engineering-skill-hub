# 每日工程 Skill/MCP 发现记录 — 2026-05-17（周日）

## 搜索策略
周日：补漏 — 本周未覆盖的领域搜索 + 上周低星候选复查

### 本周已覆盖的领域
- 周四：油藏/石油/地质, 汽车/自动驾驶, 船舶/海洋工程, 机械/CAD, 电气/PCB, 航空航天/CFD, 机器人
- 周五：工业制造/QA, 生物医学/医疗, 环境/水利/污染
- 周六：综合扫描（awesome-mcp-servers 反向提取）

### 本周未覆盖的领域（本次补漏目标）
- 材料/焊接/检测 (未在已有发现记录中)
- 能源/电力/电池 (未在已有发现记录中)
- 土木/结构/BIM (未在已有发现记录中)
- 化工/流程模拟 (未在已有发现记录中)
- 半导体/VLSI/FPGA (未在已有发现记录中)

## 查询统计
- GitHub API 查询: 24 个（5 个领域 x 3-5 个关键词）
- 候选总数: 127（去重后）
- LLM 判断通过: 3 个
- 新增收录: 3 个（2 个新领域分组）

## 新增条目

### 能源 / 电力 / 电池（新分组）

| MCP Server | 来源 | Star | 判断 |
|---|---|---|---|
| [PowerMCP](https://github.com/Power-Agent/PowerMCP) | [Power-Agent](https://github.com/Power-Agent) | 139 | 电力系统 MCP，≥100★ 自动收录 |
| [EnergyPlus-MCP](https://github.com/LBNL-ETA/EnergyPlus-MCP) | [LBNL-ETA](https://github.com/LBNL-ETA) | 90 | LBNL 官方 EnergyPlus 仿真 MCP，领域高度相关+活跃维护 |

### 半导体 / VLSI / FPGA（新分组）

| MCP Server | 来源 | Star | 判断 |
|---|---|---|---|
| [vivado-mcp](https://github.com/mapleleavessssssss-wq/vivado-mcp) | [mapleleavessssssss-wq](https://github.com/mapleleavessssssss-wq) | 41 | Vivado FPGA 开发 MCP，28 commits，2周前活跃，领域高度相关 |

## 跳过的高星/候选条目

### 材料/焊接/检测
- theNetworkChuck/docker-mcp-tutorial ★1493 — "Materials" 指培训课件材料，非工程材料科学
- tumourlove/monolith ★111 — Unreal Engine MCP 插件，非材料工程
- DmitriyGolub/threejs-devtools-mcp ★60 — Three.js 材质/着色器，非工程材料
- seehiong/blender-mcp-n8n ★37 — Blender 3D 建模 MCP，非工程材料
- aadeshrao123/Unreal-MCP ★28 — Unreal Engine MCP，非工程材料
- CodeGlimmer/welding-design-mcp ★1 — 焊接设计 MCP，Star 过低

### 能源/电力/电池
- jango-blockchained/advanced-homeassistant-mcp ★51 — Home Assistant 智能家居 MCP，非电力工程
- priyankark/phonepi-mcp ★34 — 手机+AI 工具集成，非能源工程
- es617/ble-mcp-server ★11 — BLE 蓝牙 MCP，非电力工程
- emporiaenergy/emporia-mcp ★6 — Emporia 能源 MCP，Star 过低

### 土木/结构/BIM
- mcp-servers-for-revit/revit-mcp-commandset ★53 — **已归档（archived）**，不再维护
- Show2Instruct/ifc-bonsai-mcp ★42 — 最后推送 Jan 2026（>90天），不满足活跃维护要求
- C2SAgent/c2sagent ★265 — AI agent 构建平台，非 BIM/土木专用 MCP
- Sacred-G/Civil3D-mcp ★7 — Star 过低
- antonhofstader/Civil3D-mcp-python-COM ★6 — Star 过低

### 半导体/VLSI/FPGA
- Neverdecel/nevercheese-pcileech-memprocfs-mcp ★6 — DMA 内存 MCP，非 FPGA/VLSI 工程
- catallo/misterclaw ★4 — MiSTer FPGA 远程控制，Star 过低
- jgpeiro/gowin_mcp_server ★1 — Gowin FPGA MCP，Star 过低
- qfliuyang/hipilot ★2 — VLSI 物理设计 Copilot，Star 过低
- seikaikyo/secsgem-mcp-server ★0 — SECS/GEM 半导体设备 MCP，太新

### 化工/流程模拟
- Augmented-Nature/ChEMBL-MCP-Server ★83 — 化学数据库（生物化学/制药），非化工流程模拟
- Augmented-Nature/PubChem-MCP-Server ★36 — PubChem 化学数据，非流程模拟
- PhelanShao/orca-mcp-server ★18 — ORCA 量子化学 MCP，非化工流程
- OntoLedgy/ol_dwsim_interop_services ★2 — DWSIM 流程模拟 MCP，Star 过低
- gsi-lab/APS-Agent ★0 — Aveva 流程模拟 MCP，太新

### 上周低星候选复查（无新增）
- ameyxd/petromcp: 2★（无变化）
- Cyreslab-AI/marinetraffic-mcp-server: 9★（无增长）
- emqx/sdv-mcp-demo: 7★（无增长）
- the-momentum/fhir-mcp-server: 80★（仍 <100，内容被 healthcare-mcp-public 覆盖）
- JamesANZ/medical-mcp: 91★（+2，仍 overlapping）
- OctoEverywhere/mcp: 33★（3D 打印，仍 <100）
- asmith26/jupytercad-mcp: 18★（仍 <20）
- kimimgo/viznoir: 12★（仍 <20）

## README 当前统计
- 原创 Skills: 3
- 社区精选 Skills: 1
- 社区精选 MCP Servers 分组: 12 个（新增 2 个分组：能源/电力/电池, 半导体/VLSI/FPGA）
- 社区精选 MCP Servers 总数: 21（新增 3）

## 领域效果排名
本次补漏搜索显示：
1. ✅ 能源/电力/电池 — MCP 生态有产品（PowerMCP ★139, EnergyPlus ★90），效果好
2. ✅ 半导体/VLSI/FPGA — 有萌芽生态（vivado-mcp ★41, gowin-mcp）
3. ❌ 材料/焊接/检测 — 几乎无真正工程材料科学 MCP，搜索词"materials"被教学材料污染严重
4. ❌ 土木/结构/BIM — Revit MCP 已归档，IFC/BIM MCP 推送不活跃
5. ❌ 化工/流程模拟 — 只有低星萌芽项目（DWSIM 2★, Aveva 0★）

## 搜索模式评估
- `"领域词" "mcp" in:name,description` 仍是最高信噪比的查询模式
- 化工/流程模拟领域的 MCP 生态几乎空白，化学数据库 MCP（ChEMBL, PubChem）虽有高星但不属于"流程模拟"
- 土木/BIM 领域 Revit MCP 生态已有但核心项目已归档，替代者尚未出现
