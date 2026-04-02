---
title: 04 - Discount Rate WACC
tags:
  - finance/valuation
  - dcf
  - wacc
  - capm
instructor: Aswath Damodaran (Persona)
language: th
---

# 04) Discount Rate WACC

> [!quote] Professor's Opening
> นักลงทุนจำนวนมากโต้เถียงเรื่อง growth แต่ลืมว่า valuation พังง่ายมากจาก **discount rate ที่ตั้งผิด**.

> [!info] อ่านต่อเนื่อง
> - Cash flow: [[02 - Free Cash Flow]]
> - Forecast: [[03 - Forecasting Cash Flows]]

## WACC คืออะไร

เมื่อใช้ FCFF เราต้อง discount ด้วย **WACC (Weighted Average Cost of Capital)**:

$$
WACC = \frac{E}{D+E}k_e + \frac{D}{D+E}k_d(1-T)
$$

โดย:
- $k_e$ = Cost of Equity
- $k_d$ = Pre-tax Cost of Debt
- $T$ = marginal tax rate

## Cost of Equity: CAPM และ Beta

## สูตร CAPM

$$
k_e = R_f + \beta \times ERP
$$

สำหรับประเทศเสี่ยงสูงกว่า developed market อาจเพิ่ม country risk premium (CRP):
$$
k_e = R_f + \beta \times ERP_{mature} + CRP
$$

### 1) Risk-free Rate (Rf)
เลือกให้สอดคล้อง currency ของ valuation
- ทำ valuation เป็น USD -> ใช้ US Treasury
- ทำ valuation เป็น THB -> ใช้พันธบัตรรัฐบาลไทยระยะยาว

### 2) Equity Risk Premium (ERP)
- Mature ERP = premium ของตลาดหุ้นเหนือ risk-free ในระยะยาว
- Implied ERP ใช้จากราคาตลาดปัจจุบัน (forward-looking มากกว่า historical)

### 3) Beta
Beta วัด sensitivity ต่อ market risk

แนวทางที่ robust:
1. หา unlevered beta จาก peer
2. re-lever ตามโครงสร้างทุนเป้าหมาย

Unlever:
$$
\beta_u = \frac{\beta_l}{1+(1-T)\frac{D}{E}}
$$

Re-lever:
$$
\beta_l = \beta_u\left(1+(1-T)\frac{D}{E}\right)
$$

> [!tip]
> Regression beta ดิบจาก 2 ปีรายสัปดาห์อาจ noisy มาก ใช้ bottom-up beta มักนิ่งกว่า.

## Cost of Debt

### แนวคิด
Cost of debt ควรสะท้อน "อัตราดอกเบี้ยที่บริษัทต้องจ่ายถ้ากู้ใหม่วันนี้"

วิธีประมาณ:
1. ถ้ามี bond trading -> ใช้ YTM ปัจจุบัน
2. ถ้าไม่มี -> ใช้ synthetic rating จาก interest coverage แล้ว map spread

$$
k_d = R_f + Default\ Spread
$$

After-tax cost of debt:
$$
k_d(1-T)
$$

> [!warning]
> อย่าใช้ดอกเบี้ยเฉลี่ยในอดีตโดยไม่ดูภาวะดอกเบี้ยปัจจุบัน.

## Capital Structure: ใช้น้ำหนักแบบ Market Value

หลักการ:
- น้ำหนัก E และ D ควรใช้ market value ไม่ใช่ book value
- ถ้าบริษัทมีแผนเปลี่ยน leverage ชัด ให้ใช้ target capital structure

### ตัวอย่างย่อ
- Market Cap = 2,800 bn
- Market Debt = 120 bn
- E/(D+E)=95.9%, D/(D+E)=4.1%

ถ้า $k_e=8.2\%$, $k_d=5.0\%$, $T=20\%$

$$
WACC = 0.959(8.2\%) + 0.041(5.0\%)(0.8) \approx 8.0\%
$$

## Country Risk Premium (CRP)

## ทำไมต้องมี CRP
ถ้าบริษัทมี exposure สูงในประเทศที่ sovereign risk สูงกว่า US คุณไม่ควรใช้ ERP แบบ US ล้วน

วิธีง่ายที่นิยม:
$$
CRP \approx Sovereign\ Bond\ Spread
$$

วิธีละเอียดขึ้น:
$$
CRP_{equity} = Sovereign\ Spread \times \frac{\sigma_{Equity}}{\sigma_{Bond}}
$$

### ตัวอย่างบริษัทไทย
ถ้าทำ valuation หุ้นไทยใน THB:
- ใช้ Rf ไทย
- ERP ไทย (หรือ mature ERP + CRP ไทย)
- ระวัง exposure รายได้ต่างประเทศ ถ้าบริษัท globalized สูง

> [!note]
> บริษัท listed ไทยที่รายได้ต่างประเทศมาก อาจต้องใช้ blended risk by revenue geography.

## Dynamic Discount Rate (Optional Advanced)

ในบางเคส WACC ไม่ควรคงที่ทั้ง 10 ปี:
- ช่วง early stage risk สูง -> WACC สูง
- โตจนเสถียร -> WACC ลดลง

แต่ต้องระวังไม่ใช้ dynamic WACC เพื่อ "ดัน valuation"

## Real Example Snapshot

## Apple (แนวคิด)
- Beta ใกล้ตลาด, debt cost ต่ำ, leverage ไม่สูงมาก
- WACC มักอยู่โซนกลางหลักเดียว (single-digit)

## Amazon
- Beta มักสูงกว่า Apple เล็กน้อยเพราะ cyclicality ของบาง segment
- Debt cost พอๆ กันแต่ equity risk premium impact สูงกว่า

## บริษัทไทย
- โครงสร้างทุนต่างอุตสาหกรรมต่างกันชัด (เช่น utility vs growth tech)
- CRP และ liquidity premium สำคัญขึ้นใน small cap

## Common Mistakes

1. ใช้ book debt/book equity ถ่วงน้ำหนัก WACC
2. ใช้ beta ดิบโดยไม่ปรับ leverage
3. ใช้ risk-free ผิด currency กับ cash flow
4. ลืม country risk ในตลาดเกิดใหม่
5. ใช้ effective tax rate ชั่วคราวแทน marginal tax ระยะยาว
6. ใช้ pre-tax debt cost ไป discount FCFF โดยไม่ทำ after-tax adjustment
7. ปรับ WACC เพื่อให้ได้ target price (model fitting)

## Key Takeaways

- FCFF ต้องคู่กับ WACC; FCFE ต้องคู่กับ Cost of Equity
- Cost of equity ที่ดีต้องมี beta ที่สมเหตุผลและ ERP ที่ forward-looking
- Cost of debt ต้องสะท้อนต้นทุนกู้ "วันนี้" ไม่ใช่อดีต
- ใช้ market value weights และจัดการ country risk อย่างมีหลัก
- ต่อไปเราจะลงลึก terminal value ซึ่งมักเป็นมูลค่าส่วนใหญ่ของ DCF: [[05 - Terminal Value]]
