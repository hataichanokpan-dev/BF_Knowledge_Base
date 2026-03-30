---
title: AIT Review - 2026-03-28
note_type: review
framework: QSI
version: "2.0"
created: 2026-03-28
ticker: AIT
company: Advanced Information Technology Public Company Limited
sector: Technology / Information Technology Services
qsi_score: 67
gate0_status: fail
action: PASS
mos: N/A (ATS ticker mismatch - AS row used for AIT)
position_size: 0%
watchlist: true
collaboration: Gemini + Codex + Claude (3-Round)
tags:
  - note/review
  - framework/qsi
  - sector/technology
  - stock/ait
  - source/3-round-collab
---

# AIT Review - 2026-03-28

> **Advanced Information Technology (AIT)**
> QSI Deep Dive Round 1 by Codex

## 📊 Quick Summary

| เมตริก | ค่า |
|--------|-----|
| QSI Score | **67/100** |
| Gate 0 | ❌ FAIL (Liquidity ~8.2M THB/day < 10M) |
| Action | **PASS** |
| ราคา SET ล่าสุดที่ตรวจ | **4.82 THB** |
| Position | **0%** |
| หมายเหตุสำคัญ | ATS row ใช้ `AS` แต่บริษัทคือ `AIT` (ticker mismatch) |

## 🔄 3-Round Collaboration

| Round | Gemini | Codex | Action |
|-------|--------|-------|--------|
| 1 | 72 (WATCH) | 62 (PASS) | Gap: 10 pts |
| 2 | 68 (PASS) | - | Converged |
| **Final** | - | - | **PASS (QSI 67)** |

**Key Dispute Resolved:**
- Gemini: Gate 0 YELLOW (liquidity borderline)
- Codex: Gate 0 FAIL (8.2M < 10M threshold)
- **Final: FAIL** - Liquidity clearly below 10M THB/day per QSI v2.0

---

## 📊 สถิติด่วน

| เมตริก | ค่า | แหล่งข้อมูล |
|--------|-----|-------------|
| ATS Wave 2.5 Row | `AS / MOS 66.3% / Price 2.62 / IV 7.76` | [[ATS Wave 2.5 - 2026-03-28]] |
| Ticker ที่ถูกต้องของบริษัทนี้บน SET | **AIT** | SET Factsheet / Company Profile |
| ราคา SET ล่าสุดที่ตรวจ | **4.82 THB** | SET (27 มี.ค. 2026) |
| ช่วงราคา 52 สัปดาห์ | `4.08 - 5.30 THB` | StockAnalysis / SET snapshot |
| P/E | `~12.7x` | StockAnalysis / SET |
| P/BV | `~1.9x` | StockAnalysis / SET |
| Dividend Yield | `~11.3%` | StockAnalysis |
| FY2024 Revenue | `7,198 MB` | StockAnalysis |
| FY2024 Net Profit | `572.46 MB` | StockAnalysis |
| TTM Revenue (ถึง Sep 2025) | `7,009 MB` | StockAnalysis |
| TTM Net Profit (ถึง Sep 2025) | `590.65 MB` | StockAnalysis |
| Operating Cash Flow | `524.22 MB` (FY2024), `956.69 MB` (TTM Sep 2025) | StockAnalysis |
| FY2025 Standalone Revenue | `6,817 MB` | AIT Company News (24 ก.พ. 2026) |
| FY2025 Standalone Net Profit | `582 MB` | AIT Company News (24 ก.พ. 2026) |
| เป้ารายได้ปี 2026 | `6,900 MB` | AIT Company News (24 ก.พ. 2026) |

**ข้อสังเกตสำคัญ:** ข้อมูลใน `[[ATS Wave 2.5 - 2026-03-28]]` ระบุ `AS` แต่คำอธิบายบริษัทและคำถามธุรกิจในโจทย์ตรงกับ `AIT` ชัดเจน โดยบน SET `AS` คือ `Asphere Innovations PCL.` ไม่ใช่ `Advanced Information Technology PCL.` ดังนั้นรีวิวนี้ใช้ `AIT` เป็นหลัก และ **ไม่ใช้** ราคา `2.62` กับ `IV 7.76` เป็นฐานตัดสินมูลค่า AIT

---

## 🚨 Gate 0: Knockout Rules

