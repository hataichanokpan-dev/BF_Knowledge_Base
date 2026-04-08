# B4: Value Destruction Analysis — ทำไมบางบริษัททำลายมูลค่าอย่างต่อเนื่อง?

> **Research Question:** อะไรคือสาเหตุของ Value Destruction (ROIC < WACC) อย่างต่อเนื่อง และจะตรวจจับได้อย่างไร?
> **Source:** Research Synthesis + B2 Case Studies
> **Date:** 2026-04-01

---

## 📊 Executive Summary

> [!danger] Core Thesis
> **Value Destruction ไม่ได้เกิดจากความบังเอิญ** — เกิดจากโครงสร้างธุรกิจ การบริหารเงินทุน และการตัดสินใจของผู้บริหาร
>
> Negative Spread (ROIC < WACC) ต่อเนื่อง = **โครงสร้างพื้นฐานผิดปกติ** ไม่ใช่ระยะชั่วคราว

---

## 1. Value Destruction Taxonomy

### 1.1 Root Causes Hierarchy

```
┌─────────────────────────────────────────────────────────────────┐
│                  VALUE DESTRUCTION ROOT CAUSES                   │
└─────────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  STRUCTURAL   │    │  BEHAVIORAL   │    │   CYCLICAL    │
│  (Business)   │    │ (Management)  │    │  (Industry)   │
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                    │                    │
   ┌────┴────┐          ┌────┴────┐          ┌────┴────┐
   │         │          │         │          │         │
   ▼         ▼          ▼         ▼          ▼         ▼
┌─────┐  ┌─────┐   ┌─────┐  ┌─────┐   ┌─────┐  ┌─────┐
│No   │  │High │   │Empire│  │Poor  │   │Comp-│  │Macro│
│Moat │  │Fixed│   │Build │  │M&A   │   │ress-│  │Shock│
│     │  │Cost │   │      │  │      │   │ion  │  │     │
└─────┘  └─────┘   └─────┘  └─────┘   └─────┘  └─────┘
```

### 1.2 Structural Causes (ธุรกิจโครงสร้างแย่)

| สาเหตุ | คำอธิบาย | ตัวอย่างจาก B2 |
|--------|----------|----------------|
| **[[No Economic Moat]]** | ไม่มี competitive advantage ที่ปกป้องจากการแข่งขัน | IRPC (commodity refinery) |
| **[[Commodity Trap]]** | ขายสินค้าที่แทบไม่ต่างจากคู่แข่ง ต้องแข่งราคา | IRPC, SCC (chemicals) |
| **[[High Fixed Cost Structure]]** | ต้นทุนคงที่สูง ยืดหยุ่นยาก เมื่อ demand ลด กำไรหาย | AAV (airlines), IRPC |
| **[[Capital Intensity]]** | ต้องลงทุนมหาศาล แต่ผลตอบแทนต่ำ | THCOM (satellite), SCC |
| **[[Technology Disruption]]** | ธุรกิจถูกคุกคามโดยเทคโนโลยีใหม่ | THCOM (satellite vs fiber/5G) |

### 1.3 Behavioral Causes (พฤติกรรมผู้บริหาร)

| สาเหตุ | คำอธิบาย | Warning Signs |
|--------|----------|---------------|
| **[[Empire Building]]** | เติบโตเพื่อขนาด ไม่ใช่เพื่อกำไร | M&A หลายครั้ง, Revenue โตแต่ ROIC ลด |
| **[[Poor M&A]]** |ซื้อบริษัทแพงเกินไป หรือซื้อธุรกิจที่ไม่เกี่ยวข้อง | Goodwill impairment, Integration issues |
| **[[Overinvestment]]** | ลงทุนต่อแม้ ROIC < WACC | Capex > OCF ต่อเนื่อง |
| **[[Denial]]** | ไม่ยอมรับว่าธุรกิจเปลี่ยน ดำเินการตามเดิม | "Cycle จะกลับมา" แต่ไม่มีทีท่า |
| **[[Agency Problem]]** | ผู้บริหารทำเพื่อตัวเอง ไม่ใช่ผู้ถือหุ้น | Related party transactions, Perks |

