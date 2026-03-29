---
title: "Round 2 Summary - Theoretical Mechanisms of PE Band"
note_type: debate_summary
round: 2
moderator: จานดัน
created: 2026-03-29
status: complete
---

# 📊 ROUND 2 SUMMARY: กลไกทำให้ PE Band "ทำงาน" ในทางทฤษฎี

## 🎯 คำถามหลัก (by จานดัน)

> **อะไรคือกลไกหลักที่ทำให้ PE Band Valuation "ทำงานได้" ในทางทฤษฎี? กลไกเหล่านี้ยัง valid ในตลาดไทยปัจจุบันหรือไม่? แสดง case study/ตัวอย่างจริงมาสนับสนุน**

---

## 🤖 CODEX (PRO) - สาระสำคัญ

### 🧠 กลไก 3 ตัวที่ทำให้ PE Band ทำงาน

#### 1. Mean Reversion ของ Multiple

**หลักการ:**
```
ราคาหุ้น = กำไร (E) × Multiple (PE)
```

- สำหรับธุรกิจโมเดลเสถียร (โรงพยาบาล, สื่อสาร, ค้าปลีกใหญ่)
- PE มักแกว่งรอบค่าเฉลี่ยของตัวเอง
- เมื่อ PE สูงเกิน → นักลงทุนลดน้ำหนัก
- เมื่อ PE ต่ำเกิน → นักลงทุนคุณภาพกลับเข้าซื้อ

#### 2. Behavioral Finance (Overreaction + Anchoring)

**ปรากฏการณ์:**
| เหตุการณ์ | ปฏิกิริยาตลาด | ผลลัพธ์ |
|----------|--------------|---------|
| งบไตรมาสเดียวแผ่ว | Overreaction | PE ร่วงเกิน |
| ข่าวภูมิรัฐศาสตร์ | Anchoring ข่าวลบ | หลุด -1SD/-2SD |
| Flow ต่างชาติไหลออก | Panic selling | Undervaluation |

**หน้าที่ PE Band:** เป็นกรอบวินัย ลดอารมณ์ จับจังหวะ re-rating

#### 3. Liquidity/Discount-rate Cycle

**ความสัมพันธ์:**
```
Bond Yield ↑ → PE Compress (ตลาดลด multiple)
Bond Yield ↓ → PE Expand (ตลาดเพิ่ม multiple)
```

- PE Band ไม่ได้จับแค่ "ถูก/แพง" แต่สะท้อนวัฏจักรเงินทุน

---

### ✅ ทำไมกลไกยังใช้ได้ในตลาดไทย 2025-2026

**ข้อมูลสนับสนุน:**
- SET P/E (11 มี.ค. 2026): **16.08x**
- ตลาดยังตอบสนอง valuation ระดับ multiple ชัดเจน

**เงื่อนไขการใช้งาน:**

| ประเภทหุ้น | ความเหมาะสม | ข้อควรระวัง |
|-----------|-------------|-------------|
| Large cap, กำไรสม่ำเสมอ | ✅ ใช้ได้ดี | - |
| Cyclical | ⚠️ ใช้ได้ปานกลาง | ต้องใช้ normalized EPS |
| กำไรผันผวน/ติดลบ | ❌ ใช้ยาก | Band หลอกสัญญาณ |

**สรุป PRO:** PE Band = "framework for probability" ไม่ใช่ mechanical signal 100%

---

### 📈 Case Study ที่ PRO ยกมาสนับสนุน

#### Case 1: BH (Bumrungrad)

| รายละเอียด | ข้อมูล |
|------------|--------|
| **สัญญาณ** | Forward PE ~19x (< -1SD) |
| **ช่วงเวลา** | ม.ค. 2025 |
| **52-week Range** | 130 - 214 บาท |
| **ราคาปัจจุบัน** | 176-179 บาท |
| **ผลลัพธ์** | Re-rate ขึ้นจากโซนล่าง ✅ |

**แหล่งอ้างอิง:**
- SET Factsheet: https://www.set.or.th/en/market/product/stock/quote/BH/factsheet
- Research: https://www.makemoneyinsight.com/2025/01/27/135015/

---

#### Case 2: BDMS

| รายละเอียด | ข้อมูล |
|------------|--------|
| **สัญญาณ 1** | Forward PE -1SD (ต.ค. 2024) |
| **สัญญาณ 2** | Forward PE < -2SD (มี.ค. 2026) |
| **ราคา** | 18.5-19.5 บาท |
| **ผลลัพธ์** | Mean reversion หลังแรงขาย ✅ |

**แหล่งอ้างอิง:**
- https://www.bangkokbiznews.com/finance/analysis/1148274
- https://www.makemoneyinsight.com/2026/03/13/176981/

---

#### Case 3: ADVANC

| รายละเอียด | ข้อมูล |
|------------|--------|
| **เหตุการณ์** | Bond-yield pressure กดหุ้นปันผล |
| **ช่วงเวลา** | ต้นปี 2024 |
| **52-week Range** | 264 - 410 บาท (+55%) |
| **กลไก** | Liquidity shock → Multiple compress → PE expand กลับ |

**แหล่งอ้างอิง:**
- https://www.investing.com/equities/advanced-info-historical-data

---

## 🌟 GEMINI (CON) - สาระสำคัญ

### ⚠️ จุดอ่อนร้ายแรงของกลไกทางทฤษฎี

#### ปัญหาหลัก: Ceteris Paribus Assumption

**ความหมาย:** Mean Reversion ตั้งอยู่บนสมมติฐาน "ปัจจัยอื่นๆ คงที่ตลอดเวลา"

**ซึ่งขัดแย้งกับความจริง:**

