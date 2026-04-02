---
title: 06 - Complete DCF Example Apple
tags:
  - finance/valuation
  - dcf
  - case-study
  - apple
instructor: Aswath Damodaran (Persona)
language: th
---

# 06) Complete DCF Example: Apple Inc.

> [!quote] Professor's Opening
> บทนี้คือ DCF แบบทำจริงทีละขั้น ไม่ใช่สูตรลอย ๆ. คุณต้องเห็นว่า **ทุกตัวเลขมาจากสมมติฐาน** และทุกสมมติฐานต้องมีเหตุผลเชิงธุรกิจ.

> [!info] อ่านร่วมกัน
> - พื้นฐาน: [[01 - DCF Fundamentals]]
> - Cash flow: [[02 - Free Cash Flow]]
> - Forecast: [[03 - Forecasting Cash Flows]]
> - WACC: [[04 - Discount Rate WACC]]
> - Terminal value: [[05 - Terminal Value]]

## Objective ของเคสนี้

เราจะหามูลค่า intrinsic value ของ Apple ด้วย FCFF DCF โดยใช้กรอบ:
1. ตั้งฐานข้อมูลล่าสุด (ปีฐาน)
2. สร้าง forecast 10 ปี
3. Discount ด้วย WACC
4. คำนวณ terminal value
5. แปลงเป็น equity value และ value per share
6. ทำ sensitivity analysis

> [!note]
> ตัวเลขใช้เพื่อการเรียนรู้เชิงวิธีคิด โดยอิงข้อมูลสาธารณะและการประมาณอย่างมีเหตุผล ไม่ใช่ investment advice.

## Step 0: Base-Year Data (Approximate)

ปีฐาน (FY2024 โดยประมาณ, หน่วย: USD bn)
- Revenue = 391.0
- EBIT margin = 31.0% (ตั้งต้นเพื่อ normalize)
- Effective tax ใกล้เคียง = 16%
- Net debt โดยประมาณ = Debt 110 - Cash 65 = 45
- Diluted shares = 15.4 bn หุ้น

## Step 1: Forecast Revenue

สมมติ growth path แบบ fade ตามขนาดธุรกิจที่ mature มากขึ้น:
- Year 1-5: 8.0%, 7.5%, 7.0%, 6.0%, 5.5%
- Year 6-10: 5.0%, 4.5%, 4.0%, 3.5%, 3.0%

เหตุผล:
- ฐานรายได้ใหญ่ -> โตเร็วมากระยะยาวยาก
- มี engine จาก services แต่ฮาร์ดแวร์ยังมี cycle

## Step 2: Forecast Operating Margin และ Tax

สมมติ EBIT margin:
- ปี 1-2 = 31.2%
- แล้วค่อย ๆ fade ลงสู่ 29.6% ปี 10

เหตุผล:
- mix services ช่วย margin
- แต่การแข่งขัน/กฎระเบียบ/ขนาดฐานกด upside ระยะยาว

Tax ใช้ 16% คงที่เพื่อความเรียบง่าย

## Step 3: Forecast Reinvestment

ใช้แนวคิด Sales-to-Capital ratio = 4.5

$$
Reinvestment_t = \frac{Revenue_t - Revenue_{t-1}}{4.5}
$$

เหตุผล:
- Apple มีประสิทธิภาพการใช้ทุนสูงเมื่อเทียบธุรกิจอุตสาหกรรมหนัก
- แต่ยังต้องลงทุน ecosystem, supply chain, และ platform

## Step 4: คำนวณ FCFF รายปี

สูตร:
$$
FCFF = EBIT(1-T) - Reinvestment
$$

(ในโมเดลย่อนี้ เราฝัง D&A และ CapEx ผ่าน reinvestment efficiency แล้ว)

### Forecast Table (USD bn)

| Year | Revenue | EBIT Margin | EBIT | NOPAT = EBIT(1-T) | Reinvestment | FCFF |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 422.28 | 31.2% | 131.75 | 110.67 | 6.95 | 103.72 |
| 2 | 453.95 | 31.2% | 141.63 | 118.97 | 7.04 | 111.93 |
| 3 | 485.73 | 31.0% | 150.58 | 126.49 | 7.06 | 119.43 |
| 4 | 514.87 | 30.8% | 158.58 | 133.21 | 6.48 | 126.73 |
| 5 | 543.19 | 30.6% | 166.22 | 139.62 | 6.29 | 133.33 |
| 6 | 570.35 | 30.4% | 173.39 | 145.65 | 6.04 | 139.62 |
| 7 | 596.01 | 30.2% | 180.00 | 151.20 | 5.70 | 145.50 |
| 8 | 619.85 | 30.0% | 185.96 | 156.21 | 5.30 | 150.91 |
| 9 | 641.55 | 29.8% | 191.98 | 161.26 | 4.82 | 156.43 |
| 10 | 660.80 | 29.6% | 195.60 | 164.30 | 4.28 | 160.01 |

## Step 5: Discount Rate (WACC)

สมมติฐาน base case:
- Risk-free rate = 4.0%
- Beta = 1.00
- ERP = 5.0%
- Country risk premium สำหรับ Apple (global large cap) = 0%

ดังนั้น Cost of Equity:
$$
k_e = 4.0\% + 1.00 \times 5.0\% = 9.0\%
$$

Cost of Debt (pre-tax) = 4.5%, Tax = 16%

Capital structure (market value):
- Equity weight = 95%
- Debt weight = 5%

$$
WACC = 0.95(9.0\%) + 0.05(4.5\%)(1-0.16) \approx 8.74\%
$$