### 1.4 Cyclical Causes (วัฏจักรอุตสาหกรรม)

| สาเหตุ | คำอธิบาย | Recovery Condition |
|--------|----------|-------------------|
| **[[Industry Downcycle]]** | อุตสาหกรรมอยู่ในช่วงตกต่ำ | ต้องรอ cycle กลับ |
| **[[Oversupply]]** | กำลังการผลิตเกินความต้องการ | ต้องรอ capacity ออก |
| **[[Demand Shock]]** | ความต้องการลดลงทันที (เช่น COVID) | ต้องรอ demand ฟื้น |
| **[[Input Cost Spike]]** | ต้นทุนวัตถุดิบสูงขึ้น แต่ขายไม่ได้ราคา | ต้องรอ cost normalize |

---

## 2. Financial Statement Warning Signs

### 2.1 Balance Sheet Red Flags

> [!danger] สัญญาณเตือนจากงบดุล

| Red Flag | Metric | Threshold | ความหมาย |
|----------|--------|-----------|----------|
| **Debt/Equity สูง** | D/E Ratio | > 2.0x | Leverage สูง ลด flexibility |
| **Net Debt/EBITDA สูง** | Net Debt/EBITDA | > 4.0x | ใช้เวลานานในการชำระหนี้ |
| **Current Ratio ต่ำ** | Current Assets / Current Liabilities | < 1.0x | Liquidity risk |
| **Goodwill สูง** | Goodwill / Total Assets | > 30% | เสี่ยง impairment |
| **Inventory สูง** | Inventory / Revenue | > 20% | ขายไม่ออก |
| **Receivables เพิ่มเร็วกว่า Revenue** | DSO Trend | เพิ่มขึ้น | ลูกหนี้เก็บยาก |

### 2.2 Income Statement Red Flags

> [!warning] สัญญาณเตือนจากงบกำไรขาดทุน

| Red Flag | Metric | Threshold | ความหมาย |
|----------|--------|-----------|----------|
| **Margin Compression** | Gross Margin Trend | ลดลงต่อเนื่อง | แข่งขันด้านราคา / ต้นทุนสูง |
| **SG&A / Revenue สูง** | Operating Expense Ratio | > 30% | ต้นทุนดำเนินการสูง |
| **Non-recurring Gains** | Other Income / Net Income | > 20% | พึ่งรายได้ไม่ปกติ |
| **Effective Tax Rate ต่ำ** | Tax / Pre-tax Income | < 10% | ใช้ tax benefit ชั่วคราว |
| **EPS ผันผวน** | EPS Std Dev | สูง | Earnings ไม่แน่นอน |

### 2.3 Cash Flow Red Flags

> [!caution] สัญญาณเตือนจากงบกระแสเงินสด

| Red Flag | Metric | Threshold | ความหมาย |
|----------|--------|-----------|----------|
| **OCF < Net Income** | OCF / Net Income | < 1.0x | Earnings quality ต่ำ |
| **FCF Negative** | OCF - Capex | < 0 | ไม่สร้างเงินสด |
| **Capex > OCF** | Capex / OCF | > 1.0x | ใช้เงินมากกว่าสร้าง |
| **CFF Positive** | Financing Cash Flow | > 0 ต่อเนื่อง | พึ่งการกู้เงิน |
| **CFO Negative** | Operating Cash Flow | < 0 | ขาดทุนจากการดำเนินงาน |

### 2.4 Quality of Earnings Checklist

```
EARNINGS QUALITY CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ OCF > Net Income? (Ideal: OCF/NI > 1.2x)
□ Revenue growth = Cash collection growth?
□ Minimal non-recurring items?
□ Consistent accounting policies?
□ No off-balance sheet liabilities?
□ Clean audit opinion?
□ Related party transactions disclosed?
```

---

## 3. Capital Allocation Red Flags

### 3.1 Poor Capital Allocation Patterns

> [!danger] การจัดสรรเงินทุนที่ทำลายมูลค่า

