---
title: "Round 4 Summary - Real-World Application"
note_type: debate_summary
round: 4
moderator: จานดัน
created: 2026-03-29
status: complete
---

# 📊 ROUND 4 SUMMARY: Real-World Application - Decision Framework

## 🎯 คำถามหลัก (by จานดัน)

> **"สร้าง 'Decision Framework' ที่สมบูรณ์แบบสำหรับการใช้ PE Band ในตลาดไทย"**

---

## 🤖 CODEX (PRO) - PE Band Decision Framework

### แนวคิดหลัก: PE Band เป็น "เครื่องมือจังหวะและวินัยราคา" ไม่ใช่เครื่องมือเดี่ยว

---

### 1) Step-by-Step Process (10 ขั้นตอน)

| ขั้น | ทำอะไร | เกณฑ์/ตัวเลขที่ต้องผ่าน |
|---|---|---|
| 1 | กำหนด Universe | หุ้นไทยที่มีข้อมูลย้อนหลัง ≥ 7 ปี, free float ดี |
| 2 | คัดความเหมาะสม | EPS บวก ≥ 4 ใน 5 ปีล่าสุด |
| 3 | ทำ Normalized EPS | ตัด one-off, ใช้ EPS เฉลี่ย 3-5 ปี |
| 4 | สร้าง Historical PE Band | Min / P25 / Median / P75 / Max และ SD |
| 5 | ตรวจ Regime Shift | กฎเกณฑ์, เทคโนโลยี, M&A, leverage, moat |
| 6 | เช็ค Macro Overlay | Bond yield 10Y, policy rate, ERP |
| 7 | Cross-check หลายโมเดล | DCF, DDM, EV/EBITDA, PEG, P/BV, ROIC-WACC |
| 8 | ตั้ง Entry/Exit Rules | Entry: PE ≤ P25, Exit: PE ≥ P75 |
| 9 | Position Sizing | ตาม conviction + stop thesis |
| 10 | Monitoring | EPS revision, margin, debt, governance |

**สูตรแกน:**
- `PE_t = Price_t / EPS_ttm`
- `zPE = (PE_now - PE_median_10y) / SD_10y`
- `Fair Price = PE_fair × EPS_next12m`

---

### 2) Checklist คัดกรองหุ้น

#### ✅ เหมาะกับ PE Band (ต้องผ่าน ≥ 7/10)

| # | เกณฑ์ | Threshold |
|---|-------|-----------|
| 1 | กำไรสุทธิบวกสม่ำเสมอ | บวก ≥ 4 ใน 5 ปี |
| 2 | EPS volatility | CV ≤ 35% |
| 3 | รายการพิเศษ | One-off < 20% ของกำไร 3 ปี |
| 4 | โครงสร้างธุรกิจ | ไม่มี regime break 24 เดือน |
| 5 | ROE | เฉลี่ย 5 ปี ≥ 12% |
| 6 | Net Debt/EBITDA | < 3.0x |
| 7 | สภาพคล่อง | ADTV ≥ 20 ล้านบาท/วัน |
| 8 | ข้อมูลย้อนหลัง | PE history ≥ 7 ปี |
| 9 | CFO/Net Income | 0.8-1.2x |
| 10 | Consensus dispersion | < 20% |

#### ❌ ไม่เหมาะกับ PE Band

| ลักษณะ | ทำไม PE Band พัง |
|--------|-----------------|
| กำไรติดลบสลับบวก | P/E ติดลบ/สูงลวง |
| Commodity cycle รุนแรง | PE ต่ำหลอกตอน peak |
| Turnaround ต้นน้ำ | EPS base ต่ำมาก |
| Hyper-growth bubble | Multiple re-rate ยาว |
| เปลี่ยนโมเดลธุรกิจ | Historical band ใช้ไม่ได้ |

---

### 3) Red Flags: หยุดใช้ PE Band (12 ข้อ)

