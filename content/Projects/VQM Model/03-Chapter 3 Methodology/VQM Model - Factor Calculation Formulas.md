---
title: "VQM Model — Factor Calculation Formulas"
aliases: ["VQM Factor Formulas", "สูตรคำนวณปัจจัย VQM", "VQM Metrics"]
tags: [📁/projects, 🏷️/vqm-model, 🏷️/formulas, 🏷️/calculations, status/draft]
created: 2026-04-06
modified: 2026-04-06
type: reference
status: seedling
links:
  - "[[Chapter 3 - Methodology]]"
  - "[[VQM Model - Backtesting Framework]]"
  - "[[VQM Model - Thesis Research Plan]]"
---

# VQM Model — Factor Calculation Formulas

> [!INFO] Formula Reference
> เอกสารนี้รวบรวมสูตรคำนวณทั้งหมดสำหรับ VQM Model เพื่อใช้ในการเขียนโค้ดและ documentation

---

## 1. Value Factor Metrics

### 1.1 FCF Yield

```
FCF Yield = Free Cash Flow / Enterprise Value

เมื่อ:
Free Cash Flow = Operating Cash Flow - Capital Expenditure
Enterprise Value = Market Cap + Total Debt - Cash & Equivalents

Interpretation:
- ยิ่งสูง = หุ้นถูก (undervalued)
- Benchmark: Median FCF Yield ของ universe
```

### 1.2 P/E Relative

```
P/E Relative = P/E_stock / Median(P/E_sector, P/E_market)

เมื่อ:
P/E_stock = Price per Share / EPS (TTM)
Median(P/E_sector) = ค่ามัธยฐาน P/E ใน sector เดียวกัน

Interpretation:
- < 1 = ถูกกว่าค่าเฉลี่ย
- = 1 = ราคาตามค่าเฉลี่ย
- > 1 = แพงกว่าค่าเฉลี่ย
```

### 1.3 P/B Relative

```
P/B Relative = P/B_stock / Median(P/B_sector, P/B_market)

เมื่อ:
P/B_stock = Price per Share / Book Value per Share

Interpretation:
- < 1 = ราคาต่ำกว่ามูลค่าตามบัญชี
- ยิ่งต่ำ = ยิ่งถูก (หากมี ROE ดี)
```

### 1.4 EV/EBITDA

```
EV/EBITDA = Enterprise Value / EBITDA

เมื่อ:
EBITDA = Operating Income + Depreciation & Amortization
Enterprise Value = Market Cap + Total Debt - Cash - Minority Interest

Interpretation:
- ยิ่งต่ำ = ถูก (หากมี growth potential)
- ใช้ดีกับบริษัทที่มี depreciation สูง
```

---

## 2. Quality Factor Metrics

### 2.1 ROIC - WACC (Economic Spread)

```
ROIC = NOPAT / Invested Capital

เมื่อ:
NOPAT = EBIT × (1 - Tax Rate)
Invested Capital = Total Equity + Total Debt - Cash - NOL

WACC = (E/V) × Re + (D/V) × Rd × (1 - Tax Rate)

เมื่อ:
E/V = Equity / (Equity + Debt)
D/V = Debt / (Equity + Debt)
Re = Cost of Equity (CAPM: Rf + β × Market Premium)
Rd = Cost of Debt (Interest Rate)

Economic Spread = ROIC - WACC

Interpretation:
- > 0 = สร้างมูลค่าเหนือ cost of capital
- < 0 = ทำลายมูลค่า
```

### 2.2 FCF Conversion

```
FCF Conversion = Free Cash Flow / Net Income

เมื่อ:
Free Cash Flow = Operating Cash Flow - CapEx
Net Income = Net Income (TTM)

Interpretation:
- > 100% = กำไรมีคุณภาพ (ต่ำกว่า Net Income จาก non-cash items)
- < 80% = อาจมี working capital ใหญ่หรือ CapEx สูง
- Negative = มีปัญหา cash flow (แม้กำไรตามรายงาน)
```

### 2.3 Debt/EBITDA

