---
title: "คู่มือ DCF หุ้นไทยแบบใช้งานจริง (สไตล์ Damodaran)"
date: 2026-03-30
tags: [valuation, dcf, thai-stocks, value-investing]
aliases: ["Thai DCF Practical Guide", "DCF หุ้นไทย"]
instructor: Aswath Damodaran (Persona)
language: th
---

ถ้าคุณทำ DCF ด้วยสมมติฐานสวยๆ คุณไม่ได้ "ตีมูลค่า" คุณแค่ "แต่งเรื่อง"
เป้าหมายของคู่มือนี้คือทำให้คุณใช้ DCF กับหุ้นไทยได้จริง แบบเข้มพอสำหรับเงินตัวเอง

> [!IMPORTANT]
> ตัวเลขพารามิเตอร์ด้านล่างอิงข้อมูลล่าสุดที่หาได้ ณ **30 มีนาคม 2026**
> ต้องอัปเดตก่อนใช้งานจริงทุกครั้ง

## 1) พารามิเตอร์สำหรับตลาดไทย (Thai Market Parameters)

### 1.1 Risk-free Rate (Rf) ไทย
แนวทางปฏิบัติ:
1. ใช้ผลตอบแทนพันธบัตรรัฐบาลไทยอายุยาว 10 ปี (หรือ duration ใกล้เคียงกระแสเงินสด)
2. ใช้ค่าเฉลี่ย 20-60 วัน ไม่ใช้วันเดียว เพื่อลด noise
3. ให้เป็นสกุลเดียวกับกระแสเงินสด (ถ้า DCF เป็น THB ก็ใช้ Rf THB)

ค่าอ้างอิงล่าสุด:
- ThaiBMA curve (11 มี.ค. 2026): 10Y ≈ **1.92%**
- ตลาดล่าสุดช่วงปลายมี.ค. 2026 มีการแกว่งขึ้นแถว **~2.2%** ได้ในบางวัน

> [!TIP]
> ใช้ **Rf กลางรอบ** เช่น 2.0%-2.2% ดีกว่าเลือกจุดต่ำสุด/สูงสุด

---

### 1.2 Equity Risk Premium (ERP) สำหรับไทย
จาก Damodaran (ม.ค. 2026):
- Mature market ERP ≈ **4.23%**
- Thailand Country Risk Premium (CRP) ≈ **2.07%**
- Thailand Total ERP ≈ **6.30%**

สูตรใช้งานตรง:
$$
ERP_{TH} = ERP_{mature} + CRP_{TH}
$$

---

### 1.3 Thailand Country Risk Premium
ค่าอ้างอิง Damodaran (ม.ค. 2026):
- Sovereign rating: **Baa1**
- Adjusted default spread: **1.36%**
- Country risk premium: **2.07%**
- ถ้าใช้ CDS-based ERP: **5.02%** (อีกวิธีหนึ่ง)

สูตรปรับตาม exposure บริษัท:
$$
CRP_{company} = \lambda \times CRP_{TH}
$$
โดย $\lambda$ สูงขึ้นถ้ารายได้/ความเสี่ยงผูกกับไทยมากกว่าค่าเฉลี่ย

> [!WARNING]
> อย่านับ country risk ซ้ำ: ถ้าเพิ่ม CRP ใน ERP แล้ว อย่าไปยัด premium เดิมซ้ำในจุดอื่นแบบไม่มีเหตุผล

---

### 1.4 Default Spread ไทย: หาจากไหน ใช้ยังไง
แหล่งหลัก:
1. Damodaran country default spread table
2. Sovereign CDS ไทย (ใช้เป็น cross-check)
3. ตาราง synthetic spread จาก interest coverage ratio สำหรับ spread บริษัท

การใช้:
- หา spread รัฐ (country)
- หา spread บริษัท (credit risk เฉพาะบริษัท)
- ต้นทุนหนี้ก่อนภาษีโดยทั่วไป:
$$
k_d = R_f + \text{company default spread} \;(+\text{illiquidity premium ถ้าจำเป็น})
$$

---

## 2) Beta สำหรับหุ้นไทย

### 2.1 Regression Beta vs Bottom-up Beta

