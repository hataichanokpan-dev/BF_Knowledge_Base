# ROIC-WACC Practical Framework — คู่มือปฏิบัติการลงทุน

> **Mission:** เปลี่ยนงานวิจัยให้เป็นเครื่องมือตัดสินใจลงทุน
> **For:** [[Quality Swing Investor]] | Thai Stock Market (SET)
> **Version:** 1.0 | 2026-04-01

---

## 📋 Executive Summary (2 หน้า)

### หัวใจสำคัญ

> [!tip] ใน 1 นาที
> **ROIC > WACC = Value Creation** → ซื้อ
> **ROIC < WACC = Value Destruction** → หลีกเลี่ยง
> **ความลับ:** ตลาดใช้เวลา 6-24 เดือนกว่าจะ price in เปลี่ยนแปลง

### Framework ใน 4 ขั้นตอน

```
┌─────────────────────────────────────────────────────────────────┐
│                    ROIC-WACC INVESTMENT PROCESS                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  STEP 1: CALCULATE ────► STEP 2: VALIDATE ────► STEP 3: PRICE   │
│  (ROIC - WACC)           (Moat Check)           (Fair Value)     │
│                                                                  │
│                              ▼                                   │
│                                                                  │
│                    STEP 4: DECIDE                                │
│                    (Buy/Hold/Sell)                               │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### ตัวเลขสำคัญที่ต้องจำ

| Metric | Good | Warning | Danger |
|--------|------|---------|--------|
| **ROIC - WACC** | > 5% | 1-5% | < 1% |
| **5Y Persistence** | 4+ ปี | 2-3 ปี | < 2 ปี |
| **D/E Ratio** | < 1x | 1-2x | > 2x |
| **Interest Coverage** | > 8x | 4-8x | < 4x |
| **FCF Conversion** | > 80% | 50-80% | < 50% |

---

## 🔧 PART 1: Quick Reference Cards

### Card 1: ROIC Calculation Checklist

> [!info] สูตรมาตรฐาน (Damodaran Method)

```
ROIC = NOPAT / Invested Capital

where:
NOPAT = EBIT × (1 - Tax Rate)
Invested Capital = Total Equity + Total Debt - Cash
```

#### Step-by-Step Calculation

```
□ 1. EBIT (Operating Income)
    └─ Source: Income Statement
    └─ Adjust: + Depreciation (ถ้าถูกหักออก)
    └─ Adjust: - Non-recurring items

□ 2. Tax Rate
    └─ Use: Effective Tax Rate (5Y average)
    └─ Thailand: 20% statutory
    └─ SET Average: 15-18%

□ 3. NOPAT = EBIT × (1 - Tax Rate)

□ 4. Invested Capital
    └─ Total Equity (Book Value)
    └─ + Interest-bearing Debt (Short + Long)
    └─ - Cash & Equivalents
    └─ - Excess Cash (ถ้า > 10% revenue)

□ 5. ROIC = NOPAT / Average Invested Capital
    └─ Use: (Beginning + Ending) / 2
```

#### Thai Market Adjustments

| Item | Adjustment | เหตุผล |
|------|------------|--------|
| **Goodwill** | ตรวจสอบ impairment | Thai GAAP ต่างจาก IFRS |
| **RPT Assets** | หักออกถ้า overpaid | [[Related Party Transactions]] |
| **Land Revaluation** | ใช้ book value | Revaluation bias |
| **Operating Leases** | Capitalize ถ้า material | ASC 842 equivalent |

---

### Card 2: WACC Estimation (Thai Market)

```
WACC = (E/V × Ke) + (D/V × Kd × (1 - T))

where:
E = Market Cap
D = Total Debt
V = E + D
Ke = Cost of Equity (CAPM)
Kd = Cost of Debt (YTM or Interest Expense / Total Debt)
T = Tax Rate
```

#### Cost of Equity (CAPM for Thailand)

```
Ke = Rf + β × (Rm - Rf) + CRP

