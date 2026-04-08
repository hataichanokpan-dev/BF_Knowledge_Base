---
title: SIS Review - 2026-03-28
note_type: review
framework: QSI
version: "2.0"
created: 2026-03-28
ticker: SIS
company: SiS Distribution (Thailand) Public Company Limited
sector: Technology / ICT Distribution
qsi_score: 74
gate0_status: pass
action: WATCH
mos: "69.8% (SUSPICIOUS - scanner sector mismatch)"
entry_zone: 20.50-21.50
target_1: 23.00
target_2: 24.50
stop_loss: 19.80
position_size: 3-5%
dividend_yield: "5.7%"
watchlist: true
tags:
  - note/review
  - framework/qsi
  - sector/technology
  - stock/sis
  - source/3-round-collab
  - scanner/data-mismatch
collaboration: Gemini + Codex + Claude (3-Round)
---

# รีวิว SIS แบบ Deep Dive

> **QSI Deep Dive 3-Round Collaboration** (28 มี.ค. 2026)
>
> | Round | Gemini | Codex | Claude | Action |
> |-------|--------|-------|--------|--------|
> | 1 | 77 (BUY) | 67 (WATCH) | - | Gap: 10 pts |
> | 2 | - | 72 (WATCH) | - | Converged |
> | **3 (Final)** | - | - | **74** | **WATCH** |
>
> **Key Dispute Resolved:**
> - Gemini: Value-Added segment = strong moat (55%+ GP)
> - Codex: Conservative, gross margin 8% still thin, MOS suspicious
> - **Final (Claude):** Partial acceptance - Value-Added pivot real but not full transformation. Scanner sector mismatch is critical concern.

## 📊 สถิติด่วน

| เมตริก | ค่า | แหล่งข้อมูล |
|--------|-----|-------------|
| ราคา SET ล่าสุดที่เข้าถึงได้ | **21.40 THB** | SET Factsheet (26 มี.ค. 2026) |
| ช่วงราคา 52 สัปดาห์ | 17.60 - 24.60 THB | SET Factsheet |
| Sector จริง | **Technology / ICT** | SET Factsheet |
| MOS จาก ATS Scanner | **69.8%** | [[ATS Wave 2.5 - 2026-03-28]] |
| MOS implied IV ที่ราคา 21.40 | **~70.9 THB** | คำนวณย้อนจาก MOS 69.8% |
| P/E | 8.55x | SET Factsheet |
| P/BV | 1.63x | SET Factsheet |
| Revenue 2025 | 30,109 MB | StockAnalysis / S&P Global |
| Net Profit 2025 | 876.4 MB | StockAnalysis / S&P Global |
| Operating Cash Flow 2025 | 1,657 MB | StockAnalysis / S&P Global |
| Dividend/Share | 1.22 THB | StockAnalysis / S&P Global |

**ข้อสังเกตสำคัญ:** หุ้นนี้คือ `SiS Distribution (Thailand)` ไม่ใช่ “Siam Syndicate Technology” และบน SET ถูกจัดอยู่ใน `Technology / Information & Communication Technology` ชัดเจน ดังนั้นการที่ ATS วางไว้ในหมวด `Consumer` มีโอกาสเป็น `mapping/classification error`

**ข้อสังเกตเรื่อง MOS:** ถ้าใช้ราคา `21.40` และ MOS `69.8%` จะได้ intrinsic value ราว `70.9 THB` ซึ่งดูสูงผิดธรรมชาติสำหรับ distributor ที่ net margin ราว `2.9%` และ P/E ตลาดปัจจุบันเพียง `8-9x` ดังนั้น `MOS 69.8%` ยัง **ไม่ควรเชื่อทันที** จนกว่าจะ re-check model input

---

## 🚨 Gate 0: Knockout Rules

| กฎ | สถานะ | หลักฐาน |
|----|--------|---------|
| Profit 3 Years | ✅ PASS | 2023: `645.6 MB` / 2024: `697.6 MB` / 2025: `876.4 MB` |
| CFO Negative 2+ Years | ✅ PASS | Operating Cash Flow 2023-2025 = `1,735 / 1,419 / 1,657 MB` เป็นบวกทุกปี |
| Insider / Strategic Ownership >50% | ✅ PASS | ผู้ถือหุ้นใหญ่ 2 รายแรกถือรวม `61.25%` (`47.29% + 13.96%`) |
| Major Disputes | ✅ PASS | ไม่พบคดีหรือข้อพิพาทสาระสำคัญจาก SET/company pages ที่ตรวจ |
| Trading Signs | ✅ PASS | หน้า factsheet ไม่พบ `Trading Alert` หรือ `Market Alert` ที่มีผลอยู่ |
| Liquidity | ✅ PASS | Average volume ราว `1.12M หุ้น/วัน`; คิดเป็นมูลค่าคร่าวๆ `~23-24 MB/day` |