| วิธี | ข้อดี | ข้อเสีย |
|-----|-------|--------|
| **Regression beta** | เร็ว, สะท้อนราคาตลาดจริง | หุ้นไทย liquidity ต่ำ, ราคาไม่ขยับทุกวัน, beta เพี้ยนง่าย |
| **Bottom-up beta** | เสถียรกว่า, เหมาะหุ้นเทรดบาง/มีโครงสร้างทุนเปลี่ยนเร็ว | ต้องทำ peer set และ unlever/relever เอง |

ข้อสรุปใช้งานจริง:
- หุ้นไทยส่วนใหญ่ใช้ **bottom-up beta เป็นหลัก**
- regression beta ใช้เป็น sanity check

---

### 2.2 หา Unlevered Beta จาก Peer Group
ขั้นตอน:
1. เลือก peer ธุรกิจใกล้กันจริง (ไทย + ต่างประเทศได้)
2. ดึง $\beta_L$, D/E, tax rate ของ peer
3. unlever ทีละบริษัท:
$$
\beta_U = \frac{\beta_L}{1 + (1-T)\frac{D}{E}}
$$
4. ใช้ median $\beta_U$
5. relever เป็นโครงสร้างทุนเป้าหมายบริษัทไทย

---

### 2.3 Re-lever Beta
$$
\beta_L = \beta_U \left(1 + (1-T)\frac{D}{E}\right)
$$

ตัวอย่าง:
- $\beta_U = 0.65$, $T=20\%$, $D/E=0.75$
$$
\beta_L = 0.65 \times (1 + 0.8 \times 0.75)=1.04
$$

---

### 2.4 ช่วง Beta ที่ใช้เริ่มต้นในไทย (แนวทางตั้งต้น)
อิง industry logic + global unlevered anchors (แล้วค่อยปรับด้วยโครงสร้างทุนไทย):

| อุตสาหกรรม | Beta Range |
|-----------|------------|
| Banking | 0.6-1.0 |
| Property developer | 0.9-1.3 |
| Energy integrated | 0.7-1.0 |
| Retail/commerce | 0.8-1.1 |
| Utility/infra | 0.5-0.8 |

> [!TIP]
> เริ่มจาก bottom-up แล้วค่อย "บิด" ตามความจริงไทย เช่น leverage, cyclicality, governance risk

---

### 2.5 ปัญหา beta หุ้นไทยที่เจอบ่อย
1. Low liquidity/thin trading ทำให้ beta กดต่ำปลอม
2. Family-controlled firms: ความเสี่ยง governance ไม่สะท้อนใน beta
3. Conglomerate discount: beta เดียวไม่พอถ้าธุรกิจหลากหลายมาก
4. Regime shift เร็ว (ดอกเบี้ย/การเมือง/commodity) ทำ historical beta ใช้ยาก

> [!WARNING]
> beta ไม่ใช่ risk ทั้งหมด มันคือ market risk เท่านั้น

---

## 3) Cost of Capital สำหรับไทย

### 3.1 Cost of Equity
$$
k_e = R_f + \beta_L \times ERP_{TH}
$$

ตัวอย่าง:
- $R_f=2.0\%$, $\beta_L=1.04$, $ERP_{TH}=6.30\%$
$$
k_e = 2.0\% + 1.04 \times 6.30\% = 8.55\%
$$

---

### 3.2 Cost of Debt (เมื่อ bond trading ไทยไม่ลึก)
วิธีใช้งานจริง:
1. หา interest coverage ratio:
$$
ICR = \frac{EBIT}{Interest}
$$
2. map เป็น synthetic rating
3. อ่าน default spread จากตาราง rating spread
4. คิด $k_d$

---

### 3.3 Synthetic Rating Approach สำหรับไทย
ตัวอย่าง:
- $ICR = 4.8$ เท่า → ประมาณ rating **A2/A**
- spread ประมาณ **0.78%**
- ถ้าต้องเผื่อสภาพคล่องตราสารหนี้ เพิ่ม 0.2-0.5%

---

### 3.4 WACC Step-by-Step
$$
WACC = \frac{E}{D+E}k_e + \frac{D}{D+E}k_d(1-T)
$$

ตัวอย่าง:
- $k_e=8.55\%$
- $k_d=3.08\%$
- $T=20\%$
- $E/(D+E)=60\%, D/(D+E)=40\%$