where:
Rf = Thai 10Y Government Bond (~2.5-3%)
β = Stock Beta (vs SET Index)
Rm - Rf = Thailand Equity Risk Premium (~6-7%)
CRP = Country Risk Premium (~2-3%)
```

> [!tip] Thailand-Specific Numbers
> - **Risk-free Rate:** 2.5-3.0% (Thai 10Y Bond)
> - **Market Risk Premium:** 6-7%
> - **Country Risk Premium:** 2-3%
> - **Implied ERP (Damodaran):** ~8.5% for Thailand

#### Quick WACC Table (Thai Market)

| Sector | Beta | WACC Range |
|--------|------|------------|
| Banks | 0.8-1.0 | 8-10% |
| Energy | 1.0-1.2 | 10-12% |
| Industrials | 0.9-1.1 | 9-11% |
| Consumer | 0.7-0.9 | 8-10% |
| Technology | 1.2-1.5 | 11-14% |
| Property | 1.0-1.3 | 10-13% |

---

### Card 3: Moat Identification Flowchart

```
                    ┌─────────────────────┐
                    │  Does company have  │
                    │   Economic Moat?    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              ▼                ▼                ▼
        ┌─────────┐      ┌─────────┐      ┌─────────┐
        │  ROIC   │      │ Margin  │      │ Market  │
        │ > 15%?  │      │ Trend?  │      │ Share?  │
        └────┬────┘      └────┬────┘      └────┬────┘
             │                │                │
      ┌──────┴──────┐  ┌──────┴──────┐  ┌──────┴──────┐
      Yes         No   Stable      Declining  Stable   Declining
      │            │    │            │         │         │
      ▼            ▼    ▼            ▼         ▼         ▼
   Moat?       No     Likely      No       Moat?      No
   Likely      Moat   Moat        Moat     Likely     Moat
      │
   ┌──┴──────────────────────────────────────────────────┐
   │               MOAT TYPE IDENTIFICATION               │
   ├─────────────────────────────────────────────────────┤
   │                                                      │
   │  Q1: ลูกค้าย้ายค่อยยากไหม? ──Yes──► SWITCHING COSTS   │
   │                                                      │
   │  Q2: มีแบรนด์/พัฒนาล่าช้าไหม? ──Yes──► INTANGIBLE ASSETS │
   │                                                      │
   │  Q3: ต้นทุนต่ำกว่าคู่แข่งไหม? ──Yes──► COST ADVANTAGE    │
   │                                                      │
   │  Q4: ใช้ยิ่งมากยิ่งคุ้มไหม? ──Yes──► NETWORK EFFECT     │
   │                                                      │
   │  Q5: ตลาดเล็ก ผู้เล่นน้อยไหม? ──Yes──► EFFICIENT SCALE  │
   │                                                      │
   └─────────────────────────────────────────────────────┘
```

#### Moat Scorecard (100 points)

| Factor | Weight | Score 0-5 | Points |
|--------|--------|-----------|--------|
| **ROIC-WACC Spread** | 25% | × 5 | ___/25 |
| **Margin Stability** | 20% | × 4 | ___/20 |
| **Excess Return Persistence** | 20% | × 4 | ___/20 |
| **FCF Conversion** | 15% | × 3 | ___/15 |
| **Capital Discipline** | 20% | × 4 | ___/20 |
| **TOTAL** | 100% | | **___/100** |

> [!tip] Interpretation
> - **80+ points:** Wide Moat
> - **60-79 points:** Narrow Moat
> - **< 60 points:** No Moat

---

### Card 4: Value Trap Detection Matrix

```
┌─────────────────────────────────────────────────────────────────┐
│                    VALUE TRAP DETECTION MATRIX                   │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│  Category         │ Red Flags                    │ Score        │
│  ─────────────────┼──────────────────────────────┼──────────────│
│                                                                  │
│  STRUCTURAL       │ □ No clear moat              │ +15 each     │
│                   │ □ Commodity business         │              │
│                   │ □ Price taker, not maker     │              │
│                   │ □ Disruption risk            │              │
│  ─────────────────┼──────────────────────────────┼──────────────│
│                                                                  │
│  BEHAVIORAL       │ □ Empire building (M&A)      │ +20 each     │
│                   │ □ Poor capital allocation    │              │
│                   │ □ Related party issues       │              │
│                   │ □ Governance concerns        │              │
│  ─────────────────┼──────────────────────────────┼──────────────│
│                                                                  │
│  CYCLICAL         │ □ Industry downturn          │ +10 each     │
│                   │ □ Commodity price collapse   │              │
│                   │ □ Demand cycle               │              │
│                   │ □ But moat intact            │              │
│                                                                  │
├─────────────────────────────────────────────────────────────────┤
│  SCORING: 0-30 = OK | 30-50 = CAUTION | 50+ = AVOID             │
└─────────────────────────────────────────────────────────────────┘
```

#### Financial Warning Signs

| Statement | Metric | Warning | Danger |
|-----------|--------|---------|--------|
| **Income** | Revenue Growth | < GDP | Negative |
| | EBITDA Margin | Declining > 2%/yr | < 10% |
| | Non-recurring items | > 10% EBIT | > 25% EBIT |
| **Balance** | D/E Ratio | > 1.5x | > 2.5x |
| | Net Debt/EBITDA | > 3x | > 4x |
| | Goodwill/Equity | > 30% | > 50% |
| **Cash Flow** | FCF Conversion | < 60% | < 30% |
| | Capex/Sales | Rising, ROIC falling | > 15% |
| | Working Capital | Rising faster than sales | Negative trend |

---

## 🌳 PART 2: Decision Trees

### Decision Tree 1: Buy/Hold/Sell

```
                         ┌─────────────────┐
                         │  CURRENT SPREAD │
                         │   (ROIC-WACC)   │
                         └────────┬────────┘
                                  │
         ┌────────────────────────┼────────────────────────┐
         ▼                        ▼                        ▼
    ┌─────────┐              ┌─────────┐              ┌─────────┐
    │ > 5%    │              │ 1-5%    │              │ < 1%    │
    └────┬────┘              └────┬────┘              └────┬────┘
         │                        │                        │
         ▼                        ▼                        ▼
    ┌─────────┐              ┌─────────┐              ┌─────────┐
    │ Moat    │              │ Moat    │              │ Value   │
    │ Score?  │              │ Score?  │              │ Trap?   │
    └────┬────┘              └────┬────┘              └────┬────┘
         │                        │                        │
    ┌────┴────┐              ┌────┴────┐              ┌────┴────┐
    ▼         ▼              ▼         ▼              ▼         ▼
  Wide      Narrow         Wide     Narrow          Yes       No
    │         │              │         │              │         │
    ▼         ▼              ▼         ▼              ▼         ▼
