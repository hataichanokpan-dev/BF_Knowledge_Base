---
title: Deep Value
note_type: concept
status: evergreen
version: v3
created: 2026-03-27
updated: 2026-04-02
author: Professor Damodaran (Thai Editor)
tags:
  - note/concept
  - style/value
  - thai-market
  - dual-ai
aliases:
  - Deep Value Investing
  - Cigar Butt Investing
  - Net-Net Investing
---

# Deep Value: การลงทุนแบบซื้อในราคาต่ำกว่ามูลค่าอย่างมีนัยสำคัญ

> "Buy when fear is highest, sell when greed peaks."
> — Adapted from Warren Buffett

---

## Table of Contents

1. Why Should You Care About Deep Value?
2. Core Philosophy & Definition
3. Key Metrics & Formulas
4. Screening Workflow: หาหุ้น Deep Value จากไหน?
5. Intrinsic Value Estimation
6. Investment Checklist (4 Phases)
7. Sector & Market Cap Fit
8. Thai Market Application
9. Risks & Warning Signs
10. Case Studies (Thai Examples)
11. Related Concepts
12. References

---

## 1. Why Should You Care About Deep Value?

### คุณเคยเจอแบบนี้ไหม?

**Scenario 1:** คุณเห็นหุ้นตัวหนึ่ง P/BV 0.3x ดูถูกมาก คุณก็ซื้อเลย สามปีผ่านไป ราคายังเท่าเดิม P/BV 0.3x แต่ธุรกิจแย่ลงเรื่อยๆ คุณติด Value Trap สินๆ

**Scenario 2:** บริษัทประกาศขายสินทรัพย์ หุ้นกระโดด 40% ในอาทิตย์เดียว คุณนั่งหงุดๆ คิดในใจว่า "เฮ้ย ทำไมฉันไม่เห็นมาก่อน?" คำตอบ: คุณไม่ได้ดูมูลค่าสินทรัพย์ไง

**Scenario 3:** Portfolio คุณเต็มไปด้วยหุ้น "growth" ที่ P/E แตะ 50x พอตลาดปรับลง 30% คุณนั่งอยากมีหุ้น "น่าเบื่อ" บ้างที่มี downside protection

> [!tip] บทเรียนสำคัญ
> Deep Value ไม่ใช่การซื้อหุ้น "ถูก" แต่เป็นการซื้อสินทรัพย์ในราคาต่ำกว่า intrinsic value อย่างมีนัยสำคัญ พร้อม margin of safety ที่ปกป้อง downside เมื่อทำถูกต้อง คุณจะเสียน้อยลงในช่วงตลาดตก และกำไรเมื่อตลาดตระหนักถึงมูลค่าที่แท้จริง

---

## 2. Core Philosophy & Definition

### Deep Value คืออะไร?

Deep Value เป็นกลยุทธ์การลงทุนที่พยายามซื้อหลักทรัพย์ที่ซื้อขายในราคาต่ำกว่า intrinsic value อย่างมีนัยสำคัญ โดยวัดจาก:

- **Asset-based metrics:** P/BV < 0.5x, Market Cap < NCAV
- **Earnings-based metrics:** P/E < 50% ของค่าเฉลี่ยภาคส่วน
- **Replacement value:** Market Cap < 50% ของ replacement cost

### Philosophy ในหนึ่งประโยค

> ซื้อดอลลาร์ในราคาห้าสิบเซ็นต์ พร้อม catalyst เพื่อปลดล็อคส่วนลด

### Visual Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                     DEEP VALUE SPECTRUM                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  CONSERVATIVE                    AGGRESSIVE                     │
│  ────────────────────────────────────────────────────────>      │
│                                                                 │
│  Net Cash    NCAV      NNWC      P/BV      P/E      Turnaround  │
│  > Market    < Price   < Price   < 0.5     < 5x     Distressed  │
│                                                                 │
│  RISK: Low ──────────────────────────────────────────> High     │
│  RETURN: Modest ─────────────────────────────────────> High     │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### ทำไม Deep Value ถึง Work

1. **Margin of Safety:** ซื้อที่ 50% ของ intrinsic value ให้ buffer ต่อการวิเคราะห์ผิดพลาดและเหตุการณ์ที่คาดไม่ถึง ถ้าคุณผิดไป 30% คุณยังมี cushion 20%

