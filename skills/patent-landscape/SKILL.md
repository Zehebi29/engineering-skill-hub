---
name: "patent-landscape"
description: "工程领域专利态势分析框架：提供搜索策略、分析维度和报告模板。输入技术方向关键词，引导用户完成趋势分析、主要申请人排名、技术分类、代表性专利筛选和技术空白点识别。需用户配合在本地浏览器搜索专利数据。"
author: "Zehebi29"
tags: [research, patent, engineering, landscape, ip, innovation]
version: "1.0.0"
license: MIT
compatible_with: [hermes, openclaw]
metadata:
  hermes:
    tags: [research, patent, engineering, innovation]
    related_skills: [engineering-lit-review, engineering-paper-digest, web]
  openclaw:
    requires:
      bins: [curl]
---

# 工程领域专利态势分析 (Patent Landscape)

输入一个技术方向关键词，输出结构化专利态势报告。覆盖趋势分析、主要玩家、技术分类、代表性专利和空白点识别。

## When to Use

- 用户说"帮我查一下XX方向的专利情况"、"XX技术的专利布局"
- 用户想了解某个技术领域的专利竞争格局
- 用户需要找某个方向的代表性专利
- 用户想知道某个领域还有哪些技术空白可以申请

## When NOT to Use

- 只需要查某一篇特定专利的信息（直接搜索即可）
- 需要法律层面的专利侵权分析（需要专业律师）
- 需要专利估值（需要专业评估）

---

## 交互式提问流程

**在开始分析前，先确认以下问题：**

### 必问项（4个）

1. **技术方向** — 具体的关键词或技术描述（如"机器人焊接质量检测"）
2. **地域范围** — 全球 / 中国 / 美国 / 欧洲 / 日本 / 其他
3. **时间范围** — 默认近5年，用户可指定
4. **分析深度**：
   - 快速概览（10-20篇专利，简要分析）
   - 标准分析（50-100篇，含趋势图表描述）← 默认
   - 深度分析（100+篇，含技术空白点和竞争格局）

### 可选项

5. 是否有特定关注的公司/申请人
6. 是否需要关注特定 IPC/CPC 分类号
7. 是否只看已授权专利还是包括申请中专利

### 提问模板

```
好的，我来帮你做专利态势分析。先确认几个问题：

1. 技术方向关键词是什么？
2. 地域范围：全球 / 中国 / 美国 / 欧洲？
3. 时间范围：默认近5年，有特殊要求吗？
4. 深度：A) 快速概览  B) 标准分析  C) 深度分析
```

---

## 数据源与检索策略

### 数据源优先级

| 数据源 | 访问方式 | 覆盖 | 优先级 |
|--------|---------|------|--------|
| **Google Patents** | web_search | 全球最全 | ★★★ 主力 |
| **EPO OPS** | REST API (需免费注册) | 全球100+国家 | ★★★ 补充 |
| **USPTO PatentsView** | REST API (无需key) | 美国专利 | ★★☆ 美国专利用 |
| **WIPO PATENTSCOPE** | web_search | PCT国际申请 | ★★☆ 补充 |
| **Lens.org** | web_search | 学术+专利混合 | ★★☆ 补充 |

### Google Patents 检索（主力，无需 API）

```bash
# 基本搜索
web_search("site:patents.google.com 关键词")

# 限定时间范围
web_search("site:patents.google.com 关键词 after:2021 before:2026")

# 限定地域
web_search("site:patents.google.com 关键词 country:CN")

# 限定申请人
web_search("site:patents.google.com 关键词 assignee:公司名")
```

**Google Patents URL 参数：**
- `q=keyword` — 搜索关键词
- `after=priority:YYYYMMDD` — 起始日期
- `before=priority:YYYYMMDD` — 截止日期
- `country=CN` — 国家
- `language=ENGLISH` — 语言
- `type=PATENT` — 只看授权专利

### EPO OPS 检索（补充，需免费注册）

```bash
# 获取访问令牌
curl -X POST "https://ops.epo.org/auth/v1/token" \
  -H "Authorization: Basic BASE64(key:secret)" \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials"

# 搜索专利（CQL 语法）
curl -X GET "https://ops.epo.org/3.2/rest-services/published-data/search?q=ta=keyword&Range=1-25" \
  -H "Authorization: Bearer YOUR_ACCESS_TOKEN"

# CQL 搜索语法
# ta=标题关键词
# ab=摘要关键词
# pa=申请人
# cl=IPC分类号
# pd=公开年份
# 组合：ta=machine learning AND pa=Google AND pd=2024
```

