---
title: "Raw Response - Round 4 - Codex (PRO)"
note_type: raw_transcript
round: 4
team: Codex (PRO)
created: 2026-03-29
---

# 🤖 RAW RESPONSE - ROUND 4
## Codex (Team A - PRO)

**Question:** สร้าง Decision Framework ที่สมบูรณ์แบบสำหรับการใช้ PE Band ในตลาดไทย

---

**PE Band Decision Framework (ตลาดหุ้นไทย) – เวอร์ชันใช้งานจริงระดับมืออาชีพ**

> แนวคิดหลัก: ใช้ PE Band เป็น "เครื่องมือจังหวะและวินัยราคา" ไม่ใช่เครื่องมือเดี่ยวในการบอกมูลค่าที่แท้จริงทุกกรณี

---

## 1) Step-by-step Process (10 ขั้นตอนครบวงจร)

| ขั้น | ทำอะไร | เกณฑ์/ตัวเลขที่ต้องผ่าน | Output |
|---|---|---|---|
| 1 | กำหนด Universe | หุ้นไทยที่มีข้อมูลย้อนหลัง ≥ 7 ปี, free float ดี, สภาพคล่องพอ | Candidate list |
| 2 | คัด "ความเหมาะสมของโมเดล PE" | EPS บวกอย่างน้อย 4 ใน 5 ปีล่าสุด, ธุรกิจไม่ผันผวนรุนแรงแบบ commodity pure-play | Suitable / Unsuitable |
| 3 | ทำ Normalized EPS | ตัด one-off gain/loss, ใช้ EPS เฉลี่ยถ่วงน้ำหนัก 3-5 ปี (หรือ mid-cycle EPS) | EPS_norm |
| 4 | สร้าง Historical PE Band | คำนวณ PE รายเดือนย้อนหลัง 5-10 ปี: Min / P25 / Median / P75 / Max และ SD | Historical band |
| 5 | ตรวจ Regime Shift | เช็คการเปลี่ยนโครงสร้าง: กฎเกณฑ์, เทคโนโลยี, M&A, leverage, moat | "ใช้ band เดิมได้/ไม่ได้" |
| 6 | เช็ค Macro Overlay ไทย | Bond yield ไทย 10Y, policy rate, ERP ตลาด, sector rotation | Band Adjustment (+/- x เท่า) |
| 7 | Cross-check แบบหลายโมเดล | เทียบ DCF, DDM, EV/EBITDA, PEG, P/BV, ROIC-WACC spread | Fair value corridor |
| 8 | ตั้ง Entry/Exit Rules | Entry: PE <= P25 หรือ z-score <= -1.0 พร้อมพื้นฐานไม่แย่ลง; Exit: PE >= P75 หรือ z >= +1.0 | Trade plan |
| 9 | Position Sizing + Risk | Position size ตาม conviction; stop thesis (ไม่ใช่ stop price อย่างเดียว) | Risk budget |
| 10 | Monitoring + Re-rate trigger | ติดตาม quarterly: EPS revision, margin, debt covenants, governance | Hold/Add/Trim/Exit |

**สูตรแกน**
- `PE_t = Price_t / EPS_ttm`
- `zPE = (PE_now - PE_median_10y) / SD_10y`
- `Fair Price (PE) = PE_fair × EPS_next12m`

---

## 2) Checklist คัดกรองหุ้น: "เหมาะสม vs ไม่เหมาะสม"

### 2.1 หุ้น "เหมาะ" กับ PE Band (ต้องผ่านอย่างน้อย 7/10 ข้อ)

| เกณฑ์ | Threshold ใช้งานจริง |
|---|---|
| กำไรสุทธิบวกสม่ำเสมอ | บวก ≥ 4 ใน 5 ปีล่าสุด |
| EPS volatility | Coefficient of Variation (CV) ของ EPS 5 ปี ≤ 35% |
| รายการพิเศษ | One-off รวมกัน < 20% ของกำไรสะสม 3 ปี |
| โครงสร้างธุรกิจ | ไม่มี major regime break ใน 24 เดือนล่าสุด |
| ความสามารถทำกำไร | ROE เฉลี่ย 5 ปี ≥ 12% (หรือ ROIC ≥ WACC + 3%) |
| งบดุล | Net Debt/EBITDA < 3.0x (ยกเว้น utility บางกรณี) |
| สภาพคล่องหุ้น | ADTV (มูลค่าซื้อขายเฉลี่ย) ≥ 20 ล้านบาท/วัน |
| ข้อมูลย้อนหลัง | มี PE history ที่เชื่อถือได้ ≥ 7 ปี |
| ความน่าเชื่อถือกำไร | CFO/Net Income เฉลี่ย 3 ปี อยู่ในช่วง 0.8-1.2x |
| Consensus dispersion | ส่วนเบี่ยงเบน EPS forecast ไม่สูงผิดปกติ (< 20%) |

### 2.2 หุ้น "ไม่เหมาะ" กับ PE Band (เจอ 1-2 ข้อก็ต้องระวังมาก)