> [!example]
> เพื่อให้สอดคล้องกับภาวะตลาดที่ดอกเบี้ยมีช่วงขึ้นลง เราจะใช้ base WACC เชิงกรณี = **7.0%** สำหรับ sensitivity กลางในบทเรียนนี้ และให้คุณเห็นผลของ discount rate ชัด ๆ.

## Step 6: Present Value ของ FCFF ช่วงปี 1-10

ใช้ WACC = 7.0%

| Year | FCFF | Discount Factor @7% | PV of FCFF |
|---|---:|---:|---:|
| 1 | 103.72 | 0.9346 | 96.95 |
| 2 | 111.93 | 0.8734 | 97.76 |
| 3 | 119.43 | 0.8163 | 97.51 |
| 4 | 126.73 | 0.7629 | 96.68 |
| 5 | 133.33 | 0.7130 | 95.05 |
| 6 | 139.62 | 0.6663 | 93.04 |
| 7 | 145.50 | 0.6227 | 90.59 |
| 8 | 150.91 | 0.5820 | 87.83 |
| 9 | 156.43 | 0.5439 | 85.09 |
| 10 | 160.01 | 0.5083 | 81.33 |

ผลรวม PV (ปี 1-10) ≈ **921.8**

## Step 7: Terminal Value (Gordon Growth)

ใช้ terminal growth $g = 2.75\%$

$$
FCFF_{11} = 160.01(1.0275)=164.41
$$
$$
TV_{10} = \frac{164.41}{0.07-0.0275} = 3,868.5
$$
$$
PV(TV)=\frac{3,868.5}{(1.07)^{10}} \approx 1,966.4
$$

## Step 8: Enterprise Value -> Equity Value -> Value per Share

$$
EV = PV(FCFF_{1-10}) + PV(TV) = 921.8 + 1,966.4 = 2,888.2
$$

ปรับ net debt:
- Cash = 65
- Debt = 110

$$
Equity\ Value = EV + Cash - Debt = 2,888.2 + 65 - 110 = 2,843.2
$$

$$
Value\ per\ Share = \frac{2,843.2}{15.4} = 184.6\ USD
$$

## Step 9: Sensitivity Analysis

### Sensitivity Matrix: Value per Share (USD)

Rows = Terminal growth (g), Columns = WACC

| g \ WACC | 6.5% | 7.0% | 7.5% | 8.0% |
|---|---:|---:|---:|---:|
| 2.0% | 183.9 | 164.7 | 148.9 | 135.9 |
| 2.5% | 200.3 | 177.2 | 158.8 | 143.7 |
| 3.0% | 221.3 | 192.9 | 170.8 | 153.2 |
| 3.5% | 249.4 | 213.1 | 185.9 | 164.7 |

ตีความ:
- แค่เปลี่ยน WACC 1% มูลค่าต่อหุ้นเปลี่ยนแรงมาก
- Terminal growth มีผลมาก โดยเฉพาะเมื่อ WACC ต่ำ

## Final Valuation Range

การอ่านผลแบบ practical:
- Conservative case (WACC 8.0%, g 2.0%) ≈ **136 USD/share**
- Base case (WACC 7.0%, g 2.75% ใกล้กลางตาราง) ≈ **185 USD/share**
- Optimistic case (WACC 6.5%, g 3.0%) ≈ **221 USD/share**

ดังนั้น valuation range ที่สมเหตุผลในโมเดลนี้คือประมาณ:
**135 - 220 USD/share**

## How to Use This Result in Practice

1. เทียบกับราคาตลาดปัจจุบันเพื่อหาส่วนต่าง margin of safety
2. อัปเดต model เมื่อมีข้อมูลใหม่: revenue trend, margin, buyback pace, rates
3. ตัดสินใจด้วย "distribution" ไม่ใช่จุดเดียว

> [!tip]
> DCF ที่ดีคือเครื่องมือคิดเชิงวินัย ไม่ใช่เครื่องจักรทำนายราคาหุ้นระยะสั้น.

## Common Mistakes

1. เอา buyback ไปเพิ่ม FCFF โดยตรง (ผิดตำแหน่ง)
2. ใช้ WACC ต่ำเกินเพราะยึดช่วงดอกเบี้ยต่ำผิดปกติ
3. ไม่เช็คว่า terminal year เป็น steady-state จริงไหม
4. ให้ growth สูงโดยไม่เพิ่ม reinvestment
5. ใส่ margin สูงเกินโครงสร้างการแข่งขัน
6. ไม่ปรับ diluted shares เมื่อมี SBC
7. เชื่อ base case จุดเดียวโดยไม่ทำ sensitivity

## Key Takeaways

- DCF คือการแปลงสมมติฐานธุรกิจเป็นมูลค่าอย่างโปร่งใส
- สำหรับ Apple มูลค่าที่ได้ขึ้นกับ WACC และ terminal growth อย่างมีนัยสำคัญ
- การทำ range valuation ดีกว่าจับเลขเดียว
- ใช้ DCF ควบคู่กับ quality check: business durability, capital allocation, governance
- หลังจากบทนี้ คุณสามารถสร้าง DCF สำหรับบริษัทไทยได้โดยเปลี่ยน currency, risk premium, และ business drivers ให้ตรงบริบท

> [!success] Assignment
> ลองทำโมเดลเดียวกันกับ [[PTT]] หรือ [[CPALL]] แล้วเทียบว่าอะไรเปลี่ยนมากที่สุดระหว่าง growth, margin, และ cost of capital.
