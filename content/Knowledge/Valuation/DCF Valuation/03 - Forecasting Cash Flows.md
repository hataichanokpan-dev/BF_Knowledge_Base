---
title: 03 - Forecasting Cash Flows
tags:
  - finance/valuation
  - dcf
  - forecasting
instructor: Aswath Damodaran (Persona)
language: th
---

# 03) Forecasting Cash Flows

> [!quote] Professor's Opening
> DCF ไม่ได้พังเพราะคณิตศาสตร์พัง มันพังเพราะ **การ forecast ที่ไม่เชื่อมกับเศรษฐศาสตร์ธุรกิจจริง**.

> [!info] เชื่อมบทก่อน
> - ฐานคิด: [[01 - DCF Fundamentals]]
> - นิยาม cash flow: [[02 - Free Cash Flow]]

## Framework การ Forecast แบบมืออาชีพ

ลำดับที่ควรทำ:
1. Forecast Revenue
2. Forecast Operating Margin
3. Forecast Tax Rate (normalized)
4. Forecast Reinvestment (CapEx + NWC + intangibles)
5. ได้ FCFF/FCFE รายปี
6. กำหนด transition สู่ Terminal Value

## Revenue Forecasting Methods

## วิธีที่ 1: Top-down (TAM -> Share)

$$
Revenue = Market\ Size \times Market\ Share
$$

เหมาะกับ:
- ธุรกิจใหม่
- ธุรกิจที่ market growth เป็น driver สำคัญ

ข้อดี: เชื่อม macro/story ดี
ข้อเสีย: share สมมติยาก, overconfidence สูง

## วิธีที่ 2: Bottom-up (Unit Economics)

$$
Revenue = Volume \times Price
$$

แยกตาม segment ได้ละเอียด:
- Unit sold
- Average selling price (ASP)
- Mix shift

เหมาะกับธุรกิจที่มี unit metric ชัด เช่น iPhone shipments, cloud usage

## วิธีที่ 3: Historical + Mean Reversion
ใช้ historical growth แล้วค่อย ๆ fade เข้าสู่ stable growth

แนวคิด Damodaran:
- Growth สูงไม่อยู่ถาวร
- Competitive forces จะบีบ excess growth ลงเสมอ

> [!tip]
> เลือกวิธีเดียวเป็นแกน แล้วใช้วิธีอื่นเป็น cross-check ไม่ใช่ผสมมั่ว.

## Margin Analysis

## Margin ที่ต้องดู
- Gross margin
- Operating margin (EBIT margin)
- EBITDA margin (ใช้ระวัง)

DCF ใช้ **Operating margin** เป็นหลัก เพราะใกล้กับ operating cash economics

## วิธี forecast margin แบบไม่ฝัน
1. เทียบ historical distribution ของ margin
2. เทียบ peer group economics
3. ดู scale effect และ mix effect
4. ใส่ pressure จากการแข่งขัน

### ตัวอย่าง
บริษัท software early growth margin อาจขึ้นจาก 12% -> 22%
แต่ mature แล้วอาจ stabilize ที่ 24-26% ไม่ใช่ 40% ถ้า moat ไม่ลึกพอ

> [!warning]
> Margin expansion ต้องมีเหตุผลเชิงโครงสร้าง (automation, pricing power, mix shift)
> ไม่ใช่ "เพราะอยากให้ valuation สูง".

## Growth Rates: Historical vs Forward

## Historical Growth
ใช้เพื่อรู้:
- ฐานการเติบโตที่ผ่านมา
- sensitivity ต่อ cycle

แต่ต้องไม่ blind extrapolation

## Forward Growth
ควรสะท้อน:
- Addressable market ที่เหลือ
- Reinvestment capacity
- Return on invested capital (ROIC)

สัมพันธ์สำคัญ:
$$
Growth \approx Reinvestment\ Rate \times ROIC
$$

ถ้าคุณ forecast growth สูง แต่ reinvestment ต่ำและ ROIC ปานกลาง สมการจะไม่ลงตัว

## Life Cycle Logic (High Growth -> Transition -> Stable)

แนะนำแบ่ง 3 phase:
1. **High-growth period**: growth สูง, margin และ reinvestment ผันผวน
2. **Transition period**: growth ลดลง, margin เข้าสู่ระดับยั่งยืน
3. **Stable period**: growth ใกล้เศรษฐกิจระยะยาว, ROIC ใกล้ cost of capital

> [!example] Practical Fade Pattern
> 10 ปี forecast:
> - ปี 1-3 โต 12%, 10%, 8%
> - ปี 4-7 โต 7% -> 5%
> - ปี 8-10 โต 4% -> 3%

## Terminal Value Concepts (ภาพรวมก่อนบท 5)

Terminal Value มักเป็นสัดส่วนใหญ่ของ DCF (50-80% ในหุ้น growth)

2 วิธีหลัก:
- Perpetuity growth (Gordon)
- Exit multiple

แนวปฏิบัติที่ผมแนะนำ:
- ใช้ Gordon เป็นหลักเพราะเชื่อมเศรษฐศาสตร์
- ใช้ Exit multiple เป็น market sanity check

อ่านลึกต่อใน [[05 - Terminal Value]]

## ตัวอย่างจริงเชิงวิธีคิด

## Apple (Mature Big Tech)
- Revenue growth fade เร็วกว่าบริษัทเล็ก เพราะฐานใหญ่
- Margin สูงแต่ไม่ควรขยายไม่จำกัด
- Reinvestment efficiency ดี (sales-to-capital สูง)

## Amazon (Multi-engine)
- แยก segment forecast สำคัญมาก: e-commerce vs AWS vs ads
- Margin blended อาจดูต่ำ ถ้าไม่แยกจะมองผิดว่า quality ต่ำ

## บริษัทไทย (ตัวอย่าง AOT)
- Revenue ขับด้วย traffic และ regulatory framework
- Margin ถูกกำกับด้วยโครงสร้างต้นทุน fixed cost สูง
- ใช้ scenario ดีกว่า single forecast

## Forecasting Checklist (ก่อนกดคำนวณ DCF)

- Story coherent ไหม?
- Growth path สอดคล้องกับขนาดบริษัทไหม?
- Margin path มี economic reason ไหม?
- Reinvestment พอ support growth ไหม?
- Terminal assumptions ไม่ขัดหลัก steady-state ไหม?

## Common Mistakes

1. ใช้ historical CAGR ยิงตรงไป 10 ปี
2. Growth สูงแต่ไม่เพิ่ม reinvestment
3. Margin expansion เกิน peer โดยไม่มี moat รองรับ
4. ลืม cycle และ seasonality
5. ใช้ terminal growth เกินศักยภาพเศรษฐกิจระยะยาว
6. forecast ยาวเกินความสามารถในการมองเห็น
7. ไม่เช็คความสอดคล้องระหว่าง growth, ROIC, reinvestment

## Key Takeaways

- Forecast ที่ดีต้องเริ่มจาก economics ของธุรกิจ ไม่ใช่ spreadsheet aesthetics
- Revenue, margin, reinvestment ต้องเชื่อมกันเป็นระบบ
- Growth ที่ยั่งยืนต้องมีทุนรองรับและผลตอบแทนต่อทุนที่พอ
- Terminal value ไม่ใช่ถังขยะใส่สมมติฐานเว่อร์
- บทถัดไปคือหัวใจ discounting: [[04 - Discount Rate WACC]]
