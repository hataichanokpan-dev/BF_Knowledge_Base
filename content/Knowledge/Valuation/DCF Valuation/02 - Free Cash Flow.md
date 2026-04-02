---
title: 02 - Free Cash Flow
tags:
  - finance/valuation
  - dcf
  - cash-flow
instructor: Aswath Damodaran (Persona)
language: th
---

# 02) Free Cash Flow

> [!quote] Professor's Opening
> มูลค่าถูกกำหนดด้วย **Cash Flow ที่เหลือหลังลงทุนเพื่อรักษาและโตธุรกิจ** ไม่ใช่กำไรที่สวยในงบ.

> [!info] Prerequisite
> อ่านพื้นฐานก่อนที่ [[01 - DCF Fundamentals]]

## FCFF vs FCFE

## FCFF คืออะไร

**Free Cash Flow to Firm (FCFF)** = กระแสเงินสดสำหรับผู้ให้ทุนทั้งหมด (ทั้งเจ้าหนี้และผู้ถือหุ้น) หลังหัก reinvestment ที่จำเป็น

สูตรมาตรฐาน:
$$
FCFF = EBIT(1-T) + D\&A - CapEx - \Delta NWC
$$

หรือใช้แบบ bridge จาก CFO ได้:
$$
FCFF = CFO + Interest(1-T) - CapEx
$$
(ต้องแน่ใจว่า CFO ไม่ปนรายการ non-recurring)

## FCFE คืออะไร

**Free Cash Flow to Equity (FCFE)** = เงินสดที่เหลือสำหรับผู้ถือหุ้นหลังจ่ายดอกเบี้ยและดูแลหนี้

สูตรหนึ่งที่ใช้บ่อย:
$$
FCFE = Net\ Income + D\&A - CapEx - \Delta NWC + Net\ Borrowing
$$

## เลือกใช้ FCFF หรือ FCFE เมื่อไร

- ใช้ FCFF + WACC เมื่อ leverage เปลี่ยนหรืออยากประเมิน operating asset แยกจาก financing
- ใช้ FCFE + Cost of Equity เมื่อ leverage ค่อนข้างคงที่ และต้องการมูลค่าผู้ถือหุ้นตรง ๆ

> [!tip]
> ถ้าคุณไม่มั่นใจเรื่อง debt policy ของบริษัท เลือก FCFF มักปลอดภัยกว่า.

## วิธีคำนวณจากงบการเงินจริง (Step-by-Step)

## Step 1: เริ่มที่ Operating Income (EBIT)

ดูจาก Income Statement แล้วปรับ:
- ตัด one-off gains/losses
- ปรับ restructuring ที่ไม่ recurring
- แยก operating leases/finance leases ให้ consistent

## Step 2: คูณ (1 - Tax Rate)

ใช้ **marginal tax rate ระยะยาว** มากกว่า effective rate ปีเดียว

ตัวอย่าง:
- EBIT = 100
- Tax = 20%
- EBIT(1-T) = 80

## Step 3: บวก Non-cash Charges

เช่น:
- Depreciation
- Amortization
- Impairment (ต้องระวัง recurring หรือไม่)
- Stock-based compensation (ประเด็นถกเถียง: บัญชี non-cash แต่มี dilution เชิงเศรษฐกิจ)

## Step 4: หัก CapEx

CapEx ทั้งหมด = เงินลงทุนสินทรัพย์ถาวร
- ซื้อเครื่องจักร, data center, ร้านค้า, software capitalization

ต้องแยกให้ออก:
- **Maintenance CapEx**: ลงทุนเพื่อรักษาระดับธุรกิจเดิม
- **Growth CapEx**: ลงทุนเพื่อขยายธุรกิจ

## Step 5: หักการเปลี่ยนแปลง Working Capital

$$
\Delta NWC = (NWC_t - NWC_{t-1})
$$

โดยทั่วไป:
$$
NWC = Current\ Operating\ Assets - Current\ Operating\ Liabilities
$$

หลักคิด:
- ถ้า NWC เพิ่ม = ใช้เงินสด (ลบใน FCFF)
- ถ้า NWC ลด = ปล่อยเงินสดกลับมา (บวกใน FCFF)

> [!warning]
> ห้ามเอา cash และ interest-bearing debt มาปนใน operating NWC สำหรับ FCFF.

## Adjustments สำคัญสำหรับ Non-cash และ Accounting Noise

### 1) Stock-Based Compensation (SBC)
มุมมองแบบ Damodaran:
- ใน cash flow มักบวกกลับได้ (non-cash)
- แต่ต้องสะท้อนผล dilution ด้วยจำนวนหุ้น diluted shares

### 2) Operating Leases
ภายใต้มาตรฐานใหม่ lease หลายส่วนอยู่บน balance sheet แล้ว แต่การเปรียบเทียบย้อนหลังต้อง consistent

