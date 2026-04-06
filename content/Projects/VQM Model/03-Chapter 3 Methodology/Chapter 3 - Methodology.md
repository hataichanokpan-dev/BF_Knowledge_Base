---
title: "Chapter 3 — Methodology"
aliases: ["VQM Methodology", "ระเบียบวิธีวิจัย VQM", "VQM Research Methodology"]
tags: [📁/projects, 🏷️/thesis, 🏷️/vqm-model, 🏷️/methodology, status/draft]
created: 2026-04-06
modified: 2026-04-06
type: chapter
status: seedling
links:
  - "[[VQM Model - Thesis Research Plan]]"
  - "[[VQM Model - Factor Calculation Formulas]]"
  - "[[VQM Model - Backtesting Framework]]"
  - "[[Complete Reference List]]"
---

# Chapter 3 — Methodology

> [!ABSTRACT] ระเบียบวิธีวิจัยสำหรับ VQM Model — โมเดลผสานมูลค่า-คุณภาพ-โมเมนตัม
>
> **วัตถุประสงค์:** อธิบายกรอบการวิจัย นิยามปัจจัย และขั้นตอนการทดสอบโมเดล
> **Market:** SET (Stock Exchange of Thailand) | **Period:** 2019-2024

---

## 3.1 ภาพรวมระเบียบวิธีวิจัย (Research Overview)

### 3.1.1 แนวทางการวิจัย (Research Approach)

วิทยานิพนธ์นี้ใช้ **Quantitative Research Approach** โดยอาศัยข้อมูลเชิงประจักษ์จากตลาดหุ้นไทยเพื่อ:

1. **สร้างโมเดล VQM** — รวมปัจจัย Value, Quality, Momentum
2. **ทดสอบประสิทธิภาพ** — เปรียบเทียบกับ benchmark และ single-factor strategies
3. **วิเคราะห์ความทนทาน** — ทดสอบใน market regimes ต่างกัน

```
┌─────────────────────────────────────────────────────────────────┐
│  RESEARCH FLOW                                                  │
│                                                                 │
│  Data Collection → Factor Calculation → Scoring → Backtesting  │
│         ↓              ↓               ↓           ↓            │
│     PIT Data        Z-score      Composite    Performance      │
│     2019-2024      Normalization   VQM Score    Analysis        │
└─────────────────────────────────────────────────────────────────┘
```

### 3.1.2 คำถามวิจัย (Research Questions)

| ID | คำถามวิจัย | ตัวแปรที่ใช้ |
|----|-------------|----------------|
| **RQ1** | พอร์ต VQM ให้ผลตอบแทนปรับความเสี่ยงสูงกว่า benchmark หรือไม่? | Sharpe, Alpha, IR |
| **RQ2** | การผสาน 3 ปัจจัยดีกว่า single-factor strategy หรือไม่? | Portfolio comparison |
| **RQ3** | โมเดลทนทานต่อการเปลี่ยนแปลงของ market regime หรือไม่? | Regime analysis |
| **RQ4** | ผลตอบแทนสุทธิหลัง transaction costs ยังเป็นบวกหรือไม่? | Net return |
| **RQ5** | ปัจจัยไหนมีสัดส่วนสำคัญที่สุดต่อ performance ของโมเดล? | Factor attribution |

---

## 3.2 ข้อมูลและกลุ่มตัวอย่าง (Data & Sample)

### 3.2.1 แหล่งข้อมูล (Data Sources)

| ข้อมูล | แหล่งที่มา | ความถี่ | หมายเหตุ |
|---------|-------------|---------|-----------|
| **ราคาหุ้น, Volume** | SET Data, Bloomberg | Daily | Adjusted close price |
| **Financial Statements** | SET, Company Filings | Quarterly | PIT data |
| **Index Data** | SET Index, SET50, SET100 | Daily | Benchmark |
| **Risk-free Rate** | BOT, Treasury Bill | Daily | 3-month T-Bill |
| **Sector Classification** | SET Sector List | Static | GICS standard |

### 3.2.2 กลุ่มตัวอย่าง (Sample Selection)

**Inclusion Criteria:**
- จดทะเบียนใน SET (ไม่รวม MAI)
- มีข้อมูลครบถ้วนตั้งแต่ Q1/2019
- Average Daily Volume > 20 ล้านบาท
- Market Capitalization > 5,000 ล้านบาท

