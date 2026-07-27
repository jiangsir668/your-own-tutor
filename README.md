# 教程大师 · Jiaocheng

> 将资料一站式生成客制化教程。
> *Drop materials. Auto-generate personalized courses.*
> 说「学习」随时续课。Darwin 90.8分。

---

## What · 何物

扔材料——PDF、PPT、Word。自动拆解，萃取脉络，按你的偏好织成课。每教一个概念不放过你：先让你用自己话说，再亮标准答案对照，费曼追身打到你再也不能含混其词。过不了，不准往下。

*Drop materials — PDF, PPT, Word. Auto-extract. Six-stage pipeline. Every concept: first you explain in your own words. Then we compare against the answer. Then Feynman interrogation until you can't hide behind vagueness. No pass, no advance.*

说「学习」随时续课。永远知道教到哪了。
*Say "学习" to resume. Always knows exactly where you left off.*

## Install · 安装

```bash
mkdir -p .claude/skills/your-own-tutor
curl -o .claude/skills/your-own-tutor/SKILL.md \
  https://raw.githubusercontent.com/jiangsir668/your-own-tutor/main/SKILL.md
```

## The Pipeline · 流水线

```
PDF/PPT/Word → DNA → Profile → Dependency Tree → Build Chapters → ⚡Teach→Ask→Compare→Verify→Judge
```

每个概念即教即验。*Every concept verified immediately.*

## What It Eats · 能吃

| PDF | PPT | Word |
|-----|-----|------|
| `pdftotext` + `pdftoppm` | LibreOffice → PDF | python-docx |

## Evolution · 进化纪

| 基线 32 | v5 84.0 | v10 90.6 | v17 90.8 |
|----------|---------|----------|----------|

> 认得字 ≠ 懂。过得了追问，才叫懂。
> *Survive the interrogation, then you know.*