**Gate 0: PASS** ✅  
**หมายเหตุ:** ไม่มี knockout ชัด แต่มี `yellow flag` 2 จุดคือ `sector mismatch จาก scanner` และ `MOS น่าจะเพี้ยน`

---

### 🔄 Cross-Review Debate (Gemini vs Codex)

| ประเด็น | Gemini | Codex Round 1 | Round 2 Synthesis |
|---------|--------|---------------|-------------------|
| Value-Added pivot | `Value category / SiS Cloud` ดัน gross profit เกินครึ่ง | recurring ยังต่ำ, ยังเป็น box mover | **pivot มีจริง** แต่เป็น `gross profit mix` มากกว่า `business model transformation` เต็มตัว |
| Valuation | P/E `8.5x` + yield `5.7%` = ถูก | MOS สูงผิดธรรมชาติ, อย่ารีบเชื่อว่าถูกมาก | **valuation ควร bump ขึ้นเล็กน้อย** แต่ยังต้องมี distributor discount |
| Balance sheet | debt ลดแรง = quality ดีขึ้น | รับรู้แล้ว แต่ยัง working-capital heavy | **ควรเพิ่มคะแนน Financial Health** เพราะ debt กับ OCF ดีขึ้นชัด |
| AI / Cyber tailwind | catalyst ชัด | ยังเป็น story มากกว่า confirmed re-rating | **เพิ่ม Catalyst ได้เล็กน้อย** แต่ยังไม่พอเป็น BUY |

**ข้อสรุป:** รอบ 1 ผม conservative เกินไปในเรื่อง `Value-Added mix` และ `debt reduction` เพราะแหล่งทางการของ SIS ยืนยันว่า `Value category` สร้าง `55.1%` ของ gross profit ในปี `2024` และ cloud/security มีองค์ประกอบ recurring มากขึ้นจริง แต่ผมยังไม่ยอมรับ thesis ว่า SIS กลายเป็น solution/platform play เต็มตัว เพราะ consolidated gross margin ปี `2025` ยังอยู่แค่ `8.02%` และ recurring revenue ระดับบริษัทก็ยังไม่เด่นพอ

---

## 🚦 Gate 1: Quality Score (39/50)

### 1.1 Moat (8/10)
- บริษัทเป็นตัวแทนกระจายสินค้าให้ vendor ระดับโลกมากกว่า `200` ราย
- มี dealer / customer base มากกว่า `10,000` รายทั่วประเทศ
- มี 4 segment หลัก: `Commercial Products`, `Consumer Products`, `Value Added Products`, และ `Phones`
- จากข้อความประธานกรรมการใน One Report ปี `2024` บริษัทระบุว่า `Value category` คิดเป็น `55.1%` ของ gross profit ทั้งบริษัทแล้ว
- moat จริงคือ `channel network + vendor relationship + working-capital execution`
- แต่ยังเป็น moat แบบ `narrow` เพราะ switching cost ไม่สูง และธุรกิจ distribution ถูกกด margin ตามธรรมชาติ

### 1.2 Financial Health (8/10)
| เมตริก | ค่า | มุมมอง |
|--------|-----|--------|
| Revenue 2025 | 30,109 MB | โต `+4.4% YoY` |
| Net Profit 2025 | 876.4 MB | โต `+25.6% YoY` |
| OCF 2025 | 1,657 MB | เงินสดจากการดำเนินงานแข็ง |
| Total Debt 2025 | 1,287 MB | ลดลงมากจาก `2,523 MB` ในปี 2024 |
| Net Debt 2025 | 542.6 MB | ดีขึ้นชัดเจน |
| Gross Margin 2025 | 8.02% | ดีขึ้นจาก `7.65%` ในปี 2024 |

**มุมมอง:** debt ลดแรง + OCF บวกต่อเนื่อง ทำให้ฐานะการเงินแข็งกว่าที่ผมให้ไว้รอบแรก แต่ยังต้องเผื่อคะแนนเพราะธุรกิจนี้ใช้ทุนหมุนเวียนสูงและ margin ยังบาง

