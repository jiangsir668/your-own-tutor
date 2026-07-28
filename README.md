# Your Own Tutor · 你的私人导师 &middot; [![Version](https://img.shields.io/badge/v6.8-A-blue)](https://github.com/jiangsir668/your-own-tutor) [![Tests](https://img.shields.io/badge/tests-10%2F10-green)](https://github.com/jiangsir668/your-own-tutor/blob/main/jiaocheng-tests.md) [![Darwin](https://img.shields.io/badge/darwin-A-brightgreen)](https://github.com/jiangsir668/your-own-tutor) [![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE) [![Lang](https://img.shields.io/badge/lang-中文_|_EN-blue)]()

<p align="center">
  <b>Upload a textbook. The AI makes <i>you</i> teach it back.</b><br>
  <b>上传课件 → 你来讲给 AI 听 → 答不上来诊断根因 → 跨会话续课</b><br>
  <em>Lecture · Feynman · Socratic · Translation — 4 teaching modes, bilingual, battle-tested.</em>
</p>

---

## 为什么存在 / Why This Exists

**ChatGPT 给你讲解。Your Own Tutor 逼你讲出来。**

ChatGPT explains things to you. **Your Own Tutor makes YOU explain things to it.**

基于费曼学习法——已知最有效的学习方法。你讲不清楚，就是没搞懂。这个 skill 逼你讲。每一个模糊的句子、每一个偷换的概念、每一个"我大概懂了"——都会被追问 2-5 轮。直到你真正掌握。

Based on the Feynman Technique — the single most effective learning method ever studied. If you can't explain it clearly, you don't understand it. This skill makes you explain. Every fuzzy sentence, every hand-waved concept, every "I think I get it" — gets challenged for 2-5 rounds. Until you actually own it.

它记得你学到哪、知道你错在哪、自动排螺旋复习、同步 Obsidian。它说你的语言——逐条消息独立检测，中英切换零压力。

It remembers where you left off. It knows what you got wrong. It schedules spiral reviews. It syncs to Obsidian. It speaks your language — literally, message by message.

---

## 能做什么 / What It Does

| 功能 / Feature | 通用 AI / Generic AI | 教程大师 / Your Own Tutor |
|---------|:---:|:---:|
| 讲解概念 / Explain | ✅ | ✅ |
| **逼你复述 / Make YOU explain back** | ❌ | ✅ **费曼追问 2-5 轮 / Feynman Drill 2-5 rounds** |
| **诊断卡壳根因 / Diagnose WHY stuck** | ❌ | ✅ **5 种卡壳类型 + 4 种修复策略** |
| 跨会话记忆 / Cross-session memory | ❌ | ✅ 说"学习"就续课 / Say "learn" to resume |
| 螺旋复习 + 错题本 / Spiral review + error log | ❌ | ✅ 自动排期 + 溢出强制清 / Auto-scheduled, force-cleared |
| Obsidian 笔记同步 / Sync to Obsidian | ❌ | ✅ 学习内容 + 错题自动写入 Vault |
| **一键切换教学方式 / Switch teaching style** | ❌ | ✅ **4 种模式即时切 / 4 modes, instant switch** |
| **双语逐消息检测 / Bilingual per-message** | ❌ | ✅ 每条消息独立判断语言 |
| **Session 结束自检 / Self-audit** | ❌ | ✅ **6 项不变检查阻断异常数据** |

---

## 四种教学模式 / Four Teaching Modes

### 🎙️ 讲解模式 / Lecture — "我讲透，你讲回来 / I explain, you explain back"
零基础初次接触。AI 逐字输出原文 → 大白话拆解 → 1-2 轮费曼验证。`mastery_depth = shallow`。

Best for first contact. AI outputs original text verbatim → plain-language breakdown → 1-2 round Feynman check.

### 🔥 费曼模式 / Feynman — "你来讲，我挑刺 / YOU teach, I critique" *(默认 / default)*
深度理解。AI 挤完核心知识，然后你开始讲。R1 "用你自己的话解释" → R2 "条件变了会怎样" → R3 "什么情况不适用" → R4 "跟前面学的有什么关系" → R5 "局限是什么"。答不上来→诊断根因（概念没吃透？推理断了？前面基础漏了？）→修复→重来。**全部轮次 fail → "基础断崖" → 回溯前置章节。** `mastery_depth = deep`。

