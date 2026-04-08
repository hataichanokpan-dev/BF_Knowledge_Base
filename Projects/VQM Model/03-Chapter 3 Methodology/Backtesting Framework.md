---
title: "กรอบการทดสอบย้อนหลัง"
aliases: ["Backtesting Framework", "กรอบการทดสอบย้อนหลัง", "Walk-Forward Analysis"]
tags: [📁/vqm-model, 🏷️/methodology, 🏷️/backtesting, 🏷️/performance]
created: 2026-04-06
modified: 2026-04-06
type: methodology
status: seedling
links:
  - "[[Methodology Framework]]"
  - "[[Factor Calculation Formulas]]"
  - "[[Complete Reference List]]"
---

# กรอบการทดสอบย้อนหลัง

> **Backtesting Methodology** — กรอบการทดสอบประสิทธิภาพโมเดล VQM ด้วยข้อมูลย้อนหลัง
>
> **อ้างอิงหลัก:** Lopez de Prado (2020), Bailey et al. (2014), Clarke et al. (2016)

---

## สารบัญ

1. [ภาพรวมการทดสอบ](#ภาพรวมการทดสอบ)
2. [Walk-Forward Analysis](#walk-forward-analysis)
3. [ต้นทุนและการจำลอง](#ต้นทุนและการจำลอง)
4. [ตัวชี้วัดประสิทธิภาพ](#ตัวชี้วัดประสิทธิภาพ)
5. [การวิเคราะห์ความเสี่ยง](#การวิเคราะห์ความเสี่ยง)
6. [การทดสอบความยั่งยืน](#การทดสอบความยั่งยืน)

---

## ภาพรวมการทดสอบ

### วัตถุประสงค์

1. ทดสอบประสิทธิภาพของโมเดล VQM ในช่วง 2019-2024
2. เปรียบเทียบกับ Benchmark (SET Index)
3. วิเคราะห์ความสามารถในการทำผลงานใน Market Regimes ต่างกัน

### ช่วงเวลาทดสอบ

| รายการ | รายละเอียด |
|----------|-------------|
| **ช่วงเวลา** | ม.ค. 2019 — ธ.ค. 2024 |
| **ความยาว** | 6 ปี (72 เดือน) |
| **ความถี่ Rebalancing** | รายไตรมาส (Quarterly) |
| **จำนวน Period** | 24 quarters |

### Market Regimes (ครอบคลุม)

| ช่วงเวลา | Regime | ลักษณะ |
|-----------|--------|---------|
| 2019 | Normal | ก่อน COVID |
| 2020 | Crisis | COVID Crash (Q1) + Recovery |
| 2021 | Recovery | Rebound |
| 2022 | Volatility | Inflation + Rate hike |
| 2023 | Normal | Post-pandemic |
| 2024 | [Current] | กำลังติดตาม |

---

## Walk-Forward Analysis

### รูปแบบการทดสอบ

```
┌─────────────────────────────────────────────────────────────────────┐
│                    WALK-FORWARD FRAMEWORK                           │
│                                                                      │
│  ┌──────────────────┐      ┌──────────────────┐                    │
│  │  Training (24M)  │  →   │  Test (3M)       │                    │
│  │                  │      │                  │                    │
│  │ • Factor calc    │      │ • Portfolio sel  │                    │
│  │ • Stock ranking  │      │ • Return track   │                    │
│  │ • Weight assign  │      │ • Risk measure   │                    │
│  └──────────────────┘      └──────────────────┘                    │
│         ↓                         ↓                                 │
│    Roll forward              Rebalance                            │
│    +3 months                 +3 months                            │
│                                                                      │
│  ┌──────────────────┐      ┌──────────────────┐                    │
│  │  Training (24M)  │  →   │  Test (3M)       │                    │
│  └──────────────────┘      └──────────────────┘                    │
│                                                                      │
│  Repeat for 24 quarters                                              │
└─────────────────────────────────────────────────────────────────────┘
```

### Parameters

| พารามิเตอร์ | ค่า | คำอธิบาย |
|---------------|-----|----------|
| **Training Period** | 24 เดือน | ใช้สำหรับคำนวณ Factors และ Rank |
| **Test Period** | 3 เดือน | ใช้สำหรับ Hold Portfolio |
| **Rolling Window** | 3 เดือน | เลื่อนหน้าตามความถี่ Rebalancing |
| **Initial Training** | ม.ค. 2017 — ธ.ค. 2018 | Pre-period |

### ขั้นตอนการทดสอบ

**Step 1: Initial Setup (ม.ค. 2019)**
1. ใช้ข้อมูล ม.ค. 2017 — ธ.ค. 2018 (24 เดือน)
2. คำนวณ Factors ทั้งหมด
3. Rank หลักทรัพย์ตาม VQM Score
4. เลือก Top 30 หลักทรัพย์

**Step 2: First Test (ม.ค. 2019 — มี.ค. 2019)**
1. Hold Portfolio ที่เลือก
2. Track ผลตอบแทนรายเดือน
3. คำนวณ Transaction Costs

**Step 3: Rebalance (เม.ย. 2019)**
1. เลื่อน Training Period: เม.ย. 2017 — มี.ค. 2019
2. คำนวณ Factors ใหม่
3. Rank และ Rebalance Portfolio

**Step 4: Repeat**
- ทำซ้ำทุกไตรมาส
- สิ้นสุด: ธ.ค. 2024

---

## ต้นทุนและการจำลอง

### Transaction Costs

| รายการ | ค่าต้นทุน | รายละเอียด |
|----------|------------|-------------|
| **ค่าธรรมเนียมซื้อ** | 0.15% | ตามอัตรา SET |
| **ค่าธรรมเนียมขาย** | 0.15% | ตามอัตรา SET |
| **Slippage** | 0.10% | Market Impact |
| **Stamp Duty** | 0.10% | ภาษีการซื้อขาย |
| **VAT** | 7% | บนค่าธรรมเนียม |
| **รวม Round-trip** | **~0.50%** | ซื้อ + ขาย |

**สูตร Net Return:**
```
Net_Return = Gross_Return - Transaction_Costs
```

### Slippage Model

**Assumption:**
- Large-cap: 0.05% slippage
- Mid-cap: 0.10% slippage
- Small-cap: 0.15% slippage

**สูตร:**
```
Execution_Price = Market_Price × (1 ± Slippage_Rate)
```

---

## ตัวชี้วัดประสิทธิภาพ

### Return Metrics

| ตัวชี้วัด | สูตร | เป้าหมาย |
|-----------|------|----------|
| **CAGR** | (Final/Initial)^(1/n) - 1 | > SET |
| **Alpha (p.a.)** | Return_p - Return_bench | > 3% |
| **Cumulative Return** | Π(1 + R_t) - 1 | Positive |
| **Monthly Avg Return** | Σ(R_t) / n | > SET |

### Risk-Adjusted Metrics

| ตัวชี้วัด | สูตร | เป้าหมาย |
|-----------|------|----------|
| **Sharpe Ratio** | (R_p - R_f) / σ_p | > 1.0 |
| **Sortino Ratio** | (R_p - R_f) / σ_downside | > 1.5 |
| **Information Ratio** | Alpha / Tracking_Error | > 0.5 |
| **Treynor Ratio** | (R_p - R_f) / β_p | High |

### Drawdown Metrics

| ตัวชี้วัด | สูตร | เป้าหมาย |
|-----------|------|----------|
| **Max Drawdown** | Max(Peak - Trough) / Peak | < -25% |
| **Avg Drawdown** | Σ(DD_i) / Count | Low |
| **Recovery Time** | Days from DD to Peak | Short |

---

## การวิเคราะห์ความเสี่ยง

### Volatility Analysis

**สูตร:**
```
σ_monthly = Std(Returns_monthly)
σ_annualized = σ_monthly × √12
```

### Beta Calculation

**สูตร:**
```
β = Cov(R_p, R_m) / Var(R_m)
```

**รายละเอียด:**
- R_p = ผลตอบแทนพอร์ต VQM
- R_m = ผลตอบแทนตลาด (SET Index)

### Correlation Analysis

**Asset Correlation:**
```
ρ_i,j = Cov(R_i, R_j) / (σ_i × σ_j)
```

**Factor Correlation:**
```
 corr(Value, Quality) ≈ -0.3  (จาก Literature)
 corr(Value, Momentum) ≈ -0.6 (จาก Asness 2013)
```

---

## การทดสอบความยั่งยืน

### Regime Analysis

| Regime | นิยาม | การทดสอบ |
|--------|--------|----------|
| **Bull** | SET > +10% YoY | ผลตอบแทนเกิน SET |
| **Bear** | SET < -10% YoY | Downside Protection |
| **High Vol** | VIX-SET > 20 | Consistency |
| **Low Vol** | VIX-SET < 15 | Steady Return |

### Statistical Tests

**t-test for Alpha:**
```
t = (α̂ - 0) / SE(α̂)
```

**Critical Value (95% CI):** t > 1.96

**Hypothesis:**
- H0: α = 0 (ไม่มี Alpha)
- H1: α > 0 (มี Positive Alpha)

### Sensitivity Analysis

| พารามิเตอร์ | ค่าพื้นฐาน | ทดสอบ |
|---------------|-------------|--------|
| **VQM Weights** | 45/35/20 | 40/40/20, 50/30/20 |
| **Rebalancing** | Quarterly | Monthly, Semi-annual |
| **Portfolio Size** | 30 stocks | 20, 50 stocks |
| **Transaction Cost** | 0.50% | 0.30%, 1.00% |

---

## การป้องกัน Overfitting

### 1. Out-of-Sample Testing

- Train: 2017-2018 (24 เดือน)
- Test: 2019-2024 (72 เดือน)
- **จำลองเพียงครั้งเดียว** (No optimization on test data)

### 2. Minimum Observation Rule

- ต้องมีอย่างน้อย 24 Periods (6 ปี)
- เพื่อความน่าเชื่อถือทางสถิติ

### 3. Performance Degradation Check

```
Performance_Gap = Return_Train - Return_Test
```

หาก Performance_Gap > 5% → อาจเป็นสัญญาณ Overfitting

> [!WARNING] การระวังจาก Bailey et al. (2014)
> "The probability of backtest overfitting increases with:
> - จำนวน parameters ที่ปรับ
> - ความถี่ในการทดสอบ
> - ความซับซ้อนของโมเดล"

---

## รายงานผลการทดสอบ

### รูปแบบ Output

```
┌─────────────────────────────────────────────────────────────────┐
│                    BACKTEST SUMMARY                             │
├─────────────────────────────────────────────────────────────────┤
│  Period:           Jan 2019 — Dec 2024                          │
│  Rebalancing:      Quarterly                                   │
│  Portfolio Size:   30 stocks                                    │
├─────────────────────────────────────────────────────────────────┤
│  RETURNS                                                      │
│  CAGR:              X.XX%   (Benchmark: Y.YY%)                 │
│  Alpha (p.a.):      X.XX%                                        │
│  Sharpe Ratio:      X.XX                                        │
├─────────────────────────────────────────────────────────────────┤
│  RISK                                                         │
│  Max Drawdown:      -XX.X%                                      │
│  Volatility:        XX.X%                                       │
│  Beta:              X.XX                                        │
├─────────────────────────────────────────────────────────────────┤
│  REGIME ANALYSIS                                              │
│  Bull:              X.XX%                                       │
│  Bear:              X.XX%                                       │
│  High Vol:          X.XX%                                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## อ้างอิง

- Lopez de Prado, M. (2020). *Advances in financial machine learning*. Wiley.
- Bailey, D. H., et al. (2014). The probability of backtest overfitting. *JPM, 40*(4)*.
- Clarke, R., de Silva, H., & Thorley, S. (2016). Fundamentals of multifactor portfolio construction. *JPM, 42*(5)*.
- Harvey, C. R., & Liu, Y. (2016). ...and the cross-section of expected returns. *RFS, 29*(3)*.

---

*สร้างเอกสาร: 2026-04-06*
*สถานะ: 🚧 ร่าง — รอข้อมูลตลาดจริง*