### 1.3 Growth (7/10)
- รายได้ปี 2025 โตเพียง `mid-single digit`
- แต่กำไรโตเร็วกว่า revenue มาก เพราะ margin ฟื้นและดอกเบี้ยจ่ายลด
- theme ที่ช่วย growth คือ `AI PC`, `server`, `cybersecurity`, `cloud`, `data center`, และ `clean energy solutions`
- upside มี แต่ยังไม่ใช่ธุรกิจที่เห็น recurring growth แบบชัดเจน

### 1.4 Management (8/10)
- Audit ล่าสุดเป็น `Unqualified opinion`
- ไม่พบ dilution ใหญ่หรือ RO/PP ที่กินผู้ถือหุ้น
- จ่ายปันผลสม่ำเสมอ และยังมี treasury stock บางส่วน
- ownership block ใหญ่ช่วย alignment แต่ก็ทำให้ minority discount ยังมี

### 1.5 Valuation (8/10)
| เมตริก | ค่า | มุมมอง |
|--------|-----|--------|
| P/E | 8.55x | ถูกเมื่อเทียบ SET และหุ้น tech หลายตัว |
| P/BV | 1.63x | ไม่แพง แต่ไม่ใช่ deep value สุดโต่ง |
| EV/EBITDA | 10.42x | กลางๆ |
| Dividend Yield | ~5.7-5.8% | พอช่วย downside |

**สรุป:** valuation ดูน่าสนใจกว่าที่ผมให้ไว้ในรอบแรก เพราะ earnings โต, debt ลด, และ dividend yield ช่วยรอง downside ได้บางส่วน แต่ `ไม่ถึงขั้นถูกมากแบบ ATS MOS 69.8%`

**Quality Score: 39/50** ⭐

---

## 🎯 Gate 2: Catalyst Score (21/30)

### 2.1 Events (6/7.5)
- FY2025 กำไรโต `+25.6% YoY`
- มี dividend `1.22 THB/share`, XD วันที่ `6 มี.ค. 2026`
- บริษัทเดินเกมเชิงรุกผ่านงาน `SiS Technology Showcase 2026` วันที่ `10 มี.ค. 2026` เน้น AI / Cloud / Cybersecurity / Clean Energy
- catalyst มีความเป็นรูปธรรมมากกว่าที่ผมให้ไว้รอบแรก เพราะบริษัทสื่อสาร growth themes เชิง execution ชัดเจน

### 2.2 Industry (6/7.5)
- sector จริงคือ `Technology distribution` ไม่ใช่ consumer staple
- ภาพรวมได้ประโยชน์จาก enterprise IT refresh, AI server/PC cycle, cyber spending
- แต่ยังผูกกับ capex cycle และกำลังซื้ออุปกรณ์ไอทีที่ผันผวน

### 2.3 Sentiment (4/7.5)
- ราคายังต่ำกว่า high 52 สัปดาห์ พอสมควร
- RSI ล่าสุดที่เข้าถึงได้ราว `44.9` = momentum ยังไม่เด่น
- ไม่พบข้อมูล EPS revision / foreign flow ที่แข็งพอให้ bump คะแนน

### 2.4 Risk Profile (5/7.5)
- **บวก:** customer concentration ฝั่งลูกค้าค่อนข้างต่ำ เพราะมีลูกค้ามากกว่า `10,000` ราย
- **ลบ:** recurring revenue ยังต่ำเมื่อเทียบกับ product sales
- **ลบ:** เสี่ยงด้าน vendor mix, product cycle, FX, และ margin pressure
- **ลบ:** ถ้างบโตช้าหรือ inventory หมุนช้าลง ตลาดจะ de-rate ง่าย

**Catalyst Score: 21/30** ⭐

---

## 📈 Gate 3: Swing Score (12/20)

### 3.1 Trend (3/5)
- ราคาล่าสุด `21.40` อยู่เหนือ low `17.60` พอสมควร
- แต่ยังต่ำกว่า high `24.60` ราว `13%`
- ภาพรวมเป็น `range recovery` มากกว่า breakout trend

### 3.2 Momentum (2/5)
- RSI ล่าสุดราว `44.88` จากข้อมูลที่เข้าถึงได้
- momentum จึงยังไม่ใช่ฝั่ง bullish ชัด

