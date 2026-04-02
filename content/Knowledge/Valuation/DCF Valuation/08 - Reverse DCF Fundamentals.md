---
title: "Reverse DCF Fundamentals (Damodaran Lens)"
date: 2026-03-30
tags: [valuation, dcf, reverse-dcf, market-expectations, damodaran]
aliases: ["08 Reverse DCF", "Reverse DCF พื้นฐาน"]
instructor: Aswath Damodaran (Persona)
language: th
---

[[00 - DCF Valuation Course MOC]] | [[09 - Estimating Growth Rate Realistic Approaches]] | [[10 - Reverse DCF Practical Application]]

# 08) Reverse DCF Fundamentals

> [!quote]
> "คำถามแรกไม่ใช่หุ้นถูกหรือแพง คำถามแรกคือราคาตลาดกำลังบอกว่าบริษัทต้องโตและทำกำไรแบบไหน"  
> แนวคิดนี้คือหัวใจของ Reverse DCF ในมุม Prof. Aswath Damodaran

> [!important]
> เอกสารนี้ใช้ตัวเลขตัวอย่างแบบสอนวิธี (teaching numbers) ที่สอดคล้องกับโครงจริงของกิจการขนาดใหญ่  
> จุดประสงค์คือฝึกอ่าน "Market Expectations" ไม่ใช่ให้ราคาเป้าหมายเพื่อแนะนำซื้อขายทันที

## 1) Reverse DCF คืออะไร และต่างจาก Traditional DCF อย่างไร

### Traditional DCF (Forward Valuation)
คุณตั้งสมมติฐานเองก่อน:
1. Revenue growth
2. Operating margin
3. Reinvestment
4. WACC
5. Terminal growth

แล้วคำนวณหา Intrinsic Value เพื่อเทียบกับราคา

### Reverse DCF (Market-Implied Valuation)
คุณล็อก "ราคาตลาดวันนี้" ก่อน แล้วแก้สมการย้อนกลับว่า:
- ตลาดกำลัง imply growth เท่าไร
- ตลาดกำลัง imply margin เท่าไร
- ตลาดกำลัง imply reinvestment/efficiency เท่าไร

> [!tip]
> Traditional DCF ใช้ตอบ: "มูลค่าที่ฉันเชื่อคือเท่าไร"  
> Reverse DCF ใช้ตอบ: "ตลาดกำลังเชื่ออะไรอยู่"

## 2) ทำไมต้องคิดแบบ Market Expectations

Damodaran เน้นว่า valuation ที่ดีต้องเชื่อม 3 ส่วน:
1. Narrative (เรื่องเล่าธุรกิจ)
2. Numbers (สมมติฐานเชิงตัวเลข)
3. Price (สิ่งที่ตลาดสะท้อนแล้ว)

Reverse DCF ทำให้คุณเห็นทันทีว่า:
- คุณ "ไม่เห็นด้วยกับตลาด" ตรงไหน
- ความต่างอยู่ที่ growth, margin หรือ risk
- ต้องพิสูจน์อะไรให้ได้ก่อนลงทุน

```mermaid
flowchart TD
    A[Market Price วันนี้] --> B[แปลงเป็น Enterprise Value]
    B --> C[ล็อกสมมติฐานที่สังเกตได้\nWACC / Tax / Shares / Net Debt]
    C --> D[เลือกตัวแปรที่จะแก้ย้อน\nImplied Growth หรือ Margin]
    D --> E[Goal Seek จน PV(FCFF)=EV ตลาด]
    E --> F[ได้ชุด Market-Implied Expectations]
    F --> G[เทียบกับ Base case ของเรา]
    G --> H[ตัดสินใจ Buy Hold Sell]
```

## 3) Implied Value Drivers ที่ต้องแยกอ่านให้ครบ

หลายคนทำ Reverse DCF แล้วดูแค่ implied growth ซึ่งไม่พอ ต้องอ่านทั้งระบบ

### 3.1 Growth Drivers
- Revenue CAGR ช่วง high-growth
- Fade pattern ของ growth (ลงเร็วหรือลงช้า)
- Terminal growth ($g$) ระยะยาว

### 3.2 Profitability Drivers
- Operating margin trajectory
- Mature/terminal margin
- Tax rate ที่ normalize แล้ว