| ปัญหา | รายละเอียด | ผลกระทบ |
|-------|------------|----------|
| Structural Changes | Disruption, วงจรผลิตภัณฑ์หมดอายุ | Moat ถูกทำลาย |
| Earnings Trap | "E" หดตัวรุนแรงเมื่อธุรกิจขาลง | PE ดีดกลับแพงทันที |
| Macro Regime Shifts | ยุคดอกเบี้ยต่ำ → ดอกเบี้ยปกติ | PE Mean เปลี่ยนไปเลย |

---

### ❌ ทำไมกลไก "ไม่ Valid" ในตลาดไทยปัจจุบัน

#### 1. การเติบโตของเศรษฐกิจถดถอยถาวร

```
GDP ไทยเติบโตเฉลี่ย: 2-3% (จากปัญหาเชิงโครงสร้าง)
สังคมสูงวัย: กำลังซื้อลดลง
ผลกระทบ: Growth Premium หาย → PE Downgrade ถาวร
```

#### 2. การรุกรานจากภายนอก

| อุตสาหกรรม | ภัยคุกคาม | ผลลัพธ์ |
|-----------|----------|---------|
| ยานยนต์ | EV จีน | Margin หด |
| เหล็ก | Oversupply จีน | ราคาตก |
| สินค้าอุปโภค | สินค้าราคาถูกจีน | แข่งขันไม่ได้ |

**สรุป:** ฐานกำไรในอดีต ≠ ความสามารถทำกำไรอนาคต

---

### 📉 Case Study: ความล้มเหลวของ PE Band

#### Case 1: กลุ่มสินเชื่อรายย่อย (MTC, SAWAD)

| ช่วงเวลา | PE Range | สถานการณ์ |
|----------|----------|-----------|
| 2016-2021 | 20x - 35x | Growth Stock, พอร์ตโตระเบิด |
| 2022-2023 | 18x - 20x | แตะ -2SD ดู "ถูก" |
| ปัจจุบัน | 10x - 15x | Structural Derate |

**การเปลี่ยนแปลงเชิงโครงสร้าง:**
- ธปท. คุมเพดานดอกเบี้ย
- หนี้ครัวเรือนสูง → NPL พุ่ง
- Cost of Funds สูงขึ้น

**บทเรียน:** ซื้อที่ -2SD (PE 18-20x) → ขาดทุนหนักเพราะตลาด Derate ถาวร

---

#### Case 2: SCC (ปูนซิเมนต์ไทย)

| รายละเอียด | ข้อมูล |
|------------|--------|
| **PE ในอดีต** | 12x - 15x (เสถียรยาวนาน) |
| **ปัญหา** | China Oversupply ทุ่มตลาด |
| **ผลลัพธ์** | "E" หดตัวหนัก กำไรต่ำสุดในรอบหลายปี |
| **PE Band** | หลอกว่า "ถูก" แต่พื้นฐานพัง |

**บทเรียน:** PE Band ไม่สามารถป้องกันการพังทลายของปัจจัยพื้นฐานเชิงโครงสร้าง

---

## ⚖️ ตารางเปรียบเทียบทั้งสองฝั่ง

### กลไกที่ทั้งสองฝั่งเห็นตรงกัน

| กลไก | PRO | CON |
|------|-----|-----|
| Mean Reversion | ใช่ แต่มีเงื่อนไข | ใช่ แต่ตั้งคำถามความถาวร |
| Behavioral Bias | ใช่ | ใช่ |
| Liquidity Cycle | ใช่ | ใช่ |

### จุดที่ขัดแย้งกัน

| ประเด็น | PRO | CON |
|---------|-----|-----|
| **Mean Reversion ยัง valid ไหม?** | ✅ ใช่ ในหุ้นใหญ่กำไรนิ่ง | ❌ ไม่ โดน Structural Derating |
| **PE Band = Value Trap?** | ❌ ถ้าใช้ถูกวิธีไม่ใช่ | ✅ แทบทุกกรณีในตลาดไทย |
| **Case study ไหนน่าเชื่อถือ?** | BH, BDMS, ADVANC = success | MTC, SAWAD, SCC = failure |

---

### 🔥 Case Study Showdown

| หุ้น | ฝั่งที่ยก | ผลลัพธ์ | คำอธิบาย |
|-----|----------|---------|----------|
| **BH** | PRO | 130→179 (+38%) | PE < -1SD แล้ว re-rate |
| **BDMS** | PRO | Mean reversion | PE < -2SD แล้วฟื้น |
| **ADVANC** | PRO | 264→410 (+55%) | Liquidity cycle |
| **MTC** | CON | PE 20-35x→10-15x | Structural derating |
| **SAWAD** | CON | PE 20-35x→10-15x | Regulatory change |
| **SCC** | CON | E หดหนัก | China oversupply |

---

## 📌 ประเด็นสำคัญจาก Round 2

### คำถามที่ยังไม่มีคำตอบชัดเจน

1. **Case study ไหน representative กว่ากัน?**
   - PRO: BH/BDMS/ADVANC = หุ้นใหญ่เสถียร
   - CON: MTC/SAWAD/SCC = หุ้นที่โดน structural change

2. **การตัดสินใจใช้ PE Band ต้องมีเกณฑ์อะไร?**
   - ต้องกรองหุ้นที่ "โดน structural change" ออกก่อน?
   - หรือ PE Band มีปัญหาโดยธรรมชาติ?

3. **"Structural Derating" vs "Mean Reversion"**
   - รู้ได้ยังไงว่า PE ต่ำเพราะ undervalued หรือเพราะ derating?
   - ต้องใช้เครื่องมืออะไรเสริม?

---

## 🎤 สรุปโดยจานดัน

> [รอ จานดัน ใส่สรุป]

---

*สรุปโดย Synapse-O | Round 2 Complete | Awaiting Round 3*
