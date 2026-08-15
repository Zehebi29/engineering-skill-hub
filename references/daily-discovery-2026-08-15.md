# Daily Discovery — 2026-08-15（周六）

**⚠️ Cron 缺口报告**：2026-08-14（周五）无 daily-discovery 文件，git log 最后提交停在 08-13（周四），**周五发现任务静默失败**。已按规范将周五领域（工业制造/QA、生物医学/医疗、环境/水利/污染）并入本次补扫。请用户检查 cron job `f2cc259c3af0` 状态（本周第二次缺口：08-10 周一缺失已由 08-11 补扫；08-04/05 也曾缺失）。

## 搜索领域
- 周六常规：awesome-mcp-servers 综合扫描（反向提取）
- 补扫周五：工业制造/QA、生物医学/医疗、环境/水利/污染

## 执行统计
- awesome-mcp-servers：**3821 行（与 08-08 完全相同，连续第 2 周零增量）**
- 工程 section 候选：153（section 白名单：Aerospace 3 / Art & Culture 64 / Architecture & Design 19 / Biology 38 / Embedded 16 / Environment 5 / Industrial & IoT 1 / Travel 45）
- README 去重后不在表内：141，但 LLM 精筛后全部工程相关候选**均已收录或低于门槛**
- 补扫查询：11（Way B + Way D，含 OPC UA/Modbus/SCADA/agent skill 组合）
- API 验证：18（周六短名单）+ 12（生物 section）+ 补扫全部命中
- Browser 深度验证：5（opentakeoff、biomcp、ChatSpatial、encode-toolkit、edgecore）
- **新增收录：0**

## 关键发现

### 1. 4 个"重新发现"条目实际已在 README（本日最大教训）
本周扫描把以下 4 个候选重新"发现"并 browser 验证，最终确认全部早已收录，**未重复插入**：
| 条目 | Star | 收录时间 |
|------|------|---------|
| Kentucky-ai/opentakeoff | 80（收录时 32） | 07-25（4ad375d，周六扫描） |
| genomoncology/biomcp | 591 | 07-13（1dfbd83，周六综合扫描） |
| cafferychen777/ChatSpatial | 43 | 08-02/09 补漏（ae1ddc4） |
| ammawla/encode-toolkit | 26 | 同上 |

**原因**：① 解析脚本 target_sections 里的 section 名写成了 `Biology, Medicine & Bioinformatics`，而实际 README heading 是 `Biology, Medicine and Bioinformatics`（and 非 &），导致 Biology 38 条从未进入候选池去重，biomcp/ChatSpatial/encode-toolkit 因此漏判；② opentakeoff 去重实际正确（未出现在 not-in-README 列表），但未人工复核 dedup 输出就进入 browser 验证。
**教训**：周六扫描解析全部 section 后必须与 README URL 集合逐一比对；凡准备 browser 验证的候选，先确认其在 not-in-README 列表中的存在。重新发现的已收录条目不得重复插入。

### 2. awesome-mcp-servers 增长停滞
连续第 2 周零增量（08-08 3821 → 08-15 3821）。上游列表已停止增长，周六全量 section 扫描边际收益接近零。建议：后续周六仅做增量行数检查（<10 行增量则跳过全量扫描，直接做候选 API 验证），或降为双周频率。

### 3. 补扫三领域均无新增
工业制造/QA、生物医学/医疗、环境/水利/污染全部 0 合格候选（与 08-13 结论一致，生物医学 MCP 连续多周零新增，环境/水利生态持续空白）。