### 3.3 Support / Resistance (3/5)
| ระดับ | ราคา | หมายเหตุ |
|-------|------|----------|
| Resistance 1 | 22.50 | โซนต้านใกล้ |
| Resistance 2 | 24.60 | 52-week high |
| Current | 21.40 | ราคาอ้างอิงล่าสุด |
| Support 1 | 20.50 - 21.00 | โซนรับระยะสั้น |
| Support 2 | 17.60 | 52-week low |

### 3.4 Volume (4/5)
- Average volume ราว `1.12M หุ้น/วัน`
- ที่ราคาประมาณ `21.3-21.4` คิดเป็นมูลค่าซื้อขายเฉลี่ย `~23-24 MB/day`
- ผ่านเกณฑ์ QSI ได้ แต่ยังไม่ใช่ breakout volume ระดับเด่น

**Swing Score: 12/20** ⭐

---

## 🧮 สรุป Final QSI Score

```text
Quality Score:  39 / 50  × 1.0 = 39
Catalyst Score: 21 / 30  × 1.0 = 21
Swing Score:    12 / 20  × 1.0 = 12
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
QSI Total:                    72 / 100
```

---

## 🚦 ตารางตัดสินใจ

| ช่วงคะแนน | Action | สถานะ SIS |
|-----------|--------|-----------|
| ≥80 | BUY | - |
| **65-79** | **WATCH** | **✅ 72** |
| 55-69 | SPECULATIVE | - |
| <55 | PASS | - |

**Action: WATCH**  
เหตุผลหลักคือ thesis ดีขึ้นจริงจาก `Value-Added mix + debt reduction + AI/cyber tailwind` แต่ยังไม่พอให้ re-rate เป็น `BUY` เพราะ recurring revenue ระดับบริษัท, margin structure, และ technical momentum ยังไม่ชัดพอ

---

## 📋 การกำหนดขนาดการลงทุน (Position Sizing)

| เมตริก | ค่า |
|--------|-----|
| QSI Score | 72/100 |
| Conviction | MEDIUM |
| Risk (R) | 0.25-0.5R |
| Max Position | 3-5% |
| Watch Zone | 20.50 - 21.00 THB |
| Upgrade Trigger 1 | ยืนยัน intrinsic value ใหม่แบบไม่ใช้ MOS เดิม |
| Upgrade Trigger 2 | ราคายืนเหนือ 22.50 THB พร้อม volume |
| Upgrade Trigger 3 | Q1/2026 กำไรยังโตต่อและ OCF ยังบวก |

### กลยุทธ์ที่เหมาะกว่า
1. อย่าใช้ `MOS 69.8%` ตัดสินใจซื้อทันที
2. ต้อง re-check ก่อนว่า ATS ผูก `ticker/sector/model input` ถูกตัวหรือไม่
3. ถ้าจะเล่น ให้มองเป็น `watchlist tech distributor` ไม่ใช่ `consumer compounder`

---

## ✅ Green Flags

- [x] กำไร 3 ปีล่าสุดเป็นบวก
- [x] `OCF` บวก 3 ปีล่าสุด
- [x] debt ลดลงชัดในปี 2025
- [x] gross margin ดีขึ้น
- [x] `Value category` เป็นสัดส่วน gross profit หลักแล้ว
- [x] valuation ไม่แพง
- [x] liquidity ผ่านเกณฑ์

## 🚩 Red Flags / Risks

- [ ] Scanner จัด sector ผิดจาก `Technology` ไปเป็น `Consumer`
- [ ] MOS `69.8%` ดูสูงผิดธรรมชาติ
- [ ] recurring revenue ยังต่ำ
- [ ] margin บางและแข่งขันสูง
- [ ] vendor / product cycle risk สูงกว่าธุรกิจ consumer defensive

---

## ❓ตอบคำถามหลัก

### 1) ใช่ SIS นี้ไหม?
ไม่ใช่ “Siam Syndicate Technology”  
หุ้นนี้คือ **`SiS Distribution (Thailand) PCL`** ผู้จัดจำหน่ายสินค้าไอทีและโซลูชันเทคโนโลยีในไทย

### 2) Business model คืออะไร?
- ทำหน้าที่ `technology distributor`
- รับสินค้า/solution จาก vendor ระดับโลก แล้วกระจายต่อผ่าน dealer/system integrator/customer network
- รายได้หลักมาจาก `Commercial Products`, `Consumer Products`, `Value Added Products`, และ `Phones`

