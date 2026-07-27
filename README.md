# 教程大师 · Jiaocheng

> 资料一站式生成客制化教程。
> *Drop materials. Auto-generate personalized courses.*

---

## What · 何物

扔材料——PDF、PPT、Word、视频。自动拆解，萃取脉络，按你的偏好织成课。每教一个概念不放过你：先让你用自己话说，再亮标准答案对照，费曼追身打到你再也不能含混其词。过不了，不准往下。

*Drop materials — PDF, PPT, Word, video. Auto-extract. Six-stage pipeline. Every concept: first you say it in your own words. Then we compare against the answer. Then Feynman interrogation until you can't hide behind vagueness. No pass, no advance.*

## Install · 安装

```bash
mkdir -p .claude/skills/jiaocheng
curl -o .claude/skills/jiaocheng/SKILL.md \
  https://raw.githubusercontent.com/jiangsir668/jiaocheng/main/SKILL.md
```

Say 「备课」 to build a course. Say 「教我」 to start learning.

## In One Breath · 一镜到底

```
User: 备课 [drops lecture notes] [throws video link]

→ Extract 12 PPTs + video catalog
→ Extract teaching DNA
→ Profile learner
→ Draw 13-chapter dependency tree
→ Build Ch1

User: 教我 Ch1

教  Socrates syllogism. A works. B doesn't. Why? You tell me.
问  User: "A works because of class inclusion."
对  Answer: validity = no world where premises true & conclusion false.
    You got inclusion. You missed why B fails.
验  Feynman: "If rain → wet. It rained. So wet." Where's inclusion?
    None. Yet valid. Your model breaks. Again.
判  ✅ Valid ≠ true conclusion. Inclusion is one form.
    ❌ Can't state the unified criterion. "Structure" is hollow.
    ↻ Reteach.
```

## The Pipeline · 流水线

```
PDF/PPT/Word/Video → DNA Extract → Profile → Dependency Tree → Build Chapters → ⚡Teach→Ask→Compare→Verify→Judge
```

每个概念即教即验。不讲完整章再回头。
*Every concept verified immediately. Never wait until chapter end.*

## The Rules · 十诫

1. 不跳过提取直接萃 · *Never skip extraction*
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

| 基线 32 | v2 74.6 | v3 78.3 | v4 81.1 | v5 84.0 |
|----------|---------|---------|---------|---------|

> 认得字 ≠ 懂。过得了追问，才叫懂。
> *Knowing the words ≠ knowing the thing. Survive the interrogation, then you know.*
