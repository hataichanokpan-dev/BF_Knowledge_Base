---
title: "สูตรคำนวณปัจจัย VQM"
aliases: ["Factor Formulas", "สูตรคำนวณปัจจัย", "VQM Factor Calculations"]
tags: [📁/vqm-model, 🏷️/methodology, 🏷️/factors, 🏷️/formulas]
created: 2026-04-06
modified: 2026-04-06
type: reference
status: seedling
links:
  - "[[Methodology Framework]]"
  - "[[VQM Model - Thesis Research Plan]]"
---

# สูตรคำนวณปัจจัย VQM

> **Formula Reference Guide** — สูตรคำนวณรายละเอียดสำหรับทุกปัจจัยในโมเดล VQM
>
> **เป้าหมาย:** เอกสารอ้างอิงสำหรับการคำนวณปัจจัยทั้งหมด

---

## สารบัญ

1. [สัญลักษณ์และคำนิยาม](#สัญลักษณ์และคำนิยาม)
2. [ปัจจัยมูลค่า (Value Factor)](#ปัจจัยมูลค่า-value-factor)
3. [ปัจจัยคุณภาพ (Quality Factor)](#ปัจจัยคุณภาพ-quality-factor)
4. [ปัจจัยโมเมนตัม (Momentum Factor)](#ปัจจัยโมเมนตัม-momentum-factor)
5. [การรวมคะแนน (Composite Score)](#การรวมคะแนน-composite-score)
6. [ตัวอย่างการคำนวณ](#ตัวอย่างการคำนวณ)

---

## สัญลักษณ์และคำนิยาม

| สัญลักษณ์ | คำนิยาม | หน่วย |
|-----------|----------|--------|
| P_t | ราคาหลักทรัพย์ ณ เวลา t | บาท |
| B_t | มูลค่าหนังสือต่อหุ้น ณ เวลา t | บาท |
| E_t | กำไรต่อหุ้น ณ เวลา t | บาท |
| FCF_t | Free Cash Flow ณ เวลา t | ล้านบาท |
| EV_t | Enterprise Value ณ เวลา t | ล้านบาท |
| D_t | หนี้สินรวม ณ เวลา t | ล้านบาท |
| IC_t | Invested Capital ณ เวลา t | ล้านบาท |
| NOPAT_t | Net Operating Profit After Tax | ล้านบาท |
| WACC_t | Weighted Average Cost of Capital | % |

---

## ปัจจัยมูลค่า (Value Factor)

### สูตรที่ 1: FCF Yield

**คำนิยาม:** อัตราผลตอบแทนจาก Free Cash Flow เทียบกับมูลค่ากิจการ

**สูตร:**
```
FCF Yield_t = FCF_t / EV_t
```

**รายละเอียด:**
- **FCF (Free Cash Flow)** = Operating Cash Flow - Capital Expenditure
- **EV (Enterprise Value)** = Market Cap + Debt - Cash
- **ทิศทาง:** ยิ่งสูงดี (Higher is better)

**การปรับปรุง:**
```
FCF Yield_Adjusted = FCF Yield_t / Median(FCF Yield_Sector_t)
```

---

### สูตรที่ 2: P/B Ratio

**คำนิยาม:** ราคาต่อมูลค่าหนังสือ

**สูตร:**
```
P/B Ratio_t = P_t / B_t
```

**รายละเอียด:**
- **P_t** = ราคาปิดตลาด ณ วันที่ t
- **B_t** = ส่วนของผู้ถือหุ้นทั้งหมด / จำนวนหุ้นจดทะเบียน
- **ทิศทาง:** ยิ่งต่ำดี (Lower is better)

**การปรับปรุง:**
```
P/B_Adjusted = P/B Ratio_t / Median(P/B Ratio_Sector_t)
```

---

### สูตรที่ 3: P/E Ratio

**คำนิยาม:** ราคาต่อกำไร

**สูตร:**
```
P/E Ratio_t = P_t / E_t
```

**รายละเอียด:**
- **E_t** = กำไรสุทธิ / จำนวนหุ้นจดทะเบียน
- ใช้ E จากงบการเงินล่าสุด (TTM)
- **ทิศทาง:** ยิ่งต่ำดี (Lower is better)

**ข้อควรระวัง:**
- หาก E_t < 0 → กำจัดจากการคำนวณ P/E
- หาก P/E > 50 → ใช้ค่าสูงสุดที่ 50

---

## ปัจจัยคุณภาพ (Quality Factor)

### สูตรที่ 4: ROIC - WACC Spread

**คำนิยาม:** ส่วนต่างระหว่างอัตราผลตอบแทนบนเงินลงทุนและต้นทุนเงินทุน

**Step 1: คำนวณ ROIC**
```
ROIC_t = NOPAT_t / IC_t
```

**รายละเอียด:**
- **NOPAT** = EBIT × (1 - Tax Rate)
- **IC** = Shareholder Equity + Debt - Cash - Non-operating assets

**Step 2: คำนวณ WACC**
```
WACC_t = (E/V) × R_e + (D/V) × R_d × (1 - Tax Rate)
```

**รายละเอียด:**
- **E/V** = สัดส่วน Equity
- **D/V** = สัดส่วน Debt
- **R_e** = Cost of Equity (ใช้ CAPM)
- **R_d** = Cost of Debt

**Step 3: คำนวณ Spread**
```
ROIC_WACC_Spread_t = ROIC_t - WACC_t
```

**ทิศทาง:** ยิ่งสูงดี (Higher spread = Better quality)

---

### สูตรที่ 5: FCF Conversion

**คำนิยาม:** ความสามารถในการแปลงกำไรสุทธิเป็นกระแสเงินสด

**สูตร:**
```
FCF Conversion_t = FCF_t / Net Income_t
```

**รายละเอียด:**
- **FCF** = Operating Cash Flow - CapEx
- **Net Income** = กำไรสุทธิ
- **ทิศทาง:** ยิ่งสูงดี (Higher = Better cash quality)

**การตีความ:**
- FCF Conversion > 1 = สร้างกระแสเงินสดเกินกำไรที่รายงาน
- FCF Conversion < 0.8 = อาจมีปัญหาคุณภาพกำไร

---

### สูตรที่ 6: Debt/EBITDA

**คำนิยาม:** อัตราส่วนหนี้ต่อกำไรก่อนดอกเบี้ยและภาษี

**สูตร:**
```
Debt_EBITDA_t = Total_Debt_t / EBITDA_t
```

**รายละเอียด:**
- **Total Debt** = Short-term Debt + Long-term Debt
- **EBITDA** = Net Income + Interest + Taxes + Depreciation + Amortization
- **ทิศทาง:** ยิ่งต่ำดี (Lower = Less leverage risk)

**การตีความ:**
- Debt/EBITDA < 2 = การเงินแข็งแรง
- Debt/EBITDA > 4 = ความเสี่ยงสูง

---

## ปัจจัยโมเมนตัม (Momentum Factor)

### สูตรที่ 7: Price Momentum (6-Month)

**คำนิยาม:** อัตราการเติบโตของราคาในช่วง 6 เดือน

**สูตร:**
```
Price_Momentum_6M_t = (P_t / P_{t-126}) - 1
```

**รายละเอียด:**
- **P_t** = ราคาปิด ณ วันที่ t
- **P_{t-126}** = ราคาปิด ณ วันที่ t-126 (≈ 6 เดือน)
- ใช้ราคา 6 เดือนย้อนหลัง ไม่รวมเดือนล่าสุด
- **ทิศทาง:** ยิ่งสูงดี (Higher = Stronger momentum)

**ข้อควรระวัง:**
- หลีกเลี่ยง Short-term Reversal (1-month)
- ใช้ 1-month skip: Momentum = (P_t / P_{t-1}) / (P_{t-127} / P_{t-26})

---

### สูตรที่ 8: Volume Trend

**คำนิยาม:** แนวโน้มปริมาณการซื้อขาย

**สูตร:**
```
Volume_Trend_t = Volume_MA(20)_t / Volume_MA(60)_t
```

**รายละเอียด:**
- **Volume_MA(20)** = ปริมาณเฉลี่ย 20 วันทำการ
- **Volume_MA(60)** = ปริมาณเฉลี่ย 60 วันทำการ
- **ทิศทาง:** ยิ่งสูงดี (Higher = Increasing volume)

**การตีความ:**
- Volume Trend > 1.2 = ปริมาณเพิ่มขึ้น (Bullish)
- Volume Trend < 0.8 = ปริมาณลดลง (Bearish)

---

## การรวมคะแนน (Composite Score)

### Step 1: Z-Score Normalization

**สูตร:**
```
Z_i = (X_i - Median(X)) / (1.4826 × MAD)
```

**รายละเอียด:**
- **X_i** = ค่าตัวชี้วัดของหลักทรัพย์ i
- **Median(X)** = ค่ามัธยฐานของตัวชี้วัด
- **MAD** = Median Absolute Deviation
- **1.4826** = ค่าปรับสำหรับให้เท่ากับ Standard Deviation

**สำหรับตัวชี้วัดที่ "ยิ่งต่ำดี":**
```
Z_i = -(X_i - Median(X)) / MAD
```

---

### Step 2: Factor Score Calculation

**Value Score (45%):**
```
Value_Score = 0.40 × Z_FCF_Yield + 0.30 × (-Z_P/B) + 0.30 × (-Z_P/E)
```

**Quality Score (35%):**
```
Quality_Score = 0.50 × Z_ROIC_WACC + 0.30 × Z_FCF_Conv + 0.20 × (-Z_Debt_EBITDA)
```

**Momentum Score (20%):**
```
Momentum_Score = 0.70 × Z_Price_6M + 0.30 × Z_Volume_Trend
```

---

### Step 3: VQM Composite Score

**สูตร:**
```
VQM_Score = 0.45 × Value_Score + 0.35 × Quality_Score + 0.20 × Momentum_Score
```

**ช่วงคะแนน:**
- VQM Score > 2.0 = หุ้นระดับ Top 5%
- VQM Score > 1.0 = หุ้นระดับ Top 20%
- VQM Score < 0 = หุ้นระดับ Bottom 50%

---

## ตัวอย่างการคำนวณ

### Example: Stock ABC

**ข้อมูล:**
- ราคา (P) = 50 บาท
- Book Value per Share (B) = 25 บาท
- EPS = 5 บาท
- FCF = 2,000 ล้านบาท
- EV = 50,000 ล้านบาท
- ROIC = 15%
- WACC = 10%
- Net Income = 1,500 ล้านบาท
- Debt = 10,000 ล้านบาท
- EBITDA = 3,000 ล้านบาท

**Step 1: คำนวณ Value Metrics**
```
P/B = 50 / 25 = 2.0
P/E = 50 / 5 = 10.0
FCF Yield = 2,000 / 50,000 = 4.0%
```

**Step 2: คำนวณ Quality Metrics**
```
ROIC-WACC Spread = 15% - 10% = 5.0%
FCF Conversion = 2,000 / 1,500 = 1.33
Debt/EBITDA = 10,000 / 3,000 = 3.33x
```

**Step 3: Normalize (Z-Score)**
*สมมติค่า Median และ MAD จากตลาด*
```
Z_P/B = (2.0 - 1.5) / 0.5 = 1.0
Z_P/E = (10.0 - 12.0) / 4.0 = -0.5 (หมายถึง P/B ต่ำกว่าค่ามัธยฐาน)
Z_FCF_Yield = (4.0 - 3.0) / 1.0 = 1.0
```

**Step 4: คำนวณ Factor Scores**
```
Value_Score = 0.40×1.0 + 0.30×(-1.0) + 0.30×(0.5) = 0.25
Quality_Score = 0.50×1.5 + 0.30×0.8 + 0.20×(-0.5) = 0.99
```

**Step 5: VQM Composite**
```
VQM_Score = 0.45×0.25 + 0.35×0.99 + 0.20×0.5 = 0.57
```

---

## อ้างอิง

- Novy-Marx, R. (2013). The other side of value: The gross profitability premium.
- Asness, C. S., et al. (2019). Quality minus junk.
- Sloan, R. G. (1996). Do stock prices fully reflect information in accruals?

---

*สร้างเอกสาร: 2026-04-06*
*สถานะ: ✅ สมบูรณ์*