### 3.3 Reinvestment Drivers
- Sales-to-Capital ratio
- Reinvestment rate
- ROIC และการคง ROIC เหนือ cost of capital ได้นานแค่ไหน

### 3.4 Risk/Discount Drivers
- WACC
- Capital structure target
- Country/size/liquidity risk (ถ้ามีเหตุผล)

### 3.5 Equity Bridge Drivers
- Net debt
- Cash & non-operating assets
- Minority interests / cross holdings
- Share dilution (โดยเฉพาะ SBC สูง)

> [!warning]
> Reverse DCF ผิดพลาดบ่อยที่สุดตอน "ผสม operating assumptions กับ financing assumptions แบบไม่สอดคล้อง"
> เช่น ใช้ FCFF แต่ไปหักดอกเบี้ยในกระแสเงินสดอีกครั้ง

## 4) สูตรหลักที่ใช้ใน Reverse DCF

### 4.1 Enterprise Value from FCFF
$$
EV = \sum_{t=1}^{N}\frac{FCFF_t}{(1+WACC)^t} + \frac{TV_N}{(1+WACC)^N}
$$

$$
TV_N = \frac{FCFF_{N+1}}{WACC-g}
$$

### 4.2 Free Cash Flow to Firm
$$
FCFF_t = EBIT_t(1-T) - Reinvestment_t
$$

### 4.3 Growth-Reinvestment-Return Identity
$$
g_t = Reinvestment\ Rate_t \times ROIC_t
$$

หรือเขียนเป็น:
$$
Reinvestment\ Rate_t = \frac{g_t}{ROIC_t}
$$

### 4.4 Sales-to-Capital Shortcut
$$
Reinvestment_t = \frac{\Delta Revenue_t}{Sales\ to\ Capital_t}
$$

> [!note]
> Identity นี้สำคัญมากในสไตล์ Damodaran เพราะบังคับให้ growth ต้องมี "ต้นทุนของ growth" เสมอ

## 5) ขั้นตอนทำ Reverse DCF แบบใช้งานจริง

| ขั้น | ทำอะไร | Output |
|---|---|---|
| 1 | เอา Market Cap + Debt - Cash | Enterprise Value จากตลาด |
| 2 | กำหนด forecast horizon (เช่น 10 ปี) | โครงเวลา high-growth + fade |
| 3 | ล็อก WACC, tax, terminal growth | ชุด assumptions ที่ไม่แก้ย้อน |
| 4 | เลือกตัวแปรที่จะแก้ (เช่น CAGR 10 ปี) | Unknown variable |
| 5 | สร้าง revenue, margin, reinvestment schedule | FCFF รายปี |
| 6 | Goal Seek ให้ PV เท่ากับ EV ตลาด | Implied assumption |
| 7 | เทียบกับ base/bear/bull thesis | Investment decision |

## 6) ตัวอย่างคำนวณ Step-by-step (เชิงตัวเลขจริงแบบสอนวิธี)

### 6.1 ข้อมูลตั้งต้น (สมมติฐาน ณ 30 มี.ค. 2026)

| รายการ | ค่า |
|---|---:|
| Market Cap | 2,850 bn |
| Debt | 120 bn |
| Cash | 70 bn |
| Enterprise Value (ตลาด) | 2,900 bn |
| Revenue TTM | 400 bn |
| Current EBIT Margin | 31.0% |
| Tax Rate | 21.0% |
| WACC | 8.5% |
| Terminal growth ($g$) | 2.5% |
| Terminal EBIT Margin | 30.0% |
| Sales-to-Capital (ช่วงโต) | 2.2 |
| Sales-to-Capital (ช่วง mature) | 1.8 |

### 6.2 กำหนดโครงรูปของ growth ที่ตลาดอาจคิด
เราปล่อยให้ 10-year CAGR เป็นตัวแปรที่ต้อง solve โดยวางรูปแบบการ fade ไว้ล่วงหน้า

- Years 1-3: growth สูงกว่าค่าเฉลี่ย
- Years 4-7: growth ลดลงต่อเนื่อง
- Years 8-10: เข้าใกล้ mature growth

ตัวอย่าง path ที่ solve ได้ใกล้ราคา (หนึ่งในคำตอบที่เป็นไปได้):

