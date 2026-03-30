---
title: QSI 3-Round AI Collaboration Process v2.1
note_type: process
framework: QSI
version: "2.1"
created: 2026-03-28
updated: 2026-03-28
source: Meta-analysis of 11 stocks
tags:
  - note/process
  - framework/qsi
  - multi-ai-collaboration
  - gemini
  - codex
---

# QSI 3-Round AI Collaboration Process v2.1

> Two-Way Evidence Check Pattern

---

## 📊 Meta-Analysis Results

| Metric | Value |
|--------|-------|
| Stocks Analyzed | 11 |
| Average Gemini Score | ~75 |
| Average Codex Score | ~65 |
| **Average Gap** | **~10 pts** |
| Convergence Rate | 90%+ |

---

## 🔄 Process Flow

### Round 1: Independent Analysis

```
┌─────────────────────────────────────────────────┐
│                PARALLEL EXECUTION                │
├─────────────────────────────────────────────────┤
│                                                  │
│   Gemini                    Codex                │
│   ───────                   ─────                │
│   • Web Search              • Logic Check        │
│   • Build Thesis            • Find Risks         │
│   • Optimistic View         • Skeptical View     │
│   • "What could go RIGHT?"  • "What could fail?" │
│                                                  │
│   Score A                   Score B              │
│   (~75 avg)                 (~65 avg)            │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Expected Gap:** 8-12 points (Gemini higher)

---

### Round 2: Two-Way Evidence Check ⭐ NEW

```
┌─────────────────────────────────────────────────┐
│              TWO-WAY VERIFICATION               │
├─────────────────────────────────────────────────┤
│                                                  │
│   Part A: Gemini → Codex's Concerns             │
│   ─────────────────────────────────             │
│   Codex raised:                                 │
│   1. "MOS 69.8% suspicious"                     │
│      → Gemini: "Here's source..."               │
│   2. "Gross margin only 8%"                     │
│      → Gemini: "Value-Added = 55% GP"           │
│                                                  │
│   Part B: Codex → Gemini's Claims               │
│   ─────────────────────────────────             │
│   Gemini claimed:                               │
│   1. "Value-Added margin ~15%"                  │
│      → Codex: [✅ Verified / ⚠️ Questioned]      │
│   2. "AI-PC refresh cycle"                      │
│      → Codex: [✅ Real tailwind / ❌ Hype]       │
│                                                  │
│   Part C: Score Adjustment                      │
│   ─────────────────────────                     │
│   | AI     | R1  | R2  | Delta |               │
│   |--------|-----|-----|-------|               │
│   | Gemini | 77  | 75  | -2    |               │
│   | Codex  | 67  | 72  | +5    |               │
│                                                  │
│   Gap: 10 → 3 (Converged ✅)                    │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Key Rules:**
- Codex adjusts UP when Gemini provides **verifiable primary sources**
- Codex holds when only **thesis without hard evidence**
- Gemini adjusts DOWN when Codex finds **structural flaws**

---

### Round 3: Synthesis (Claude)

```
┌─────────────────────────────────────────────────┐
│                  FINAL DECISION                  │
├─────────────────────────────────────────────────┤
│                                                  │
│   • Review both adjusted scores                 │
│   • Resolve remaining disputes                  │
│   • Weigh evidence quality                      │
│   • Final QSI + Action                          │
│                                                  │
│   Final Score = Weighted average or             │
│                  Judge's decision               │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## 🧠 Why Gemini Scores Higher

| Factor | Gemini Bias | Codex Bias | Delta |
|--------|-------------|------------|-------|
| Moat | Credits transformation | Demands evidence | +1-2 |
| Growth | Believes guidance | Questions sustainability | +1-2 |
| Catalyst | Sees tailwinds as positive | Sees as uncertain | +2-3 |
| Valuation | P/E < 10x = cheap | Also checks MOS validity | +2-3 |
| Sentiment | Scores high | Scores neutral | +1-2 |
| **Total** | | | **~10 pts** |

---

## 🎯 When Codex Adjusts Up

### ✅ Adjusts Up (Accepts Gemini's Evidence)
- Primary source confirms claim
- Financial statement data matches
- Industry trend is verifiable
- Management track record supports thesis

### ❌ Holds (Rejects Gemini's Thesis)
- Only forward-looking statements
- No primary source for key claim
- Logical inconsistency detected
- Sector/data mismatch in scanner

---

## 📋 Template: Round 2 Two-Way Check

```markdown
## Round 2: Two-Way Evidence Check

### Part A: Gemini → Codex's Concerns

| Codex Concern | Gemini Response | Evidence |
|---------------|-----------------|----------|
| MOS 69.8% suspicious | Gross margin improved | SET Factsheet |
| Sector mismatch | Confirmed Tech sector | SET classification |

### Part B: Codex → Gemini's Claims

| Gemini Claim | Codex Verification | Status |
|--------------|-------------------|--------|
| Value-Added = 55% GP | Found in annual report | ✅ Verified |
| Margin ~15% | Only found ~8% gross | ⚠️ Questioned |

### Part C: Score Adjustment

| AI | R1 Score | R2 Score | Delta | Reason |
|----|----------|----------|-------|--------|
| Gemini | 77 | 75 | -2 | Accepted sector risk |
| Codex | 67 | 72 | +5 | Verified Value-Added GP |

### Convergence Status
- Gap: 3 pts (target: ≤5)
- Status: ✅ Converged
```

---

## 🔗 Related Notes

- [[QSI Deep Dive Checklist]]
- [[Quality Swing Investor]]
- [[Stock Reviews MOC]]

---

*Created: 2026-03-28*
*Source: Meta-analysis of 11 stocks (BTG, AURA, MEGA, OSP, ADVANC, SAWAD, JAK, ONEE, AIT, SIS)*