2. **Mean Reversion:** Valuation metrics มักจะกลับสู่ค่าเฉลี่ยทางประวัติศาสตร์ หุ้นที่ P/BV 0.3x มักจะเคลื่อนไปสู่ 0.8-1.2x สร้างผลตอบแทนแม้ไม่มีการเติบโตของกำไร

3. **Catalyst Potential:** ที่ระดับราคาต่ำมาก ข่าวดีเล็กน้อยสามารถ trigger re-rating ได้อย่างมีนัยสำคัญ การขายสินทรัพย์ เปลี่ยนผู้บริหาร หรือ sector rotation สามารถปลดล็อคมูลค่าได้อย่างรวดเร็ว

4. **Asymmetric Risk-Reward:** Downside จำกัด (สินทรัพย์เป็น floor) พร้อม upside ที่มีนัยสำคัญ (re-rating สู่ fair value)

---

## 3. Key Metrics & Formulas

### Metric 1: Price-to-Book Value (P/BV)

**Formula:**
```
P/BV = Market Price / Book Value Per Share

Where:
Book Value Per Share = (Total Assets - Total Liabilities) / Shares Outstanding
```

**Thresholds:**
| Level | P/BV | Interpretation |
|-------|------|----------------|
| Deep Value | < 0.5x | ส่วนลดมีนัยสำคัญต่อสินทรัพย์ |
| Value | 0.5x - 0.8x | ส่วนลดปานกลาง |
| Fair Value | 0.8x - 1.5x | ราคาสมเหตุผล |
| Expensive | > 1.5x | Premium valuation |

**Thai Market Context:**
- Banking sector average: 0.8-1.2x
- Property sector average: 0.5-0.8x
- Industrial sector average: 1.0-1.5x

> [!example] ตัวอย่างหุ้นไทย
> **SC Asset (SC):**
> - Market Price: 2.50 THB
> - Book Value Per Share: 8.10 THB
> - P/BV = 2.50 / 8.10 = 0.31x (Deep Value territory)

---

### Metric 2: Net Current Asset Value (NCAV) - Benjamin Graham's Classic

**Formula:**
```
NCAV Per Share = (Current Assets - Total Liabilities) / Shares Outstanding

Where:
Current Assets = Cash + Receivables + Inventory + Other Current Assets
Total Liabilities = All short-term and long-term debt
```

**Thresholds:**
| Level | Price vs NCAV | Action |
|-------|---------------|--------|
| Graham Bargain | Price < 0.67 × NCAV | Strong Buy |
| Moderate Value | Price < 1.0 × NCAV | Consider |
| Fair Value | Price = 1.0-1.5 × NCAV | Hold |
| Expensive | Price > 1.5 × NCAV | Avoid |

> [!info] ทำไม NCAV ถึงสำคัญ
> - เป็นตัวแทนของ liquidation value ของ working capital
> - สมมติว่า fixed assets เป็นศูนย์ (conservative)
> - Graham's original "cigar butt" strategy ใช้ metric นี้

**Example Calculation:**
```
Hypothetical Thai Manufacturing Company:
- Cash: 500M THB
- Receivables: 300M THB
- Inventory: 400M THB
- Other Current Assets: 100M THB
- Current Assets = 1,300M THB

- Total Liabilities: 600M THB
- Shares Outstanding: 100M shares

NCAV Per Share = (1,300 - 600) / 100 = 7.00 THB

If Market Price = 4.00 THB:
Price/NCAV = 4.00 / 7.00 = 0.57x (Graham Bargain!)
```

---

### Metric 3: Net Net Working Capital (NNWC) - More Conservative

**Formula:**
```
NNWC Per Share = (Cash + 0.75×Receivables + 0.50×Inventory - Total Liabilities) / Shares
```

> [!warning] ทำต้องปรับลด?
> - Receivables อาจไม่ได้รับเงินเต็มจำนวน
> - Inventory อาจต้องลดราคาเพื่อขาย
> - เป็นการประเมิน liquidation ที่ realistic กว่า

**Thresholds:**
| Level | Price vs NNWC | Signal |
|-------|---------------|--------|
| Deep Bargain | Price < 0.67 × NNWC | Very Attractive |
| Bargain | Price < 1.0 × NNWC | Attractive |
| Fair | Price > 1.0 × NNWC | Pass |