| กฎ | สถานะ | หลักฐาน |
|----|--------|---------|
| Profit 3 Years | ✅ PASS | กำไรสุทธิเป็นบวกต่อเนื่อง: `2022 = 541.64 MB`, `2023 = 503.67 MB`, `2024 = 572.46 MB`, `TTM Sep 2025 = 590.65 MB` |
| CFO Negative 2+ Years | ✅ PASS | Operating CF เป็นบวก: `2023 = 957.40 MB`, `2024 = 524.22 MB`, `TTM Sep 2025 = 956.69 MB` |
| Insider >50% = GOOD | ⚪ ไม่ใช่จุดเด่น | จากข้อมูลที่ตรวจ TKC เป็น strategic shareholder ราว `34.9%` หลัง partial tender offer ปี 2025 และ disclosure ปี 2023 ระบุฝั่งผู้บริหาร/ครอบครัวเดิมราว `7.5%` จึงยังไม่เห็น owner concentration >50% |
| Major Disputes | ✅ PASS | ไม่พบข้อพิพาทใหญ่หรือ governance event เชิงลบจาก SET/company news ที่ตรวจ |
| Trading Signs | ✅ PASS | ไม่พบ sign เตือนแบบ `SP / NC / CB / CS / CF / CC` ที่มีผลอยู่บนหน้า SET quote ที่ตรวจ |
| Trading Value | ❌ FAIL | Average volume จาก StockAnalysis `1,702,549 หุ้น/วัน` ที่ราคาประมาณ `4.82 THB` คิดเป็นมูลค่าซื้อขายเฉลี่ยราว `8.2 MB/day` ต่ำกว่าเกณฑ์ `10 MB/day` ของ QSI v2.0 |

**Gate 0: FAIL** ❌

**ข้อสรุป:** AIT ไม่ได้ fail เพราะงบหรือ governance แต่ fail เพราะ `liquidity` ต่ำกว่าเกณฑ์ QSI v2.0 ชัดเจน

---

## 🚦 Gate 1: Quality Score (36/50)

### 1.1 Moat (7/10)
- AIT เป็น `system integrator (SI)` และผู้รับเหมาวางระบบ ICT แบบครบวงจร มีประสบการณ์กว่า 30 ปี
- SET ระบุชัดว่าบริษัททำ `turnkey project` ตั้งแต่ consultation, design, implementation, installation, training และ maintenance
- พอร์ตบริการครอบคลุม `data center and cloud`, `enterprise network`, `cyber security`, `collaboration`, `IoT`, `enterprise applications`, `managed services`
- มี reference customer จำนวนมากทั้งฝั่งรัฐ รัฐวิสาหกิจ โทรคมนาคม ธนาคาร และ enterprise
- แต่ moat ยังเป็น `execution moat` ไม่ใช่ `asset moat`; ลูกค้าสามารถเปลี่ยน integrator ได้ และ hyperscaler/ผู้ให้บริการรายใหญ่ยังเป็นแรงกดดัน

**สรุป:** เป็น `quality local integrator` มากกว่าธุรกิจ platform หรือ owner ของ infrastructure เอง และจุดนี้เป็น `inference` จาก business type, service portfolio และ reference customers

### 1.2 Financial Health (8/10)
| เมตริก | ค่า | มุมมอง |
|--------|-----|--------|
| D/E Ratio | `0.09x` | งบดุลเบา |
| Net Debt / Equity | `-0.45x` | สถานะใกล้ net cash |
| Current Ratio | `2.46x` | สภาพคล่องดี |
| ROE | `14.74%` | อยู่ในเกณฑ์ดี |
| Operating CF | บวกต่อเนื่อง | คุณภาพกำไรใช้ได้ |

**มุมมอง:** จุดแข็งของ AIT คือ balance sheet ไม่หนักและ cash flow ยังเป็นบวก แม้ธุรกิจจะ project-based

### 1.3 Growth (5/10)
- ปี `2024` รายได้โตเป็น `7,198 MB` จาก `6,520 MB` ในปี 2023
- แต่ `TTM Sep 2025` รายได้อยู่ที่ `7,009 MB` ต่ำกว่า FY2024 เล็กน้อย สะท้อนความผันผวนของจังหวะรับรู้รายได้
- บริษัทระบุว่าปี `2025` งบเฉพาะกิจการทำรายได้ `6,817 MB` และกำไรสุทธิ `582 MB` เพิ่มขึ้นเพียงราว `2%`
- ลักษณะธุรกิจขึ้นกับ backlog และ timing ของโครงการ ทำให้ growth ไม่ smooth แบบ recurring software company