## 观察对象（低星/类型待复查）
| 仓库 | Star | 领域 | 说明 |
|------|------|------|------|
| anviod/edgecore | 110 | 工业自动化 | 工业边缘网关平台（Go，13 南向协议，MCP 为 AI 特性之一），平台优先非 MCP server（Pitfall #64 v3），跳过；高星平台值得跟踪其 MCP 面是否独立化 |
| nodeblue-ai/ignition-mcp-server | 10 | 工业自动化 | Ignition SCADA MCP，07-24 ★4 → 今 ★10，增长中，最接近门槛的品牌级 SCADA MCP |
| midhunxavier/opcua-mcp | 16 | 工业自动化 | OPC UA MCP，★16 <20，pushed 2026-06-05 |
| Zhonghao1995/Agentic-MIKE-Plus | 7 | 环境/水利 | DHI MIKE+ 水动力模型 agent（Skills+MCP 混合），与已收录 agentic-swmm-workflow 同作者，★7 过低；水动力仿真新方向 |
| cyanheads/usgs-water-mcp-server | 1 | 环境/水利 | USGS 水文数据 MCP（cyanheads 作者，同 pubmed/clinicaltrials 作者），★1 过低 |
| malkreide/swiss-environment-mcp | 1 | 环境/水利 | 瑞士环境数据 MCP（NABEL 空气质量/水文/BAFU），★1 过低 |
| zackpeters93/ugs-mcp | 5 | 机械/CAD/CAM | CNC Universal GCode Sender MCP，★5 过低 |
| vessel-api/vesselapi-mcp | 1 | 船舶/海洋工程 | VesselAPI 船舶数据 MCP，★1 过低 |
| viventine-space/orbit-sentinel-mcp | 1 | 航空航天 | 航天监管申报（FCC/ITU/UNOOSA/FAA-AST）MCP，★1 过低 |
| cobanov/teslamate-mcp | 133 | 汽车/自动驾驶 | TeslaMate 车辆遥测 MCP，★133 但消费级（车主数据查询），非工程服务，跳过（上游也归入 Travel） |

## 跳过（重点候选及原因）
- anviod/edgecore ★110 — 工业边缘网关平台，MCP 只是 AI 特性（无独立 MCP adapter 包），平台优先跳过（Pitfall #64 v3，与 rosclaw ★178 同类）
- yaoisai/serialrun ★35 — SerialRUN 模式噪音（串口调试工具附带 Modbus/PLC），07-17 已记录过滤规则
- biotender-max/awesome-bio-agent-skills ★146 — awesome list 类型，非 skill 集合（07-24 已记录）
- ai-evos/agent-skills ★24 — 物流/制造/零售/能源四领域泛化 + pushed 2026-02-25 不活跃
- boheling/skillbench ★44 — 通用 agent skill 基准测试框架，非工程领域专用
- the-momentum/fhir-mcp-server ★97 — 与 wso2/fhir-mcp-server（已收录 ★130）功能重叠 + 不活跃（2025-10）
- OctoEverywhere/mcp ★35 — 3D 打印远程监控，pushed 2025-07-03 不活跃 + 与 mcp-3D-printer-server 重叠
- asmith26/jupytercad-mcp ★20 — JupyterCAD MCP，pushed 2025-10 不活跃
- PatrickPalmer/MayaMCP ★96 — Autodesk Maya（DCC 工具非工程 CAD）+ pushed 2025-05 不活跃
- IO-Aerospace-software-engineering/mcp-server — **404**（awesome-mcp-servers 链接失效，条目名称与 URL 不一致，上游列表问题，无需处理）

## 查询效果观察
- awesome-mcp-servers 连续 2 周零增量，周六扫描进入边际收益接近零状态，建议降频。
- 生物医学/医疗：biomcp（★591）已于 07-13 收录，该表已覆盖多源数据访问，Way B 连续多周零新增。
- 工业自动化：品牌级 PLC/SCADA MCP 全部 <20★（ignition-mcp-server ★10 最接近），继续观察。
- 环境/水利：Agentic-MIKE-Plus（MIKE+）与 agentic-swmm-workflow 形成"水文模型 agent 化"细分方向，虽 ★<20 但值得每月复查。

## README 统计
- 社区精选 Skills：42 条（今日 0 新增）
- 社区精选 MCP Servers：102 条（今日 0 新增）