```
┌─────────────────────────────────────────────────────────────────┐
│              CAPITAL ALLOCATION DECISION TREE                    │
└─────────────────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │  Excess Cash    │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  Reinvest     │   │  Return to    │   │  Pay Down     │
│  in Business  │   │  Shareholders │   │  Debt         │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        ▼                   ▼                   ▼
   ROIC > WACC?        Dividend/Buyback    Debt > Optimal?
        │                   │                   │
   ┌────┴────┐         ┌────┴────┐        ┌────┴────┐
   │         │         │         │        │         │
   ▼         ▼         ▼         ▼        ▼         ▼
┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐  ┌─────┐
│ YES │  │ NO  │  │Yield │  │Stock │  │ YES │  │ NO  │
│     │  │     │  │> Cost│  │Over- │  │     │  │     │
│ ✓   │  │ ✗   │  │of Eq │  │valued│  │ ✓   │  │ ✗   │
│Value│  │Value│  │?     │  │?     │  │Value│  │Value│
│Create│  │Dest │  │✓/✗   │  │✓/✗   │  │Create│  │Dest │
└─────┘  └─────┘  └─────┘  └─────┘  └─────┘  └─────┘
```

### 3.2 Capital Allocation Red Flags Checklist

| Category | Red Flag | คำอธิบาย |
|----------|----------|----------|
| **Capex** | Capex > OCF ต่อเนื่อง 3+ ปี | ลงทุนมากกว่าสร้างเงินสด |
| **Capex** | ROIC ลดลงหลัง capex cycle | ลงทุนไม่คุ้ม |
| **M&A** | Goodwill > 30% of assets | ซื้อบริษัทแพง |
| **M&A** | ROIC ลดลงหลัง M&A | ซื้อไม่คุ้ม |
| **Dividend** | จ่ายปันผลแม้ FCF ติดลบ | ยืมเงินจ่ายปันผล |
| **Buyback** | Buyback ตอนราคาสูงสุด | ซื้อหุ้นแพง |
| **Debt** | กู้เพิ่มแม้ Debt/EBITDA สูง | เพิ่ม leverage แม้มีแล้วเยอะ |
| **Debt** | Short-term debt สำหรับ long-term assets | Maturity mismatch |

### 3.3 Management Behavior Red Flags

> [!caution] พฤติกรรมผู้บริหารที่น่าเป็นห่วง

| Red Flag | สัญญาณ | ความหมาย |
|----------|--------|----------|
| **Over-promising** | Guidance เป็นบวกเสมอ แต่ results ผิด | Management ไม่ realistic |
| **Blaming External** | โทษ macro/competition เสมอ | ไม่ยอมรับความผิดพลาด |
| ** empire Building** | M&A หลายครั้ง ขยาย size | เน้น size ไม่ใช่ value |
| **Related Party** | ทำธุรกรรมกับบริษัทในเครือ | Agency problem |
| **Compensation** | CEO pay ไม่ผูกกับ ROIC | Incentive ผิด |
| **Board** | Board ไม่มี independent directors | Governance อ่อน |

---

## 4. Cyclical vs Structural Value Destruction

### 4.1 Decision Framework

> [!important] คำถามสำคัญ: Value Destruction เป็นชั่วคราวหรือถาวร?

```
┌─────────────────────────────────────────────────────────────────┐
│         CYCLICAL vs STRUCTURAL DECISION FRAMEWORK               │
└─────────────────────────────────────────────────────────────────┘

                    ┌─────────────────┐
                    │  ROIC < WACC    │
                    │  (Negative Spread)
                    └────────┬────────┘
                             │
                             ▼
                ┌────────────────────────┐
                │ คำถามที่ 1:            │
                │ Industry structure เปลี่ยน?│
                └────────────┬───────────┘
                             │
              ┌──────────────┴──────────────┐
              │                             │
              ▼                             ▼
        ┌───────────┐               ┌───────────┐
        │   YES     │               │    NO     │
        │ STRUCTURAL│               │  CHECK    │
        └───────────┘               └─────┬─────┘
                                          │
                                          ▼
                              ┌────────────────────────┐
                              │ คำถามที่ 2:            │
                              │ Competitive position เปลี่ยน?│
                              └────────────┬───────────┘
                                           │
                            ┌──────────────┴──────────────┐
                            │                             │
                            ▼                             ▼
                      ┌───────────┐               ┌───────────┐
                      │   YES     │               │    NO     │
                      │ STRUCTURAL│               │  CHECK    │
                      └───────────┘               └─────┬─────┘
                                                        │
                                                        ▼
                                            ┌────────────────────────┐
                                            │ คำถามที่ 3:            │
                                            │ Management เปลี่ยนพฤติกรรม?│
                                            └────────────┬───────────┘
                                                         │
                                          ┌──────────────┴──────────────┐
                                          │                             │
                                          ▼                             ▼
                                    ┌───────────┐               ┌───────────┐
                                    │   NO      │               │   YES     │
                                    │ STRUCTURAL│               │  CYCLICAL │
                                    │ (Behavior)│               │ (Temporary)│
                                    └───────────┘               └───────────┘
```

