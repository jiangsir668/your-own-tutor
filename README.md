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
用户: 备课 [drops lecture notes]

→ Extract 12 PPTs → DNA → Profile → 13-ch dependency tree → Build Ch1

用户: 学习

→ 进度：Ch2「命题与论证」，2.1 论证结构
→ Ch1 已完成：1.1✅ 1.2✅ 1.3✅

教  论证不只是前提+结论。下面两段推理，谁的前提是什么？结论是什么？
    "今天会下雨，因为我看了天气预报。"
    "你该回家了。天已经黑了，而且你没吃饭。"
```

## The Pipeline · 流水线

```
PDF/PPT/Word → DNA Extract → Profile → Dependency Tree → Build Chapters → ⚡Teach→Ask→Compare→Verify→Judge
```

每个概念即教即验。不讲完整章再回头。

## What It Eats · 能吃

| PDF | PPT | Word |
|-----|-----|------|
| `pdftotext` + `pdftoppm` | LibreOffice → PDF | python-docx |

## The Rules · 十诫

1. 不跳过预检直接萃 · 2. 不用定义开场 · 3. 费曼不到位不诊断 · 4. 含混不放过 · 5. 讲不超10分无停点 · 6. 不跳反例上习题 · 7. 不用"大致""基本"带过 · 8. 不答非所问超两次不拉回 · 9. 不教完立刻亮答案 · 10. 不讲完整章再验

## Evolution · 进化纪

| 基线 32 | v2 74.6 | v3 78.3 | v4 81.1 | v5 84.0 | v9 87.1 | v10 90.6 | v14 90.8 |
|----------|---------|---------|---------|---------|---------|----------|----------|

> 认得字 ≠ 懂。过得了追问，才叫懂。

> 关掉重进？说「学习」就行。进度一分不丢。