| # | Red Flag | เกณฑ์ |
|---|----------|-------|
| 1 | EPS ติดลบ | 2 ปีติด |
| 2 | EPS revision | ลง > 15% ใน 3 เดือน |
| 3 | One-off สูง | > 30% ของกำไร |
| 4 | Governance issue | ผู้สอบบัญชีตั้งข้อสังเกต |
| 5 | M&A ใหญ่ | > 30% สินทรัพย์ |
| 6 | Net Debt/EBITDA | > 4.0x |
| 7 | ROIC-WACC | พลิกลบ > 2 ปี |
| 8 | Industry structure | เปลี่ยนถาวร |
| 9 | Free float | ต่ำ/สภาพคล่องแห้ง |
| 10 | Narrative-driven | Price +80% แต่ EPS < +10% |
| 11 | Dilution | หุ้นเพิ่มทุน/convertible สูง |
| 12 | PE dispersion | > 2 SD จาก peer |

---

### 4) Case Studies จริง

#### 🟢 Case A: ADVANC (Success)

| ข้อมูล | ตัวเลข |
|--------|--------|
| P/E 2020-2025 | 15.6x → 21.7x → 23.3x → 19.4x |
| ผลตอบแทน 2021-2024 | +21.86%, -14.83%, +16.95%, +37.60% |
| สะสม 4 ปี | ~+67% (ไม่รวมปันผล) |

**ทำไมสำเร็จ:**
- ธุรกิจ recurring, EPS เสถียร
- PE 2020 อยู่โซนต่ำของประวัติศาสตร์
- Regime ไม่เปลี่ยน
- Cross-check DDM รองรับได้

**บทเรียน:** Quality + Visibility = PE Band มีประโยชน์

#### 🟢 Case B: BDMS (Success เชิงป้องกัน)

| ข้อมูล | ตัวเลข |
|--------|--------|
| P/E 2021-2025 | 42.3x → 34.4x → 29.6x → 23.8x → 19.3x |
| ผลตอบแทน 2023-2025 | -2.02%, -8.10%, -12.97% |

**ทำไมสำเร็จ:**
- PE สูงมาก (zPE > +1) → สัญญาณลดน้ำหนัก
- ไม่ไล่ซื้อตอน PE 42x
- เลี่ยง drawdown ต่อเนื่อง

**บทเรียน:** PE Band กัน "ซื้อแพงเกินจริง"

#### 🔴 Case C: PTTGC (Failure)

| ข้อมูล | ตัวเลข |
|--------|--------|
| P/E 2021-2024 | 5.28x → -23x → 166x → -3.57x |
| EPS 2021-2025 | 10.01 → -1.94 → 0.22 → -6.62 → -3.61 |
| ผลตอบแทน 2022-2025 | -19.86%, -16.50%, -35.37%, -8.20% |

**ทำไมล้มเหลว:**
- Cyclical สูง + EPS flip บวก/ลบแรง
- PE ต่ำ 2021 เป็น low PE trap
- กำไรหด → PE ใช้ไม่ได้ทันที

**บทเรียน:** หุ้นวัฏจักร ใช้ PE Band เป็นตัวหลักไม่ได้

---

### 5) Integration กับเครื่องมืออื่น

| เครื่องมือ | ใช้เมื่อไหร่ | Integration |
|-----------|-------------|-------------|
| DCF | กระแสเงินสดคาดการณ์ได้ | DCF = anchor, PE Band = timing |
| DDM | หุ้นปันผล | ตรวจ implied yield |
| EV/EBITDA | Leverage สูง | กัน distortion จากโครงสร้างทุน |
| PEG | หุ้นเติบโต | เช็ค growth รองรับไหม |
| P/BV + ROE | ธนาคาร/ประกัน | ดู quality ของ book |
| ROIC-WACC | Quality compounding | ปรับ fair PE ขึ้น/ลง |

### Action Grid