### 4.2 Cyclical Value Destruction Indicators

> [!info] บ่งชี้ว่าเป็นชั่วคราว (Cyclical)

| Indicator | คำอธิบาย | Recovery Signal |
|-----------|----------|-----------------|
| **Industry-wide** | ทุกคนในอุตสาหกรรมได้รับผลกระทบ | Competitors ฟื้น |
| **Historical Precedent** | เคยเกิดขึ้นแล้วและฟื้นได้ | Cycle เดิม |
| **Demand-driven** | ความต้องการลด แต่โครงสร้างยังดี | Demand กลับ |
| **External Shock** | เหตุการณ์ภายนอก (COVID, War) | เหตุการณ์ผ่าน |
| **Balance Sheet Intact** | งบดุลยังแข็งแกร่ง | รอได้ |
| **Management Quality** | ผู้บริหารมี track record ดี | น่าเชื่อถือ |

### 4.3 Structural Value Destruction Indicators

> [!danger] บ่งชี้ว่าเป็นถาวร (Structural)

| Indicator | คำอธิบาย | Why Permanent |
|-----------|----------|---------------|
| **Industry Disruption** | เทคโนโลยีใหม่ทำลายเก่า | ไม่มีทางกลับ |
| **Structural Oversupply** | กำลังผลิตเกินถาวร | ต้องลด capacity |
| **Commoditization** | สินค้ากลายเป็น commodity | ไม่มี pricing power |
| **Regulatory Change** | กฎระเบียบเปลี่ยนถาวร | โครงสร้างเปลี่ยน |
| **Balance Sheet Broken** | หนี้สินสูงเกินไป | ต้อง restructure |
| **Management Quality** | ผู้บริหารไม่ดี ไม่เปลี่ยน | ทำลายค่าต่อไป |

### 4.4 Case Study Analysis (from B2)

| Company | Type | Evidence | Verdict |
|---------|------|----------|---------|
| **SCC** | Cyclical | Chemicals downcycle, LSP drag | **Recovery Candidate** |
| **AAV** | Cyclical (Post-COVID) | Demand recovering, high leverage | **High-Beta Turnaround** |
| **IRPC** | Structural + Cyclical | Commodity trap, no moat | **Value Trap Territory** |
| **THCOM** | Structural | Technology disruption, FCF negative | **Speculative** |
| **ANAN** | Structural | Condo oversupply, balance sheet weak | **Value Trap** |

---

## 5. Value Destruction Warning Signs Checklist

### 5.1 Master Checklist