**Exclusion Criteria:**
- หุ้นประกันภัย (Insurers) — โครงสร้างการเงินแตกต่าง
- หุ้นเทคนิคพิเศษ (REITs, DR, NVDR) — ไม่ใช่ common stock
- หุ้นที่ถูก suspend > 6 เดือน

**Final Universe:** ~250-300 หุ้น (จาก ~600+ ใน SET)

### 3.2.3 Point-in-Time (PIT) Data

> [!WARNING] Look-ahead Bias Prevention
> การใช้ข้อมูลที่ "รู้ผลล่วงหน้า" จะทำให้ผลการทดสอบเกินจริง
>
> **Solution:** ใช้ข้อมูลณ เวลานั้น (PIT) เท่านั้น

```
Example: รายงาน Q1/2020 ประกาศเดือน พ.ค. 2020
- ❌ Wrong: ใช้ data ตั้งแต่ 1 ม.ค. 2020
- ✅ Right: ใช้ตั้งแต่ 1 มิ.ย. 2020 (หลังจากประกาศ)
```

---

## 3.3 นิยามปัจจัย (Factor Definitions)

### 3.3.1 Value Factor (45%)

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **FCF Yield** | Free Cash Flow / Enterprise Value | ยิ่งสูง = ถูก |
| **P/E Relative** | (P/E) / Median(P/E, Sector) | < 1 = ถูกกว่าค่าเฉลี่ย |
| **P/B Relative** | (P/B) / Median(P/B, Sector) | < 1 = ถูกกว่าค่าเฉลี่ย |
| **EV/EBITDA** | Enterprise Value / EBITDA | ยิ่งต่ำ = ถูก |

**สูตรคำนวณ Value Score:**
```
Value_Score = Mean(Z_score(FCF Yield), Z_score(P/E Relative * -1),
                  Z_score(P/B Relative * -1), Z_score(EV/EBITDA * -1))
```

### 3.3.2 Quality Factor (35%)

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **ROIC - WACC** | Return on Invested Capital - WACC | > 0 = สร้างมูลค่า |
| **FCF Conversion** | Free Cash Flow / Net Income | ยิ่งสูง = คุณภาพกำไร |
| **Debt/EBITDA** | Total Debt / EBITDA | ยิ่งต่ำ = สุขภาพดี |
| **Gross Margin** | (Revenue - COGS) / Revenue | ยิ่งสูง = competitive advantage |

**สูตรคำนวณ Quality Score:**
```
Quality_Score = Mean(Z_score(ROIC - WACC), Z_score(FCF Conversion),
                      Z_score(Debt/EBITDA * -1), Z_score(Gross Margin))
```

### 3.3.3 Momentum Factor (20%)

| Metric | Formula | Interpretation |
|--------|---------|----------------|
| **Price 6M** | (Price_t / Price_t-6M) - 1 | ยิ่งสูง = uptrend |
| **Earnings Revision** | (EPS_Est_Current / EPS_Est_3M) - 1 | ยิ่งบวก = positive revision |
| **Volume Trend** | Volume_MA(20) / Volume_MA(60) | > 1 = หนุนการเคลื่อนไหว |

**สูตรคำนวณ Momentum Score:**
```
Momentum_Score = Mean(Z_score(Price 6M), Z_score(Earnings Revision),
                        Z_score(Volume Trend))
```

### 3.3.4 Z-score Normalization

```
Z_score(i, k, t) = (X(i, k, t) - Median_t) / (1.4826 × MAD_t)

เมื่อ:
- X(i, k, t) = ค่า metric k ของหุ้น i ณ เวลา t
- Median_t = ค่ามัธยฐานของ metric k ณ เวลา t
- MAD_t = Median Absolute Deviation ณ เวลา t
- 1.4826 = ค่าปรับจาก MAD เป็น SD (สำหรับ normal distribution)
```

### 3.3.5 Composite VQM Score

```
VQM_Score(i, t) = 0.45 × Value_Score(i, t) +
                  0.35 × Quality_Score(i, t) +
                  0.20 × Momentum_Score(i, t)
```