---

### Metric 4: Price-to-Earnings (P/E) with Sector Context

**Formula:**
```
P/E = Market Price / Earnings Per Share (EPS)

Relative P/E = Stock P/E / Sector Average P/E
```

**Thresholds:**
| Level | Relative P/E | Interpretation |
|-------|--------------|----------------|
| Deep Value | < 0.5 | ส่วนลด 50% ต่อภาคส่วน |
| Value | 0.5 - 0.8 | ส่วนลดปานกลาง |
| Fair | 0.8 - 1.2 | สอดคล้องกับภาคส่วน |
| Expensive | > 1.2 | Premium |

> [!danger] ระวัง!
> P/E ต่ำเพียงอย่างเดียวไม่พอ ต้อง verify:
> - กำไรยั่งยืน (ไม่ใช่ one-time gains)
> - ไม่มีการปรับแต่งบัญชี
> - ธุรกิจไม่ได้อยู่ในช่วง structural decline

---

### Metric 5: Enterprise Value to EBITDA (EV/EBITDA)

**Formula:**
```
EV = Market Cap + Total Debt - Cash
EV/EBITDA = Enterprise Value / EBITDA
```

**Thresholds:**
| Level | EV/EBITDA | Signal |
|-------|-----------|--------|
| Deep Value | < 4x | Very Cheap |
| Value | 4x - 6x | Cheap |
| Fair | 6x - 10x | Reasonable |
| Expensive | > 10x | Pricey |

**Thai Market Context:**
- Banking sector: Not applicable (use P/BV)
- Property sector average: 6-8x
- Industrial sector average: 5-7x
- Energy sector average: 4-6x

> [!tip] ทำไมใช้ EV/EBITDA?
> - Capital structure neutral
> - เปรียบเทียบบริษัทที่มี leverage ได้ดีกว่า
> - Useful for M&A context

---

### Metric 6: Free Cash Flow Yield

**Formula:**
```
FCF Yield = Free Cash Flow Per Share / Market Price × 100%

Where:
Free Cash Flow = Operating Cash Flow - Capital Expenditure
```

**Thresholds:**
| Level | FCF Yield | Signal |
|-------|-----------|--------|
| Excellent | > 15% | Deep Value |
| Good | 10% - 15% | Value |
| Fair | 5% - 10% | Reasonable |
| Poor | < 5% | Expensive |

**Thai Market Context:**
- Typical Thai large caps: 4-6%
- Property sector: 5-8% (capex heavy)
- Industrial sector: 6-10%
- Cash-rich companies: 10%+ (rare)

---

## 4. Screening Workflow: หาหุ้น Deep Value จากไหน?

### SETSMART Screener Setup

**Step 1: Access SETSMART**
1. Login to SETSMART (subscription required)
2. Navigate to "Screener" or "Stock Selection"
3. Create new custom screen

**Step 2: Set Basic Filters**
```
Filter 1: P/BV < 0.7
Filter 2: Market Cap > 1,000M THB (avoid micro-caps)
Filter 3: Trading Volume > 1M THB/day (liquidity)
Filter 4: SET ESG Rating exists (any rating)
```

**Step 3: Add Quality Filters**
```
Filter 5: Debt/Equity < 1.5
Filter 6: Current Ratio > 1.0
Filter 7: Positive EPS in latest year
```

**Step 4: Export and Manual Review**
1. Export results to Excel
2. Apply Gate 0 checklist manually
3. Check RPT in 56-1 for remaining candidates

### Manual Screening Approach

**Option A: SET Factsheet Review**
1. Go to SET website > Company Information
2. Filter by sector (Property, Industrial, Energy)
3. Sort by P/BV ascending
4. Review top 20 lowest P/BV stocks

**Option B: Brokerage Screeners**
- Maybank Kim Eng: Good for Thai market
- KGI Securities: Has value screening tools
- Bualuang Securities: Research access

**Option C: Free Alternatives**
- SET website: Basic financial data
- Stock Exchange app: Mobile screening
- Thaiinvestor.org: Some free tools

### Weekly Screening Routine

> [!tip] Monday (30 minutes)
> 1. Run SETSMART screener with saved filters
> 2. Export new candidates to watchlist
> 3. Check for any trading halts/suspensions

