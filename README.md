# 教程大师 · Your Own Tutor

<div align="center">

**上传课件 → AI 拆课 → 你来讲，AI 挑刺 → 跨会话追踪 → Obsidian 同步**

[![Version](https://img.shields.io/badge/version-6.1-blue)](https://github.com/jiangsir668/your-own-tutor)
[![Tests](https://img.shields.io/badge/tests-10%2F10-green)](https://github.com/jiangsir668/your-own-tutor/blob/main/jiaocheng-tests.md)
[![Darwin Score](https://img.shields.io/badge/darwin-85%2F100_A-brightgreen)](https://github.com/jiangsir668/your-own-tutor)
[![License](https://img.shields.io/badge/license-MIT-lightgrey)](https://github.com/jiangsir668/your-own-tutor/blob/main/LICENSE)

</div>

---

## 为什么叫 Your Own Tutor

普通的 AI 教学是「AI 讲，你听」。费曼学习法反过来了——**你讲给 AI 听，AI 挑刺**。

你越讲不清楚，AI 越知道你没掌握。每一个模糊的句子、每一次回避的措辞、每一个偷换的概念——都会被追着问到你说清楚为止。

这就是教程大师的核心。你把它装进 Claude Code，它就是你随身的学习教练。随时随地"学习"，它记得你学到哪、卡在哪、哪些该复习了。

---

## 跟通用 AI 有什么不一样

| | ChatGPT / 豆包 | 教程大师 |
|---|---|---|
| 讲完就结束 | ✅ | ✅ |
| 讲完让你复述 | ❌ | ✅ **费曼追问 2-5 轮** |
| 答不上来诊断根因 | ❌ | ✅ 五种卡壳类型 + 四种修复策略 |
| 跨会话记住进度 | ❌ | ✅ 说"学习"就续课 |
| 螺旋复习 + 错题本 | ❌ | ✅ 自动排期 + 强制清队列 |
| Obsidian 同步 | ❌ | ✅ 学习内容 + 错题自动写入 Vault |
| 一键换教学方式 | ❌ | ✅ 四模式即时切换 |

---

## 四种教学模式

### 🎙️ 讲解模式 — "我先给你讲透，你再给我讲回来"

适合新概念、零基础入门。

AI 一字不差输出原文 → 零基础大白话拆解 → **你用自己话复述**。讲对了过关，讲偏了换角度重讲。

```
AI: [一字不差输出原文，附页码]

AI: 通俗解读——这东西说白了就是一个"等多久才发生"的模型。
    比如灯泡用了 1000 小时，还能撑多久？和刚开始用一样——它不记得自己已经老了。

AI: 轮到你。用你自己的话说，指数分布在干什么？

你: [复述]

AI: 到位。✅ 或者：偏了，应该是 X，我们换个角度。
```

### 🔥 费曼模式 — "你来讲，我来挑刺"

适合深度理解、概念消化。**默认主力模式。**

AI 挤完核心知识 → 然后你开始讲。五轮递进：

1. 「用你自己的话解释」
2. 「如果条件变了会怎样」
3. 「什么情况下不适用」
4. 「跟前面学的有什么关系」
5. 「你觉得它的局限是什么」

答不上来 → AI **诊断根因**（概念没吃透？推理断了？前面基础漏了？）→ 修复 → 重新来。

**全部轮次全挂 → 判"基础断崖" → 回溯前置章节。**

### 🔮 苏格拉底模式 — "我不讲，问到你走到结论"

适合批判思维、方法论课程。

AI 一个问题接一个问题，让你自己推翻自己不完整的理解，一步步走到结论。

### 🌐 翻译模式 — "只关心你能不能英文表达清楚"

适合英文学术写作。AI 给原文 → 你翻译 → 三维诊断（用词/句法/风格）→ 给参考译法 → 你说出差在哪。

---

## 安装

```bash
npx skills add jiangsir668/your-own-tutor
```

兼容 Claude Code / Cursor / Codex / OpenClaw 等任意 Agent Runtime。

---

## 怎么用

### 备课
```
上传 PPT/PDF/DOCX → AI 自动拆章拆概念 → "哪些你已经会了？" → 确认架构 → 进教学
```

### 学习（日常）
```
你: 学习

AI: 📍 工程统计学
    Ch3 中心极限定理 (practicing)
    上次答到 R3 卡住了，正用工厂类比修复。连续学了 5 天。
    继续？
```

### 换模式
```
你: 换模式

AI: 1. 讲解 — 我给你讲透你再讲回来
    2. 费曼 — 你讲我来挑刺 ← 推荐：这难度需要费曼深究
    3. 苏格拉底 — 我问你走到结论
    4. 翻译 — 只关心你英文表达
    选哪个？
```

---

## 质量保证

- **10/10 自动化测试全绿** — 费曼中间态、模式切换、卡壳天花板、不变检查
- **三轮多 Agent 独立审计** — 逻辑冲突清零
- **六项 Session 结束自检** — 字段缺失、状态冲突、残留数据自动阻断
- **Darwin Skill 评分** — **85/100（A 级）**

---

## 文件结构

```
your-own-tutor/
├── SKILL.md              # skill 本体（12KB，单文件自包含）
├── README.md             # 你现在在看
├── jiaocheng-tests.md    # 10 条自动化测试
└── LICENSE               # MIT
```

---

## 贡献

提 Issue 或者 PR 都欢迎。改完 SKILL.md 之后跑一下 `jiaocheng-tests.md` 里的 10 条测试。

---

## License

MIT © 2026 [jiangsir668](https://github.com/jiangsir668)
