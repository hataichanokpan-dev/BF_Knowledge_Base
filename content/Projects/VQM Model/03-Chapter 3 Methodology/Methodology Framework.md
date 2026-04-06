---
title: "กรอบการวิจัย — บทที่ 3"
aliases: ["Methodology Framework", "กรอบการวิจัย VQM", "Chapter 3 Methodology"]
tags: [📁/vqm-model, 🏷️/methodology, 🏷️/chapter-3, 🏷️/research-design]
created: 2026-04-06
modified: 2026-04-06
type: methodology
status: seedling
links:
  - "[[VQM Model - Thesis Research Plan]]"
  - "[[Factor Calculation Formulas]]"
  - "[[Backtesting Framework]]"
  - "[[Complete Reference List]]"
---

# กรอบการวิจัย — บทที่ 3

> **บทที่ 3: Methodology** — วิธีการวิจัยและกรอบการทดสอบโมเดล VQM
>
> **จุดประสงค์:** อธิบายวิธีการวิจัย การกำหนดปัจจัย และกรอบการทดสอบประสิทธิภาพ
>
> **อ้างอิงหลัก:** Fama & French (1992), Jegadeesh & Titman (1993), Lopez de Prado (2020)

---

## สารบัญ

1. [3.1 รูปแบบการวิจัย](#31-รูปแบบการวิจัย)
2. [3.2 แหล่งข้อมูลและคำอธิบายข้อมูล](#32-แหล่งข้อมูลและคำอธิบายข้อมูล)
3. [3.3 คำนิยามปัจจัยและสูตรคำนวณ](#33-คำนิยามปัจจัยและสูตรคำนวณ)
4. [3.4 การสร้างพอร์ตหลักทรัพย์](#34-การสร้างพอร์ตหลักทรัพย์)
5. [3.5 กรอบการทดสอบย้อนหลัง](#35-กรอบการทดสอบย้อนหลัง)
6. [3.6 ตัวชี้วัดประเมินผล](#36-ตัวชี้วัดประเมินผล)

---

## 3.1 รูปแบบการวิจัย

### 3.1.1 ประเภทการวิจัย

การวิจัยนี้เป็น **การวิจัยเชิงประจักษ์ (Quantitative Research)** โดยใช้ข้อมูลอนุกรมเวลา (Time-series Data) และข้อมูลตัดขวาง (Cross-sectional Data) ในการวิเคราะห์ประสิทธิภาพของโมเดล VQM

### 3.1.2 ระยะเวลาวิจัย

| รายการ | รายละเอียด |
|----------|-------------|
| **ช่วงเวลา** | มกราคม 2019 — ธันวาคม 2024 |
| **ความยาว** | 6 ปี (72 เดือน) |
| **จุดประสงค์** | ครอบคลุมหลาย market regimes (bull, bear, high volatility) |
| **ความถี่การทดสอบ** | รายไตรมาส (Quarterly) |

### 3.1.3 ประชากรและกลุ่มตัวอย่าง

**ประชากร (Universe):**
- หลักทรัพย์ที่จดทะเบียนในตลาดหลักทรัพย์แห่งประเทศไทย (SET)
- ยกเว้น: SET50, SET100, mai (ใช้เฉพาะ SET Broad)

**เกณฑ์การคัดเลือก (Inclusion Criteria):**
1. มูลค่าซื้อขายเฉลี่ยต่อวัน ≥ 20 ล้านบาท
2. มีข้อมูลครบถ้วนสำหรับการคำนวณปัจจัยทั้ง 3 ด้าน
3. ไม่อยู่ในกลุ่ม Financials (ยกเว้นในการวิเคราะห์เฉพาะ)

### 3.1.4 ตัวแปรวิจัย

| ประเภท | ตัวแปร | คำนิยาม |
|----------|----------|----------|
| **ตัวแปรตาม** | ผลตอบแทนหลักทรัพย์ | Monthly total return |
| **ตัวแปรอิสระ** | VQM Score | Composite score from 3 factors |
| **ตัวแปรควบคุม** | Market Cap, Sector | Size, Industry classification |

---

## 3.2 แหล่งข้อมูลและคำอธิบายข้อมูล

### 3.2.1 แหล่งข้อมูลหลัก

| ประเภทข้อมูล | แหล่งข้อมูล | รายละเอียด |
|----------------|---------------|-------------|
| **ราคาหลักทรัพย์** | SET Data / Bloomberg / Refinitiv Eikon | Daily prices, Total Return Index |
| **งบการเงิน** | SET MMP / Thai SEC / Company Reports | Quarterly Balance Sheet, Income Statement, Cash Flow |
| **ดัชนีตลาด** | SET Index | Daily SET Index, SET TRI |
| **ข้อมูลพื้นฐาน** | SET Smart / Bloomberg | Market Cap, Sector classification, Liquidity metrics |

> [!INFO] แหล่งข้อมูลหลัก
> - **SET Data**: ข้อมูลราคาและดัชนีจากตลาดหลักทรัพย์แห่งประเทศไทย
> - **SET MMP (Market Monitoring Platform)**: ข้อมูลงบการเงินและข้อมูลพื้นฐาน
> - **Bloomberg/Eikon**: แหล่งข้อมูลรองสำหรับข้อมูลที่ไม่มีในระบบ SET

### 3.2.2 การประมวลผลข้อมูล

**Data Cleaning:**
- จัดการ Missing Values: ใช้ Median ของหมวดอุตสาหกรรมเดียวกัน
- จัดการ Outliers: Winsorize ที่ 1st และ 99th percentile
- การปรับเทียบ (Adjustments): ปรับราคาสำหรับ Split, Dividend, Rights Offering

**Point-in-Time (PIT) Data:**
- ใช้ข้อมูลที่พร้อมใช้ได้ในจุดเวลานั้น (T+0)
- หลีกเลี่ยง Look-ahead bias
- บันทึก Data availability lag สำหรับแต่ละรายการ

### 3.2.3 การควบคุมความเอนเอียง

| ประเภทความเอนเอียง | วิธีควบคุม |
|----------------------|---------------|
| **Survivorship Bias** | รวมบริษัทที่ถูก delisted |
| **Look-ahead Bias** | ใช้ PIT data, Lag accounting data |
| **Selection Bias** | กำหนดเกณฑ์การคัดเลือนที่ชัดเจน |

---

## 3.3 คำนิยามปัจจัยและสูตรคำนวณ

### 3.3.1 ภาพรวมปัจจัย VQM

```
┌─────────────────────────────────────────────────────────────────────┐
│                    VQM MODEL FACTOR STRUCTURE                       │
│                                                                     │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐                  │
│  │   VALUE     │  │   QUALITY   │  │  MOMENTUM   │                  │
│  │   (45%)     │  │   (35%)     │  │   (20%)     │                  │
│  ├─────────────┤  ├─────────────┤  ├─────────────┤                  │
│  │ • FCF Yield │  │ • ROIC-WACC │  │ • Price 6M  │                  │
│  │ • P/B Ratio │  │ • FCF Conv  │  │ • Volume    │                  │
│  └─────────────┘  └─────────────┘  └─────────────┘                  │
└─────────────────────────────────────────────────────────────────────┘
```

### 3.3.2 ปัจจัยมูลค่า (Value Factor)

**น้ำหนัก: 45%**

| ตัวชี้วัด | สูตร | ทิศทาง |
|-----------|------|--------|
| FCF Yield | Free Cash Flow / Enterprise Value | ยิ่งสูงดี |
| P/B Ratio | Price / Book Value per Share | ยิ่งต่ำดี |
| P/E Ratio | Price / Earnings per Share | ยิ่งต่ำดี |

### 3.3.3 ปัจจัยคุณภาพ (Quality Factor)

**น้ำหนัก: 35%**

| ตัวชี้วัด | สูตร | ทิศทาง |
|-----------|------|--------|
| ROIC - WACC Spread | ROIC - WACC | ยิ่งสูงดี |
| FCF Conversion | FCF / Net Income | ยิ่งสูงดี |
| Debt/EBITDA | Total Debt / EBITDA | ยิ่งต่ำดี |

### 3.3.4 ปัจจัยโมเมนตัม (Momentum Factor)

**น้ำหนัก: 20%**

| ตัวชี้วัด | สูตร | ทิศทาง |
|-----------|------|--------|
| Price 6M | (Price_t / Price_t-6) - 1 | ยิ่งสูงดี |
| Volume Trend | Volume_MA(20) / Volume_MA(60) | ยิ่งสูงดี |

> [!INFO] รายละเอียดสูตรคำนวณแบบเต็ม
> ดูสูตรคำนวณแบบละเอียดได้ที่ [[Factor Calculation Formulas]]

---

## 3.4 การสร้างพอร์ตหลักทรัพย์

### 3.4.1 การคำนวณคะแนนรวม (Composite Score)

**Step 1: Normalization (Z-Score)**
```
Z_score(i,k,t) = (X(i,k,t) - Median_k) / MAD_k
```
เมื่อ:
- X(i,k,t) = ค่าตัวชี้วัด k ของหลักทรัพย์ i ในเวลา t
- Median_k = ค่ามัธยฐานของตัวชี้วัด k
- MAD_k = Median Absolute Deviation

**Step 2: Factor Score**
```
Value_Score(i,t) = 0.40×FCF_Yield_Z + 0.30×P/B_Z + 0.30×P/E_Z
Quality_Score(i,t) = 0.50×ROIC_WACC_Z + 0.30×FCF_Conv_Z + 0.20×Debt_Z
Momentum_Score(i,t) = 0.70×Price_6M_Z + 0.30×Volume_Z
```

**Step 3: VQM Composite Score**
```
VQM_Score(i,t) = 0.45×Value_Score + 0.35×Quality_Score + 0.20×Momentum_Score
```

### 3.4.2 การคัดเลือกหลักทรัพย์เข้าพอร์ต

**วิธีที่ 1: Top Quintile (20%)**
- คัดเลือกหลักทรัพย์ 20% แรกตาม VQM Score
- จำนวนหลักทรัพย์: ประมาณ 50-80 ใบ

**วิธีที่ 2: Top N Stocks**
- คัดเลือกหลักทรัพย์ 30 ใบแรกตาม VQM Score
- เหมาะสำหรับการจัดการพอร์ตขนาดเล็ก

### 3.4.3 การกำหนดน้ำหนัก (Weighting)

**Equal-Weight (พื้นฐาน):**
```
Weight_i = 1 / N
```

**Score-Weighted (ทางเลือก):**
```
Weight_i = VQM_Score_i / Σ(VQM_Score)
```

### 3.4.4 เงื่อนไขข้อจำกัด (Constraints)

| ข้อจำกัด | ค่า | วัตถุประสงค์ |
|-----------|-----|---------------|
| Max Weight per Stock | 5% | ความเสี่ยงการกระจุกตัว |
| Max Weight per Sector | 10% | ความหลากหลายกลุ่มอุตสาหกรรม |
| Min Liquidity | ADV ≥ 20M | สภาพคล่องเพียงพอ |

---

## 3.5 กรอบการทดสอบย้อนหลัง

### 3.5.1 Walk-Forward Analysis

**รูปแบบ:**
```
┌─────────────────────────────────────────────────────────────┐
│                   WALK-FORWARD FRAMEWORK                    │
│                                                             │
│  Training Period          Test Period                       │
│  ┌───────────────┐      ┌───────────────┐                  │
│  │ 24 months     │      │  3 months     │                  │
│  │ Factor calc   │  →   │ Portfolio     │                  │
│  │ Stock ranking │      │ Performance   │                  │
│  └───────────────┘      └───────────────┘                  │
│         ↓                       ↓                           │
│     Roll forward          Rebalance                        │
└─────────────────────────────────────────────────────────────┘
```

**Parameters:**
- Training Period: 24 เดือน
- Test Period: 3 เดือน
- Rebalancing: รายไตรมาส (Quarterly)

### 3.5.2 ต้นทุนธุรกรรม (Transaction Costs)

| รายการ | ค่าต้นทุน |
|----------|------------|
| ค่าธรรมเนียมซื้อ | 0.15% |
| ค่าธรรมเนียมขาย | 0.15% |
| ค่า Slippage | 0.10% |
| **รวม Round-trip** | **0.30%** |

### 3.5.3 การจัดการความเสี่ยง

**Stop-Loss Mechanism:**
- หากหุ้นตัวใดลดลงเกิน 20% จากราคาซื้อ → ขายทิ้ง

**Rebalancing Rules:**
- Review รายไตรมาส
- Rebalance ถ้า weight ผิดเพี้ยนเกิน ±2%

> [!INFO] รายละเอียดเพิ่มเติม
> ดูกรอบการทดสอบย้อนหลังแบบละเอียดได้ที่ [[Backtesting Framework]]

---

## 3.6 ตัวชี้วัดประเมินผล

### 3.6.1 ตัวชี้วัดผลตอบแทน

| ตัวชี้วัด | สูตร | เป้าหมาย |
|-----------|------|----------|
| **CAGR** | (Final_Value / Initial_Value)^(1/n) - 1 | ต่ำกว่า SET |
| **Alpha** | Return_Portfolio - Return_Benchmark | > 3% p.a. |
| **Beta** | Cov(R_p, R_m) / Var(R_m) | ≈ 1.0 |
| **Sharpe Ratio** | (R_p - R_f) / σ_p | > 1.0 |
| **Sortino Ratio** | (R_p - R_f) / σ_downside | > 1.5 |

### 3.6.2 ตัวชี้วัดความเสี่ยง

| ตัวชี้วัด | สูตร | เป้าหมาย |
|-----------|------|----------|
| **Max Drawdown** | Max(Peak - Trough) / Peak | < -25% |
| **Volatility** | Std(Returns) × √12 | ต่ำกว่า SET |
| **Downside Deviation** | Std(Negative Returns) | ต่ำ |
| **VaR (95%)** | Percentile(Returns, 5%) | ต่ำ |

### 3.6.3 ตัวชี้วัดความสามารถในการทำนาย

| ตัวชี้วัด | สูตร | เป้าหมาย |
|-----------|------|----------|
| **Hit Rate** | Win / (Win + Loss) | > 55% |
| **Information Ratio** | Alpha / Tracking Error | > 0.5 |
| **R-squared** | 1 - (SS_res / SS_tot) | สูง |

---

## สรุปบท

บทนี้นำเสนอกรอบการวิจัยสำหรับการทดสอบโมเดล VQM โดยครอบคลุม:

1. ✅ รูปแบบการวิจัยและช่วงเวลาทดสอบ
2. ✅ แหล่งข้อมูลและวิธีการประมวลผล
3. ✅ คำนิยามปัจจัยทั้ง 3 ด้าน (Value, Quality, Momentum)
4. ✅ วิธีการสร้างและจัดการพอร์ต
5. ✅ กรอบการทดสอบย้อนหลังด้วย Walk-forward
6. ✅ ตัวชี้วัดประเมินผลที่ครอบคลุม

---

## อ้างอิง

- Fama, E. F., & French, K. R. (1992). The cross-section of expected stock returns.
- Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers.
- Lopez de Prado, M. (2020). Advances in financial machine learning.
- Clarke, R., de Silva, H., & Thorley, S. (2016). Fundamentals of multifactor portfolio construction.

---

*สร้างเอกสาร: 2026-04-06*
*สถานะ: 🚧 ร่าง — รอข้อมูลตลาดจริง*