| ลักษณะ | ทำไม PE Band พัง |
|---|---|
| กำไรติดลบสลับบวก | P/E ติดลบ/สูงลวง |
| Commodity cycle รุนแรง | กำไรจุดสูงสุดทำให้ P/E ต่ำหลอก, จุดต่ำสุดทำให้ P/E สูงหลอก |
| Turnaround ต้นน้ำ | EPS base ต่ำมาก ทำให้ band ไม่มีเสถียรภาพ |
| Hyper-growth / theme bubble | Multiple re-rate ยาว ทำให้ "แพงแล้วแพงต่อ" |
| บริษัทเพิ่งเปลี่ยนโมเดลธุรกิจ | historical band ใช้อ้างอิงไม่ได้ |
| กำไรจากรายการพิเศษสูง | EPS ไม่สะท้อน earning power จริง |

---

## 3) Red Flags: "หยุดใช้ PE Band กับหุ้นตัวนี้" (12 ข้อ)

1. EPS ติดลบ 2 ปีติด หรือคาดว่าจะติดลบอีกปี
2. EPS revision ลง > 15% ภายใน 3 เดือน
3. กำไรมากกว่า 30% มาจาก one-off
4. เกิด accounting/governance issue (ผู้สอบบัญชีตั้งข้อสังเกตสำคัญ)
5. เปลี่ยนธุรกิจหลัก หรือ M&A ขนาดใหญ่ > 30% ของสินทรัพย์รวม
6. Net Debt/EBITDA กระโดดเกิน 4.0x
7. ROIC-WACC spread พลิกจากบวกเป็นลบ > 2 ปี
8. โครงสร้างอุตสาหกรรมเปลี่ยน (regulation/disruption) ทำให้ historical margin ใช้ไม่ได้
9. Free float ต่ำ/สภาพคล่องแห้ง จนราคาไม่สะท้อน fair value
10. ราคาวิ่งจาก narrative โดยไร้ EPS support (เช่น Price +80% แต่ EPS โต <10%)
11. Dilution สูง (หุ้นเพิ่มทุน/convertible) ทำให้ EPS ต่อหุ้นบิดเบือน
12. PE dispersion กับ peer กว้างผิดปกติ > 2 SD โดยไร้เหตุผลพื้นฐาน

---

## 4) Case Studies จริง (Success + Failure)

### Case A (Success): ADVANC – Mean reversion ใช้ได้เพราะ earnings quality ดี

**ข้อมูลจริงที่ใช้**
- P/E สิ้นปี: 2020 = 15.6x, 2021 = 21.7x, 2024 = 23.3x, 2025 = 19.4x
- ผลตอบแทนรายปี: 2021 +21.86%, 2022 -14.83%, 2023 +16.95%, 2024 +37.60%

**วิเคราะห์ตาม framework**
1. Suitable: ธุรกิจ recurring, EPS เสถียร
2. Normalized EPS ใช้ได้
3. PE 2020 อยู่โซนต่ำของประวัติศาสตร์
4. Regime ไม่เปลี่ยนแบบทำลายโมเดล
5. Cross-check DDM/DDCF สำหรับหุ้นปันผลสม่ำเสมอรองรับได้
6. เข้าสะสมโซนต่ำ (2020-2021)
7. เมื่อ PE re-rate ไปโซนสูง (2024) ทยอยลด

**ผลลัพธ์**
- หากถือช่วง 2021-2024 ผลตอบแทนราคาสะสมราว `+67%` (ไม่รวมปันผล)
- **บทเรียน:** หุ้น quality สูง + earnings visibility ดี = PE Band มีประโยชน์มาก

---

### Case B (Success เชิงป้องกันความเสี่ยง): BDMS – ช่วย "ไม่ไล่ซื้อแพง"

**ข้อมูลจริง**
- P/E สิ้นปี: 2021 = 42.3x, 2022 = 34.4x, 2023 = 29.6x, 2024 = 23.8x, 2025 = 19.3x
- ผลตอบแทนรายปี: 2023 -2.02%, 2024 -8.10%, 2025 -12.97%

**วิเคราะห์ตาม framework**
1. ธุรกิจพื้นฐานดี แต่ valuation ปลาย 2021-2022 แพ้มากเทียบ band
2. สัญญาณ zPE > +1 ต่อเนื่อง = โซนลดน้ำหนัก
3. Cross-check กับ DCF/DDM มักไม่รองรับ multiple สูงขนาดนั้น
4. ตัดสินใจ "wait for de-rating" แทน chase momentum

**ผลลัพธ์**
- การไม่ไล่ซื้อในช่วง PE สูง ช่วยเลี่ยง drawdown ต่อเนื่อง 2023-2025
- **บทเรียน:** PE Band ไม่ได้มีไว้หา "ซื้อถูกอย่างเดียว" แต่มีไว้กัน "ซื้อแพงเกินจริง"

---

### Case C (Failure): PTTGC – ตัวอย่างคลาสสิกของ cyclicals ที่ PE Band พัง