> [!info] Wednesday (1 hour)
> 1. Review watchlist candidates
> 2. Pull 56-1 for top 3-5 candidates
> 3. Check Gate 0 criteria

> [!success] Friday (30 minutes)
> 1. Update price data for candidates
> 2. Review news/announcements
> 3. Prioritize for weekend deep analysis

**Watchlist Management:**
- Keep 10-20 candidates on watch
- Update monthly or after earnings
- Remove if Gate 0 fails or thesis breaks
- Add new candidates as they appear

---

## 5. Intrinsic Value Estimation

### Quick Method: NCAV/NNWC

**NCAV Method:**
```
Intrinsic Value = NCAV Per Share

Buy if: Price < 0.67 × NCAV (Graham's rule)
Margin of Safety = (NCAV - Price) / NCAV
```

> [!example] ตัวอย่าง
> **Company A:**
> - NCAV = 10 THB/share
> - Price = 6 THB
> - Discount = 40%
> - Margin of Safety = (10 - 6) / 10 = 40%
>
> Verdict: EXCEEDS 30% requirement ✓

**NNWC Method (More Conservative):**
```
Intrinsic Value = NNWC Per Share

Buy if: Price < 0.67 × NNWC
```

### Detailed Method: Sum of Parts

**For Asset-Heavy Companies (Property, Industrial):**

```
Intrinsic Value = 
  + Cash & Equivalents (100%)
  + Marketable Securities (100%)
  + Receivables (80% - allowance for bad debt)
  + Inventory (50-70% - liquidation discount)
  + Fixed Assets (50-80% - depending on quality)
  + Investment Property (70-90% - appraisal value)
  - Total Liabilities (100%)
  ÷ Shares Outstanding
```

> [!example] Property Developer
> **Assets (per share):**
> - Cash: 2.00 THB (100%) = 2.00
> - Receivables: 1.50 THB (80%) = 1.20
> - Inventory (land): 5.00 THB (70%) = 3.50
> - Fixed Assets: 1.00 THB (50%) = 0.50
> - Total = 7.20 THB
>
> Liabilities (per share): 2.00 THB
>
> Intrinsic Value = 7.20 - 2.00 = 5.20 THB
>
> If Price = 3.00 THB:
> Discount = (5.20 - 3.00) / 5.20 = 42%
> Verdict: EXCEEDS 30% requirement ✓

### Margin of Safety Application

**The 30% Rule:**
```
Minimum Buy Price = Intrinsic Value × 0.70

Example:
If Intrinsic Value = 10 THB
Minimum Buy Price = 10 × 0.70 = 7 THB

Buy at 7 THB or below for 30%+ margin of safety
```

> [!info] ทำไม 30%?
> - ครอบคลุม estimation errors (10%)
> - ครอบคลุม unforeseen events (10%)
> - เป็น profit cushion (10%)

**Aggressive vs Conservative:**
| Investor Type | Margin of Safety | Buy Trigger |
|---------------|------------------|-------------|
| Conservative | 40-50% | Price < 0.50-0.60 × IV |
| Standard | 30% | Price < 0.70 × IV |
| Aggressive | 20% | Price < 0.80 × IV |

**Practical Application:**
1. Calculate NCAV (quick check)
2. Calculate Sum of Parts (detailed check)
3. Use LOWER of the two as Intrinsic Value
4. Apply 30% discount for Buy Price
5. Set price alerts at Buy Price level

---

## 6. Investment Checklist

### Phase 1: Universe Screening (Gate 0 - Knockout Criteria)

> [!danger] ตรวจสอบก่อน ANY analysis

**Before ANY analysis, verify these minimum requirements:**

- [ ] **SET ESG Rating 2025 Available:** Company has SET ESG rating
  - Why: Baseline governance check
  - Pass: Any rating (AAA to B)
  - Fail: No rating = skip
  - Check: SET website or SEC Thailand

- [ ] **Free Float >= 20%:** Sufficient shares available for trading
  - Why: Liquidity risk
  - Pass: >= 20%
  - Fail: < 20% = high manipulation risk

- [ ] **No Trading Signs:** Not on SET caution/suspension list
  - Why: Regulatory issues
  - Pass: Clean status
  - Fail: Any warning sign = skip