**Weight Rationale:**
- **Value 45%** — พื้นฐานการลงทุน มี evidence มากที่สุด
- **Quality 35%** — ลดความเสี่ยง "value trap"
- **Momentum 20%** — ช่วย timing entry/exit แต่ใช้น้อยเพื่อลด crash risk

---

## 3.4 การสร้างพอร์ต (Portfolio Construction)

### 3.4.1 Portfolio Selection

```
Step 1: คำนวณ VQM Score สำหรับทุกหุ้น
Step 2: Rank จากสูงไปต่ำ
Step 3: เลือก Top N หุ้น (N = 20, 25, 30 สำหรับ sensitivity)
Step 4: กำหนด weight แก่แต่ละหุ้น
```

### 3.4.2 Weighting Schemes

| Scheme | Formula | ข้อดี | ข้อเสีย |
|--------|---------|--------|----------|
| **Equal Weight** | 1/N | Simple, ไม่ bias toward large cap | ไม่สะท้อน conviction |
| **Score Weight** | w_i = Score_i / Σ(Score) | ให้ weight ตาม quality | มี concentration risk |
| **Optimized** | Mean-Variance optimization | พิจารณา risk | ใช้ covariance, unstable |

**หลักการ:** เริ่มด้วย Equal Weight (baseline) แล้วทดสอบ sensitivity

### 3.4.3 Constraints

```
Max Weight per Stock ≤ 5%
Max Weight per Sector ≤ 10%
Min Stock in Portfolio ≥ 20
```

---

## 3.5 การทดสอบย้อนหลัง (Backtesting Protocol)

### 3.5.1 Walk-Forward Analysis

```
┌─────────────────────────────────────────────────────────────┐
│  WALK-FORWARD FRAMEWORK                                     │
│                                                             │
│  ┌─────┬─────┬─────┬─────┬─────┬─────┬─────┬─────┐        │
│  │Training│Test│Training│Test│Training│Test│Training│Test│ ...
│  └─────┴─────┴─────┴─────┴─────┴─────┴─────┴─────┘        │
│    ↓              ↓              ↓              ↓          │
│  Q1/19 Q2/19 Q3/19 Q4/19 Q1/20 Q2/20 Q3/20 Q4/20          │
└─────────────────────────────────────────────────────────────┘
```

**Procedure:**
1. **Training Period:** ใช้ข้อมูล 12 เดือนย้อนหลังเพื่อคำนวณ factors
2. **Test Period:** สร้างพอร์ต แล้ว hold 3 เดือน
3. **Roll Forward:** เลื่อนหน้าต่าง 3 เดือน ทำซ้ำ

### 3.5.2 Rebalancing Rules

| Parameter | Value | เหตุผล |
|-----------|-------|---------|
| **Frequency** | Quarterly | Balance between turnover & cost |
| **Rebalance Date** | 1st trading day of quarter | Consistency |
| **Execution Price** | Open price of rebalance day | Realistic execution |

### 3.5.3 Transaction Costs

```
Cost Model = 0.25% per leg (buy/sell)
Total Round-trip Cost = 0.50%

Components:
- Commission: 0.15% (SET fee + broker fee)
- Slippage: 0.10% (market impact estimate)
```

### 3.5.4 Performance Measurement

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| **Total Return** | (P_t - P_0) / P_0 | SET Index |
| **Sharpe Ratio** | (R_p - R_f) / σ_p | SET Index |
| **Sortino Ratio** | (R_p - R_f) / σ_downside | SET Index |
| **Max Drawdown** | Max(Peak - Trough) / Peak | N/A |
| **Information Ratio** | α_p / Tracking Error | N/A |
| **Hit Rate** | Win / (Win + Loss) | N/A |

---

## 3.6 การทดสอบทางสถิติ (Statistical Tests)

### 3.6.1 Alpha Significance Test

```
H0: α = 0 (ไม่มี excess return)
H1: α ≠ 0 (มี excess return)

t-statistic = α̂ / SE(α̂)

Reject H0 if |t-stat| > 1.96 (p < 0.05)
```

### 3.6.2 Comparison Tests

| Test | Purpose | Variables |
|------|---------|-----------|
| **Paired t-test** | เปรียบเทียบ VQM vs SET | Monthly returns |
| **Wilcoxon Signed-rank** | Non-parametric comparison | Monthly returns |
| **F-test** | เปรียบเทียบ variance | Volatility |

