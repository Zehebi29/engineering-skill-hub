# Contributing to Engineering Skill Hub

感谢你的贡献！以下是添加新 skill 的指南。

## 添加新 Skill

### 1. Fork & Clone

```bash
git clone https://github.com/YOUR_USERNAME/engineering-skill-hub.git
```

### 2. 创建 Skill 目录

```
skills/
└── your-skill-name/
    ├── SKILL.md              ← 必须：skill 主文件
    ├── references/           ← 可选：参考文档
    ├── templates/            ← 可选：模板文件
    └── scripts/              ← 可选：辅助脚本
```

### 3. 编写 SKILL.md

必须包含 YAML frontmatter，兼容 Hermes 和 OpenClaw：

```yaml
---
name: "your-skill-name"
description: "一行描述，说明触发条件和行为"
author: "your-github-username"
tags: [engineering, your-domain]
version: "1.0"
license: MIT
compatible_with: [hermes, openclaw]
metadata:
  hermes:
    tags: [engineering, your-domain]
    related_skills: []
  openclaw:
    requires:
      bins: [curl, python3]    # 可选：依赖的命令行工具
---
```

**Frontmatter 字段说明：**

| 字段 | 必须 | 说明 |
|------|------|------|
| `name` | ✅ | 小写 + 短横线，≤64字符 |
| `description` | ✅ | 一行描述，≤1024字符 |
| `author` | ✅ | GitHub 用户名 |
| `tags` | ✅ | 至少2个标签 |
| `version` | ✅ | 语义版本号 |
| `license` | ✅ | MIT / Apache-2.0 / 等 |
| `compatible_with` | ✅ | 支持的平台列表 |
| `metadata.hermes` | ⚪ | Hermes 专属配置（可选） |
| `metadata.openclaw` | ⚪ | OpenClaw 专属配置（可选） |

正文建议包含：
- **Overview** — 这个 skill 做什么，为什么需要
- **When to Use** — 触发条件
- **Workflow** — 核心步骤（带代码/命令示例）
- **Output Format** — 输出格式说明
- **Common Pitfalls** — 常见踩坑

### 4. 更新 README

在 `README.md` 的 Skills 表格中添加一行。

### 5. 提交 PR

```bash
git checkout -b add-your-skill-name
git add .
git commit -m "feat: add your-skill-name"
git push origin add-your-skill-name
```

然后在 GitHub 上创建 Pull Request。

## Skill 质量标准

- ✅ Frontmatter 完整（name, description, author, tags, version, license, compatible_with）
- ✅ 有清晰的触发条件描述
- ✅ 包含可执行的工作流步骤
- ✅ 记录了已知问题和踩坑经验
- ✅ 总长度在 2,000-15,000 字符之间
- ✅ 工程领域相关

## 不接受的类型

- ❌ 与工程领域无关的通用 prompt
- ❌ 纯理论无实操的文档
- ❌ 过度依赖付费 API 的 skill（需在文档中注明）

## 问题反馈

有任何问题请开 Issue 讨论！