**มุมมอง:** ยังโตได้ แต่เป็น growth แบบ `lumpy` มากกว่าต่อเนื่อง

### 1.4 Management (7/10)
- Audit ล่าสุดเป็น `Unqualified opinion`
- หลัง TKC เข้ามาเป็น strategic partner บริษัทประกาศชัดว่าทีมบริหารเดิมยังบริหารงานต่อ
- นโยบายปันผลยังสม่ำเสมอ และข่าวล่าสุดเตรียมจ่ายเพิ่ม `0.21 THB/share`
- จุดที่ต้องระวังคือการพึ่งพางานประมูลและ public-sector pipeline ทำให้ execution risk ยังสูงกว่าธุรกิจ recurring

### 1.5 Valuation (9/10)
| เมตริก | ค่า | มุมมอง |
|--------|-----|--------|
| P/E | `~12.7x` | ไม่แพง |
| P/BV | `~1.9x` | รับได้เมื่อเทียบ ROE |
| EV/EBITDA | `~6.1x` | ค่อนข้างถูกสำหรับ ICT services |
| Dividend Yield | `~11.3%` | สูงมาก |

**ข้อควรระวัง:** `MOS 66.3%` จาก ATS รอบนี้ใช้กับ `AS` ไม่ใช่ `AIT` จึงยัง **ห้าม** ใช้เป็น valuation anchor ของ AIT จนกว่าจะ fix ticker mapping

**Quality Score: 36/50** ⭐

---

## 🎯 Gate 2: Catalyst Score (19/30)

### 2.1 Events (5/7.5)
- บริษัทตั้งเป้ารายได้ปี `2026` ที่ `6,900 MB`
- เตรียมขึ้น XD ปันผลเพิ่ม `0.21 THB/share` วันที่ `22 เม.ย. 2026`
- Management ชู backlog ในมือและตั้งเป้า net profit margin เฉลี่ย `7-8%`
- ยังมีโอกาสจากงานประมูลใหม่ใน cloud, cyber security, big data, SDN และ IoT

### 2.2 Industry (6/7.5)
- Krungsri Research คาด `digital services` ไทยปี `2025-2027` โตเฉลี่ย `9.5-10.0%`
- กลุ่ม `software and software services` คาดโต `9.0-9.5%`
- แรงหนุนหลักมาจาก `cloud`, `data center`, `big data`, `AI/data-driven strategy`, `cybersecurity`
- ธีมนี้ตรงกับ competency ของ AIT พอสมควร

### 2.3 Sentiment (4/7.5)
- จุดบวกคือ dividend yield สูง ทำให้หุ้นดู defensive ในเชิง cash return
- แต่ยังไม่เห็นหลักฐานชัดจาก source ที่ตรวจว่า market ให้ rerating ฝั่ง earnings หรือ foreign flow
- ภาพราคาโดยรวมยังไม่สะท้อน momentum เชิงรุก

### 2.4 Risk Profile (4/7.5)
- ณ `1 มี.ค. 2024` backlog `6,200 MB` แบ่งเป็น `Service Provider 28%`, `Government 23%`, `State Enterprise 18%`, `Financial Services 18%`, `Enterprise 13%`
- ถ้ามองรวม `Government + State Enterprise + Service Provider` จะคิดเป็น `69%` ของ backlog ซึ่งสะท้อน `segment concentration` สูง
- ยังไม่พบ disclosure ว่ามี `single client >35%` ของรายได้ แต่ exposure ต่อ public-sector/telco cycle ค่อนข้างเด่น
- ความเสี่ยงอีกด้านคือการแข่งขันจากผู้เล่น cloud/global vendors และการเลื่อนเซ็นงาน

**Catalyst Score: 19/30** ⭐

---

## 📈 Gate 3: Swing Score (7/20)

> ใช้แบบ conservative เพราะ official source ไม่ได้เปิด EMA/RSI/MACD ครบเหมือนแพลตฟอร์ม charting โดยตรง

