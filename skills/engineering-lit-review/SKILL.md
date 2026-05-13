---
name: "engineering-lit-review"
description: "工程领域文献综述自动化：多数据库检索（Semantic Scholar、IEEE、PubMed）、三级去重、主题综合、BibTeX 输出。适用于制造业、材料、焊接、机器人、结构检测等工程方向。"
author: "Zehebi29"
tags: [research, literature-review, engineering, academic, bibtex, semantic-scholar, ieee]
version: "3.0.0"
license: MIT
compatible_with: [hermes, openclaw]
metadata:
  hermes:
    tags: [research, literature-review, engineering, academic]
    related_skills: [arxiv, ocr-and-documents, web]
  openclaw:
    requires:
      bins: [curl, python3]
---

# 工程领域文献综述 (Engineering Literature Review)

针对**工程领域**的系统性文献调研，覆盖制造业、材料科学、焊接、机器人、结构检测等方向。支持中英文输出，涵盖多数据库检索、主题综合、引用验证。

## When to Use

- 用户要求做"文献调研"、"文献综述"、"系统性综述"
- 研究方向属于工程领域（制造、材料、焊接、检测、机器人等）
- 需要输出 Markdown + BibTeX 格式的学术综述

## When NOT to Use

- 纯 CS/AI 理论（用通用学术工具）
- 医学/生物方向（用 PubMed 为主的专业工具）
- 只需要快速找几篇论文（直接搜索即可，不需要综述流程）

---

## ⚠️ 首要：交互式提问流程

**用户请求文献调研时，必须先问清楚以下问题再动手。** 不要自行假设。

### 必问项（7个）

1. **调研主题** — 具体的研究问题或关键词
2. **主题方向** — 制造 / 材料 / 焊接 / 机器人 / 结构检测 / 其他
3. **时间范围** — 默认近3年。快速演进领域（LLM、Agent 等）建议默认1年
4. **综述深度**：
   - 快速概览（5-10篇，500-1000字）
   - 标准综述（20-40篇，3000-5000字）← 默认
   - 深度综述（50+篇，8000+字）
5. **输出语言** — 默认中文，可选英文
6. **引用风格** — GB/T 7714（默认）/ APA 7th / IEEE / Nature
7. **分类依据** — 用户可能指定分类轴（如"基于CAD vs 非CAD"）。**建议主动询问是否需要多个分类维度**

### 可选项

8. 是否需要覆盖传统方法还是只看最新方法
9. 是否有偏好的子方向/应用场景
10. 是否有已知的关键论文

### 提问模板

```
好的，我来帮你做文献调研。先确认几个问题：

1. 调研主题是什么？
2. 方向偏向：A) 制造  B) 材料  C) 焊接  D) 机器人  E) 结构检测  F) 其他
3. 时间范围：默认近3年，有特殊要求吗？
4. 深度：A) 快速概览(5-10篇)  B) 标准综述(20-40篇)  C) 深度综述(50+篇)
5. 语言：中文 / English？
6. 有没有你希望的分类维度？（比如按方法类型、按应用场景等）
```

---

## 数据库与信息源

按优先级排列，**至少使用3个互补来源**。优先已发表/同行评审论文。

| 数据库 | 覆盖领域 | 访问方式 | 优先级 |
|--------|---------|---------|--------|
| **Semantic Scholar** | 2亿+跨学科论文，含引用数据 | REST API (无需key, 1req/s) | ★★★ 主力 |
| **IEEE Xplore** | 工业应用+工程（已发表） | web_search (摘要免费) | ★★★ 工程必用 |
| **PubMed/PMC** | 生物医学+医疗工程 | E-utilities API (无需key) | ★★☆ 医疗工程用 |
| **ACM DL** | 计算机+人机交互 | web_search (摘要免费) | ★★☆ |
| **Papers With Code** | AI论文+代码+基准排名 | REST API | ★★☆ |
| **OpenAlex** | 开放学术图谱 | REST API (无需key) | ★★☆ |
| **Google Scholar** | 最广泛覆盖 | web_search | ★★☆ 补充 |
| **arXiv** | CS/AI/ML 预印本 | REST API (无需key) | ★☆☆ 仅补充前沿 |

### 工程领域数据库选择

| 主题方向 | 主力库 | 必用库 | 补充库 |
|---------|--------|--------|--------|
| 制造/焊接/检测 | Semantic Scholar | IEEE Xplore | ACM, PwC, arXiv |
| 材料科学 | Semantic Scholar | IEEE Xplore | Google Scholar |
| 机器人 | Semantic Scholar | IEEE Xplore + ACM | PwC, arXiv |
| AI+工程 | Semantic Scholar | IEEE Xplore | ACM, PwC, arXiv |

---

## 核心工作流（7个阶段）

### Phase 1: 选题分析与策略制定

1. 提取2-4个核心概念
2. 列出每个概念的同义词、缩写、相关术语
3. 构建布尔搜索策略
4. 确定数据库组合

### Phase 2: 多数据库检索

**检索顺序**：Semantic Scholar → IEEE Xplore（工程必用）→ Papers With Code → Google Scholar/OpenAlex → arXiv（前沿补充）

#### Semantic Scholar 检索

```bash
curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=QUERY&limit=20&fields=title,authors,year,citationCount,abstract,externalIds,publicationVenue&year=2023-2026"
```

#### CrossRef API（兜底方案）