| สถานะ | เงื่อนไข | การกระทำ |
|-------|----------|----------|
| Strong Buy | PE ≤ P25 + DCF upside ≥ 20% + ไม่มี Red Flag | 60-100% target |
| Buy | PE < median + โมเดลอื่นยืนยัน | 30-60% |
| Hold | PE ≈ median + upside จำกัด | ถือ/รอ |
| Trim | PE ≥ P75 + growth ชะลอ | -25-50% |
| Exit | โครงสร้างเปลี่ยน/Red Flag รุนแรง | ปิดสถานะ |

---

## 🌟 GEMINI (CON) - First Principles Framework (ไม่พึ่ง PE Band)

### แนวคิดหลัก: PE Band = ขับรถมองกระจกหลังท่ามกลางถนนที่เปลี่ยนไปแล้ว

> **"เงิน 1 บาทที่บริษัทลงทุนไปในวันนี้ จะสร้างกระแสเงินสดกลับมาได้เท่าไหร่ในอนาคต?"**

---

### 1) First Principles Framework (10 ขั้นตอน)

| ขั้น | ทำอะไร | หลักการ |
|---|---|---|
| 1 | TAM & Profit Pool | ตลาดขยาย/หด? (ICE → EV = profit pool หด) |
| 2 | Moat & Competitive Dynamics | สินค้าเป็น Commodity → ตัดทิ้ง |
| 3 | Unit Economics | รายได้ต่อสาขา, CAC vs LTV, กำไรต่อตัน |
| 4 | ROIC vs WACC Spread | ต้อง > +5% ถ้าติดลบ = ทำลายมูลค่า |
| 5 | Incremental ROIC (RONIC) | เงินลงทุนใหม่ได้ผลตอบแทนเท่าเดิมไหม |
| 6 | Cash Conversion | CFO/NI > 80-100% |
| 7 | Capital Allocation | จ่ายปันผลสมเหตุสมผลไหม หรือ Di-worsification |
| 8 | Balance Sheet Stress Test | Interest Coverage ใน worst-case |
| 9 | Reverse DCF | ตลาดคาดหวัง growth ระดับไหน? สูงเกินจริงไหม |
| 10 | Margin of Safety | ซื้อต่ำกว่า intrinsic value ≥ 30% |

---

### 2) Checklist: Structural Derating vs Undervalued

| Metric | ⚠️ Derating (Value Trap) | ✅ Undervalued |
|--------|-------------------------|----------------|
| ROIC Trend | ลดลง → < WACC (8-10%) | ทรงตัว > WACC (12-15%) |
| Gross Margin | หด > 3% ติดต่อกัน | หดชั่วคราวจากวัตถุดิบ |
| Market Share | สูญเสียให้คู่แข่งใหม่ | รักษา/เพิ่มขึ้น |
| Cash Conversion | Days Inventory พุ่ง | วงจรคงที่ |
| Growth Runway | Penetration > 80% | Penetration < 40% |
| Regulatory | โดนคุมถาวร | ไม่มีความเสี่ยง |
| CFO/NI | < 1.0 ติดต่อกัน > 4Q | > 1.0 สม่ำเสมอ |

---

### 3) Red Flags: PE Band พาลงเหว (10 ข้อ)

| # | Red Flag | คำอธิบาย |
|---|----------|----------|
| 1 | Regulatory Regime Shift | คุมเพดานดอกเบี้ย 28% → 24% |
| 2 | Technological Obsolescence | HDD → SSD, ICE → EV |
| 3 | Capex/Sales > 15-20% | Maintenance Capex สูง รายได้ไม่โต |
| 4 | SG&A/Gross Profit > 70% | แข่งขันรุนแรง อัดโปรโมชั่น |
| 5 | Inventory > Sales Growth | 2Q ติดต่อกัน = ขายไม่ออก |
| 6 | Debt-Funded Dividends | ก่อหนี้เพื่อจ่ายปันผล |
| 7 | NPL Migration | Stage 2 > 15% ของพอร์ต |
| 8 | Commodity Spread Collapse | ร่วงหลุด Cash Cost |
| 9 | Insider Selling | เทขายตอน PE -1SD/-2SD |
| 10 | Frequent Restructuring | ตั้งด้อยค่า "ทุก 1-2 ปี" |

