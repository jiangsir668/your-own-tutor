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
User: 学习

→ Globs progress.json
→ 进度报告：第2章「命题与论证」，概念 2.1 论证结构
→ 第1章已完成：1.1 有效性定义 ✅ 1.2 有效≠结论真 ✅ 1.3 逻辑研究形式 ✅
→ 总进度：▰▰░░░░░░░░░░ 1/13 章
→ 立即开教。

教  论证不只是前提+结论。下面这两段推理，谁的前提是什么？结论又是什么？
    ——"今天会下雨，因为我看了天气预报。"
    ——"你该回家了。天已经黑了，而且你没吃饭。"
    谁是谁的前提？谁是谁的结论？
```

## The Pipeline · 流水线

```
PDF/PPT/Word → DNA Extract → Profile → Dependency Tree → Build Chapters → ⚡Teach→Ask→Compare→Verify→Judge
```

每个概念即教即验。不讲完整章再回头。
*Every concept verified immediately. Never wait until chapter end.*

## What It Eats · 能吃

| PDF | PPT | Word |
|-----|-----|------|
| `pdftotext` + `pdftoppm` | LibreOffice → PDF | python-docx |

## The Rules · 十诫

1. 不跳过预检直接萃 · *Never skip preflight*
2. 不用定义开场 · *Never open with definitions*
3. 费曼追问不到底不出诊断 · *Never diagnose until interrogation exhausts*
4. 含混不放过 · *Never let vagueness slide*
5. 讲不超10分无停点 · *Never lecture >10min without pause*
6. 不跳反例上习题 · *Never skip counterexamples into exercises*
7. 不用"大致""基本"搪塞 · *Never accept "roughly" "basically" as answers*
8. 不答非所问超两次不拉回 · *Never let off-topic answers slide past two*
9. 不教完立刻亮答案——先让自陈 · *Never reveal answer before learner speaks*
10. 不讲完整章再验——每概念即教即验 · *Never verify entire chapter at once*

## Evolution · 进化纪

| 基线 32 | v2 74.6 | v3 78.3 | v4 81.1 | v5 84.0 | v9 87.1 | v10 90.6 | v13 91.3 |
|----------|---------|---------|---------|---------|---------|----------|----------|

> 认得字 ≠ 懂。过得了追问，才叫懂。
> *Knowing the words ≠ knowing the thing. Survive the interrogation, then you know.*

> 关掉重进？说「学习」就行。进度一分不丢。
> *Closed the app? Say "学习". Your progress is never lost.*