### 3.1 Trend (2/5)
- ราคาล่าสุด `4.82` ยังห่างจาก 52-week high ที่ `5.30`
- Technical summary จาก Investing/StockAnalysis ชี้ภาพรวมค่อนข้างอ่อน
- ยังไม่ใช่ breakout trend

### 3.2 Momentum (1/5)
- RSI ที่ตรวจได้อยู่ราว `36-41`
- โมเมนตัมยังค่อนไปทางอ่อน ไม่เข้าเกณฑ์หุ้น swing แข็ง

### 3.3 Support / Resistance (3/5)
| ระดับ | ราคา | หมายเหตุ |
|-------|------|----------|
| Resistance 1 | `5.00` | แนวจิตวิทยา |
| Resistance 2 | `5.10 - 5.30` | โซนยอดเดิม |
| Current | `4.82` | ราคาแถวล่าสุด |
| Support 1 | `4.80` | โซนรับระยะสั้น |
| Support 2 | `4.50 - 4.60` | พื้นฐานเดิม |
| Support 3 | `4.08` | 52-week low |

### 3.4 Volume (1/5)
- avg trading value ราว `8.2 MB/day`
- ต่ำกว่าเกณฑ์ QSI ที่ต้องการ `>=10 MB/day`
- จึงไม่เหมาะกับ swing setup ตาม framework

**Swing Score: 7/20** ⭐

---

## 🧮 สรุป Final QSI Score

### Raw Score

```text
Quality Score:  36 / 50  × 1.0 = 36
Catalyst Score: 19 / 30  × 1.0 = 19
Swing Score:     7 / 20  × 1.0 = 7
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Raw QSI Total:                62 / 100
```

### Effective Decision

ถ้าดูแค่พื้นฐาน `AIT` ไม่ได้แย่: งบดุลดี, valuation ไม่แพง, dividend สูง, และได้ tailwind จาก digital transformation

แต่ตามกรอบ `QSI v2.0` หุ้นนี้ **ต้องเป็น `PASS`** เพราะ `Gate 0 FAIL` จาก `liquidity`

---

## ❓ คำตอบคำถามสำคัญ

### 1. AIT เป็น IT infrastructure / services provider ไหม? business model คืออะไร?
**ใช่**

AIT เป็น `IT infrastructure and services provider` ชัดเจนในบทบาท `system integrator (SI)` ไม่ใช่ software pure-play หรือ cloud owner บริษัทหาเงินจากการขาย ออกแบบ ติดตั้ง บริหารโครงการ ฝึกอบรม ดูแลหลังการขาย และบำรุงรักษาระบบ ICT แบบ turnkey รวมถึงมีบริการ `managed services` และ `equipment rental`

### 2. Client concentration risk เป็นฝั่งรัฐบาลหรือ enterprise?
**มี concentration เชิง segment ค่อนข้างสูง และเอนเอียงไปฝั่งรัฐ/รัฐวิสาหกิจ/telecom มากกว่า enterprise**

จาก backlog ณ `1 มี.ค. 2024` สัดส่วน `Government 23% + State Enterprise 18% + Service Provider 28%` รวมกันเป็น `69%` ขณะที่ `Enterprise` มี `13%` เท่านั้น ดังนั้น risk หลักคือ `sector/tender concentration` มากกว่า enterprise diversification

### 3. รายได้ recurring หรือ project-based?
**ผสมกัน แต่แกนหลักยังเป็น project-based**

ฝั่ง recurring มีจาก `maintenance`, `service support`, `managed services`, `rental` และงานดูแลระบบต่อเนื่อง แต่ disclosure ของบริษัทและโครงสร้าง backlog บ่งชี้ว่ารายได้ส่วนใหญ่ยังผูกกับงานโครงการและจังหวะส่งมอบงาน ข้อนี้เป็น `inference` จาก segment/business description มากกว่าตัวเลข recurring revenue ที่บริษัทเปิดตรงๆ

### 4. Competitive moat ต่อสู้กับ cloud providers ได้ไหม?
**ไม่ใช่ moat แบบชนตรงกับ hyperscaler**

AIT ไม่ได้ชนะด้วยการเป็นเจ้าของ cloud ขนาดใหญ่ แต่ชนะในบทบาท `local integrator/orchestrator` ที่ช่วยลูกค้าทำ `hybrid cloud`, เชื่อมระบบเดิม, ทำ security, networking, compliance, deployment และ after-sales support ในไทย นี่เป็น niche ที่ยังมีค่า แต่ถ้าลูกค้าหันไปซื้อ managed stack ตรงจาก hyperscaler หรือ telco integrator มากขึ้น moat ของ AIT จะไม่กว้าง ข้อนี้เป็น `inference` จาก product pages และ partner ecosystem

