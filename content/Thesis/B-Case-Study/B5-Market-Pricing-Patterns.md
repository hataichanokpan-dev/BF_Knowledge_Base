# B5: Market Pricing Patterns — ตลาดตั้งราคา ROIC-WACC Spread อย่างไร?

> **Research Question:** ตลาดตั้งราคาหุ้นตาม ROIC-WACC Spread อย่างมีประสิทธิภาพหรือไม่? มีโอกาส mispricing ตรงไหน?
> **Source:** Academic + Practitioner Research Synthesis
> **Date:** 2026-04-01

---

## 📊 Executive Summary

> [!tip] Core Finding
> ตลาดมี **Semi-Efficient Pricing** ต่อ ROIC-WACC Spread — เข้าใจ concept แต่มี lag และ bias อย่างเป็นระบบ

**4 โอกาส Mispricing หลัก:**
1. **Timing Lag** — ใช้เวลา 12-24 เดือนกว่า spread เปลี่ยนจะสะท้อนในราคา
2. **Analyst Inertia** — Consensus estimates ปรับช้า
3. **Growth Bias** — ตลาดให้ราคา high-growth/low-ROIC สูงเกินไป
4. **Sector Blind Spots** — เปรียบเทียบข้าม sector ผิดพลาด

---

## 1. หลักฐาน Market Efficiency

### 1.1 Academic Consensus

> [!info] งานวิจัยหลัก

| Study | สรุป | ผลกระทบ |
|-------|------|---------|
| **Ohlson (1995)** | Residual income อธิบาย 70-80% ของ market value | ตลาดเข้าใจ concept |
| **Feltham-Ohlson (1995)** | Framework เชื่อม spread กับ intrinsic value | ฐานทางทฤษฎีแข็งแกร่ง |
| **Frankel & Lee (1998)** | Residual income model ทำนาย 1-year returns (R² = 0.15) | มี predictive power |
| **Biddle et al. (1997)** | EVA เพิ่มข้อมูลน้อย vs earnings | ตลาดอาจ priced in แล้ว |

### 1.2 คำถาม: Priced In แล้วหรือยัง?

> [!abstract] คำตอบสั้น: **Partially, but with lag and noise**

**หลักฐานสนับสนุน Efficiency:**
- หุ้น ROIC สูง ซื้อขายที่ premium multiples (P/E, EV/EBITDA)
- ตลาด reward positive spread announcements
- Analysts track ROIC ใน models

**หลักฐานสนับสนุน Inefficiency:**
- **Timing lag:** 6-18 เดือนกว่า spread เปลี่ยนจะสะท้อน
- **Overreaction:** ตลาดให้น้ำหนัก ROIC changes ล่าสุดมากเกินไป
- **Growth confounding:** High-growth firms ที่มี negative spreads มัก overvalued

### 1.3 Persistence Premium

> [!quote] Novy-Marx (2013)
> "Profitability factor (gross profits-to-assets) generates significant alpha"

**ความหมาย:** ตลาด **underestimate persistence** ของ high ROIC
- บริษัทใน top ROIC quintile มีโอกาส 70% อยู่ที่เดิมปีถัดไป
- ตลาด priced ในแค่ 50% persistence
- **Gap นี้ = Opportunity**

---

## 2. โอกาส Mispricing

### 2.1 เมื่อไรตลาดตั้งราคาผิด?

| Scenario | ประเภท Mispricing | โอกาส |
|----------|-------------------|-------|
| **[[ROIC Inflection Point]]** | ตลาดช้ารับรู้การปรับปรุง | ซื้อตอน ROIC ข้าม WACC |
| **Sector Rotation** | Cross-sector comparison ผิดพลาด | ซื้อ high-spread ใน sector ที่ไม่ได้รับความนิยม |
| **Earnings Miss + ROIC Stable** | ตลาด overreact ต่อ EPS ไม่สน spread | ซื้อตอน selloff จาก earnings |
| **Capex Cycle Peak** | ตลาดลงโทษ investment ไม่เห็น future ROIC | ซื้อตอน capex ลดลง |
| **Cyclical Trough** | ROIC ต่ำแต่ moat ยัง intact | ซื้อ cyclicals ตอน cycle bottom |

### 2.2 Quality at Reasonable Price (QARP)

> [!quote] Asness, Frazzini, Israel (2018) - AQR Research
> "Quality stocks (high ROIC, low leverage, stable earnings) outperform when bought at reasonable valuations"

| Strategy | Alpha ต่อปี |
|----------|-------------|
| Pure Quality Factor | 0.5-1.0% |
| **Quality + Value Constraint** | **2-4%** |

> [!important] บทเรียน
> **Spread อย่างเดียวไม่พอ** — ต้องผสมกับ [[Valuation Discipline]]

### 2.3 The Growth Trap

> [!warning] หลักฐานจาก Lakonishok, Shleifer, Vishny (1994)

