---
title: 01 - DCF Fundamentals
tags:
  - finance/valuation
  - dcf
  - fundamentals
instructor: Aswath Damodaran (Persona)
language: th
---

# 01) DCF Fundamentals

> [!quote] Professor's Opening
> ผมคือ Aswath Damodaran. ถ้าคุณจำได้แค่ประโยคเดียวจากบทนี้ ให้จำว่า: **Value มาจาก Cash Flows, Growth, และ Risk** ไม่ใช่แค่ Story ที่เล่าสวย.

> [!info] แผนที่คอร์ส
> - บทนี้: ฐานคิดของ DCF
> - ต่อด้วย [[02 - Free Cash Flow]]
> - แล้วไป [[03 - Forecasting Cash Flows]], [[04 - Discount Rate WACC]], [[05 - Terminal Value]]
> - ปิดท้ายที่ [[06 - Complete DCF Example Apple]]

## DCF คืออะไร? และทำไมต้องใช้?

**Discounted Cash Flow (DCF)** คือการประเมินมูลค่ากิจการจากมูลค่าปัจจุบันของกระแสเงินสดอนาคต:

$$
Value = \sum_{t=1}^{n}\frac{CF_t}{(1+r)^t} + \frac{Terminal\ Value}{(1+r)^n}
$$

โดย:
- $CF_t$ = กระแสเงินสดในปีที่ $t$
- $r$ = discount rate (สะท้อนความเสี่ยง)
- $Terminal\ Value$ = มูลค่าหลังช่วง forecast แบบ explicit

### ทำไม DCF เป็นแกนกลางของ Valuation

1. มันบังคับให้คุณเชื่อม **Story -> Numbers**
2. มันบังคับให้คุณแยก **มูลค่า (Value)** ออกจาก **ราคา (Price)**
3. มันทำให้คุณเห็นชัดว่าอะไรเป็น driver จริงของมูลค่า:
- Operating margin
- Reinvestment efficiency
- Cost of capital
- Duration ของ growth

> [!tip] Damodaran Rule
> นักลงทุนเก่งไม่ใช่คนที่เดาราคาแม่นที่สุด แต่เป็นคนที่เข้าใจว่า **ทำไม** มูลค่าถึงเปลี่ยนเมื่อสมมติฐานเปลี่ยน.

## Time Value of Money: พื้นฐานที่ห้ามพลาด

### หลักคิด
เงิน 100 บาทวันนี้ มีค่ามากกว่า 100 บาทอีก 1 ปี เพราะ:
- เอาไปลงทุนได้
- มีความเสี่ยงว่าจะไม่ได้รับ
- มี inflation ลดอำนาจซื้อ

### สูตรสำคัญ

Future Value:
$$
FV = PV(1+r)^n
$$

Present Value:
$$
PV = \frac{FV}{(1+r)^n}
$$

### ตัวอย่างเร็ว
สมมติคุณจะได้เงิน 1,000 บาทอีก 3 ปี และ required return = 10%

$$
PV = \frac{1,000}{(1.10)^3} = 751.3
$$

แปลว่าเงิน 1,000 บาทในอีก 3 ปี มีมูลค่าเท่า 751.3 บาทวันนี้

> [!example] Intuition
> บริษัทที่สร้าง cash flow ช้ากว่า (อีกไกล) จะโดน discount หนักกว่าเสมอ. นี่คือเหตุผลที่หุ้น growth แพ้ทางเมื่ออัตราดอกเบี้ยขึ้น.

## Cash Flow vs Earnings

### ทำไม Net Income ไม่ใช่ Cash
กำไรบัญชี (accrual earnings) มีข้อจำกัด:
- รับรู้รายได้/ค่าใช้จ่ายตามมาตรฐานบัญชี ไม่ใช่ตาม cash movement จริง
- มีรายการ non-cash เช่น depreciation, stock-based compensation
- มี one-off gains/losses ที่ไม่สะท้อนกำลังทำเงินระยะยาว