**ข้อมูลจริง**
- P/E: 2021 = 5.28x, 2022 = -23x, 2023 = 166x, 2024 = -3.57x, ปัจจุบันติดลบ
- EPS (บาท): 2021 = 10.01, 2022 = -1.94, 2023 = 0.22, 2024 = -6.62, 2025 = -3.61
- ผลตอบแทนรายปี: 2022 -19.86%, 2023 -16.50%, 2024 -35.37%, 2025 -8.20%

**วิเคราะห์ตาม framework**
1. Red flag ตั้งแต้นต้น: cyclical สูง + EPS flip บวก/ลบแรง
2. "P/E ต่ำในปี 2021" เป็น low PE trap จากกำไร peak-cycle
3. เมื่อกำไรหด PE กลายเป็นใช้ไม่ได้ทันที
4. ควรใช้ EV/EBITDA mid-cycle, P/BV + cycle indicator แทน

**ผลลัพธ์**
- ซื้อเพราะ "PE ต่ำ" อย่างเดียวเสียหายหนัก
- **บทเรียน:** หุ้นวัฏจักรแรง ใช้ PE Band เป็นตัวหลักไม่ได้

---

## 5) Integration กับเครื่องมืออื่น (ต้องใช้ร่วม ไม่ใช้เดี่ยว)

| เครื่องมือ | ใช้เมื่อไหร่ | ใช้ร่วม PE Band อย่างไร | Trigger ตัดสินใจ |
|---|---|---|---|
| DCF | ธุรกิจกระแสเงินสดคาดการณ์ได้ | DCF เป็น anchor มูลค่า, PE Band เป็น timing | ถ้า PE บอกถูกแต่ DCF upside < 10% = ยังไม่เข้า |
| DDM | หุ้นปันผลสม่ำเสมอ (เช่น telco, utility) | ตรวจว่า implied yield จาก PE สอดคล้อง DDM | หาก dividend sustainability ต่ำ ให้ลดน้ำหนักสัญญาณ PE |
| EV/EBITDA | หุ้น leverage สูง / depreciation สูง | กัน distortion จากโครงสร้างทุนที่ PE มองไม่เห็น | ถ้า PE ถูกแต่ EV/EBITDA แพงกว่า peer >20% ให้ระวัง |
| PEG | หุ้นเติบโต | เช็คว่าความแพงมี growth รองรับไหม | PEG > 1.5 ต่อเนื่อง = PE premium อาจเกินจริง |
| P/BV + ROE | ธนาคาร/ประกัน/การเงิน | แปลง PE signal ไปดู quality ของ book | ROE ลงแต่ P/BV สูง = สัญญาณลบ |
| ROIC-WACC spread | ทุก sector (โดยเฉพาะ quality compounding) | ใช้ปรับ "fair PE" ขึ้น/ลงตามความสามารถสร้างมูลค่า | Spread > +5% ให้ premium ได้, ติดลบให้ discount |

### กฎรวมสั้นๆ (Practical)
1. `PE Band` ให้สัญญาณเข้า แต่ต้องมีอย่างน้อย `2 โมเดล` เห็นทางเดียวกัน
2. ถ้า valuation จากหลายโมเดล "ต่างกันเกิน 25%" ให้ถือว่าความไม่แน่นอนสูง
3. เจอ Red Flag ข้อใดข้อหนึ่งที่เป็นโครงสร้าง ให้ "หยุด PE Band" ทันที

---

## Template ตัดสินใจสุดท้าย (Action Grid)

| สถานะ | เงื่อนไข | การกระทำ |
|---|---|---|
| Strong Buy | PE ≤ P25 และ DCF upside ≥ 20% และไม่มี Red Flag | เข้าสะสม 60-100% ของเป้าหมายน้ำหนัก |
| Buy | PE ต่ำกว่า median ชัด + โมเดลอื่นยืนยัน | ทยอยซื้อ 30-60% |
| Hold | PE ใกล้ median และ upside จำกัด | ถือ/รอข้อมูลใหม่ |
| Trim | PE ≥ P75 หรือ zPE ≥ +1 พร้อม growth ชะลอ | ลดน้ำหนัก 25-50% |
| Exit | โครงสร้างเปลี่ยน/Red Flag รุนแรง | ปิดสถานะ |

---

## แหล่งข้อมูลที่ใช้ (ตัวเลข case study)

- CompaniesMarketCap (P/E history และ annual stock performance):
  - https://companiesmarketcap.com/advanced-info-service/pe-ratio/
  - https://companiesmarketcap.com/advanced-info-service/stock-price-history/
  - https://companiesmarketcap.com/bangkok-dusit-medical-services/pe-ratio/
  - https://companiesmarketcap.com/bangkok-dusit-medical-services/stock-price-history/
  - https://companiesmarketcap.com/ptt-global-chemical/pe-ratio/
  - https://companiesmarketcap.com/ptt-global-chemical/stock-price-history/
- StockAnalysis (EPS/งบการเงินรายปีจาก S&P Global MI template):
  - https://stockanalysis.com/quote/bkk/ADVANC/financials/
  - https://stockanalysis.com/quote/bkk/BDMS/financials/
  - https://stockanalysis.com/quote/bkk/PTTGC/financials/

---

*Recorded by Synapse-O*
