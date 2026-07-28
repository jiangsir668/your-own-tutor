# Jiaocheng Agent Definitions / Agent 定义文件

This directory contains agent definition files for **Claude Code**. / 此目录包含用于 **Claude Code** 的 agent 定义文件。

> ⚠️ These are **reference files only**. The current Jiaocheng implementation runs on Claude Desktop and uses inline agent prompts. These agent definitions are ready when Claude Desktop supports custom agent types.
>
> ⚠️ 这些是**参考文件**。当前 Jiaocheng 在 Claude Desktop 上运行，使用内联 agent prompt。这些 agent 定义文件在 Claude Desktop 支持自定义 agent 类型时可立即使用。

## How to Use / 如何使用

```bash
cp agents/*.md ~/.claude/agents/
# or / 或
cp agents/*.md .claude/agents/
```

## Architecture / 架构

| File / 文件 | Role / 角色 | Tools / 工具 | Model / 模型 |
|---|---|---|---|
| `jiaocheng-teacher.md` | Teaching / 教学 | Read-only / 只读 | sonnet |
| `jiaocheng-file-writer.md` | File writing / 文件写入 | Read, Write, Edit, Bash | haiku |
| `jiaocheng-course-builder.md` | Course creation / 建课 | Read | sonnet |

## Current Status / 当前状态

As of v18.0 (2026-07-29), Claude Desktop does not support custom agent types via `.claude/agents/`. These definitions are ready but awaiting platform support. In the meantime, equivalent inlined prompts are embedded directly in `SKILL.md`. / 截至 v18.0（2026-07-29），Claude Desktop 不支持 `.claude/agents/` 自定义 agent 类型。这些定义文件已就绪，等待平台支持。同时，等效的内联 prompt 已直接嵌入 `SKILL.md`。