- [ ] **Audit Opinion: Unqualified:** Clean audit report
  - Why: Financial integrity
  - Pass: Unqualified opinion only
  - Fail: Qualified/adverse = skip

> [!warning] Gate 0 FAIL = STOP
> Do not proceed to Phase 2.

---

### Phase 2: Quantitative Filters

**Asset-Based Filters:**

- [ ] P/BV < 0.5x (or < 0.7x for quality businesses)
- [ ] Price < 0.67 × NCAV (Graham criterion)
- [ ] Price < NNWC (more conservative)
- [ ] Market Cap < 50% of replacement cost

**Earnings-Based Filters:**

- [ ] P/E < 50% of sector average
- [ ] EV/EBITDA < 6x
- [ ] FCF Yield > 10%
- [ ] Positive earnings in 3 of last 5 years

**Balance Sheet Filters:**

- [ ] Current Ratio > 1.0 (short-term solvency)
- [ ] Debt-to-Equity < 1.0 (or < 2.0 for capital-intensive)
- [ ] Net Debt/EBITDA < 3x
- [ ] No going concern issues in audit report

**Scoring:**
- 8+ checks pass = Strong candidate
- 5-7 checks pass = Worth investigating
- < 5 checks pass = Skip

---

### Phase 3: Qualitative Checks

**Business Quality:**

- [ ] Business model is understandable (can explain in 2 minutes)
- [ ] Revenue source is clear and sustainable
- [ ] Not in structural decline (check industry trends)
- [ ] Product/service still relevant in 5 years

**Management & Governance (Critical for Thai Market):**

- [ ] CEO and Chairman are different people
- [ ] At least 2 independent directors on board
- [ ] No related party transactions > 10% of revenue
- [ ] No loans/guarantees to related parties
- [ ] Management owns meaningful equity (alignment)
- [ ] Track record of shareholder-friendly actions

**Thai-Specific Governance Checks:**

> [!warning] RPT (Related Party Transactions) Risk Level

- [ ] **Green (Acceptable):** RPT < 10% of revenue
  - Check: 56-1 filing, Note to Financial Statements
  - Action: Proceed with normal due diligence

- [ ] **Yellow (Investigate Deeply):** RPT 10-20% of revenue
  - Check: Detailed RPT disclosure, nature of transactions
  - Action: Verify fairness, check independent director approval
  - Risk: Potential minority shareholder disadvantage

- [ ] **Red (Avoid):** RPT > 20% of revenue
  - Check: High governance risk, potential value expropriation
  - Action: Skip unless exceptional circumstances

- [ ] Family control < 70% of voting rights
  - Check: Shareholder structure in 56-1
  - Red Flag: > 70% = minority shareholders disadvantaged

- [ ] No cross-shareholdings or pyramid structures
  - Check: Related company disclosures
  - Red Flag: Complex structures hide risks

- [ ] Auditor is Big 4 or reputable local firm
  - Check: Audit firm in annual report
  - Red Flag: Unknown auditor = lower credibility

**Value Realization Path:**

- [ ] Identifiable catalyst exists:
  - Asset sale/restructuring
  - Management change
  - Sector rotation
  - Regulatory change
  - M&A potential
- [ ] Insider buying in recent 6 months
- [ ] Share buyback program announced

---

### Phase 4: Entry Conditions

**Valuation Confirmation:**

- [ ] Price offers 30%+ margin of safety to intrinsic value
- [ ] Multiple valuation methods converge (P/BV, NCAV, Sum of Parts)
- [ ] Not a "falling knife" - price stabilized for 2-4 weeks

**Liquidity Check:**

- [ ] Daily trading volume > 10M THB
- [ ] Bid-ask spread < 2%
- [ ] Can exit position in 5-10 trading days

**Portfolio Fit:**

- [ ] Position size <= 5% of portfolio (Deep Value is risky)
- [ ] Not correlated with existing holdings
- [ ] Adequate cash reserve for averaging down

---

## 7. Sector & Market Cap Fit

### Sector Suitability

| Sector | Fit Level | Why | Key Considerations |
|--------|-----------|-----|-------------------|
| Banking | Medium | P/BV works well | Watch NPL ratios, capital adequacy |
| Property | High | Asset-rich, cyclical | Land bank valuation, debt levels |
| Industrial | Medium | Tangible assets | Utilization rates, order backlog |
| Energy | Medium | Asset-based | Oil price volatility, reserves |
| Technology | Low | Intangible assets | P/BV less relevant |
| Services | Low | Asset-light | Use P/E or EV/EBITDA instead |