### 3) Client concentration risk ไหม?
`ต่ำทางฝั่งลูกค้า` เพราะมี dealer/customer มากกว่า `10,000` ราย  
แต่ `ไม่ได้แปลว่าความเสี่ยงต่ำทั้งหมด` เพราะฝั่งที่ต้องระวังคือ `vendor concentration`, `product cycle`, และ `margin compression`

### 4) Recurring revenue หรือ project-based?
หลักๆ ยังเป็น `transaction-based / project-based distribution`  
มีส่วนของ service, rental, cloud/security solution ที่ recurring กว่าบ้าง แต่ยัง **ไม่ใช่ recurring-heavy model**

### 5) Competitive moat คืออะไร?
moat อยู่ที่ `channel breadth + vendor access + execution + balance-sheet discipline`  
เป็น moat แบบ `narrow` ไม่ใช่ moat แบบแบรนด์ผูกขาดหรือ subscription platform

### 6) Growth outlook เป็นอย่างไร?
`กลางค่อนไปบวก`  
ปี 2025 โตจริง และปี 2026 มี tailwind จาก AI infra / enterprise refresh / cybersecurity แต่ธุรกิจนี้ยัง cyclical และ upside ไม่ควรถูกตีราคาแบบ high-multiple compounder

---

## 🧠 สรุป Thesis

`SIS` เป็นหุ้นเทคโนโลยี distributor ที่พื้นฐานดีขึ้นจริง: กำไรโต, cash flow บวก, หนี้ลด, valuation ไม่แพง และ mix กำไรเริ่มขยับไปทาง `Value-Added`

แต่จุดที่สำคัญกว่าตัวงบคือ **ข้อมูลจาก scanner ดูผิดบริบท** ทั้งเรื่อง `sector` และน่าจะรวมถึง `MOS` ด้วย ถ้าโมเดลตั้งต้นผิด ต่อให้เลข MOS ดูสวยก็ไม่มีประโยชน์

ดังนั้นข้อสรุปที่ตรงที่สุดตอนนี้คือ:

- บริษัทจริง = `Technology distributor`, ไม่ใช่ consumer play
- customer concentration `ไม่ใช่ risk หลัก`
- `Value-Added pivot` จริง แต่ยังไม่ใช่ full transformation
- recurring revenue `ดีขึ้น แต่ยังไม่สูงพอ`
- moat `ดีขึ้นเล็กน้อย แต่ยังไม่กว้าง`
- growth `กลางค่อนไปบวก`
- **Final Recommendation: `WATCH` ที่ QSI `72/100` และ re-check valuation model ก่อน**

---

## 📎 โน้ตที่เกี่ยวข้อง

- [[ATS Wave 2.5 - 2026-03-28]]
- [[Quality Swing Investor]]
- [[QSI Deep Dive Checklist]]
- [[Stock Reviews MOC]]

---

## 🔗 แหล่งข้อมูล

- [SET Factsheet: SIS](https://www.set.or.th/en/market/product/stock/quote/sis/factsheet)
- [SET Latest Balance / Quote Snapshot: SIS](https://www.set.or.th/en/market/product/stock/quote/SIS/financial-statement/latest/balance)
- [SET F45 FY2024: SIS](https://www.set.or.th/en/market/news-and-alert/newsdetails?id=93510900&symbol=SIS)
- [SIS IR Home](https://sis.listedcompany.com/)
- [SIS Online News Clippings](https://sis.listedcompany.com/newsroom_clippings.html)
- [SETTRADE Major Shareholders: SIS](https://www.settrade.com/th/equities/quote/sis/company-profile/major-shareholders)
- [StockAnalysis Overview: SIS](https://stockanalysis.com/quote/bkk/SIS/)
- [StockAnalysis Income Statement: SIS](https://stockanalysis.com/quote/bkk/SIS/financials/)
- [StockAnalysis Cash Flow: SIS](https://stockanalysis.com/quote/bkk/SIS/financials/cash-flow-statement/)
- [StockAnalysis Balance Sheet: SIS](https://stockanalysis.com/quote/bkk/SIS/financials/balance-sheet/)

---

*สร้างโดย Gemini + Codex (Round 2)*
*Date: 2026-03-28*
*Framework: QSI v2.0*
