# Your Own Tutor &middot; [![Version](https://img.shields.io/badge/version-6.1-blue)](https://github.com/jiangsir668/your-own-tutor) [![Tests](https://img.shields.io/badge/tests-10%2F10-green)](https://github.com/jiangsir668/your-own-tutor/blob/main/jiaocheng-tests.md) [![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE) [![Lang](https://img.shields.io/badge/lang-中文_|_EN-blue)]()

> 你来当讲师，AI 来挑刺 —— 基于费曼学习法的 AI 互动教学 skill。

- 📚 **自动建课** 上传课件，AI 拆章拆概念，问你会什么跳过什么
- 🎙️ **四模式教学** 讲解·费曼·苏格拉底·翻译，一键切换
- 🔥 **费曼追问** 你讲给 AI 听，答不上来诊断根因，不是给答案
- 💾 **跨会话追踪** 说"学习"就续课，进度、错题、复习队列全记着
- 📝 **Obsidian 同步** 学习内容 + 错题自动写入你的 Vault
- 🛡️ **自动复检** 每次结束检测 6 项不变条件，异常直接阻断

[安装](#安装) ·
[怎么用](#怎么用) ·
[测试覆盖](#测试覆盖) ·
[文件结构](#文件结构) ·
[贡献](#贡献) ·
[License](#license)

---

## 安装

```bash
npx skills add jiangsir668/your-own-tutor
```

支持 Claude Code、Cursor、Codex、OpenClaw 等任意 Agent Runtime。

---

## 怎么用

**中英双语支持**：中文说「备课」「学习」「换模式」，English: `teach`, `learn`, `explain`, `switch mode` 

### 建课

上传 PPT、PDF、DOCX，或直接粘贴大纲。AI 自动提取章节和概念，问"哪些你已经会了？"，然后确认课程架构。

```
你: 备课
[上传 or 粘贴课件]

AI: 从课件中提取了 6 章、34 个概念。
    这些概念你哪些已经会了？

你: Ch1 前两个会了，中间那个不重要

AI: 📐 课程架构预览
    Ch1 概率论基础
      ⚠ 样本空间 (你说会了，待验证)
      ○ 条件概率 Lv3
      ⊘ 随机变量 (已跳过)
    确认？输入 ok 进入教学。
```

### 日常学习

任何时候说"学习"，续上上次的课。

```
你: 学习

AI: 📍 工程统计学
    Ch3 中心极限定理 (practicing)
    上次答到 R3 卡住了，用工厂类比修复中。
    连续 5 天打卡。继续？
```

### 费曼追问

AI 讲一句 → 你用自己的话讲回来 → 五轮递进追问。

```
AI: [一句话讲完核心知识]

AI: 用你自己的话说，条件概率在干什么？

你: [复述]

AI: 偏了。你应该先区分条件概率和联合概率。
    再来——条件概率的分子和分母分别是什么？

—— 三次答不上 ——

AI: 你不是不懂条件概率，是你对联合概率的基础没打好。
    要不要回去补一下 Ch1 的联合概率？
```

### 随时换模式

```
你: 换模式

AI: 1. 讲解 — 我给你讲透你再讲回来
    2. 费曼 — 你讲我来挑刺  ← 推荐：这概念需要深究
    3. 苏格拉底 — 我问你走到结论
    4. 翻译 — 只关心你英文表达
    选哪个？
```

---

## 工作流

```
上传课件 → 自动拆课 → 概念过滤 → 🔴 确认架构
                                      ↓
                               进入教学循环
                                      ↓
                         ┌────────────┴────────────┐
                    讲解模式                   费曼模式
                  原文→解读→验证              讲解→追问(2-5轮)
                         ↓                          ↓
                    mastery=shallow           mastery=deep
                         ↓                          ↓
                         └──── 🔴 模式切换 ←────────┘
                                      ↓
                           苏格拉底 / 翻译
                       追问链 / 翻译→诊断
                                      ↓
                             卡壳? → 诊断→修复→重试
                             修复≥3次 → 强制放弃
                             全部轮次fail → 基础断崖
                                      ↓
                           Session 结束 → 6项复检
```

---

## 测试覆盖

| 场景 | 状态 |
|------|:----:|
| 费曼中间态（部分 pass 部分 fail）判定 | ✅ |
| 模式切换 mode_step 重置 + session_state 翻转 | ✅ |
| 卡壳修复天花板（repair≥3 强制放弃） | ✅ |
| 翻译模式无限循环防护 | ✅ |
| force_review 残留清理 | ✅ |
| mastery_depth 缺失检测 & 阻断 | ✅ |
| 四布尔互斥校验 | ✅ |
| shallow 守卫（讲解 mastered 切换费曼强制重来） | ✅ |
| already_know 快速验证幂等 | ✅ |
| 换模式推荐路由（8 种状态） | ✅ |

全部 10 条：[jiaocheng-tests.md](jiaocheng-tests.md)

---

## 文件结构

```
your-own-tutor/
├── SKILL.md              # skill 本体（12KB，单文件）
├── README.md             # 本文件
├── jiaocheng-tests.md    # 10 条自动化测试
└── LICENSE               # MIT
```

---

## 贡献

提 Issue 讨论改进方向，提 PR 直接改。修改后请对照 `jiaocheng-tests.md` 跑一遍 10 条测试，确保全绿。

---

## License

MIT © 2026 [jiangsir668](https://github.com/jiangsir668)