### Market Cap Suitability

| Size | Fit | Considerations |
|------|-----|----------------|
| Large Cap (>50B THB) | Good | More liquid, better governance, slower re-rating |
| Mid Cap (10-50B THB) | Best | Balance of liquidity and upside potential |
| Small Cap (<10B THB) | Caution | Higher alpha but liquidity and governance risks |

### Thai Market Deep Value Opportunities by Sector

> [!info] ตัวอย่าง ณ วันที่ 2026-04-02
> Verify current metrics before analysis.

**Property Sector (Most Common):**
- Cyclical downturns create deep value
- Land banks often undervalued on books
- Watch: SC Asset, Property Perfect, Sansiri

**Industrial/Manufacturing:**
- Asset-heavy with tangible book value
- Economic cycles create entry points
- Watch: Thai Steel, Siam Cement (during downturns)

**Banking:**
- Trade at P/BV, well-understood metric
- Crisis creates deep value opportunities
- Watch: TMB, KGI (smaller banks)

---

## 8. Thai Market Application

### Sample Thai Deep Value Stocks

> [!warning] Data as of 2026-04-02
> Verify current prices and metrics before making any investment decisions. These are examples for illustration, not recommendations.

| Stock | Sector | P/BV | Key Metric | Notes |
|-------|--------|------|------------|-------|
| SC Asset (SC) | Property | 0.31x | NCAV positive | Land bank undervalued |
| Property Perfect (PF) | Property | 0.4x | Asset-rich | Turnaround story |
| Asian Property (AP) | Property | 0.5x | Quality assets | Stronger balance sheet |
| LH Financial (LHFG) | Financial | 0.6x | NCAV approach | Micro-cap bank |
| MFC (MFC) | Insurance | 0.7x | Book value | Hidden assets |
| Italian-Thai (ITD) | Industrial | 0.5x | Asset-heavy | Construction cyclical |
| STECON | Industrial | 0.6x | NCAV positive | Infrastructure play |

### Thai-Specific Risks for Deep Value

| Risk | What to Check | Red Flag | Mitigation |
|------|---------------|----------|------------|
| **Governance** | Board independence | CEO = Chairman | Require independent board |
| **Related Party Transactions** | 56-1 filing | RPT > 20% revenue (Red level) | Avoid high RPT companies |
| **Liquidity** | Daily volume | < 10M THB daily | Position size accordingly |
| **Concentration** | Major holders | > 70% held by one group | Require free float > 20% |
| **Accounting Quality** | Audit opinion | Qualified opinion | Unqualified only |
| **Political Risk** | Government links | Policy sensitivity | Diversify |

### Data Sources for Thai Market

**Primary Sources (Required):**
- **SET Factsheet:** Financial metrics, P/BV, P/E, market data
- **56-1 Annual Report:** RPT, governance, shareholder structure
- **Company IR:** Presentation, analyst calls

**Secondary Sources:**
- **SETSMART:** Historical data, screening
- **SEC Thailand:** Regulatory filings
- **Brokerage Research:** For cross-check

**What to Check Where:**

| Information | Source | Where to Look |
|-------------|--------|---------------|
| P/BV, P/E | SET Factsheet | First page, valuation section |
| RPT | 56-1 | Notes to Financial Statements |
| Board Composition | 56-1 | Corporate Governance section |
| Shareholder Structure | 56-1 | Share Ownership section |
| Related Party Loans | 56-1 | Related Party Transactions note |
| Audit Opinion | 56-1 | Auditor's Report |

---

## 9. Risks & Warning Signs

### Major Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| **Value Trap** | High | High | Require catalyst, check business viability |
| **Governance Issues** | Medium | Very High | RPT check, board independence |
| **Liquidity Risk** | Medium | Medium | Free float > 20%, daily volume check |
| **Extended Holding Period** | High | Medium | Patience required, opportunity cost |
| **Business Deterioration** | Medium | High | Check earnings trend, not just assets |
| **Fraud/Accounting Issues** | Low | Very High | Audit opinion, cash flow verification |