---

### 4) Case Studies

#### 🔴 Case 1: SCC - Ultimate Value Trap

**สถานการณ์:**
- PE -2SD, PE ~10-12x, P/BV < 1x
- นักลงทุนคิดว่า "ถูกมาก Blue Chip"

**First Principles ชี้ให้เห็น:**
| ขั้น | สิ่งที่พบ |
|-----|----------|
| Industry Structure | จีนเพิ่มกำลังผลิต = Structural Oversupply |
| ROIC/Margins | Spread ต่ำสุด 10 ปี ไม่มีทีท่าฟื้น |
| Capital Allocation | Long Son เสร็จตอนตลาดล้น |

**ผล:** ราคา 400 → 230-250 บาท, E collapse ทำให้ PE "ถูก" กลายเป็นแพง

#### 🔴 Case 2: SAWAD/MTC - Regime Shift

**สถานการณ์:**
- PE 25-30x → 15-18x (แตะ -2SD)
- PE Band บอก "ซื้อแบบหลับตา"

**First Principles ชี้ให้เห็น:**
| ขั้น | สิ่งที่พบ |
|-----|----------|
| Regulatory | เพดานดอกเบี้ย 28% → 24% → 23% |
| Unit Economics | Yield ลด, CoF ขึ้น, Credit Cost พุ่ง |
| Derating | ROE 25-30% → 15-18% = PE ต้องลด |

**ผล:** Structural Derating ฐาน PE ถูกกดลงถาวร

#### 🟢 Case 3: KEX - หลีกเลี่ยงสำเร็จ

**สถานการณ์:**
- ร่วงจาก IPO ลงมาเรื่อยๆ
- P/S, P/BV ดูต่ำ

**First Principles ชี้ให้เห็น:**
| ขั้น | สิ่งที่พบ |
|-----|----------|
| Moat | แข่งราคากับ Flash, J&T = Pure Commodity |
| Unit Economics | พัสดุต่อชิ้นขาดทุน (Negative GM) |

**ผล:** First Principles สั่ง "ห้ามแตะ" → รอดจาก -90%

---

### 5) Alternative Framework: ROIC-WACC & CAP

**ทำไมดีกว่า PE Band:**

| ข้อ | คำอธิบาย |
|----|----------|
| 1 | แก้ภาพลวงตาของ growth ที่ ROIC < WACC |
| 2 | รวม Capital Intensity ที่ PE มองไม่เห็น |
| 3 | กำหนดระยะเวลา Moat (CAP) |

**Valuation Matrix:**

| กลุ่ม | ตัวอย่าง | วิธีประเมิน |
|------|----------|-------------|
| High ROIC, High CAP | AOT, BDMS | DCF, EVA |
| High ROIC, Low CAP | แฟชั่น, เครื่องดื่ม | ห้าม Terminal Value สูง |
| Low ROIC | วัฏจักร, ตะวันตกดิน | ห้ามใช้ PE, ใช้ P/BV + Liquidation |

---

## ⚖️ ตารางเปรียบเทียบ Framework

### Step-by-Step Process

| ด้าน | CODEX (PRO) | GEMINI (CON) |
|------|-------------|--------------|
| จุดเริ่มต้น | Universe → คัดเหมาะสม → สร้าง Band | TAM → Moat → Unit Economics |
| ตัวชี้วัดหลัก | PE, z-score, Median | ROIC-WACC, Cash Conversion, RONIC |
| การตัดสินใจ | Action Grid (PE zone) | Margin of Safety ≥ 30% |
| Integration | รวม DCF/DDM/EV-EBITDA | ใช้ ROIC-WACC & CAP เป็นหลัก |

### Checklist เปรียบเทียบ

