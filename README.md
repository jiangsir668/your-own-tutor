# 教程大师 · Jiaocheng

> 将资料一站式生成客制化教程。
> *Drop materials. Auto-generate personalized courses.*

---

## What · 何物

扔材料——PDF、PPT、Word。自动拆解，萃取脉络，按你的偏好织成课。每教一个概念不放过你：先让你用自己话说，再亮标准答案对照，费曼追身打到你再也不能含混其词。过不了，不准往下。

说「学习」随时续课。永远知道教到哪了。

*Drop materials — PDF, PPT, Word. Auto-extract. Six-stage pipeline. Every concept: first you say it in your own words. Then we compare against the answer. Then Feynman interrogation until you can't hide behind vagueness. No pass, no advance.*

*Say "学习" to resume anytime. Always knows exactly where you left off.*

## Install · 安装

```bash
mkdir -p .claude/skills/your-own-tutor
curl -o .claude/skills/your-own-tutor/SKILL.md \
  https://raw.githubusercontent.com/jiangsir668/your-own-tutor/main/SKILL.md
```

## In One Breath · 一镜到底

```
User: 备课 [drops lecture notes]

→ Extract 12 PPTs → DNA → Profile → 13-ch dependency tree → Build Ch1

User: 学习

→ 进度：Ch2「命题与论证」，2.1 论证结构 cleared
→ Ch1 已完成：1.1✅ 1.2✅ 1.3✅
→ 继续 Ch2.2 命题vs语句

教  "现在正在下雨"和"It is raining"——这是同一句话，还是两句话？
```

## The Pipeline · 流水线

```
PDF/PPT/Word → DNA Extract → Profile → Dependency Tree → Build Chapters → ⚡Teach→Ask→Compare→Verify→Judge
```

## What It Eats · 能吃

| PDF | PPT | Word |
|-----|-----|------|
| `pdftotext` + `pdftoppm` | LibreOffice → PDF | python-docx |

## Evolution · 进化纪

| 基线 32 | v2 74.6 | v3 78.3 | v4 81.1 | v5 84.0 | v9 87.1 | v10 90.6 | v17 90.8 |
|----------|---------|---------|---------|---------|---------|----------|----------|

> 认得字 ≠ 懂。过得了追问，才叫懂。
> 关掉重进？说「学习」就行。
