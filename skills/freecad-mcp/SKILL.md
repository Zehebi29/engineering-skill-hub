---
name: "freecad-mcp"
description: "FreeCAD MCP server: AI agent driven 3D CAD modeling, parametric design, FEM analysis via Model Context Protocol"
author: "neka-nat"
tags: [cad, 3d-modeling, freecad, mcp, fem, engineering]
version: "1.0.0"
license: MIT
compatible_with: [hermes, openclaw]
metadata:
  hermes:
    tags: [engineering, cad, simulation]
    related_skills: [engineering-paper-digest, patent-landscape]
  openclaw:
    requires:
      bins: [python3, uvx]
---

# FreeCAD MCP Server

> 本 skill 原始来源：[neka-nat/freecad-mcp](https://github.com/neka-nat/freecad-mcp)，star 数：933
> 集成时间：2026-05-13 | 原作者：neka-nat

通过 Model Context Protocol (MCP) 连接 AI agent 与 FreeCAD，实现自然语言驱动的 3D CAD 建模和有限元分析。

## 适用场景

- 用自然语言描述零件，agent 自动在 FreeCAD 中建模
- 参数化设计：修改尺寸、特征、约束
- FEM 有限元分析（CalculiX 求解器）
- 从 2D 图纸生成 3D 零件
- 从零件库插入标准件

## 前置条件

1. 安装 FreeCAD（1.0 或 1.1）
2. 安装 uv/uvx：`curl -LsSf https://astral.sh/uv/install.sh | sh`
3. 安装 FreeCAD MCP 插件（见下方）

## 安装步骤

### 1. 安装 FreeCAD MCP 插件

```bash
git clone https://github.com/neka-nat/freecad-mcp.git
cd freecad-mcp

# Linux (Ubuntu/Debian)
cp -r addon/FreeCADMCP ~/.FreeCAD/Mod/

# Linux (Arch/CachyOS, FreeCAD 1.1)
mkdir -p ~/.local/share/FreeCAD/v1-1/Mod/
cp -r addon/FreeCADMCP ~/.local/share/FreeCAD/v1-1/Mod/

# macOS (FreeCAD 1.1)
cp -r addon/FreeCADMCP ~/Library/Application\ Support/FreeCAD/v1-1/Mod/

# macOS (FreeCAD 1.0)
cp -r addon/FreeCADMCP ~/Library/Application\ Support/FreeCAD/v1-0/Mod/

# Windows
# 复制 addon/FreeCADMCP 到 %APPDATA%\FreeCAD\Mod\
```

重启 FreeCAD，在 Workbench 列表中选择 "MCP Addon"。

### 2. 启动 RPC Server

在 FreeCAD 中：MCP Addon 工具栏 -> "Start RPC Server"。

可选：勾选 "Auto-Start Server" 实现 FreeCAD 启动时自动开启 RPC。

### 3. 配置 MCP Client

在 Claude Desktop / Hermes Agent / 其他 MCP client 的配置中添加：

```json
{
  "mcpServers": {
    "freecad": {
      "command": "uvx",
      "args": ["freecad-mcp"]
    }
  }
}
```

节省 token 模式（仅文本反馈，不返回截图）：

```json
{
  "mcpServers": {
    "freecad": {
      "command": "uvx",
      "args": ["freecad-mcp", "--only-text-feedback"]
    }
  }
}
```

远程连接（控制另一台机器上的 FreeCAD）：

```json
{
  "mcpServers": {
    "freecad": {
      "command": "uvx",
      "args": ["freecad-mcp", "--host", "192.168.1.100"]
    }
  }
}
```

远程连接需在 FreeCAD MCP 工具栏中勾选 "Remote Connections" 并配置允许的 IP。

## 可用工具

| 工具 | 功能 |
|------|------|
| `create_document` | 创建新文档 |
| `create_object` | 创建新对象 |
| `edit_object` | 编辑对象 |
| `delete_object` | 删除对象 |
| `execute_code` | 在 FreeCAD 中执行任意 Python 代码 |
| `insert_part_from_library` | 从零件库插入标准件 |
| `get_view` | 获取当前视图截图 |
| `get_objects` | 获取文档中所有对象 |
| `get_object` | 获取指定对象 |
| `get_parts_list` | 获取零件库列表 |
| `run_fem_analysis` | 运行 CalculiX FEM 分析，返回最大 von Mises 应力、最大位移、节点数 |

## 使用示例

### 设计法兰盘

```
用户：设计一个外径 100mm、内径 50mm、厚 20mm 的法兰盘，带 6 个均匀分布的 M8 螺栓孔。

Agent 调用流程：
1. create_document("flange")
2. create_object(外径圆柱 100x20)
3. create_object(内径孔 50x20)
4. execute_code(创建 6 个螺栓孔阵列)
5. get_view() 返回截图确认
```

### FEM 分析

```
用户：对这个悬臂梁施加 1000N 端部载荷，分析应力分布。

Agent 调用流程：
1. execute_code(创建梁几何体)
2. execute_code(设置材料属性和边界条件)
3. execute_code(创建 FemAnalysis 对象)
4. run_fem_analysis() -> 返回最大应力、最大位移
5. get_view() 返回应力云图
```

## Pitfalls

1. **FreeCAD 必须运行**：MCP server 通过 RPC 与 FreeCAD 通信，FreeCAD 未启动时所有调用失败。
2. **版本兼容**：FreeCAD 1.0 和 1.1 的插件目录不同，注意区分。
3. **execute_code 安全**：`execute_code` 可执行任意 Python，在生产环境中应限制使用。
4. **截图 token 消耗**：`get_view` 返回截图会消耗大量 token，可用 `--only-text-feedback` 模式减少消耗。
5. **FEM 需要 CalculiX**：`run_fem_analysis` 依赖 CalculiX 求解器，需单独安装（FreeCAD 通常自带）。

## 参考链接

- 仓库：https://github.com/neka-nat/freecad-mcp
- FreeCAD 官网：https://www.freecad.org/
- MCP 协议：https://modelcontextprotocol.io/