### 3) R&D Capitalization (โดยเฉพาะ Tech/Pharma)
ถ้ามอง R&D เป็นการลงทุน ไม่ใช่ค่าใช้จ่ายทันที:
- ปรับ EBIT เพิ่มกลับ R&D expense
- สร้าง "R&D asset" แล้วตัด amortization ตาม useful life
- CapEx ต้องรวม economic R&D reinvestment

### 4) Acquisitions
ถ้าบริษัทโตผ่าน M&A อย่างต่อเนื่อง แต่คุณใช้ organic CapEx อย่างเดียว จะ undervalue reinvestment need

## Working Capital Changes แบบลึก

### Operating Working Capital Components ที่พบบ่อย
- Accounts receivable
- Inventories
- Accounts payable
- Accrued operating liabilities

### ธุรกิจที่ NWC ติดลบ (Negative WC)
เช่น retail บางประเภท:
- เก็บเงินลูกค้าเร็ว
- จ่าย supplier ช้ากว่า
- โตแล้วได้ cash float เพิ่ม

นี่ทำให้ช่วงโตเร็ว FCFF ดูดีมาก ต้องระวังว่าเป็น structural หรือ cycle ชั่วคราว

> [!example] ตัวอย่างย่อ
> บริษัทค้าปลีก NWC ปีนี้ -50, ปีหน้า -60
> \(\Delta NWC = -10\) -> ในสูตร \(-\Delta NWC\) = +10
> แปลว่าโตแล้ว "ปล่อย cash" เพิ่ม

## CapEx vs Maintenance CapEx

## ทำไมต้องแยก
- ถ้าคุณหัก CapEx ทั้งหมด คุณอาจกด FCF ต่ำเกินสำหรับธุรกิจที่กำลัง scale
- ถ้าคุณไม่หัก maintenance CapEx คุณจะ overvalue ทันที

## วิธีประมาณ Maintenance CapEx

วิธีที่ใช้ได้จริง:
1. ใช้ Depreciation เป็น proxy ในธุรกิจ mature
2. ใช้ % of revenue ระยะยาวจากประวัติ
3. ใช้ disclosure จากผู้บริหาร (ถ้ามี)
4. reverse-engineer จาก capacity utilization

## ตัวอย่างเชิงตัวเลข

สมมติ (ล้านบาท):
- EBIT = 12,000
- Tax = 20%
- D&A = 2,500
- CapEx = 3,800 (Maintenance 2,200 + Growth 1,600)
- NWC เพิ่ม 600

FCFF = 12,000(0.8) + 2,500 - 3,800 - 600
= 9,600 + 2,500 - 4,400
= **7,700**

ถ้าปีนี้บริษัทหยุดขยายชั่วคราว (growth CapEx = 0) FCF normalized อาจสูงขึ้นเป็น 9,300

> [!note]
> งาน valuation ที่ดีต้องแยก **normalized FCF** ออกจาก **current-year noisy FCF**.

## Real Example Snapshot

### Apple (แนวคิด)
- D&A สูงแต่ CapEx ไม่สูงเท่าบริษัทอุตสาหกรรมหนัก
- Working capital มีประสิทธิภาพสูง
- FCFF conversion จาก EBIT ดีมาก

### Amazon (แนวคิด)
- CapEx และ content/infrastructure spend สูงมากในบางช่วง
- ถ้าไม่ normalize cycle ของ investment จะอ่าน FCF ผิดทิศได้ง่าย

### บริษัทไทย (เช่น CPALL)
- ต้องระวัง lease, expansion pace, และ seasonality ของ inventory

## Common Mistakes

1. ใช้ CFO ตรง ๆ โดยไม่ปรับดอกเบี้ย/one-off
2. ใช้ tax rate ปีเดียวที่ผิดปกติเป็นตัวแทนระยะยาว
3. ลืมปรับ SBC dilution
4. ไม่แยก maintenance vs growth CapEx
5. รวม cash/debt ใน NWC จน FCFF เพี้ยน
6. ละเลย acquisition-based reinvestment
7. ใช้ตัวเลขรายไตรมาสแล้ว annualize แบบไม่ดู seasonality

## Key Takeaways

- FCFF และ FCFE เป็นคนละมุมมองของ "cash distributable"
- สูตรจะง่าย แต่ความยากอยู่ที่ adjustments และ normalization
- Working capital และ CapEx เป็นจุดที่ valuation พังบ่อยที่สุด
- ธุรกิจต่างกันต้องใช้ judgement ต่างกัน ไม่มีสูตรลัดเดียว
- ขั้นต่อไปคือการ forecast สมมติฐานให้ coherent: [[03 - Forecasting Cash Flows]]