Best for real understanding. AI gives the core concept → you explain. R1 "In your own words" → R2 "What if conditions change?" → R3 "When does it fail?" → R4 "How does it connect?" → R5 "What are the limits?" Stuck? Diagnosed (concept gap? reasoning flaw? prerequisite missing?) → repaired → retried. **All rounds fail → Foundation Cliff → go back to prerequisites.**

### 🔮 苏格拉底模式 / Socratic — "我只问，你走到结论 / I only ask, you conclude"
批判思维。5 轮追问链。每个回答都被挑战。你自己推翻自己，一步步走到结论。`mastery_depth = deep`。

Best for critical thinking. 5-question chain. Each answer challenged. You revise your own framework until it holds.

### 🌐 翻译模式 / Translation — "只关心你能不能表达清楚 / I only care if you can express it"
英文学术写作。AI 给原文 → 你翻译 → 三维诊断（用词/句法/风格）→ 给参考译法 → 你说出差在哪。`mastery_depth = deep`。

Best for academic English. Original → your translation → 3-axis diagnosis (accuracy/syntax/style) → reference translation → you explain the gap.

---

## 快速开始 / Quick Start

```bash
npx skills add jiangsir668/your-own-tutor
```

| 中文触发词 | EN Trigger | 做什么 / Action |
|---|---|---|
| `备课` / `teach` | 上传课件建课 | PPT/PDF/DOCX → 自动提取 → 自评 → 🔴 确认架构 |
| `学习` / `learn` | 续课 | 一口报进度 + 断点续接追问或修复 |
| `继续` / `continue` | 续课 | 同上 / Same as above |
| `讲一下` / `explain` | 讲解概念 | 进入讲解模式 / Lecture mode |
| `通俗解释` / `in plain terms` | 大白话讲解 | Lecture mode, plain language |
| `学到哪了` / `where was I` | 查进度 | 报全部课程进度 / Reports all course progress |
| `换模式` / `switch mode` | 切换教学模式 | 列出 4 种模式 + 推荐最优 + 🔴 等确认 |

### 交互演示 / Demo

```
你: 学习

AI: 📍 工程统计学
    Ch3 中心极限定理 (practicing)
    上次答到 R3 卡住了，用工厂类比修复中。
    连续 5 天打卡。继续？

你: 换模式

AI: 1. 讲解 / Lecture — 我讲透你再讲回来 / I explain, you explain back
    2. 费曼 / Feynman — 你讲我来挑刺 / You teach, I critique  ← 推荐：这概念需要深究
    3. 苏格拉底 / Socratic — 我只问，你走到结论 / I only ask
    4. 翻译 / Translation — 只关心你的英文表达
    选哪个？/ Which one?

AI (EN material detected): "This material is in English. Would you like to learn in English or Chinese?"
```

---

## 质量保证 / Quality

- **10/10 自动化测试全绿** — 费曼中间态、模式切换、修复天花板、不变检查
- **10/10 automated tests** — Feynman mid-states, mode switching, repair ceiling, invariants
- **3 轮多Agent独立审计** — HIGH 逻辑冲突清零
- **3 rounds multi-agent audits** — zero HIGH conflicts remaining
- **6 项 Session 结束复检** — 阻断异常状态落盘
- **6 invariant checks at session end** — blocks corrupt state
- **Darwin 评分: A (87%+)** — 独立评分 Agent 审计
- **Darwin Score: A (87%+)** — audited by independent scoring agents
- **双语逐消息检测** — 中英混用以字符数仲裁
- **Bilingual, per-message** — character-count arbitration for mixed input

---

## 文件 / Files

```
your-own-tutor/
├── SKILL.md              # 10.7KB, 单文件自包含 / self-contained skill
├── README.md             # 本文件 / This file
├── jiaocheng-tests.md    # 10 条自动化测试 / 10 automated tests
└── LICENSE               # MIT
```

---

## 贡献 / Contribute

欢迎提 Issue 和 PR / Issues & PRs welcome。改完跑 `jiaocheng-tests.md`——10 条必须全绿 / Run after any change — all 10 must pass。

---

## License

MIT © 2026 [jiangsir668](https://github.com/jiangsir668)

---

<p align="center">
  <sub>Built with Darwin Skill Optimizer · Audited by multi-agent adversarial review</sub><br>
  <sub>由 Darwin Skill 优化器构建 · 多 Agent 对抗审计验证</sub>
</p>