```
Debt/EBITDA = Total Debt / EBITDA

เมื่อ:
Total Debt = Short-term Debt + Long-term Debt
EBITDA = EBIT + Depreciation + Amortization

Interpretation:
- < 2x = สุขภาพดีมาก
- 2-3x = สุขภาพดี
- 3-5x = ปานกลาง
- > 5x = เสี่ยงสูง (Financial leverage risk)
```

### 2.4 Gross Margin

```
Gross Margin = (Revenue - COGS) / Revenue = Gross Profit / Revenue

Interpretation:
- ยิ่งสูง = มี competitive advantage หรือ pricing power
- Benchmark: เทียบกับค่าเฉลี่ย sector
- Trend: สำคัญกว่าค่าสัมบูรณ์ (Improving trend = good)
```

---

## 3. Momentum Factor Metrics

### 3.1 Price 6-Month Momentum

```
Price_6M = (Price_t / Price_t-6M) - 1

เมื่อ:
Price_t = ราคาปิดวันล่าสุด
Price_t-6M = ราคาปิด 6 เดือนก่อน (approximately 120 trading days)

Interpretation:
- > 0 = Uptrend (bullish)
- < 0 = Downtrend (bearish)
- ยิ่งสูง = momentum แรง
```

### 3.2 Earnings Revision

```
Earnings Revision = (EPS_Estimate_Current / EPS_Estimate_3M_Ago) - 1

เมื่อ:
EPS_Estimate_Current = ค่าประมาณ EPS ล่าสุด (mean consensus)
EPS_Estimate_3M_Ago = ค่าประมาณ EPS เมื่อ 3 เดือนก่อน

Interpretation:
- > 0 = Analyst ปรับขึ้น (Positive surprise)
- < 0 = Analyst ปรับลง (Negative surprise)
- ใช้ 3 เดือนย้อนหลังเพื่อลด noise
```

### 3.3 Volume Trend

```
Volume Trend = Volume_MA(20) / Volume_MA(60)

เมื่อ:
Volume_MA(20) = ค่าเฉลี่ย volume 20 วัน
Volume_MA(60) = ค่าเฉลี่ย volume 60 วัน

Interpretation:
- > 1 = Volume ขยายตัว (มีแรงซื้อขาย)
- < 1 = Volume หดตัว (นิ่ว)
- 1.2-1.5 = Strong momentum (มี institutional interest)
```

---

## 4. Z-score Normalization

### 4.1 Standard Z-score

```
Z_score = (X - μ) / σ

เมื่อ:
X = ค่าตัวแปร
μ = ค่าเฉลี่ย (Mean)
σ = ส่วนเบี่ยงเบนมาตรฐาน (Standard Deviation)
```

### 4.2 Robust Z-score (MAD-based)

```
Z_score_robust = (X - Median) / (1.4826 × MAD)

เมื่อ:
Median = ค่ามัธยฐาน
MAD = Median Absolute Deviation = Median(|X_i - Median|)
1.4826 = ค่าปรับ (สำหรับ Normal Distribution, MAD ≈ 0.6745σ)

ทำไมใช้ MAD-based:
- Resistant to outliers (ทนทานต่อค่าผิดปกติ)
- เหมาะกับ financial data ที่มี skewness
- Median ไม่ได้รับผลจาก extreme values
```

### 4.3 Example Calculation

```
Suppose FCF Yield for 10 stocks:
[2%, 3%, 4%, 5%, 6%, 7%, 8%, 15%, 20%, 25%]

Mean = 9.5%
Median = 6.5%
MAD = Median([4%, 3.5%, 2.5%, 1.5%, 0.5%, 0.5%, 1.5%, 8.5%, 13.5%, 18.5%]) = 2.5%

For Stock with FCF Yield = 15%:
Z_score_robust = (15 - 6.5) / (1.4826 × 2.5)
               = 8.5 / 3.7065
               = 2.29 (Very high FCF Yield)
```

---

## 5. Composite Scoring

### 5.1 Value Score