```python
import urllib.request, urllib.parse, json
title = "paper title here"
q = urllib.parse.quote(title)
url = f"https://api.crossref.org/works?query.title={q}&rows=3"
req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 (research bot)"})
resp = urllib.request.urlopen(req, timeout=20)
data = json.loads(resp.read())
```

### Phase 3: 结果整合与去重

按 DOI / Semantic Scholar ID / 标题去重，按引用数排序。

### Phase 4: 筛选与评估

**引用量参考阈值**：

| 论文年龄 | 高影响力 | 重要 | 里程碑 |
|---------|---------|------|--------|
| 0-1年 | 20+ | 50+ | 100+ |
| 1-3年 | 50+ | 200+ | 500+ |
| 3-5年 | 100+ | 500+ | 1000+ |
| 5年+ | 500+ | 1000+ | 5000+ |

### Phase 5: 主题综合与撰写

**按主题组织，而非逐篇罗列**。每个主题段落应有：
- 综合性陈述
- 共识与分歧
- 证据强度判断
- **每节末尾附文献汇总表**

### Phase 6: 引用验证

1. 检查 DOI 是否可解析：`curl -sL -o /dev/null -w "%{http_code}" "https://doi.org/..."`
2. 确认作者、标题、年份匹配
3. 优先使用已发表版本（而非预印本）

### Phase 7: 产物生成

输出 `review.md` + `refs.bib`，格式规范见下方。

---

## 输出格式规范

### review.md 格式

1. **引用格式**：每篇文献以超链接形式给出原文 URL，后附 `\cite{key}`
   ```markdown
   Zou和Zeng[1](https://doi.org/10.1016/j.measurement.2023.112492) \cite{zou2023lightweight}，
   提出了基于SOLOv2的轻量化分割网络...
   ```

2. **每节文献汇总表**：
   ```markdown
   | # | 文献 | 年份 | 方法 | 期刊/会议 | 关键贡献 |
   |:-:|:-----|:----:|:-----|:----------|:---------|
   | [1] | Zou & Zeng | 2023 | SOLOv2轻量化分割 | Measurement | 42次引用 |
   ```

3. **参考文献列表**：综述末尾按编号列出所有文献，每条附超链接

4. **预印本标注**：arXiv 论文标注"[预印本]"

### refs.bib 格式

- 标准 BibTeX 格式（@article, @inproceedings, @misc）
- key 命名：`{姓氏小写}{年份}{标题首词}` 如 `zou2023lightweight`
- 必须包含 doi 或 eprint 字段

---

## 三级去重算法

**必须按顺序检查三级，不能只靠 DOI**：

```python
def is_duplicate(new_paper, existing_bibs):
    """三级去重：DOI → arXiv ID → 标题相似度"""
    
    # 1. DOI 精确匹配（最可靠，覆盖率 ~93%）
    if new_paper.get("doi"):
        for bib in existing_bibs:
            if bib.get("doi") and bib["doi"].lower() == new_paper["doi"].lower():
                return True, "DOI match"
    
    # 2. arXiv ID / eprint 匹配（覆盖预印本）
    if new_paper.get("arxiv_id"):
        for bib in existing_bibs:
            if bib.get("eprint") and bib["eprint"] == new_paper["arxiv_id"]:
                return True, "arXiv match"
    
    # 3. 标题相似度兜底（>85% 词重合）
    new_title = normalize(new_paper["title"])
    new_words = set(new_title.split())
    for bib in existing_bibs:
        existing_title = normalize(bib.get("title", ""))
        existing_words = set(existing_title.split())
        if not new_words or not existing_words:
            continue
        overlap = len(new_words & existing_words) / max(len(new_words), 1)
        if overlap > 0.85:
            return True, f"Title similarity: {overlap:.0%}"
    
    return False, "New paper"
```

---

## 增量更新（Phase 8）

已有主题补充新文献时，支持两种路径：

### 路径 A：主动搜索新增

1. 读取现有 bib，提取所有已有 DOI 和 title
2. Semantic Scholar + arXiv + web_search，限定日期在上次综述之后
3. 自动去重（三级策略）
4. 分类 → 更新 review.md + refs.bib

### 路径 B：用户手动提供

- B1：用户发 PDF → 解析元数据 → 查询 → 去重 → 入库
- B2：用户给标题/DOI/链接 → 查询 → 去重 → 入库

---

## ⚠️ 已知问题与踩坑

### Semantic Scholar 限流

**实际经验：即使间隔2秒，连续5-6个查询就会触发429。**

应对策略：
- 每次搜索间隔 1.5 秒以上
- 被限流期间切换到 CrossRef API（无限流）
- 等待 120 秒再重试 Semantic Scholar
- 用 web_search 作为最终兜底

### CrossRef API 兜底

用户给论文标题但 Semantic Scholar 被限流时，用 CrossRef 查元数据。CrossRef 无需 key，无限流限制。

### ScienceDirect 无法直接抓取

ScienceDirect 返回 403。通过 CrossRef 标题搜索映射到 DOI 再查元数据。

---

## 注意事项

1. **宁缺毋滥**：不确定的论文不纳入，不编造引用
2. **时效性**：工程领域优先近3年论文
3. **可复现**：记录所有搜索词和数据库
4. **诚实**：明确指出证据不足或存在争议的领域
5. **引用真实**：每一条引用必须有超链接指向原文，绝不编造 DOI 或 arXiv ID
6. **arXiv 标注**：arXiv 论文在参考文献中标注"[预印本]"
7. **每节表格**：每个小节必须附文献汇总表
