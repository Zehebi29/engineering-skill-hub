---
name: "engineering-paper-digest"
description: "工程论文速读：给定论文 URL/DOI/标题，输出结构化中文摘要（研究问题、方法、关键结果、局限性、工程应用价值）。比文献综述轻量，适合日常读论文。"
author: "Zehebi29"
tags: [research, paper-reading, engineering, digest, summary, academic]
version: "1.0.0"
license: MIT
compatible_with: [hermes, openclaw]
metadata:
  hermes:
    tags: [research, paper-reading, engineering, academic]
    related_skills: [engineering-lit-review, arxiv, web]
  openclaw:
    requires:
      bins: [curl]
---

# 工程论文速读 (Engineering Paper Digest)

给定一篇工程领域论文的 URL、DOI 或标题，输出结构化中文摘要。比文献综述轻量得多，适合日常读论文场景。

## When to Use

- 用户发来一篇论文的链接/DOI/标题，想快速了解内容
- 用户说"帮我看看这篇论文"、"这篇论文讲了什么"
- 用户需要中文摘要以便快速决策是否深入阅读

## When NOT to Use

- 需要系统性综述多篇论文（用 engineering-lit-review）
- 论文不在工程领域（直接用通用摘要即可）
- 用户只需要论文的引用信息（直接查元数据即可）

---

## 工作流程

### Step 1: 获取论文信息

根据用户输入，获取论文的元数据和全文。

**输入类型处理：**

| 输入类型 | 处理方式 |
|---------|---------|
| DOI | `curl -sL "https://doi.org/DOI" -o /dev/null -w "%{url_effective}"` 获取最终 URL，然后提取内容 |
| arXiv URL/ID | 直接访问 `https://arxiv.org/abs/ID` 提取摘要，或 `https://export.arxiv.org/api/query?id_list=ID` |
| 期刊 URL | 尝试 web_extract 提取摘要和关键信息 |
| 论文标题 | 用 Semantic Scholar API 搜索：`curl -s "https://api.semanticscholar.org/graph/v1/paper/search?query=TITLE&limit=1&fields=title,authors,year,citationCount,abstract,externalIds"` |

**Semantic Scholar 获取详细信息：**

```bash
# 通过 DOI
curl -s "https://api.semanticscholar.org/graph/v1/paper/DOI:10.xxxx?fields=title,authors,year,citationCount,abstract,externalIds,publicationVenue,tldr,references"

# 通过 arXiv ID
curl -s "https://api.semanticscholar.org/graph/v1/paper/ARXIV:2401.xxxxx?fields=title,authors,year,citationCount,abstract,externalIds,publicationVenue,tldr"
```

### Step 2: 提取关键信息

从论文中提取以下要素：

1. **研究问题** — 解决什么工程问题？
2. **现有方法的不足** — 为什么现有方法不够好？
3. **提出的方法** — 核心技术路线是什么？
4. **实验验证** — 在什么数据集/场景上验证？结果如何？
5. **局限性** — 作者自己提到的不足，或你能看出的局限
6. **工程应用价值** — 实际工程中能用在哪？

### Step 3: 输出结构化摘要

按以下格式输出：

```markdown
## [论文标题]
**作者**: 前3位作者 et al. | **年份**: YYYY | **期刊/会议**: Venue | **引用数**: N

### 研究问题
一句话概括：这篇论文要解决什么工程问题。

### 方法概述
2-3 句话描述核心技术路线。避免过于技术化的细节，重点说清楚"做了什么"而非"怎么做的"。

### 关键结果
- 结果1（量化指标）
- 结果2（量化指标）
- 与 baseline 对比的提升幅度

### 局限性
- 局限1
- 局限2

### 工程应用价值
1-2 句话：这个方法在实际工程中能用在哪？有什么落地潜力？

### 一句话总结
用一句大白话概括这篇论文的核心贡献。
```

---

## 多篇论文批量速读

用户一次发来多篇论文时，按以下流程：

1. 逐篇获取信息（注意 Semantic Scholar 限流，间隔 1.5 秒）
2. 每篇输出独立的结构化摘要
3. 最后加一个**横向对比表**：

```markdown
| 论文 | 年份 | 方法 | 数据集 | 关键指标 | 局限性 |
|------|------|------|--------|---------|--------|
| Paper A | 2025 | Method A | Dataset X | mAP 92.3% | 仅适用2D |
| Paper B | 2026 | Method B | Dataset Y | IoU 0.89 | 计算量大 |
```

---

## 提取全文的技巧

### 可直接抓取的来源

- **arXiv**: `https://arxiv.org/html/ID`（HTML 版本，最容易解析）
- **PMC**: `https://www.ncbi.nlm.nih.gov/pmc/articles/PMCID/`（开放获取）
- **MDPI/Sensors**: 通常开放获取

### 需要间接获取的来源

- **ScienceDirect/Elsevier**: 返回 403，用 Semantic Scholar 的 abstract + tldr 字段兜底
- **IEEE Xplore**: 摘要免费，全文需订阅，用摘要 + Semantic Scholar 元数据
- **Springer**: 部分开放获取，尝试 `web_extract`

### 兜底策略

当无法获取全文时：
1. 优先用 Semantic Scholar 的 `abstract` 和 `tldr` 字段
2. 如果有 `tldr` 字段，直接使用（这是 Semantic Scholar 自动生成的摘要）
3. 只基于摘要输出，但在开头注明"本文基于摘要信息，未获取全文"

---

## 输出风格

- **语言**: 默认中文，用户指定英文时用英文
- **语气**: 客观、简洁，不要用"本文创新性地提出了"这种八股文
- **量化**: 尽可能给出具体数字（精度、速度、数据集大小等）
- **诚实**: 如果信息不足以判断某项，在该处注明"信息不足"

---

## 已知问题

### Semantic Scholar 限流

连续 5-6 个请求会触发 429。应对：
- 单篇速读不受影响
- 批量速读时，每篇间隔 1.5 秒
- 被限流后等待 120 秒再重试

### 部分论文无法获取全文

ScienceDirect、IEEE Xplore 等付费期刊无法直接抓取。此时仅基于摘要 + Semantic Scholar 的 tldr 字段输出。在输出中注明"基于摘要信息"。

### 中文论文支持

中文论文（如知网）无法通过 Semantic Scholar 获取。需要用户提供 PDF 或截图，然后通过 OCR 提取内容。