| Year | Revenue Growth | Revenue | EBIT Margin | EBIT(1-T) | Reinvestment | FCFF |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 10.0% | 440.0 | 31.2% | 108.5 | 18.2 | 90.3 |
| 2 | 9.0% | 479.6 | 31.4% | 119.0 | 18.0 | 101.0 |
| 3 | 8.0% | 518.0 | 31.6% | 129.4 | 17.4 | 112.0 |
| 4 | 7.0% | 554.3 | 31.5% | 138.1 | 18.3 | 119.8 |
| 5 | 6.0% | 587.6 | 31.3% | 145.6 | 18.5 | 127.1 |
| 6 | 5.0% | 617.0 | 31.0% | 151.1 | 16.3 | 134.8 |
| 7 | 4.5% | 644.8 | 30.8% | 156.6 | 15.4 | 141.2 |
| 8 | 4.0% | 670.6 | 30.5% | 161.7 | 14.3 | 147.4 |
| 9 | 3.5% | 694.1 | 30.2% | 166.0 | 13.2 | 152.8 |
| 10 | 3.0% | 714.9 | 30.0% | 169.4 | 11.6 | 157.8 |

หน่วย: bn

### 6.3 Discount กระแสเงินสด
$$
PV(FCFF_{1-10}) \approx 1{,}010
$$

### 6.4 Terminal Value
ปี 11:
$$
FCFF_{11}=FCFF_{10}\times(1+g)=157.8\times1.025=161.7
$$

$$
TV_{10}=\frac{161.7}{0.085-0.025}=2{,}695
$$

$$
PV(TV_{10})=\frac{2{,}695}{(1.085)^{10}}\approx 1{,}890
$$

### 6.5 สรุปเทียบกับตลาด
$$
EV_{model}=1{,}010+1{,}890=2{,}900 \approx EV_{market}
$$

ดังนั้น ในชุดสมมติฐานนี้ ตลาดกำลัง imply โดยคร่าวว่า:
- growth เฉลี่ย 10 ปีราว 6-7% พร้อม fade ลง
- margin ทรงตัวแถว 30%+
- reinvestment efficiency ยังดี (Sales-to-Capital ไม่พัง)

> [!tip]
> Reverse DCF ไม่มีคำตอบเดียว  
> ถ้าให้ margin สูงขึ้น implied growth ที่ต้องการจะต่ำลง และกลับกัน

## 7) Reverse DCF ที่ดีต้องผูกกับ Narrative เสมอ

ให้เขียน "เรื่อง" ก่อนว่าทำไมบริษัทถึงทำได้ตาม implied expectations:

1. บริษัทมี moat ที่รองรับ margin จริงไหม
2. โอกาสขยายตลาดใหญ่พอรองรับ growth หรือไม่
3. ต้องลงทุนเพิ่มเท่าไรจึงจะได้ growth ตามนั้น
4. คู่แข่งจะกด ROIC ลงเร็วแค่ไหน

> [!warning]
> ถ้า narrative อธิบายตัวเลขไม่ได้ ให้เชื่อตัวเลขว่าเรื่องเล่าเราอาจผิด

## 8) Checklist ก่อนเชื่อผล Reverse DCF

- ใช้ EV/FCFF ให้สอดคล้อง (ไม่สลับ FCFE)
- หนี้และเงินสดอัปเดตล่าสุด
- ปรับ one-off items ใน EBIT แล้ว
- รวมผล dilution จาก SBC แล้ว
- growth ช่วงท้ายไม่เกินเศรษฐกิจระยะยาว
- ROIC ระยะยาวมีเหตุผลเทียบอุตสาหกรรม

## 9) สรุปมุมมอง Damodaran

Reverse DCF ไม่ได้มีหน้าที่บอกว่า "ราคาถูกหรือแพง" ทันที  
หน้าที่ของมันคือ decode price ให้เห็นว่า "ตลาดต้องเชื่ออะไร" แล้วคุณค่อยตัดสินว่าความเชื่อนั้นสมเหตุสมผลหรือไม่

อ่านต่อ:
- [[09 - Estimating Growth Rate Realistic Approaches]]
- [[10 - Reverse DCF Practical Application]]