### สิ่งที่ DCF ต้องการคือ "กระแสเงินสดที่แจกจ่ายได้"
ขึ้นกับมุมมอง:
- ถ้าจะประเมินทั้งกิจการ: ใช้ [[02 - Free Cash Flow#FCFF คืออะไร]]
- ถ้าจะประเมินมูลค่าผู้ถือหุ้นโดยตรง: ใช้ FCFE

### ตัวอย่างเปรียบเทียบ
บริษัท A และ B มีกำไรสุทธิเท่ากัน 10,000 ล้านบาท
- A ต้องลงทุนเพิ่มโรงงานทุกปี (CapEx สูง)
- B ธุรกิจ asset-light ลงทุนต่ำ

แม้ earnings เท่ากัน มูลค่าอาจต่างมาก เพราะ cash flow หลัง reinvestment ไม่เท่ากัน

> [!warning] ข้อสอบที่พังบ่อย
> "กำไรโต = มูลค่าสูง" ไม่จริงเสมอ ถ้าการโตต้องใช้ทุนมหาศาลและผลตอบแทนต่อทุนต่ำ.

## เมื่อไหร่ DCF ใช้ได้ดี / ใช้ไม่ค่อยดี

## When DCF Works Well

DCF ทำงานดีเมื่อ:
1. ธุรกิจมี **cash flow เป็นบวกหรือมองเห็นทางเป็นบวกได้**
2. โมเดลธุรกิจเข้าใจได้ (unit economics ชัด)
3. มีฐานข้อมูลพอ forecast ได้ (รายได้, margin, reinvestment)
4. ความเสี่ยงสามารถ map เป็น discount rate ได้พอสมเหตุผล

ตัวอย่างเหมาะกับ DCF:
- Consumer staples โตช้าแต่เสถียร
- Large tech ที่เริ่ม mature (เช่น Apple)
- Infrastructure/utility ที่รายได้คาดการณ์ได้

## When DCF Works Poorly

DCF อ่อนแรงเมื่อ:
1. ธุรกิจอยู่ในช่วงเปลี่ยนโมเดลหนัก ๆ (business model pivot)
2. Cash flow ติดลบยาวและไม่ชัดว่าจะ positive เมื่อไร
3. บริษัท cyclical แรงมากและคุณใช้ปีเดียวเป็นฐาน
4. ความไม่แน่นอนสูงจน sensitivity กว้างเกินใช้งาน

ตัวอย่างที่ต้องระวัง:
- Early-stage biotech ที่พึ่ง binary event
- Deep commodity cycle ถ้าทำ normalized earnings ไม่เป็น
- บริษัทที่ accounting quality ต่ำ

> [!note]
> DCF ไม่ได้ "ผิด" สำหรับบริษัทเสี่ยงสูง แต่ **input uncertainty** อาจสูงจน output ไม่มี usefulness เชิงตัดสินใจ.

## โครงสร้างความคิดแบบ Damodaran: Story -> Numbers -> Value

### Step 1) Story
- บริษัทจะโตจากอะไร?
- moat คืออะไร?
- ขนาดตลาดพอไหม?

### Step 2) Numbers
- Revenue growth path
- Margin path
- Reinvestment needs
- Risk (cost of capital)

### Step 3) Value
- คำนวณ FCFF/FCFE
- discount กลับมา
- sensitivity analysis

> [!tip]
> ถ้า story เปลี่ยน แต่ model ไม่เปลี่ยน แปลว่า model ของคุณ "ไม่ได้คิด".

## Mini Real Example: Apple vs Amazon (Framework View)

### Apple
- Mature, high margin, cash conversion สูง
- Growth ไม่ explosive แต่ฐานรายได้ใหญ่
- เหมาะกับ DCF ที่เน้น stability + moderate growth fade

### Amazon
- หลาย segment (e-commerce, AWS, ads)
- Margin profile ต่างกันมากระหว่าง segment
- DCF ต้องทำแบบ sum-of-parts หรืออย่างน้อยแยก logic margin transition

### บริษัทไทย (ตัวอย่างแนวคิด)
- [[CPALL]]: กระแสเงินสดค่อนข้างเสถียร แต่ต้องระวัง lease accounting และการขยายสาขา
- [[AOT]]: โครงสร้างกึ่ง infrastructure ต้อง model traffic + regulation risk

## Common Mistakes

1. ใช้ growth สูงยาวเกินจริงโดยไม่ลดลงสู่ steady state
2. ใช้ discount rate เดียวกับทุกบริษัทโดยไม่สะท้อน business risk
3. ใช้ earnings แทน cash flow ตรง ๆ
4. ลืม reinvestment (โดยเฉพาะ working capital และ maintenance CapEx)
5. ใช้ terminal growth สูงกว่า nominal GDP ระยะยาว
6. ไม่ทำ sensitivity analysis แล้วเชื่อ point estimate เดียว
7. ใช้ตัวเลข 2 ตำแหน่งทศนิยมจนดูแม่น แต่สมมติฐานไม่ robust

## Key Takeaways

- DCF คือเครื่องมือแปลง "อนาคต" เป็น "มูลค่าปัจจุบัน" ผ่าน cash flow และ risk
- Value driver หลักมี 4 ตัว: cash flow level, growth, reinvestment efficiency, discount rate
- DCF ดีมากถ้าธุรกิจพอคาดการณ์ได้ และแย่ถ้า uncertainty สูงจนสมมติฐานไร้ฐาน
- เริ่มจาก story ที่ coherent แล้วแปลงเป็น numbers อย่างมีวินัย
- บทถัดไปจะลงลึกว่า cash flow ที่ควรใช้ใน DCF ต้องนิยามอย่างไร: [[02 - Free Cash Flow]]
