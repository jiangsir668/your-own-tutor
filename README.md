# Your Own Tutor &middot; [![Version](https://img.shields.io/badge/v6.8-A-blue)](https://github.com/jiangsir668/your-own-tutor) [![Tests](https://img.shields.io/badge/tests-10%2F10-green)](https://github.com/jiangsir668/your-own-tutor/blob/main/jiaocheng-tests.md) [![Darwin](https://img.shields.io/badge/darwin-A-brightgreen)](https://github.com/jiangsir668/your-own-tutor) [![License](https://img.shields.io/badge/license-MIT-lightgrey)](LICENSE) [![Lang](https://img.shields.io/badge/lang-中文_|_EN-blue)]()

<p align="center">
  <b>Upload a textbook. The AI makes you teach it back.</b><br>
  上传课件 → 你来讲给 AI 听 → 答不上来诊断根因 → 跨会话追踪<br>
  <em>Lecture · Feynman · Socratic · Translation — 4 modes, bilingual, battle-tested.</em>
</p>

---

## Why This Exists

ChatGPT explains. **Your Own Tutor interrogates.**

Based on the Feynman Technique — the single most effective learning method ever studied. If you can't explain it clearly, you don't understand it. This skill makes you explain. Every fuzzy sentence, every hand-waved concept, every "I think I get it" — gets challenged. For 2-5 rounds. Until you actually own the concept.

It remembers where you left off. It knows what you got wrong. It schedules spiral reviews. It syncs to Obsidian. It speaks your language — literally, message by message.

---

## What It Does

<div align="center">

| Feature | Generic AI | Your Own Tutor |
|---------|:---:|:---:|
| Explain a concept | ✅ | ✅ |
| Make YOU explain it back | ❌ | ✅ **Feynman Drill (2-5 rounds)** |
| Diagnose WHY you're stuck | ❌ | ✅ **5 fault types + 4 repair strategies** |
| Cross-session memory | ❌ | ✅ Say "learn" — picks up where you stopped |
| Spiral review + error log | ❌ | ✅ Auto-scheduled, force-cleared when overflow |
| Sync to Obsidian | ❌ | ✅ Notes + errors auto-written to your Vault |
| Switch teaching style on demand | ❌ | ✅ **4 modes, instant switch** |
| Bilingual, per-message | ❌ | ✅ Detects language of each message |
| Self-audit at session end | ❌ | ✅ **6 invariant checks** — blocks corrupt data |

</div>

---

## Four Teaching Modes

### 🎙️ Lecture — "I explain, you explain back"
Best for first contact. AI outputs the original text verbatim → plain-language breakdown → 1-2 round Feynman check. `mastery_depth = shallow`.

### 🔥 Feynman — "YOU teach, I critique" *(default)*
Best for real understanding. AI gives you the core concept in one breath. Then: R1 "Explain in your own words" → R2 "What if conditions change?" → R3 "When does it fail?" → R4 "How does it connect to X?" → R5 "What are the limits?" Stuck? Diagnosed (concept gap? reasoning flaw? prerequisite missing?) → repaired → retried. **All rounds fail → "Foundation cliff" → go back to prerequisites.** `mastery_depth = deep`.

### 🔮 Socratic — "I only ask, you reach the conclusion"
Best for critical thinking. 5-question chain. Each answer is challenged. You revise your own framework until it holds.

### 🌐 Translation — "I only care if you can express it"
Best for academic English. Original → your translation → 3-axis diagnosis (accuracy / syntax / style) → reference translation → you explain the gap.

---

## Quick Start

```bash
npx skills add jiangsir668/your-own-tutor
```

| Trigger (中文) | Trigger (EN) | Action |
|---|---|---|
| `备课` / `teach` | Upload + build course | PPT/PDF/DOCX → auto-extract → self-assess → 🔴 confirm |
| `学习` / `learn` | Resume learning | Reports progress + picks up mid-drill |
| `继续` / `continue` | Continue | Same as above |
| `讲一下` / `explain` | Explain concept | Lecture mode |
| `换模式` / `switch mode` | Switch teaching mode | Lists 4 modes + recommends best + 🔴 waits |

---

```
You: "learn"

AI: 📍 Engineering Statistics
    Ch3 Central Limit Theorem (practicing)
    Stuck at R3 — repairing with factory analogy.
    5-day streak. Continue?

You: "switch mode"

AI: 1. Lecture — I explain thoroughly, you explain back
    2. Feynman — YOU teach, I critique  ← Recommended: needs deep drill
    3. Socratic — I only ask, you conclude
    4. Translation — I only care if you can express it
    Which one?

You: "This material is in English. Would you like to learn in English or Chinese?"
```

---

## Quality

- **10/10 automated tests** — Feynman mid-states, mode switching, repair ceiling, invariants
- **3 rounds multi-agent audits** — zero HIGH conflicts remaining
- **6 invariant checks** at every session end — blocks corrupt state
- **Darwin Score: A** (87%+) — audited by independent scoring agents
- **Bilingual, per-message** — character-count arbitration for mixed input

---

## Files

```
your-own-tutor/
├── SKILL.md              # 10.7KB, self-contained skill
├── README.md             # This file
├── jiaocheng-tests.md    # 10 automated tests
└── LICENSE               # MIT
```

---

## Contribute

Issues & PRs welcome. Run `jiaocheng-tests.md` after any change — all 10 must pass.

---

## License

MIT © 2026 [jiangsir668](https://github.com/jiangsir668)

---

<p align="center">
  <sub>Built with Darwin Skill Optimizer. Audited by multi-agent adversarial review.</sub>
</p>