### Warning Signs (Sell Immediately If You See These)

> [!danger] ขายทันทีถ้าเห็นสิ่งเหล่านี้

- [ ] Qualified audit opinion appears
- [ ] RPT increases to Red level (> 20% of revenue)
- [ ] Management sells significant stake
- [ ] Related party loans appear on balance sheet
- [ ] Cash flow turns negative for 2+ quarters
- [ ] Key customer or contract lost
- [ ] Regulatory investigation announced
- [ ] CEO/CFO resigns unexpectedly

### When to Exit

**Profit-Taking Exit:**
- Price reaches 90-100% of intrinsic value
- P/BV expands to sector average
- Catalyst has played out
- Position becomes > 10% of portfolio

**Stop-Loss Exit:**
- Investment thesis breaks
- Business deteriorates beyond recovery
- Governance red flags appear
- Better opportunity elsewhere

**Time-Based Exit:**
- If no catalyst after 2-3 years, reconsider position
- Opportunity cost of capital
- May rotate to better opportunity

---

## 10. Case Studies

### Case Study 1: SC Asset (SC) - Live Position

**Company Background:**
- Thai property developer
- Part of SCG ecosystem
- Focus on residential and commercial

**Entry Analysis:**
- Entry Date: 2026-03-15
- Entry Price: 2.45 THB
- Book Value: 8.10 THB
- P/BV at Entry: 0.30x (Deep Value)

**Investment Thesis:**
1. Asset-rich with undervalued land bank
2. SCG backing provides governance comfort
3. Property cycle recovery potential
4. Significantly below liquidation value

**Key Metrics at Entry:**
| Metric | Value | Assessment |
|--------|-------|------------|
| P/BV | 0.30x | Deep Value |
| NCAV/Price | 1.5x | Asset backing |
| Debt/Equity | 0.8x | Manageable |
| Free Float | 25% | Adequate |
| RPT Level | Green (< 10%) | Governance OK |

> [!info] Current Status
> - Status: **Live Position - Not Yet Resolved**
> - Holding Period: ~2 weeks (as of 2026-04-02)
> - Catalyst Wait: Property cycle recovery, asset monetization

**Lessons So Far:**
- Asset-based valuation works for property
- Parent company backing reduces governance risk
- Patience required for cycle recovery

---

### Case Study 2: Value Trap Example (Hypothetical)

**Company:** Thai Manufacturing Company (hypothetical)

**Initial Screen:**
- P/BV: 0.4x
- P/E: 4x
- Looked attractive

**What Went Wrong:**
1. Industry in structural decline (not cyclical)
2. Management was expropriating value via RPT
3. Assets were obsolete, not saleable
4. Earnings were declining, not recovering

**Red Flags Missed:**
- RPT was 25% of revenue (Red level - too high)
- CEO was also Chairman
- Inventory obsolescence not recognized
- No catalyst identified

> [!danger] Loss: 40% over 2 years

**Lessons:**
- Cheap can get cheaper
- Check WHY it's cheap
- Governance matters more than metrics
- Structural decline != cyclical downturn

---

### Case Study 3: DELTA - Governance Over Metrics

**Background:**
- Delta Electronics Thailand
- AI/Data Center tailwinds
- Strong growth story

**The Divergence:**
| AI Assessment | Score | Key Reason |
|---------------|-------|------------|
| Gemini | 84 (BUY) | Growth story, AI tailwinds |
| Codex | 38 (PASS) | Gate 0 FAIL |

> [!warning] ทำไม Codex บอก PASS (Gate 0 Methodology)
> 1. No SET ESG Rating 2025 - Fails governance baseline
> 2. Free Float only 23.57% - Borderline liquidity risk
> 3. Connected transaction risks - RPT concerns
> 4. Governance concerns outweigh growth potential

**Gate 0 Explained:**
Gate 0 is a knockout criteria system that MUST pass before any valuation analysis. It screens for:
- SET ESG Rating exists (any rating = pass)
- Free Float >= 20%
- No trading warnings
- Clean audit opinion

If ANY Gate 0 criterion fails, the stock is rejected regardless of how attractive the valuation metrics appear.

> [!success] Lesson for Deep Value
> - Even great businesses can be poor investments
> - Governance checks BEFORE valuation
> - Growth does not compensate for governance risk
> - Thai market requires extra caution