$$
WACC = 0.6(8.55\%) + 0.4(3.08\%)(1-0.2)=6.11\%
$$

---

## 4) Conservative Approach (แนวทาง Conservative)

### 4.1 Margin of Safety
เกณฑ์ใช้งาน:
- ธุรกิจนิ่ง/คาดการณ์ง่าย: MOS 20-25%
- ธุรกิจวัฏจักร/หนี้สูง/ธรรมาภิบาลน่ากังวล: MOS 30-40%

---

### 4.2 Growth Assumptions
หลักคุมเกม:
1. ช่วงเติบโตสูงต้องมีเหตุผลจาก ROIC + reinvestment
2. ระยะยาวห้ามโตเกินเศรษฐกิจไปตลอด

สำหรับไทยตอนนี้:
- IMF คาด real GDP 2026 แถว **1.6%**
- BOT inflation target ระยะกลาง **1-3%**
- ดังนั้น nominal growth ระยะยาวแบบอนุรักษ์นิยมใช้ประมาณ **2-4%**
- terminal $g$ แนะนำ **1.5-2.5%** สำหรับหุ้นส่วนใหญ่

---

### 4.3 Terminal Value
$$
TV_n = \frac{FCFF_{n+1}}{WACC-g}
$$

เงื่อนไข:
- $g < WACC$
- $g$ ต้องสมเหตุผลกับศักยภาพเศรษฐกิจไทยระยะยาว

---

### 4.4 ปรับค่าเพื่อความปลอดภัย
1. ใช้ normalized margin (ไม่ใช้ปีพีค)
2. ลด growth ช่วงแรกลง 1-2%
3. เพิ่ม reinvestment rate ถ้าโตเร็ว
4. เพิ่ม spread ฝั่งหนี้ถ้าหนี้ refinance เสี่ยง
5. ทำ sensitivity matrix ทุกครั้ง

---

### 4.5 Cross-check กับ Relative Valuation
ตรวจทาน:
1. เทียบ EV/EBITDA, P/E กับหุ้นใกล้เคียง
2. ถ้า DCF ให้มูลค่าสูงเวอร์ แต่ multiple แพงกว่ากลุ่มมาก ต้องย้อนเช็คสมมติฐาน

> [!IMPORTANT]
> DCF ไม่ใช่ความจริง มันคือ "เครื่องตรวจความสอดคล้องของสมมติฐาน"

---

## 5) ตัวอย่างคำนวณเต็ม (CPALL)

> [!NOTE]
> ตัวอย่างนี้เป็น **case เชิงสอน** ใช้ตัวเลขกลม + พารามิเตอร์ตลาดล่าสุด
> ไม่ใช่คำแนะนำลงทุน

### 5.1 Inputs (ณ 30 มี.ค. 2026)
| Parameter | Value |
|-----------|-------|
| $R_f$ | 2.0% |
| $ERP_{TH}$ | 6.30% |
| $\beta_U$ retail peer | 0.65 |
| Target $D/E$ | 0.75 |
| $T$ | 20% |
| Synthetic spread | 0.78% + liquidity 0.30% → $k_d=3.08\%$ |
| โครงสร้างทุน | E 60% / D 40% |
| FCFF ปีฐาน | 38,000 ล้านบาท |
| Growth ปี 1-5 | 7%, 6%, 5%, 4%, 3% |
| Terminal growth $g$ | 2.0% |

### 5.2 คำนวณ Discount Rate
$$
\beta_L = 0.65(1+0.8 \times 0.75)=1.04
$$
$$
k_e = 2.0\% + 1.04(6.30\%) = 8.55\%
$$
$$
WACC=6.11\%
$$

### 5.3 คำนวณ FCFF และมูลค่ากิจการ
FCFF (ลบ.):
- Y1: 40,660
- Y2: 43,100
- Y3: 45,255
- Y4: 47,065
- Y5: 48,477

Terminal:
$$
FCFF_6 = 48{,}477(1+0.02)=49{,}446
$$
$$
TV_5 = \frac{49{,}446}{0.0611-0.02}=1{,}202{,}822 \text{ ล้านบาท}
$$