```
═══════════════════════════════════════════════════════════════════
VALUE DESTRUCTION WARNING SIGNS CHECKLIST
═══════════════════════════════════════════════════════════════════

SECTION A: ROIC-WACC SPREAD (Primary)
─────────────────────────────────────
[ ] ROIC < WACC ต่อเนื่อง 3+ ปี?      → HIGH RISK
[ ] ROIC trend ลดลงต่อเนื่อง?         → HIGH RISK
[ ] Spread ติดลบ > -3%?              → HIGH RISK
[ ] WACC สูงขึ้นต่อเนื่อง?             → MEDIUM RISK

SECTION B: CAPITAL ALLOCATION
─────────────────────────────────────
[ ] Capex > OCF ต่อเนื่อง 3+ ปี?      → HIGH RISK
[ ] FCF negative ต่อเนื่อง?           → HIGH RISK
[ ] M&A ทำให้ ROIC ลด?               → MEDIUM RISK
[ ] จ่ายปันผลแม้ FCF ติดลบ?          → HIGH RISK
[ ] Buyback ตอนราคาสูง?              → MEDIUM RISK

SECTION C: BALANCE SHEET
─────────────────────────────────────
[ ] Debt/Equity > 2.0x?              → HIGH RISK
[ ] Net Debt/EBITDA > 4.0x?          → HIGH RISK
[ ] Current Ratio < 1.0x?            → HIGH RISK
[ ] Goodwill > 30% of assets?        → MEDIUM RISK
[ ] Inventory / Revenue > 20%?       → MEDIUM RISK

SECTION D: EARNINGS QUALITY
─────────────────────────────────────
[ ] OCF / Net Income < 1.0x?         → HIGH RISK
[ ] Non-recurring gains > 20% of NI? → MEDIUM RISK
[ ] Margin compression 3+ ปี?        → HIGH RISK
[ ] EPS volatility สูง?              → MEDIUM RISK

SECTION E: MANAGEMENT & GOVERNANCE
─────────────────────────────────────
[ ] Related party transactions สูง?  → HIGH RISK
[ ] CEO turnover สูง?                → MEDIUM RISK
[ ] Auditor change / issues?         → HIGH RISK
[ ] Compensation ไม่ผูกกับ ROIC?      → MEDIUM RISK
[ ] Board independence ต่ำ?          → MEDIUM RISK

SECTION F: INDUSTRY & COMPETITIVE
─────────────────────────────────────
[ ] Industry disruption?             → HIGH RISK
[ ] Structural oversupply?           → HIGH RISK
[ ] Loss of market share?            → HIGH RISK
[ ] Pricing power หาย?               → HIGH RISK
[ ] New competition รุนแรง?          → MEDIUM RISK

═══════════════════════════════════════════════════════════════════
SCORING:
• 3+ HIGH RISK → AVOID (Value Trap)
• 2 HIGH RISK + 2+ MEDIUM → HIGH CAUTION
• 1-2 HIGH RISK → WATCH CLOSELY
• 0 HIGH RISK + 3+ MEDIUM → RESEARCH DEEPER
═══════════════════════════════════════════════════════════════════
```

### 5.2 Quick Screening Tool

| Score | Risk Level | Action |
|-------|------------|--------|
| **8+** | 🔴 Extreme | AVOID — Value Trap |
| **6-7** | 🟠 High | Very Cautious — Deep research required |
| **4-5** | 🟡 Medium | Watch — Monitor closely |
| **0-3** | 🟢 Low | OK — Standard due diligence |

---

## 6. Recovery Path Analysis

### 6.1 When Value Destruction Can Reverse

> [!success] เงื่อนไขที่ Value Destruction สามารถกลับเป็น Value Creation

| Condition | สิ่งที่ต้องเกิด | Timeline |
|-----------|---------------|----------|
| **Cyclical Recovery** | Industry cycle กลับขึ้น | 1-3 years |
| **Restructuring** | ขาย non-core assets, ลดหนี้ | 2-3 years |
| **Management Change** | CEO ใหม่, กลยุทธ์ใหม่ | 2-4 years |
| **Industry Consolidation** | Competitors ออก, supply ลด | 3-5 years |
| **Disruption Fades** | เทคโนโลยีใหม่ไม่แรงเท่าคาด | Varies |

### 6.2 Recovery Probability Matrix

```
┌─────────────────────────────────────────────────────────────────┐
│              RECOVERY PROBABILITY MATRIX                         │
└─────────────────────────────────────────────────────────────────┘

                         BALANCE SHEET
                    ┌───────────┬───────────┐
                    │   WEAK    │  STRONG   │
              ┌─────┼───────────┼───────────┤
              │     │           │           │
              │  C  │    LOW    │  MEDIUM   │
   CAUSE      │  Y  │  (10-30%) │ (30-50%)  │
              │  C  │           │           │
              │  L  │  ANAN,    │  SCC,     │
              │  I  │  THCOM    │  IRPC     │
              │  C  │           │           │
              │  A  ├───────────┼───────────┤
              │  L  │           │           │
              │     │  MEDIUM   │   HIGH    │
              │  S  │  (30-50%) │ (50-70%)  │
              │  T  │           │           │
              │  R  │  AAV      │  (Ideal   │
              │  U  │           │   Candidate)│
              │  C  │           │           │
              │  T  ├───────────┼───────────┤
              │  U  │           │           │
              │  R  │   LOW     │  MEDIUM   │
              │  A  │  (10-20%) │ (20-40%)  │
              │  L  │           │           │
              └─────┴───────────┴───────────┘
```

