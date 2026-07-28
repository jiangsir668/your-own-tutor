# 📚 教程大师 / Your Own Tutor — AI-Powered Interactive Learning System

<p align="center">
  <b>Upload courseware → AI builds your course → Teaches you in 4 modes → Tracks everything</b><br>
  上传课件 → AI 自动建课 → 四种模式教学 → 全流程追踪
</p>

<p align="center">
  <img src="https://img.shields.io/badge/version-18.0-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/efaimo-A%20(94)-brightgreen?style=for-the-badge" />
  <img src="https://img.shields.io/badge/skilltest-27%2F29%20passed-success?style=for-the-badge" />
  <img src="https://img.shields.io/badge/tests-56%2F56%20passed-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/license-MIT-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/platform-Claude%20Desktop%20%7C%20Claude%20Code-lightgrey?style=for-the-badge" />
</p>

> [!NOTE]
> **English follows Chinese. All documentation is bilingual. 所有文档均为双语。**

---

## 🎯 What Is This? / 这是什么？

Jiaocheng (教程 = "tutorial" in Chinese) turns any courseware — PDF slides, lecture notes, textbooks — into a structured interactive course with **four distinct teaching modes**, automatic progress tracking, and Obsidian-synced study notes.

Jiaocheng（教程）把任何课件——PDF 幻灯片、讲义、教材——变成一门结构化互动课程，配有**四种教学模式**、自动进度追踪、Obsidian 同步学习笔记。

> **One PDF in. Mastery out. 一份课件进去，精通出来。**

---

## ✨ Features / 功能

| Feature / 功能 | Description / 描述 |
|---|---|
| 🏗️ **Auto Course Building**<br>**自动建课** | Upload a PDF/PPT/DOCX. AI extracts every concept, groups by dependency, tags difficulty, estimates study time. 上传课件，AI 自动提取知识点、建立依赖关系、标注难度、估算学时。 |
| 🎓 **4 Teaching Modes**<br>**四种教学模式** | Lecture (explain + verify), Feynman (you teach, I grill), Socratic (I only ask questions), Translation (academic translation with 3D diagnosis). 讲解、费曼追问、苏格拉底推导、翻译三维诊断。 |
| 📝 **Smart Note-Taking**<br>**智能笔记** | Pops up after every mastered concept — choose language, auto-saves to Obsidian with your own Feynman restatement. 每学完一个概念弹窗询问，按你选的语言自动写进 Obsidian。 |
| 📊 **Error Book**<br>**错题本** | Concepts you struggle with (repair ≥2 or fail ≥2) get logged in a cross-course error book. 卡了两遍的概念自动提醒加入错题本，跨课程汇总追踪。 |
| 🗺️ **Live Roadmap**<br>**实时路线图** | Chapter progress auto-updates (⏳ → ✅) as you complete every concept. 每章所有概念通完后自动标记完成，不弹窗打扰。 |
| 🔒 **Safety Gates**<br>**安全闸门** | All file paths double-sanitized before write. Capacity limits. Path isolation. Consistency self-check after every progress write. 文件名双重净化后写盘，容量上限，路径隔离，一致性自检。 |
| 🌐 **Bilingual Everywhere**<br>**全流程双语** | Per-message language detection. Popups follow your current language. Notes and error book in your chosen language. 逐条消息检测语言，弹窗跟随，笔记错题本自选。 |
| 🧠 **SCAN Attention Gate**<br>**SCAN 注意力闸** | State anchor forces the model to regenerate tracking tokens every interaction — proven to recover attention weights in long sessions. 每次交互强制输出状态锚点，恢复长会话中的注意力权重。 |

---

## 🚀 Quick Start / 快速开始

### Prerequisites / 前提
- Claude Desktop (Pro/Max) or Claude Code
- Obsidian Vault (optional — course files auto-sync)
- Claude Desktop（Pro/Max）或 Claude Code
- Obsidian Vault（可选——课程文件自动同步）

### Install / 安装

#### Claude Desktop
1. Open Claude Desktop → Skills panel
2. Import `SKILL.md` from this repo
3. Done. Type `jiaocheng` or upload a PDF.

#### Claude Desktop
1. 打开 Claude Desktop → Skills 面板
2. 导入本仓库的 `SKILL.md`
3. 完成。输入"jiaocheng"或上传课件。

#### Claude Code
```bash
cd ~/Documents/Obsidian\ Vault
mkdir -p .claude/skills/jiaocheng
cp SKILL.md .claude/skills/jiaocheng/SKILL.md
claude
# Then type: jiaocheng
```

### First Run / 首次运行
```
You: jiaocheng
→ Upload a PDF or say "teach me" / 上传课件或说"教我"
→ AI builds your course → shows roadmap → ask "ready to learn?"
→ 4 modes available / 四种模式随时切换
```

---

## 🏗️ Architecture / 架构

```
User Message / 用户消息
    │
    ▼
┌─────────────────────┐
│   ORCHESTRATOR      │  ← Language detection + route / 语言检测+路由
│   (Main Skill)      │     Never teaches, never writes files
│   主 Skill           │     不教学，不写盘
└──────┬──────┬───────┘
       │      │
       ▼      ▼
┌──────────┐ ┌──────────┐ ┌──────────────┐
│ COURSE   │ │ TEACHER  │ │ FILE WRITER  │
│ BUILDER  │ │ AGENT    │ │ AGENT        │
│ 建课     │ │ 教学     │ │ 文件写入      │
│          │ │          │ │              │
│ sonnet   │ │ sonnet   │ │ haiku        │
│ One-time │ │ Per-round│ │ Double-gate  │
│ 一次性    │ │ 每轮调用  │ │ sanitization │
│          │ │ No Write │ │ 双重净化      │
└──────────┘ └──────────┘ └──────────────┘
       │           │              │
       ▼           ▼              ▼
  course.json  teaching_output  Obsidian Vault
               + state_changes  /jiaocheng/{course_id}/
                                ├── 学习路线.md / roadmap.md
                                ├── 错题本.md / errorbook.md
                                ├── 笔记/ / notes/
                                └── progress.json
```