PV รวมโดยประมาณ:
- PV ช่วง explicit ≈ 187,606 ลบ.
- PV terminal ≈ 893,576 ลบ.
- Enterprise value ≈ **1,081,183 ลบ.**

สมมติ Net debt (ปรับแล้ว) = 360,000 ลบ.
$$
Equity\ Value = 1{,}081{,}183 - 360{,}000 = 721{,}183 \text{ ลบ.}
$$

หุ้นสามัญ ~8,983 ล้านหุ้น:
$$
Intrinsic\ Value \approx 80.3 \text{ บาท/หุ้น}
$$

### 5.4 Sensitivity Analysis (บาท/หุ้น)

| WACC \ g | 1.5% | 2.0% | 2.5% |
|---|---:|---:|---:|
| 5.6% | 82.9 | 97.6 | 117.0 |
| 6.1% | 69.1 | 80.3 | 94.6 |
| 6.6% | 58.6 | 67.5 | 78.7 |

สรุปเชิงปฏิบัติ:
- base case 80.3
- ถ้าอยาก MOS 25%: ราคาเข้าซื้อ $\le$ ~60 บาท
- ถ้าอยาก MOS 35%: ราคาเข้าซื้อ $\le$ ~52 บาท

---

## 6) Checklist & Quick Reference

### 6.1 Data Sources สำหรับตลาดไทย
| Data | Source |
|------|--------|
| Risk-free THB | ThaiBMA Government Bond Yield Curve |
| Country risk/ERP/default spread | Damodaran country risk table |
| Synthetic rating spreads | Damodaran ratings table |
| ข้อมูลหุ้นไทย/หุ้นคงค้าง/งบ | SET factsheet + 56-1 One Report |
| Macro guardrail | BOT (inflation target), IMF (GDP/inflation projections) |

### 6.2 Common Mistakes ในตลาดไทย
1. ใช้ beta regression ตรงๆ กับหุ้นเทรดบาง
2. เอา growth สูงระยะยาวเกิน nominal GDP
3. ใช้ปีพิเศษ (กำไรพีค/ขาดทุนพีค) เป็นฐาน
4. ใช้ WACC กับธนาคาร/ประกันเหมือนหุ้นทั่วไป
5. ไม่ปรับ minority interest / cross-holding
6. นับ risk premium ซ้ำซ้อนหลายชั้น
7. ไม่ทำ sensitivity แล้วมั่นใจในเลขจุดเดียว

### 6.3 Quick Formula Reference

**Cost of equity:**
$$
k_e=R_f+\beta ERP
$$

**Unlever beta:**
$$
\beta_U=\frac{\beta_L}{1+(1-T)\frac{D}{E}}
$$

**Relever beta:**
$$
\beta_L=\beta_U\left(1+(1-T)\frac{D}{E}\right)
$$

**Cost of debt:**
$$
k_d=R_f+\text{default spread}
$$

**WACC:**
$$
WACC=\frac{E}{D+E}k_e+\frac{D}{D+E}k_d(1-T)
$$

**Terminal value:**
$$
TV_n=\frac{FCFF_{n+1}}{WACC-g}
$$

---

## แหล่งอ้างอิง (ใช้จริงในเอกสารนี้)
- [Damodaran: Country Default Spreads and Risk Premiums (อัปเดต 5 ม.ค. 2026)](https://pages.stern.nyu.edu/adamodar/New_Home_Page/datafile/ctryprem.html)
- [Damodaran: Global Betas by Sector (Jan 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/BetasGlobal.html)
- [Damodaran: Ratings, Interest Coverage Ratios and Default Spreads (Jan 2026)](https://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/ratings.html)
- [ThaiBMA Government Bond Yield Curve](https://www.thaibma.or.th/compositerpt/GovYieldCurve.aspx)
- [BOT Monetary Policy Target 2026 (inflation target 1.0-3.0%)](https://www.bot.or.th/en/our-roles/monetary-policy/monetary-policy-target.html)
- [IMF Article IV Thailand (13 ก.พ. 2026)](https://www.imf.org/en/news/articles/2026/02/13/pr26048-thailand-imf-executive-board-concludes-2025-article-iv-consultation-with-thailand)
- [SET CPALL Factsheet](https://www.set.or.th/en/market/product/stock/quote/CPALL/factsheet)