### USPTO PatentsView（美国专利）

```bash
curl -X POST "https://api.patentsview.org/patents/query" \
  -H "Content-Type: application/json" \
  -d '{
    "q": {"_contains": {"patent_title": "keyword"}},
    "f": ["patent_number", "patent_title", "patent_date", "patent_abstract", "assignee_organization"],
    "o": {"per_page": 25},
    "s": [{"patent_date": "desc"}]
  }'
```

---

## 分析框架

### 1. 专利申请趋势

统计各年份的专利申请/公开数量，识别：
- 上升期：技术正在快速发展
- 平台期：技术趋于成熟
- 下降期：技术可能被替代

### 2. 主要申请人排名

按专利数量排序，识别：
- 头部玩家（前10名）
- 企业 vs 高校 vs 研究机构的分布
- 中国 vs 外国申请人的比例

### 3. 技术分类分布

按 IPC/CPC 代码统计，了解：
- 主要技术分支
- 交叉领域（技术融合点）
- 新兴分类（最近才出现的分支）

### 4. 代表性专利筛选

选出 5-10 篇代表性专利，标准：
- 高被引专利
- 近期重要专利
- 来自头部申请人的专利
- 覆盖不同技术分支

### 5. 技术空白点识别

分析专利覆盖不到的区域：
- 关键词组合搜索结果为零的方向
- 主要玩家未布局的细分领域
- 近年新出现但专利还少的方向

---

## 输出格式

```markdown
# [技术方向] 专利态势分析报告

分析时间：YYYY-MM-DD | 地域：全球 | 时间范围：2021-2026

## 一、专利申请趋势

近5年专利公开数量：
- 2021: N 件
- 2022: N 件
- 2023: N 件
- 2024: N 件
- 2025: N 件（截至X月）

趋势判断：[上升/平台/下降]，主要原因：...

## 二、主要申请人

| 排名 | 申请人 | 专利数 | 类型 | 代表专利 |
|:----:|--------|:------:|------|---------|
| 1 | 公司A | 45 | 企业 | US1234567 |
| 2 | 大学B | 32 | 高校 | CN12345678 |
| ... | ... | ... | ... | ... |

## 三、技术分类分布

| IPC 代码 | 含义 | 专利数 | 占比 |
|----------|------|:------:|:----:|
| G06N | 计算装置 | 56 | 28% |
| B23K | 焊接 | 34 | 17% |
| ... | ... | ... | ... |

## 四、代表性专利

### 1. [专利号] — 专利标题
- **申请人**: 公司名 | **公开日**: YYYY-MM-DD
- **摘要**: 一句话概括
- **核心权利要求**: 关键技术特征
- **链接**: https://patents.google.com/patent/专利号

### 2. ...
（共5-10篇）

## 五、技术空白点

基于现有专利分析，以下方向专利布局较少：

1. **[空白方向1]** — 简要说明为什么有潜力
2. **[空白方向2]** — 简要说明

## 六、结论与建议

1-2 句话总结整体态势，给出行动建议。
```

---

## 已知问题

### Google Patents 无 API 且限流严格

Google Patents 没有官方 API，只能通过 xhr endpoint 搜索。**从服务器端连续请求 5-6 次后会被 Google 完全封锁**（返回 "Sorry..." 页面），需要等待较长时间才能恢复。

**应对策略**：
- 单次分析最多搜 3-4 个关键词，避免触发限流
- 如果被限流，切换到 EPO OPS（需免费注册）
- 最佳方案：在用户本地浏览器中通过 web_search 搜索，避免服务器 IP 被封

### 所有专利 API 都有反爬限制

从服务器 IP（云服务器）批量访问以下服务都会被 Cloudflare/Google 拦截：
- Google Patents (xhr endpoint) — 5-6次后封IP
- Lens.org — Cloudflare 验证
- WIPO PATENTSCOPE — 403 Forbidden
- Espacenet — 需要浏览器 JS 渲染
- USPTO PatentsView — 已迁移到新平台，API 不稳定

**根本原因**：专利数据库对云服务器 IP 的反爬比学术数据库严格得多。

**建议**：
1. 优先用 EPO OPS（有正式 API，免费注册，有 rate limit 但不会封 IP）
2. 单次分析控制搜索次数（3-5个关键词组合）
3. 如果需要大量数据，建议用户在本地浏览器中搜索后导出

### IPC 分类需要专业知识

IPC/CPC 分类号体系复杂，建议结合关键词搜索而非仅依赖分类号。

### 语言障碍

中国专利摘要可能是中文，需要翻译处理。
