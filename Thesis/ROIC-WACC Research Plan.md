# ROIC-WACC Research Plan

> **Goal:** วิจัยว่า ROIC-WACC spread ช่วย stock selection ได้จริงไหม
> **Approaches:** A (Quantitative) + B (Case Study)
> **Agents:** Codex, Gemini, Synapse-O (orchestrator)

---

## 📋 Phase 1: Research Topics Breakdown

### 🔬 Approach A: Quantitative Portfolio Test

| # | Topic | Agent | Deliverable |
|---|-------|-------|-------------|
| A1 | EVA/ROIC-WACC Literature Review | Gemini | Summary of academic evidence |
| A2 | SET Data Requirements & Methodology | Codex | Data template + calculation methodology |
| A3 | Portfolio Construction Framework | Gemini | Quintile strategy + rebalancing rules |
| A4 | Statistical Tests Design | Codex | Regression model + hypothesis tests |
| A5 | Risk-Adjustment Metrics | Gemini | Sharpe, Sortino, Max Drawdown framework |

### 🏢 Approach B: Case Study Analysis

| # | Topic | Agent | Deliverable |
|---|-------|-------|-------------|
| B1 | High Spread Companies Selection | Gemini | 5 SET stocks with sustained ROIC>WACC |
| B2 | Negative Spread Companies Selection | Codex | 5 SET stocks with sustained ROIC<WACC |
| B3 | Moat Analysis Framework | Gemini | What drives high ROIC? |
| B4 | Value Destruction Analysis | Codex | Why negative spread persists? |
| B5 | Market Pricing Analysis | Both | When does market misprice? |

---

## 🗓️ Phase 2: Execution Plan

### Week 1: Foundation

```
Day 1-2: Literature & Framework
├── [Gemini] A1: EVA Literature Review
│   └── Output: ทฤษฎี EVA, หลักฐานเชิงวิชาการ, ข้อโต้แย้ง
├── [Codex] A2: Data Methodology
│   └── Output: ROIC/WACC formula, adjustments needed, data sources
└── [Synapse-O] Consolidate → Obsidian Note

Day 3-4: Portfolio Framework
├── [Gemini] A3: Portfolio Construction
│   └── Output: Quintile rules, rebalancing, sector neutral?
├── [Codex] A4: Statistical Design
│   └── Output: Regression equations, control variables
└── [Synapse-O] Consolidate → Obsidian Note
```

### Week 2: Case Studies

```
Day 5-6: Company Selection
├── [Gemini] B1: High Spread Companies (5 stocks)
│   └── Output: Company profiles, 5Y ROIC-WACC history
├── [Codex] B2: Negative Spread Companies (5 stocks)
│   └── Output: Company profiles, why spread negative
└── [Synapse-O] Consolidate → Obsidian Note

Day 7-8: Deep Analysis
├── [Gemini] B3: Moat Analysis
│   └── Output: Competitive advantages, sustainability
├── [Codex] B4: Value Destruction
│   └── Output: Capital allocation issues, restructuring needs
└── [Synapse-O] Consolidate → Obsidian Note
```

### Week 3: Synthesis

```
Day 9-10: Cross-Analysis
├── [Both] B5: Market Pricing Patterns
│   └── Output: When does spread predict returns?
├── [Synapse-O] Final Synthesis
│   └── Output: Integrated findings, practical framework
└── [User] Review & Iterate
```

---

## 📝 Prompt Templates สำหรับแต่ละ Agent

### Gemini Prompts (Optimistic, Big Picture)

```
A1: EVA Literature Review
---
คุณเป็นนักวิจัยการเงิน ช่วยทำ literature review เรื่อง EVA (Economic Value Added)
และ ROIC-WACC spread สำหรับการเลือกหุ้น

ให้ครอบคลุม:
1. ที่มาของ EVA (Stewart, 1991)
2. หลักฐานเชิงวิชาการที่สนับสนุน
3. หลักฐานที่โต้แย้ง
4. ข้อจำกัดของ metric
5. การประยุกต์ใช้ในตลาด emerging markets

Format: Structured summary พร้อม citations

---

B1: High Spread Companies (SET)
---
ค้นหา 5 บริษัทใน SET ที่มี ROIC > WACC อย่างต่อเนื่อง 3+ ปี

สำหรับแต่ละบริษัท ให้ระบุ:
1. Ticker และชื่อบริษัท
2. Business model สั้นๆ
3. ประมาณ ROIC และ WACC (ถ้ามีข้อมูล)
4. อะไรขับเคลื่อน ROIC สูง
5. ความยั่งยืนของ competitive advantage

เน้น: บริษัทที่มี economic moat ชัดเจน
```

### Codex Prompts (Conservative, Detail-Oriented)

```
A2: Data Methodology
---
Design data collection methodology for ROIC-WACC analysis on SET stocks

Requirements:
1. ROIC calculation formula with necessary adjustments
2. WACC calculation (cost of equity, cost of debt, weights)
3. Data sources for Thai market
4. Handling of: negative earnings, cash holdings, leases
5. Time period: 10 years (2016-2025)

Output: Step-by-step methodology with formulas

---

B2: Negative Spread Companies (SET)
---
Identify 5 SET companies with sustained ROIC < WACC (value destruction)

For each company:
1. Ticker and company name
2. Why ROIC is low (commoditized business? high capex? poor allocation?)
3. Why WACC is high (leverage? beta? distressed?)
4. Management response (restructuring? ignored?)
5. Market valuation vs intrinsic (trading at discount?)

Focus: Companies where market may be mispricing recovery potential
```

---

## 📂 Output Structure

```
BF-Vault/Thesis/
├── ROIC-WACC Research Design.md       ← Framework
├── ROIC-WACC Research Plan.md         ← This file
├── A-Quantitative/
│   ├── A1-EVA-Literature-Review.md    ← Gemini
│   ├── A2-Data-Methodology.md         ← Codex
│   ├── A3-Portfolio-Construction.md   ← Gemini
│   ├── A4-Statistical-Design.md       ← Codex
│   └── A5-Risk-Metrics.md             ← Gemini
├── B-Case-Study/
│   ├── B1-High-Spread-Companies.md    ← Gemini
│   ├── B2-Negative-Spread-Companies.md ← Codex
│   ├── B3-Moat-Analysis.md            ← Gemini
│   ├── B4-Value-Destruction.md        ← Codex
│   └── B5-Market-Pricing.md           ← Both
└── Synthesis/
    └── ROIC-WACC-Final-Findings.md    ← Synapse-O
```

---

## ✅ Checkpoint Points

| Checkpoint | When | Review |
|------------|------|--------|
| CP1 | After A1, A2 | Literature & Methodology OK? |
| CP2 | After A3, A4 | Portfolio design sound? |
| CP3 | After B1, B2 | Company selection appropriate? |
| CP4 | After B3, B4 | Analysis depth sufficient? |
| CP5 | Final | Ready to synthesize? |

---

## 🎯 Success Criteria

- [ ] Literature covers both support & criticism
- [ ] Methodology handles edge cases (negative earnings, etc.)
- [ ] 10 case study companies with complete profiles
- [ ] Clear patterns identified (when does it work/fail?)
- [ ] Practical framework for stock selection

---

*Created: 2026-04-01*
*Status: Pending Review*