> **Design principle / 设计原则**: The orchestrator does not teach. The teacher does not write files. The file writer does not teach. Three roles, one workflow. 编排器不教学，教师不写盘，文件写入器不教学。三个角色，一条流程。

---

## 🎓 Teaching Modes / 教学模式

### 📖 Lecture / 讲解模式
AI explains → gives a problem → you answer → repeat until mastery.
Easy concepts: 2 rounds. Medium: 3. Hard: 4.

AI 讲解 → 出题 → 你回答 → 重复直到掌握。简单概念 2 轮，中等 3 轮，困难 4 轮。

### 💡 Feynman / 费曼模式
You explain in your own words. AI grills you through 5 rounds:
R1: Restate → R2: Counterexample → R3: Failure conditions → R4: Connect to known → R5: Limits

你用自己的话解释。AI 五轮追问：用自己的话复述 → 举反例 → 找失效条件 → 关联已有知识 → 识别边界。

### 🗣️ Socratic / 苏格拉底模式
AI only asks questions. You derive the concept yourself. No answers given. Genuine understanding required — "I get it" without explanation does not count.

AI 只提问不回答。你自主推导。空洞的"我懂了"不视为掌握，必须给出具体解释或新例子。

### 🌐 Translation / 翻译模式
AI gives original text → you translate → 3D diagnosis (accuracy/fluency/naturalness) → reference → you identify differences. Fail ≥3: degrade to lecture.

AI 出原文 → 你翻译 → 三维诊断（准确性/流畅度/地道程度）→ 参考译文 → 你说出差异。连挂 3 次自动降级。

---

## 🔄 Teaching Loop (9 Steps) / 教学循环（9 步）

```
1. Read progress.json / 读进度
2. State anchor 📌 / 状态锚点
3. Spawn teacher agent / 启动教师 agent
4. Update state / 更新状态
5. Popup notes? / 弹窗笔记？
6. Popup error book? / 弹窗错题本？
7. Update roadmap (silent) / 静默更新路线图
8. Write progress (MANDATORY) + consistency check / 写进度（必做）+ 一致性校验
9. Auto-advance to next concept / 自动推进到下一个知识点
```

Every user message triggers one complete cycle. Nothing is skipped. 每条用户消息触发一次完整循环。不跳过任何步骤。

---

## 🔒 Safety & Security / 安全机制

| Gate / 闸门 | What It Does / 作用 |
|---|---|
| **Write-Before-Sanitize**<br>**写盘前净化** | Every Write must be preceded by a visible sanitize output line in chat. Missing → recovery → still writes. 每条 Write 前面必须在聊天里输出可见的净化行。漏了 → 补救 → 仍然写盘。 |
| **Double-Gate in File Writer**<br>**文件写入器双重闸门** | Sanitize again in the file-writer agent. Verify path is under vault/jiaocheng/. Reject if not. 写盘 agent 内再净化一次。校验路径在 vault 下，否则拒绝。 |
| **Capacity Guard**<br>**容量上限** | Notes ≤200 files/course, error book ≤500 rows, roadmap ≤50KB. Alert but don't block teaching. 笔记 ≤200 文件/课，错题 ≤500 行，路线图 ≤50KB。告警不阻塞。 |
| **Path Isolation**<br>**路径隔离** | All files under `{vault}/jiaocheng/{course_id}/`. Degrade to memory if vault unreachable — no data loss. 全部文件在指定路径下。vault 不可写则退化到内存——不丢数据。 |
| **Consistency Auto-Fix**<br>**一致性自动修复** | After every progress write: check depth non-empty when mastered, repair≥3 forced abandoned, four-bool mutex. Inconsistency → auto-fix with visible warning. 每次写进度后检查必填字段完整性，不一致自动修复并输出警告。 |

---

## 🧪 Quality / 质量验证

| Tool / 工具 | Result / 结果 |
|---|---|
| **efaimo** (Agent Skills Spec Audit) | **A (94/100)** — 0 errors, 1 warning |
| **skilltest** (29-point Static Analysis) | **27/29 passed** — 0 failures |
| **Internal Test Suite** (56-point) | **56/56 passed** — Security 8/8, Runtime 15/15 |

---

## 📁 Repository Structure / 仓库结构

```
jiaocheng/
├── SKILL.md                 # Main skill file / 主 skill 文件
├── CAPABILITIES.md           # Full capability document / 完整能力文档
├── README.md                 # This file / 本文件
├── LICENSE                   # MIT
└── agents/                   # Agent definitions (for Claude Code)
    ├── jiaocheng-teacher.md
    ├── jiaocheng-file-writer.md
    └── jiaocheng-course-builder.md
```

---

## 🤝 Contributing / 参与贡献

Found a bug? Have an idea? 发现 bug 或有想法？

1. Fork → branch → commit → PR
2. Describe what you changed and why / 描述你改了什么和为什么
3. Response within 48h / 48 小时内回复

---

## 📄 License / 许可

MIT © [jiangsir668](https://github.com/jiangsir668)

---

<p align="center">
  <sub>Built with ❤️ for students who want to learn better. 为好学者而建。</sub>
</p>