| Category | Future Returns | การตั้งราคาของตลาด |
|----------|---------------|-------------------|
| High Growth, High ROIC | Moderate | Fairly valued |
| **High Growth, Low ROIC** | **Poor** | **Overvalued** |
| **Low Growth, High ROIC** | **Strong** | **Undervalued** |
| Low Growth, Low ROIC | Poor | Fairly valued |

> [!danger] สรุป
> ตลาดจ่ายเกินไปสำหรับ growth แต่ underestimate profitable mature businesses

---

## 3. Timing Analysis

### 3.1 ใช้เวลานานแค่ไหน?

> [!info] Research Findings

| Study | Horizon | สรุป |
|-------|---------|------|
| Frankel & Lee (1998) | 12-24 เดือน | Residual income ทำนาย returns 1-2 ปี |
| Dechow et al. (1999) | 6-18 เดือน | ตลาดค่อยๆ incorporate ROIC |
| Novy-Marx (2013) | 12-36 เดือน | Profitability factor returns คงอยู่หลายปี |

> [!tip] บทเรียน
> ROIC-WACC Spread เป็น **Medium-Term Signal (6-24 เดือน)** ไม่ใช่ short-term

### 3.2 Catalysts เร่งการตั้งราคา

| Catalyst | Effect |
|----------|--------|
| **Earnings Revision** | Analysts upgrade forecasts |
| **Management Guidance** | สื่อสาร ROIC targets ชัดเจน |
| **Activist Involvement** | บังคับให้เปลี่ยน capital allocation |
| **Dividend/Buyback Increase** | ส่งสัญญาณ confidence ใน spread |
| **M&A Announcement** | Acquirer's spread มักถูก reward |

### 3.3 Mean Reversion Timeline

> [!quote] Mauboussin (2006)

| Initial ROIC Decile | Year 1 | Year 3 | Year 5 | Year 10 |
|---------------------|--------|--------|--------|---------|
| Top 10% | 20%+ | 18% | 15% | 12% |
| Bottom 10% | 5% | 8% | 10% | 10% |

> [!important] บทเรียน
> Mean reversion เป็น **ช้า** — ใช้เวลา 5-10 ปี
> ทำให้มี multi-year window ในการ exploit spread anomalies

---

## 4. Moderating Factors

### 4.1 Growth Interaction

#### ROIC-Growth Matrix

|  | High ROIC | Low ROIC |
|---|-----------|----------|
| **High Growth** | [[Value Creation]] (ถ้า ROIC > WACC) | [[Growth Trap]] (value destruction) |
| **Low Growth** | [[Cash Cow]] (undervalued opportunity) | [[Value Trap]] (avoid) |

> [!tip] Key Finding
> **Growth amplifies spread effect** — แต่ต้องเป็นกรณีที่ ROIC > WACC

### 4.2 Risk Factors

| Factor | Effect on Predictive Power |
|--------|---------------------------|
| **High Leverage** | เพิ่ม volatility ลด reliability |
| **High Beta** | Market sensitivity ครอบ spread signal |
| **Small Cap** | Noise เพิ่ม แต่ alpha potential สูง |
| **Low Liquidity** | Inefficiencies คงอยู่นานกว่า |

### 4.3 Sector Effects

| Sector | Spread Predictiveness | เหตุผล |
|--------|----------------------|--------|
| **Industrials** | High | Capital-intensive, moats ชัดเจน |
| **Consumer Staples** | High | Stable ROIC, predictable spreads |
| **Financials** | Medium | ROIC definition แตกต่าง |
| **Technology** | Low | Growth ครอบ, intangible assets |
| **Utilities** | Low | Regulated returns, limited spread variation |
| **Energy** | Low | Commodity price volatility |

> [!tip] บทเรียน
> **ใช้ Sector-Relative Spreads** ไม่ใช่ absolute

### 4.4 Sentiment Interaction

> [!quote] Baker & Wurgler (2006)

| Market Sentiment | High ROIC Stocks | Low ROIC Stocks |
|------------------|------------------|-----------------|
| **High (Bull Market)** | Underperform (overvalued) | Outperform (speculation) |
| **Low (Bear Market)** | **Outperform (flight to quality)** | Underperform (distress risk) |

> [!important] Strategy Implication
> High-spread strategy **work best ตอน sentiment ต่ำ**

---

## 5. Practical Screening Framework

### 5.1 4-Step Screening Process

```
┌─────────────────────────────────────────────────────────────────┐
│              ROIC-WACC SPREAD SCREENING FRAMEWORK                │
└─────────────────────────────────────────────────────────────────┘

STEP 1: SPREAD FILTER
─────────────────────
• ROIC - WACC > 3% (absolute)
• Spread vs Sector: Top 30%
• Output: 30-40 stocks from SET 100

STEP 2: PERSISTENCE FILTER
──────────────────────────
• Positive spread 3+ consecutive years
• Trend: Current > 3Y average
• Output: 15-20 stocks

STEP 3: VALUATION FILTER
────────────────────────
• P/E vs Sector < 1.0x
• EV/EBITDA vs Sector < 1.0x
• P/Fair Value < 0.9
• Output: 8-12 stocks

STEP 4: QUALITY FILTER
──────────────────────
• Debt/EBITDA < 3.0x
• Interest Coverage > 5.0x
• Earnings Stability: StdDev < 20%
• Output: 5-8 stocks → Deep dive 3-5 stocks
```