┌───────┐ ┌───────┐    ┌───────┐ ┌───────┐    ┌───────┐ ┌───────┐
│Check  │ │Check  │    │Check  │ │Hold/  │    │SELL   │ │HOLD   │
│Price  │ │Price  │    │Price  │ │Watch  │    │       │ │Watch  │
└───┬───┘ └───┬───┘    └───┬───┘ └───────┘    │       │ │closely│
    │         │            │                  │       │ └───────┘
    ▼         ▼            ▼                  │       │
┌───────┐ ┌───────┐    ┌───────┐              │       │
│P/FV   │ │P/FV   │    │P/FV   │              │       │
│< 0.8? │ │< 0.9? │    │< 0.9? │              │       │
└───┬───┘ └───┬───┘    └───┬───┘              │       │
    │         │            │                  │       │
    ▼         ▼            ▼                  │       │
  BUY       HOLD         BUY                 │       │
```

### Decision Tree 2: Cyclical vs Structural

```
                    ┌─────────────────────────────┐
                    │  SPREAD DECLINED            │
                    │  Is it Cyclical or          │
                    │  Structural?                │
                    └──────────────┬──────────────┘
                                   │
                    ┌──────────────┼──────────────┐
                    ▼              ▼              ▼
              ┌──────────┐  ┌──────────┐  ┌──────────┐
              │ Q1: Is   │  │ Q2: Is   │  │ Q3: Is   │
              │ Industry │  │ Company  │  │ Moat     │
              │ Cyclical │  │ Specific │  │ Intact?  │
              │ Overall? │  │ Issue?   │  │          │
              └────┬─────┘  └────┬─────┘  └────┬─────┘
                   │             │             │
         ┌─────────┴───┐    ┌────┴────┐   ┌────┴────┐
         ▼             ▼    ▼         ▼   ▼         ▼
        Yes           No   Yes       No  Yes       No
         │             │    │         │   │         │
         ▼             │    ▼         │   ▼         ▼
    ┌─────────┐        │  COMPANY  ───┘  MOAT     STRUCTURAL
    │ Q2: Is  │        │  SPECIFIC      INTACT    ISSUE
    │ Company │        │                │         │
    │ Worse   │        │                │         │
    │ Than    │        │                │         │
    │ Peers?  │        │                │         │
    └────┬────┘        │                │         │
         │             │                │         │
    ┌────┴────┐        │                │         │
    ▼         ▼        │                │         │
   Yes       No        │                │         │
    │         │        │                │         │
    ▼         ▼        ▼                ▼         ▼
 COMPANY   CYCLICAL   HOLD/            POTENTIAL  SELL/
 SPECIFIC  (Industry  AVOID            RECOVERY   AVOID
 ISSUE     Downturn)                   CANDIDATE