### 6.3 Turnaround Investment Criteria

> [!tip] ตรวจสอบก่อนลงทุนใน Turnaround

```
TURNAROUND INVESTMENT CHECKLIST
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
□ ROIC กำลังกลับขึ้น? (แม้ยังต่ำกว่า WACC)
□ FCF กลับเป็นบวก?
□ Debt ลดลง?
□ Management มีแผนชัดเจน?
□ Balance Sheet แข็งแกร่งพอรอ?
□ Valuation ต่ำกว่า Fair Value มาก?
□ Catalyst ชัดเจน?
□ Risk/Reward น่าสนใจ? (3:1+)
```

---

## 7. Application to SET Stocks

### 7.1 B2 Companies Warning Signs Summary

| Company | Structural | Behavioral | Cyclical | Recovery Path |
|---------|------------|------------|----------|---------------|
| **ANAN** | Condo trap, No moat | Overexpansion | Demand weak | Low |
| **IRPC** | Commodity trap | N/A | Cycle down | Low-Medium |
| **SCC** | Chemicals cyclical | LSP investment | Cycle down | Medium |
| **THCOM** | Tech disruption | Overinvestment | N/A | Low |
| **AAV** | High fixed cost | N/A | Post-COVID | Medium |

### 7.2 Value Trap Probability Ranking

| Rank | Company | Probability | Key Reason |
|------|---------|-------------|------------|
| 1 | **ANAN** | 🔴 High | Structural + Balance Sheet |
| 2 | **THCOM** | 🔴 High | Structural (Disruption) |
| 3 | **IRPC** | 🟠 Medium-High | Commodity trap |
| 4 | **AAV** | 🟡 Medium | Cyclical (Recovering) |
| 5 | **SCC** | 🟢 Low-Medium | Cyclical + Strong Balance Sheet |

---

## 8. Key Learnings

### 8.1 Summary Framework

> [!abstract] สรุป Value Destruction Analysis

```
VALUE DESTRUCTION = f(Structure, Behavior, Cycle)

Where:
• Structure = Industry + Competitive Position
• Behavior = Management Decisions
• Cycle = Timing in Industry Cycle

Investment Decision:
• Structural → AVOID (除非 turnaround catalyst)
• Behavioral → WATCH (management change?)
• Cyclical → OPPORTUNITY (at right price)
```

### 8.2 Key Questions Before Investing

```
BEFORE BUYING "CHEAP" STOCK:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
1. Why is ROIC < WACC?
   □ Structural → AVOID
   □ Behavioral → WATCH
   □ Cyclical → RESEARCH

2. Can it recover?
   □ What needs to happen?
   □ Timeline?
   □ Probability?

3. Is balance sheet strong enough?
   □ Debt/Equity?
   □ FCF?
   □ Liquidity?

4. What's the catalyst?
   □ Cycle recovery?
   □ Restructuring?
   □ Management change?

5. What's my edge?
   □ Why market wrong?
   □ What do I know that others don't?
```

---

## 🔗 Related Notes

- [[B1-High-Spread-Companies]] — บริษัทที่สร้างมูลค่า
- [[B2-Negative-Spread-Companies]] — Case studies เต็ม
- [[ROIC-WACC Research Design]]
- [[A1-EVA-Literature-Review]]
- [[Capital Allocation]]
- [[Value Trap]]
- [[Economic Moat]]
- [[Quality Swing Investor]]
- [[Investing MOC]]

---

*Research: Synthesis from B2 Case Studies + Knowledge Base*
*Created: 2026-04-01*