### 5. Growth outlook ของ IT services ไทยเป็นอย่างไร?
**ภาพรวมยังบวก**

Krungsri Research มองว่า `digital services` ไทยช่วง `2025-2027` จะโตเฉลี่ย `9.5-10.0%` และ `software/software services` โต `9.0-9.5%` จากการลงทุนใน `cloud`, `data center`, `big data`, `AI`, และ `cybersecurity` ดังนั้น market tailwind ยังดี แต่รายได้ของ AIT จะยังผันผวนตามรอบประมูลงานและการรับรู้ backlog

---

## 🚦 ตารางตัดสินใจ

| ช่วงคะแนน | Action | สถานะ AIT |
|-----------|--------|-----------|
| ≥80 | BUY | - |
| 65-79 | WATCH/ACCUMULATE | Raw Score ยังไม่ถึง |
| 55-69 | SPECULATIVE | Raw Score = 62 |
| <55 | PASS | Effective outcome = PASS เพราะ Gate 0 FAIL |

**Framework Override:** `PASS` เพราะ `Gate 0 FAIL` จากสภาพคล่อง ❌

---

## 📋 การกำหนดขนาดการลงทุน (Position Sizing)

| เมตริก | ค่า |
|--------|-----|
| Raw QSI Score | `62/100` |
| Effective Action | **PASS / Watchlist only** |
| Conviction | LOW |
| Risk (R) | `0R` |
| Max Position | `0% ตอนนี้` |
| Upgrade Trigger 1 | avg trading value > `10 MB/day` อย่างสม่ำเสมอ |
| Upgrade Trigger 2 | revenue growth กลับมาชัดกว่าปี 2025 |
| Upgrade Trigger 3 | ยืนยัน valuation ใหม่ด้วย ticker `AIT` ที่ถูกต้อง ไม่ใช่ ATS row `AS` |

---

## ✅ Green Flags

- [x] เป็น SI/ICT infrastructure player ที่มีประสบการณ์ยาว
- [x] งบดุลแข็งแรง D/E ต่ำ
- [x] Operating cash flow ยังเป็นบวก
- [x] ได้ประโยชน์จาก cloud / cybersecurity / digital transformation
- [x] dividend yield สูง
- [x] valuation ไม่แพง

## 🚩 Red Flags / Risks

- [ ] `Liquidity` ต่ำกว่าเกณฑ์ QSI = Gate 0 fail
- [ ] รายได้หลักยัง project-based และผันผวนตามการส่งมอบงาน
- [ ] backlog concentration สูงในรัฐ/รัฐวิสาหกิจ/telecom
- [ ] moat ไม่กว้างเมื่อเทียบ hyperscaler และผู้เล่น integrator รายใหญ่
- [ ] ATS row ปัจจุบัน map ticker/company ผิด ทำให้ MOS ใช้งานไม่ได้

---

## 🧠 สรุป Thesis

`AIT` เป็นหุ้น ICT services ที่พื้นฐานดีกว่าภาพราคาพอสมควร: งบดุลดี, ปันผลสูง, valuation ไม่แพง และอยู่ในอุตสาหกรรมที่ยังได้แรงหนุนจาก cloud, cyber security และ digital transformation

แต่ถ้ามองผ่านกรอบ `QSI v2.0` แบบเคร่ง หุ้นนี้ยัง **ไม่ผ่าน** เพราะ `liquidity` ต่ำกว่าเกณฑ์ซื้อ และรายได้หลักยังขึ้นกับงานโครงการมากกว่า recurring service แบบเหนียวแน่น ดังนั้นตอนนี้เหมาะกับ `watchlist` มากกว่าเข้าซื้อจริง

---

## 🔗 แหล่งข้อมูล