### 3.6.3 Factor Attribution Analysis

```
R_p - R_f = α + β_mkt(R_mkt - R_f) + β_SMB SMB + β_HML HML + β_RMW RMW + ε

เมื่อ:
- α = Jensen's Alpha (skill)
- β_mkt = Market beta
- β_SMB = Size factor loading
- β_HML = Value factor loading
- β_RMW = Quality factor loading
```

---

## 3.7 การวิเคราะห์ Market Regime (Regime Analysis)

### 3.7.1 Regime Definition

| Regime | Condition | Periods (2019-2024) |
|--------|-----------|---------------------|
| **Bull** | SET Index MA(6) > MA(12) + 5% | 2019, 2020 Q3-Q4, 2021-2022 |
| **Bear** | SET Index MA(6) < MA(12) - 5% | 2020 Q1-Q2 (COVID) |
| **Sideways** | Other | Transition periods |

### 3.7.2 Regime Performance Comparison

```
For each regime:
- Compute cumulative return
- Compute volatility
- Compute Sharpe ratio
- Compare with benchmark
```

---

## 3.8 การวิเคราะห์ Sensitivity (Sensitivity Analysis)

### 3.8.1 Parameter Variations

| Parameter | Base Case | Variation 1 | Variation 2 |
|-----------|-----------|-------------|-------------|
| **Portfolio Size** | 25 stocks | 20 stocks | 30 stocks |
| **VQM Weights** | 45/35/20 | 50/30/20 | 40/40/20 |
| **Rebalance** | Quarterly | Semi-annual | Monthly |
| **Transaction Cost** | 0.50% | 0.30% | 0.75% |

### 3.8.2 Robustness Checks

```
1. Sub-period analysis (2019-2021 vs 2022-2024)
2. Sector-neutral test (control sector bias)
3. Liquidity filter test (ADV > 10M vs > 20M)
```

---

## 3.9 ข้อจำกัดและข้อสันนิษฐาน (Limitations & Assumptions)

### 3.9.1 ข้อสันนิษฐานหลัก

| Assumption | Justification |
|------------|---------------|
| **Past factors predict future returns** | Supported by literature |
| **Transaction costs are 0.50%** | Conservative estimate |
| **Market prices reflect available information** | EMH semi-strong form |
| **No survivorship bias** | Using PIT data |

### 3.9.2 ข้อจำกัด

1. **Data Constraints:** บางหุ้นมีข้อมูลไม่ครบในช่วงต้น period
2. **Model Risk:** ปัจจัยที่เลือกอาจไม่ครอบคลุมทุก dimension
3. **Execution Risk:** การซื้อขายจริงอาจมี slippage มากกว่าที่สมมติ
4. **Market Condition:** ผลการทดสอบอาจไม่สามารถ generalization ไปยังสภาพตลาดอื่น

---

## 3.10 บทสรุปภาค (Chapter Summary)

บทนี้อธิบายระเบียบวิธีวิจัยสำหรับ VQM Model ซึ่งประกอบด้วย:

1. **Data & Sample** — SET 2019-2024, PIT data, ~250-300 หุ้น
2. **Factor Definitions** — Value (4 metrics), Quality (4 metrics), Momentum (3 metrics)
3. **Scoring** — Z-score normalization, Composite VQM Score
4. **Portfolio Construction** — Top 20-30 stocks, Equal-weight baseline
5. **Backtesting** — Walk-forward, Quarterly rebalancing, 0.50% transaction cost
6. **Statistical Tests** — Alpha significance, Comparison tests, Factor attribution
7. **Regime Analysis** — Bull/Bear market performance
8. **Sensitivity** — Parameter variations, Robustness checks

บทต่อไป (Chapter 4) จะนำเสนอผลการทดสอบ

---

## References

(ดึงจาก Complete Reference List)

---

## 🔗 Linked References

- [[VQM Model - Factor Calculation Formulas]] — สูตรคำนวณรายละเอียด
- [[VQM Model - Backtesting Framework]] — เฟรมเวิร์กการทดสอบ
- [[Complete Reference List]] — รายการอ้างอิงครบถ้วน

---

*Document created: 2026-04-06*
*Status: Methodology Draft — Ready for implementation*