| ด้าน | CODEX (PRO) | GEMINI (CON) |
|------|-------------|--------------|
| เป้าหมาย | คัดหุ้นที่ PE Band ใช้ได้ | แยก Derating vs Undervalued |
| เกณฑ์หลัก | EPS stability, ROE ≥ 12% | ROIC > WACC + 5%, CFO > NI |
| Red Flags | 12 ข้อ (ครอบคลุม) | 10 ข้อ (เน้นโครงสร้าง) |

### Case Studies

| Case | CODEX มองว่า | GEMINI มองว่า |
|------|-------------|---------------|
| ADVANC | ✅ Success: Quality + Visibility | ไม่ได้วิเคราะห์ |
| BDMS | ✅ Success: กันซื้อแพง | ไม่ได้วิเคราะห์ |
| PTTGC | ❌ Failure: Cyclical trap | ไม่ได้วิเคราะห์ |
| SCC | ไม่ได้วิเคราะห์ | ❌ Value Trap: Structural Oversupply |
| SAWAD/MTC | ไม่ได้วิเคราะห์ | ❌ Regime Shift: ห้ามซื้อ |
| KEX | ไม่ได้วิเคราะห์ | ✅ หลีกเลี่ยงสำเร็จ |

---

## 🔥 ประเด็นขัดแย้งสำคัญ

| ประเด็น | CODEX (PRO) | GEMINI (CON) |
|---------|-------------|--------------|
| **PE Band ใช้ได้ไหม?** | ✅ ได้ ถ้าคัดหุ้นถูก + ใช้ร่วมกับโมเดลอื่น | ❌ ไม่ควรพึ่ง ให้ใช้ First Principles |
| **ตัวชี้วัดสำคัญที่สุด** | PE relative to history | ROIC-WACC spread |
| **การตัดสินใจซื้อ** | PE ≤ P25 + โมเดลอื่นยืนยัน | Intrinsic value discount ≥ 30% |
| **Integration** | PE Band + DCF/DDM/EV-EBITDA | ใช้ ROIC-WACC & CAP แทน |
| **Red Flag ร้ายแรงสุด** | EPS ติดลบ 2 ปี / ROIC-WACC พลิกลบ | Regulatory Shift / Unit Economics พัง |

---

## 📌 คำถามที่ยังต้องถกเถียง (ไป Round 5)

1. **ถ้าต้องวิเคราะห์ ROIC-WACC แล้ว ยังต้องใช้ PE Band อีกทำไม?**
   - CODEX: PE Band = Timing tool
   - GEMINI: ไม่จำเป็น, First Principles เพียงพอ

2. **ทั้งสองฝั่งต่างยอมรับ Red Flags คล้ายกัน แล้วต่างกันตรงไหน?**
   - CODEX: ใช้ Red Flags เพื่อ "หยุดใช้ PE Band"
   - GEMINI: ใช้ Red Flags เพื่อ "ยืนยันว่า PE Band ใช้ไม่ได้ตั้งแต่ต้น"

3. **ใครมี Approach ที่ "ใช้งานได้จริง" มากกว่า?**
   - CODEX: มี Action Grid ชัดเจน, threshold วัดได้
   - GEMINI: First Principles ลึกซึ้งกว่า แต่ใช้เวลามากกว่า

---

## 🎤 สรุปโดยจานดัน

> [รอ จานดัน ใส่สรุป]

---

## 📊 สถิติการโต้วาที

| Metric | CODEX | GEMINI |
|--------|-------|--------|
| Steps ใน Framework | 10 | 10 |
| Checklist items | 10 (เหมาะ) + 5 (ไม่เหมาะ) | 7 (แยก Derating) |
| Red Flags | 12 | 10 |
| Case Studies | 3 (2 success, 1 failure) | 3 (ทั้งหมดเกี่ยวกับการหลีกเลี่ยง/ติดกับดัก) |
| Integration tools | 6 | 1 (ROIC-WACC & CAP) |

---

*สรุปโดย Synapse-O | Round 4 Complete | Awaiting Round 5: Final Synthesis*