- [AIT SET Factsheet](https://www.set.or.th/en/market/product/stock/quote/AIT/factsheet)
- [AIT SET Shareholders](https://www.set.or.th/en/market/product/stock/quote/AIT/major-shareholders)
- [AIT Website Home](https://www.ait.co.th/en/)
- [AIT 56-1 One Report 2024](https://www.ait.co.th/en/annual-report-form-56-1/)
- [AIT MD&A Page](https://www.ait.co.th/en/mda/)
- [AIT Company News 24 Feb 2026](https://www.ait.co.th/th/updates/company-news/422/ait-%E0%B8%9B%E0%B8%B1%E0%B8%81%E0%B8%98%E0%B8%87%E0%B8%9B%E0%B8%B5-69-%E0%B8%A3%E0%B8%B2%E0%B8%A2%E0%B9%84%E0%B8%94%E0%B9%89%E0%B8%97%E0%B8%B0%E0%B8%A5%E0%B8%B8%E0%B9%80%E0%B8%9B%E0%B9%89%E0%B8%B2-6900-%E0%B8%A5%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%9A%E0%B8%B2%E0%B8%97-%E0%B8%A1%E0%B8%B8%E0%B9%88%E0%B8%87%E0%B8%AA%E0%B8%B9%E0%B9%88%E0%B8%9C%E0%B8%B9%E0%B9%89%E0%B8%99%E0%B8%B3-ict-%E0%B8%84%E0%B8%A3%E0%B8%9A%E0%B8%A7%E0%B8%87%E0%B8%88%E0%B8%A3-%E0%B8%AB%E0%B8%A5%E0%B8%B1%E0%B8%87%E0%B8%9B%E0%B8%B5-68-%E0%B8%9B%E0%B8%B4%E0%B8%94%E0%B8%88%E0%B9%8A%E0%B8%AD%E0%B8%9A-%E0%B8%97%E0%B8%B3%E0%B8%81%E0%B8%B3%E0%B9%84%E0%B8%A3%E0%B8%AA%E0%B8%B8%E0%B8%97%E0%B8%98%E0%B8%B4-582-%E0%B8%A5%E0%B9%89%E0%B8%B2%E0%B8%99%E0%B8%9A%E0%B8%B2%E0%B8%97-%E0%B9%80%E0%B8%95%E0%B8%A3%E0%B8%B5%E0%B8%A2%E0%B8%A1%E0%B8%88%E0%B9%88%E0%B8%B2%E0%B8%A2%E0%B8%9B%E0%B8%B1%E0%B8%99%E0%B8%9C%E0%B8%A5%E0%B9%80%E0%B8%9E%E0%B8%B4%E0%B9%88%E0%B8%A1-021-%E0%B8%9A%E0%B8%B2%E0%B8%97%E0%B8%95%E0%B9%88%E0%B8%AD%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99-%E0%B8%95%E0%B8%AD%E0%B8%81%E0%B8%A2%E0%B9%89%E0%B8%B3%E0%B8%AB%E0%B8%B8%E0%B9%89%E0%B8%99-dividend-stock)
- [AIT 2024 Strategy / Backlog Mix](https://www.ait.co.th/ait-%E0%B9%80%E0%B8%9B%E0%B8%B4%E0%B8%94-5-%E0%B8%81%E0%B8%A5%E0%B8%A2%E0%B8%B8%E0%B8%97%E0%B8%98%E0%B9%8C%E0%B8%82%E0%B8%B1%E0%B8%9A%E0%B9%80%E0%B8%84%E0%B8%A5%E0%B8%B7%E0%B9%88%E0%B8%AD%E0%B8%99/)
- [AIT StockAnalysis Overview](https://stockanalysis.com/quote/bkk/AIT/)
- [AIT StockAnalysis Financials](https://stockanalysis.com/quote/bkk/AIT/financials/)
- [AIT StockAnalysis Cash Flow](https://stockanalysis.com/quote/bkk/AIT/financials/cash-flow-statement/)
- [AIT StockAnalysis Ratios](https://stockanalysis.com/quote/bkk/AIT/financials/ratios/)
- [Krungsri Research Thailand Industry Outlook 2025-2027](https://www.krungsri.com/en/research/industry/summary-outlook/thailand-industry-outlook-summary-2025-2027)

---

## 📝 บันทึกการวิเคราะห์

| รอบ | AI | คะแนน | Gate 0 | ประเด็นหลัก |
|-----|----|--------|--------|-------------|
| 1 | Codex | 62 | FAIL | งบดุลดี แต่ liquidity ต่ำ และ ATS ticker mismatch |