### 5.2 Entry Rules

| Signal | Criteria |
|--------|----------|
| **Spread Improving** | ROIC - WACC > 3% และ rising |
| **Valuation Attractive** | Below intrinsic or sector median |
| **Momentum** | Positive earnings revisions |
| **Catalyst** | New product, M&A, restructuring |

### 5.3 Exit Rules

| Signal | Criteria |
|--------|----------|
| **Spread Compress** | Below 1% |
| **Overvaluation** | Price > Fair Value 20%+ |
| **Quality Deteriorate** | Earnings quality issues |
| **Moat Erode** | Competitive position weakens |

### 5.4 Position Sizing

| Conviction Level | Criteria | Position Size |
|------------------|----------|---------------|
| **High** | 5%+ spread, 5Y persistence, catalyst | 5-8% |
| **Medium** | 3-5% spread, 3Y persistence | 3-5% |
| **Speculative** | Improving but unproven | 1-3% |

---

## 6. Thai Market Applications

### 6.1 SET-Specific Considerations

| Factor | Consideration |
|--------|---------------|
| **Data Quality** | ใช้ 5-year median, verify adjustments |
| **WACC Estimation** | เพิ่ม Thailand Country Risk Premium (2-3%) |
| **Liquidity** | Focus on SET 50-100 |
| **Sector Concentration** | เปรียบเทียบภายใน sector |
| **Family Ownership** | ระวัง [[Related Party Transactions]] |

### 6.2 Recommended Adaptations

1. **ใช้ 5-year median spread** แทน point-in-time
2. **เพิ่ม governance screen** (หลีกเลี่ยง low governance scores)
3. **Sector-neutral comparison** (ตลาดไทย concentrate ใน few sectors)
4. **Monitor insider buying** (ส่งสัญญาณ management confidence)

---

## 7. Key Research Citations

### Academic Sources

| Study | Contribution |
|-------|-------------|
| **Ohlson (1995)** | Foundational residual income model |
| **Feltham-Ohlson (1995)** | Theoretical framework for ROIC-WACC |
| **Frankel & Lee (1998)** | Empirical evidence of predictive power |
| **Novy-Marx (2013)** | Quality/profitability factor evidence |
| **Asness et al. (2018)** | Quality at reasonable price strategy |
| **Lakonishok et al. (1994)** | Growth trap evidence |

### Practitioner Sources

| Source | Contribution |
|--------|-------------|
| **Mauboussin (2006)** | Mean reversion timeline |
| **Damodaran** | Practical ROIC measurement |
| **Morningstar** | Moat identification framework |

---

## 8. Summary: Answering Research Questions

### Q1: ตลาด price efficiently ไหม?

**Answer: Semi-Efficient**
- 6-18 เดือน pricing lag
- Overreaction ต่อ growth, underreaction ต่อ persistence
- Sector comparison errors

### Q2: โอกาส mispricing คืออะไร?

**Answer: 3 Main Opportunities**
1. **[[Quality at Reasonable Price]]** — High-spread firms at reasonable valuations
2. **[[ROIC Inflection]]** — เมื่อ spread กลับเป็นบวกหรือขยายตัว
3. **[[Sentiment Extremes]]** — Quality stocks oversold ใน bear markets

### Q3: ใช้เวลานานแค่ไหน?

**Answer: 6-24 เดือน typically**
- Catalysts เร่งการตั้งราคา
- Large caps เร็วกว่า small caps
- Bear markets เร็วกว่า bull markets (flight to quality)

### Q4: ปัจจัยอะไร moderate relationship?

**Answer: 4 Key Moderators**
1. **Growth** — Amplifies effect เมื่อ ROIC > WACC
2. **Risk** — High leverage/beta ลด predictability
3. **Sector** — Effect แรงสุดใน capital-intensive, stable industries
4. **Sentiment** — Strategy work best ใน low-sentiment environments

---

## 🔗 Related Notes

- [[A1-EVA-Literature-Review]] — พื้นฐานทางวิชาการ
- [[A2-Data-Methodology]] — วิธีการคำนวณ
- [[B1-High-Spread-Companies]] — Case studies
- [[B2-Negative-Spread-Companies]] — Value destruction cases
- [[B3-Moat-Analysis-Framework]] — Moat identification
- [[B4-Value-Destruction-Analysis]] — Value trap analysis
- [[ROIC-WACC Research Design]] — Overall framework
- [[Quality Swing Investor]] — Investment philosophy
- [[Valuation Discipline]] — Price matters
- [[Growth Trap]] — ระวัง growth ที่ไม่สร้าง value
- [[Investing MOC]]

---

*Research: Academic + Practitioner Synthesis*
*Thai Adaptation: Synapse-O*
*Created: 2026-04-01*