```

#### 3-Question Tree Summary

| Q1: Industry Cyclical? | Q2: Company-Specific? | Q3: Moat Intact? | Verdict |
|------------------------|----------------------|------------------|---------|
| Yes | No | Yes | **Cyclical** (potential buy) |
| Yes | No | No | **Structural** (avoid) |
| Yes | Yes | Yes | **Company Issue** (deep dive) |
| Yes | Yes | No | **Structural** (avoid) |
| No | Yes | Yes | **Company Issue** (deep dive) |
| No | Yes | No | **Structural** (avoid) |
| No | No | - | **N/A** (no decline) |

---

## 🔍 PART 3: Screening Templates

### Template 1: Quality Screen

```yaml
# ROIC-WACC Quality Screen (SET 100)

STEP 1: Spread Filter
─────────────────────
- ROIC - WACC > 3% (absolute)
- OR Spread vs Sector: Top 30%
- Expected Output: 30-40 stocks

STEP 2: Persistence Filter
──────────────────────────
- Positive spread 3+ consecutive years
- Trend: Current > 3Y average
- Expected Output: 15-20 stocks

STEP 3: Valuation Filter
────────────────────────
- P/E vs Sector < 1.0x
- EV/EBITDA vs Sector < 1.0x
- P/Fair Value < 0.9
- Expected Output: 8-12 stocks

STEP 4: Quality Filter
──────────────────────
- Debt/EBITDA < 3.0x
- Interest Coverage > 5.0x
- Earnings Stability: StdDev < 20%
- Expected Output: 5-8 stocks
```

### Template 2: Value Screen (Turnaround)

```yaml
# Value Turnaround Screen

STEP 1: Spread Recovery Candidates
──────────────────────────────────
- Current spread: 0-2%
- Prior spread (3Y ago): > 4%
- Or: Spread trending up 2+ consecutive years
- Expected Output: 20-30 stocks

STEP 2: Solvency Check
──────────────────────
- D/E < 2x
- Interest Coverage > 3x
- No debt covenant violations
- Expected Output: 10-15 stocks

STEP 3: Moat Intact
───────────────────
- Still has competitive advantages
- Market share stable
- No structural disruption
- Expected Output: 5-8 stocks

STEP 4: Valuation Cushion
─────────────────────────
- P/TBV < 1.5x
- P/Normalized Earnings < 12x
- Expected Output: 3-5 stocks
```

### Template 3: Avoid Screen

```yaml
# Value Trap Avoidance Screen

RED FLAGS (Any = PASS to avoid)
───────────────────────────────
□ ROIC < WACC 3+ consecutive years
□ D/E > 2.5x
□ Interest Coverage < 2x
□ Negative FCF 2+ years
□ Significant related party transactions
□ Governance score: Bottom quartile
□ Auditor: Non-Big 4 or qualified opinion
□ Management turnover: High (3+ changes in 2 years)
□ Significant goodwill impairment
□ Litigation or regulatory issues

Expected Output: 20-30 stocks to AVOID
```

---

## 🇹🇭 PART 4: Thai Market Adaptations

### SET-Specific Considerations

| Factor | Thai Market Reality | Adaptation |
|--------|---------------------|------------|
| **Data Quality** | Restatements common | Use 5Y median |
| **WACC** | Higher risk premium | Add 2-3% CRP |
| **Liquidity** | Concentrated in top 50 | Focus SET 50-100 |
| **Sector Mix** | Heavy in Banks, Energy | Sector-relative comparison |
| **Family Control** | 70%+ family-owned | Check [[Related Party Transactions]] |
| **Governance** | Variable quality | Add governance screen |

### Thai Market Red Flags

> [!danger] ต้องระวังเป็นพิเศษ

| Red Flag | คำอธิบาย | การตรวจสอบ |
|----------|----------|------------|
| **[[Related Party Transactions]]** | ทำธุรกรรมกับบริษัทในเครือ | Footnotes, 56-1 |
| **Land Revaluation** | ปรับประเมินที่ดินเพิ่ม | Balance sheet, Notes |
| **Goodwill from M&A** | ซื้อกิจการราคาสูง | Impairment history |
| **Insider Selling** | ผู้บริหารขายหุ้น | SET announcements |
| **Auditor Rotation** | เปลี่ยน auditor บ่อย | 56-1, governance report |
| **Complex Structure** | โครงสร้างซับซ้อน | Org chart, subsidiaries |

### Governance Quick Check

```
□ Board Independence: > 40%
□ Audit Committee: Independent chair
□ Related Party Policy: Clear & disclosed
□ Voting Structure: 1 share = 1 vote
□ Dividend Policy: Consistent
□ Investor Relations: Responsive
□ SET CG Score: > 70 (if available)
```

---

## 📊 PART 5: Portfolio Construction

### Position Sizing

| Conviction | Criteria | Position |
|------------|----------|----------|
| **High** | 5%+ spread, 5Y persistence, catalyst | 5-8% |
| **Medium** | 3-5% spread, 3Y persistence | 3-5% |
| **Speculative** | Improving but unproven | 1-3% |

### Portfolio Constraints

```
Max single position: 10%
Max sector exposure: 30%
Min positions: 10 stocks
Max positions: 25 stocks
Cash buffer: 5-10%
```

### Rebalancing Rules

| Trigger | Action |
|---------|--------|
| **Price > Fair Value 20%** | Trim 50% of position |
| **Price > Fair Value 35%** | Sell all |
| **Spread < 1%** | Review for exit |
| **Spread negative 2Q** | Exit |
| **Thesis broken** | Exit immediately |

---

## 📝 PART 6: Research Workflow

### Pre-Investment Checklist

```
□ STEP 1: Quantitative Screen
  └─ Run quality/value screen
  └─ Output: 10-15 candidates