---

## 11. Related Concepts

### Directly Related

- **[[Value Investing]]** - Parent philosophy
- **[[Dividend Play]]** - Often overlaps (cheap + yield)
- **[[Asset Play]]** - Specific focus on asset value
- **[[Net-Net]]** - Graham's original deep value formula

### Complementary Strategies

- **[[Quality GARP]]** - For balancing portfolio
- **[[Quality Swing Investor]]** - Uses deep value as entry signal
- **[[Special Situations]]** - Catalyst-focused variant

### Opposing Approaches

- **[[Growth Investing]]** - Pay up for growth vs. discount for value
- **[[Momentum Investing]]** - Follow trends vs. contrarian

### Key Thinkers

- **Benjamin Graham** - Father of value investing, NCAV formula
- **Warren Buffett** - Early cigar butt, later quality at fair price
- **Seth Klarman** - Margin of Safety, deep value practitioner
- **Howard Marks** - Contrarian thinking, market cycles

---

## 12. References

### Books

1. **The Intelligent Investor** - Benjamin Graham
   - Chapter 14: Stock Selection for Defensive Investor
   - Original NCAV formula

2. **Security Analysis** - Graham & Dodd
   - Asset valuation principles
   - Balance sheet analysis

3. **Margin of Safety** - Seth Klarman
   - Risk-averse value investing
   - Deep value philosophy
   - Note: Out of print. Excerpts available online; alternative: "The Manual of Ideas" by John Mihaljevic

4. **Contrarian Investment Strategies** - David Dreman
   - Psychology of value investing
   - Mean reversion evidence

### Research Papers

1. **"The Cross-Section of Expected Stock Returns"** - Fama & French
   - Value factor evidence

2. **"Value vs. Growth: The International Evidence"** - Capaul et al.
   - Global value premium

### Thai Market Resources

1. **SET Factsheet** - Company financial metrics
   - URL: https://www.set.or.th/en/company/stock-info.html
2. **56-1 Annual Reports** - Governance and RPT data
   - URL: https://www.set.or.th/en/company/listed.html
3. **SEC Thailand** - Regulatory filings
   - URL: https://www.sec.or.th/EN/
4. **SET ESG Ratings** - Corporate governance assessment
   - URL: https://www.set.or.th/en/market/initiatives/sustainability.html

### Websites

- **SET Or Bor Jor** - SET official data (https://www.set.or.th)
- **SEC Thailand** - Regulatory information (https://www.sec.or.th)
- **GuruFocus** - Value screening tools
- **Old School Value** - NCAV calculator

---

## Quick Reference Card

### Key Formulas

| Metric | Formula | Deep Value Threshold |
|--------|---------|---------------------|
| P/BV | Price / BVPS | < 0.5x |
| NCAV | (CA - TL) / Shares | Price < 0.67 × NCAV |
| NNWC | (Cash + 0.75×AR + 0.5×Inv - TL) / Shares | Price < NNWC |
| P/E | Price / EPS | < 50% sector avg |
| EV/EBITDA | (MktCap + Debt - Cash) / EBITDA | < 4x |
| FCF Yield | FCF / Price | > 10% |

### Checklist Summary

1. **Gate 0:** ESG rating + Free Float > 20% + No warnings + Clean audit
2. **Quantitative:** P/BV < 0.5x + NCAV positive + Balance sheet healthy
3. **Qualitative:** Business viable + Governance clean + Catalyst exists
4. **Entry:** 30% margin of safety + Liquidity + Portfolio fit

### RPT Risk Levels

| Level | RPT % of Revenue | Action |
|-------|------------------|--------|
| Green | < 10% | Proceed with normal DD |
| Yellow | 10-20% | Investigate deeply |
| Red | > 20% | Avoid |

> [!success] Thai Market Golden Rules
> 1. Always check RPT in 56-1
> 2. Require independent directors
> 7. Free float must be > 20%
> 8. Trust but verify audit quality
> 9. Governance over metrics

---

*Created: 2026-03-27 | Version: v3 (Evergreen)*
*Author: Professor Damodaran (Thai Editor)*
*Review: Gemini Round 1 Complete (78/100)*
*Collaborators: Claude (Orchestrator), Codex (Drafter), Gemini (Reviewer)*
