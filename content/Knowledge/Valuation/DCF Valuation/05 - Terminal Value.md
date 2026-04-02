---
title: 05 - Terminal Value
tags:
  - finance/valuation
  - dcf
  - terminal-value
instructor: Aswath Damodaran (Persona)
language: th
---

# 05) Terminal Value

> [!quote] Professor's Opening
> ใน DCF ส่วนที่โกหกง่ายที่สุดคือ Terminal Value เพราะมันอยู่ไกลและดูเหมือนเล็ก แต่จริง ๆ มีน้ำหนักสูงมาก.

> [!info] เชื่อมบท
> - Forecast logic: [[03 - Forecasting Cash Flows]]
> - Discount rate: [[04 - Discount Rate WACC]]

## Terminal Value คืออะไร

คือมูลค่าของกระแสเงินสดหลังช่วง forecast แบบ explicit (เช่น หลังปีที่ 10)

โดยปกติ TV คิดเป็น 50-80% ของ Enterprise Value ในบริษัทโตดี

## Gordon Growth Model (Perpetuity Growth)

สูตร FCFF version:
$$
TV_n = \frac{FCFF_{n+1}}{WACC-g}
$$

เงื่อนไขสำคัญ:
- $g < WACC$ เสมอ
- $g$ ต้องสอดคล้องศักยภาพเศรษฐกิจระยะยาว
- ปีสุดท้ายต้องเป็น "steady-state economics"

### วิธีทำให้ปีสุดท้ายเป็น steady state
1. Margin ไม่กระโดดผิดธรรมชาติ
2. Reinvestment rate สอดคล้องกับ growth
3. ROIC มีแนวโน้มเข้าใกล้ cost of capital

สัมพันธ์ที่ต้องจำ:
$$
Reinvestment\ Rate = \frac{g}{ROIC}
$$

ถ้าคุณตั้ง g = 3% แต่ reinvestment = 0 แปลว่า model ขัดแย้งในตัวเอง

> [!tip]
> Gordon model ไม่ใช่สูตรลัด มันเป็น "ข้อสรุปเชิงเศรษฐศาสตร์" ของ steady-state.

## Exit Multiple Approach

แนวคิด:
- คำนวณ metric ปีสุดท้าย (เช่น EBITDA ปี 10)
- คูณ multiple สมมติ (เช่น EV/EBITDA = 12x)

$$
TV_n = Multiple \times Metric_n
$$

### ข้อดี
- เข้าใจง่าย
- ใช้เทียบกับ market convention ได้

### ข้อเสีย
- แอบพึ่งพา relative valuation
- ถ้า multiple ที่ใช้ฝังความ over/undervalued ของตลาดอยู่ จะลาก DCF ผิด

> [!warning]
> Exit multiple ทำให้ดูเหมือน DCF แต่แก่นจริงกลายเป็น comparables model.

## Which to Use When?

## ใช้ Gordon เมื่อ
- ต้องการ internal consistency สูง
- มีสมมติฐาน steady-state ที่ชัด
- ต้องการเชื่อม story เข้ากับ economics ระยะยาว

## ใช้ Exit Multiple เมื่อ
- ทำ investment banking process ที่ต้องเทียบกับตลาดปัจจุบัน
- ธุรกิจมี metric ที่ market pricing ชัดมาก

## แนวทางที่ผมใช้
1. ใช้ Gordon เป็น base case
2. ใช้ Exit multiple เป็น sanity check
3. ถ้าสองวิธีต่างกันมาก ให้กลับไปตรวจ terminal-year assumptions

## ตัวอย่างเชิงตัวเลข

สมมติปี 10:
- FCFF ปี 10 = 100
- WACC = 8%
- g = 2.5%

$$
FCFF_{11}=100(1.025)=102.5
$$
$$
TV_{10}=\frac{102.5}{0.08-0.025}=1,863.6
$$

ถ้า discount กลับปัจจุบันอีก 10 ปี:
$$
PV(TV)=\frac{1,863.6}{(1.08)^{10}}=863.3
$$

สังเกตว่า TV เพียงส่วนเดียวอาจใหญ่กว่ามูลค่าช่วง explicit ทั้งก้อน

## Advanced Topic: Terminal Economics Consistency

คุณควรตรวจ 4 อย่างใน terminal year:
1. Stable growth ไม่เกิน nominal GDP ระยะยาวของ currency นั้น
2. ROIC ใกล้หรือสูงกว่า WACC เล็กน้อย (ถ้าธุรกิจมี moat)
3. Reinvestment rate เพียงพอ support growth
4. Capital structure ใกล้ long-run target

## Real Company Perspective

## Apple
- บริษัทขนาดใหญ่และ mature มากขึ้น
- ใช้ Gordon growth ได้ดี เพราะ economics ค่อนข้างเสถียร
- Exit multiple ใช้เป็น check ไม่ใช่แกน

## Amazon
- ถ้า model blended margin ยังไม่เสถียร อาจทำให้ terminal year noisy
- ควรระวังการ set multiple ที่ไม่สะท้อน mix shift ของธุรกิจ

## บริษัทไทย
- ธุรกิจ concession/regulation สูง: terminal growth ต้องเคร่งกว่าปกติ
- small cap liquidity ต่ำ: multiple ระยะท้ายอาจผันผวนสูง

## Common Mistakes

1. ตั้ง g สูงเกินจริง (เช่น 5-6% ในธุรกิจ mature)
2. ใช้ WACC ต่ำเกินเพื่อดัน TV
3. ปีสุดท้ายยังอยู่ high-growth economics แต่เอาไปเข้า perpetuity ทันที
4. ใช้ exit multiple จากช่วงตลาดร้อนเกินเหตุ
5. ไม่ตรวจความสอดคล้อง g, ROIC, reinvestment
6. ปล่อยให้ TV > 90% ของมูลค่าโดยไม่ตั้งคำถาม
7. ไม่ทำ sensitivity analysis ของ WACC และ g

## Key Takeaways

- Terminal Value เป็นจุด leverage สูงสุดของ DCF
- Gordon growth ให้กรอบเศรษฐศาสตร์ที่ coherent กว่า
- Exit multiple ใช้ได้ แต่ต้องรู้ว่าคุณกำลังยืม pricing จากตลาด
- หัวใจคือทำ terminal year ให้เป็น steady-state จริง
- บทถัดไปเราจะประกอบทุกชิ้นเป็นเคสจริงแบบครบ: [[06 - Complete DCF Example Apple]]