□ STEP 2: ROIC-WACC Calculation
  └─ Calculate 5Y spread history
  └─ Verify data quality
  └─ Output: 5-8 candidates

□ STEP 3: Moat Analysis
  └─ Identify moat type
  └─ Score moat (0-100)
  └─ Check sustainability
  └─ Output: 3-5 candidates

□ STEP 4: Valuation
  └─ DCF with spread assumptions
  └─ Relative valuation vs sector
  └─ Margin of safety check
  └─ Output: 2-3 candidates

□ STEP 5: Deep Dive
  └─ Management quality
  └─ Governance check
  └─ Catalyst identification
  └─ Risk assessment
  └─ Output: 1-2 positions

□ STEP 6: Decision
  └─ Position sizing
  └─ Entry price
  └─ Exit rules
  └─ Monitoring plan
```

### Ongoing Monitoring

| Frequency | Check |
|-----------|-------|
| **Quarterly** | Earnings, spread update |
| **Semi-annually** | Moat reassessment, valuation |
| **Annually** | Full thesis review |
| **As needed** | Material announcements |

---

## 🔗 Related Notes

### Foundation Research
- [[A1-EVA-Literature-Review]] — พื้นฐานทางวิชาการ EVA
- [[A2-Data-Methodology]] — วิธีการคำนวณ ROIC-WACC

### Case Studies
- [[B1-High-Spread-Companies]] — บริษัทที่สร้างมูลค่า
- [[B2-Negative-Spread-Companies]] — บริษัททำลายมูลค่า

### Synthesis
- [[B3-Moat-Analysis-Framework]] — การวิเคราะห์คูเศรษฐกิจ
- [[B4-Value-Destruction-Analysis]] — การตรวจจับ value trap
- [[B5-Market-Pricing-Patterns]] — รูปแบบการตั้งราคาของตลาด

### Investment Philosophy
- [[ROIC-WACC Research Design]] — กรอบงานวิจัย
- [[Quality Swing Investor]] — ปรัชญาการลงทุน
- [[Valuation Discipline]] — วินัยการประเมินราคา

### Supporting Concepts
- [[Economic Moat]] — คูเศรษฐกิจ
- [[Value Creation]] — การสร้างมูลค่า
- [[Value Trap]] — กับดักมูลค่า
- [[Growth Trap]] — กับดักการเติบโต
- [[Quality at Reasonable Price]] — QARP strategy
- [[Capital Allocation]] — การจัดสรรเงินทุน
- [[Related Party Transactions]] — ธุรกรรมที่เกี่ยวข้อง

---

## 📚 Sources

### Academic
- Ohlson (1995), Feltham-Ohlson (1995) — Residual Income Model
- Frankel & Lee (1998) — Predictive Power
- Novy-Marx (2013) — Profitability Factor
- Lakonishok, Shleifer, Vishny (1994) — Growth Trap

### Practitioner
- Damodaran — ROIC & Valuation
- Mauboussin — Mean Reversion
- Morningstar — Moat Framework
- AQR (Asness et al.) — Quality Factor

---

*Framework Version: 1.0*
*Created: 2026-04-01*
*Research: Gemini + Codex + Synapse-O*
*Language: Thai with English terms*