```
Value_Score = (Z_FCF_Yield - Z_EV_EBITDA_inv - Z_PE_Rel_inv - Z_PB_Rel_inv) / 4

เมื่อ:
Z_FCF_Yield = Z-score ของ FCF Yield
Z_EV_EBITDA_inv = -1 × Z-score ของ EV/EBITDA (ติดลบคือดี)
Z_PE_Rel_inv = -1 × Z-score ของ P/E Relative (ติดลบคือดี)
Z_PB_Rel_inv = -1 × Z-score ของ P/B Relative (ติดลบคือดี)

Note: ถ้า metric "ต่ำ = ดี" ให้คูณด้วย -1
```

### 5.2 Quality Score

```
Quality_Score = (Z_ROIC_Spread + Z_FCF_Conv - Z_Debt_EBITDA + Z_Gross_Margin) / 4

เมื่อ:
Z_ROIC_Spread = Z-score ของ (ROIC - WACC)
Z_FCF_Conv = Z-score ของ FCF Conversion
Z_Debt_EBITDA = -1 × Z-score ของ Debt/EBITDA (ต่ำ = ดี)
Z_Gross_Margin = Z-score ของ Gross Margin
```

### 5.3 Momentum Score

```
Momentum_Score = (Z_Price_6M + Z_Earnings_Rev + Z_Volume_Trend) / 3

เมื่อ:
Z_Price_6M = Z-score ของ Price 6-Month Momentum
Z_Earnings_Rev = Z-score ของ Earnings Revision
Z_Volume_Trend = Z-score ของ Volume Trend
```

### 5.4 VQM Composite Score

```
VQM_Score = 0.45 × Value_Score +
            0.35 × Quality_Score +
            0.20 × Momentum_Score

Range: -3 ถึง +3 (โดยประมาณ)
- ยิ่งสูง = ยิ่งดี (High Value + High Quality + High Momentum)
```

---

## 6. Missing Data Handling

### 6.1 Rules

| Condition | Action |
|-----------|--------|
| **Missing single metric** | Use median of sector/market (marked as imputed) |
| **Missing > 25% metrics** | Exclude from current period ranking |
| **Financial data not available** | Use TTM data from previous quarter (marked) |
| **Price data missing** | Use previous day close (if gap < 5 days) |

### 6.2 Data Quality Flags

```
Flag System:
- 0 = Complete data
- 1 = 1 metric imputed
- 2 = 2 metrics imputed
- 3 = 3+ metrics imputed (exclude from top 20%)
```

---

## 7. Calculation Frequency

| Metric | Frequency | Update Timing |
|--------|-----------|---------------|
| **Price, Volume** | Daily | End of day |
| **PE, PB, EV** | Daily | ตามราคา |
| **Financials** | Quarterly | หลังจากรายงาน Q |
| **Analyst Estimates** | Monthly | ตาม consensus update |
| **Composite Score** | Quarterly | Rebalancing date |

---

## 8. Python Code Snippet (Pseudo-code)

```python
def calculate_z_score_obust(series):
    median = series.median()
    mad = (series - median).abs().median()
    return (series - median) / (1.4826 * mad)

def calculate_value_score(df):
    df['z_fcf_yield'] = calculate_z_score_robust(df['fcf_yield'])
    df['z_ev_ebitda'] = -1 * calculate_z_score_robust(df['ev_ebitda'])
    df['z_pe_rel'] = -1 * calculate_z_score_robust(df['pe_relative'])
    df['z_pb_rel'] = -1 * calculate_z_score_robust(df['pb_relative'])

    df['value_score'] = (df['z_fcf_yield'] + df['z_ev_ebitda'] +
                         df['z_pe_rel'] + df['z_pb_rel']) / 4
    return df

def calculate_vqm_score(df):
    df = calculate_value_score(df)
    df = calculate_quality_score(df)
    df = calculate_momentum_score(df)

    df['vqm_score'] = (0.45 * df['value_score'] +
                       0.35 * df['quality_score'] +
                       0.20 * df['momentum_score'])
    return df
```

---

## 🔗 Linked References

- [[Chapter 3 - Methodology]] — ระเบียบวิธีวิจัย
- [[VQM Model - Backtesting Framework]] — เฟรมเวิร์กการทดสอบ
- [[Complete Reference List]] — อ้างอิงทางทฤษฎี

---

*Document created: 2026-04-06*
*Status: Formula Reference — Ready for coding*
