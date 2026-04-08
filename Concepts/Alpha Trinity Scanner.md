---
title: Alpha Trinity Scanner
note_type: concept
status: evergreen
created: 2026-03-27
updated: 2026-03-27
tags:
  - note/concept
  - tool/scanner
  - framework/valuation
aliases:
  - ATS
  - Trinity Scanner
source: Damodaran + Klarman principles
---

# ระบบ Alpha Trinity Scanner

> ระบบคัดกรองหุ้นที่อิง Damodaran DCF + Klarman Margin of Safety

## ภาพรวม

Alpha Trinity Scanner เป็นระบบคัดกรองหุ้นแบบ Multi-Wave:
- **Wave 1:** ตัวกรองคุณภาพแบบเร็ว (รายเดือน)
- **Wave 2:** การประเมินมูลค่าแบบ DCF เชิงลึก (รายไตรมาส)
- **Wave 2.5:** Cross-Check แบบหลายวิธี
- **Wave 3:** เครื่องคำนวณกลยุทธ์การเข้า

## ที่ตั้ง

```
C:\Users\bfipa\projects\stock-screen\alpha-trinity-scanner\
```

## โครงสร้าง Wave

| Wave | เป้าหมาย | ความถี่ | ผลลัพธ์ |
|------|---------|-----------|--------|
| **1** | ตัวกรองคุณภาพแบบเร็ว | รายเดือน | 50-100 ตัว |
| **2** | การประเมินมูลค่าเชิงลึก (DCF) | รายไตรมาส | 8-20 ตัว |
| **2.5** | Multi-Method Cross-Check | รายไตรมาส | การยืนยันผล |
| **3** | กลยุทธ์การเข้า | ตามต้องการ | ขนาดสถานะ |

## Wave 1: ตัวกรองคุณภาพ

### ระบบให้คะแนน (ผ่าน = 25+ คะแนน)

| ตัวชี้วัด | เกณฑ์ | คะแนน |
|--------|-----------|--------|
| Revenue Growth YoY | >= 15% | 10 |
| ROE | >= 20% | 10 |
| Gross Margin | > 30% | 5 |
| Operating Margin | > 15% | 5 |
| Debt/Equity | < 0.5 | 5 |
| Current Ratio | > 1.5 | 5 |
| FCF Positive | > 0 | 5 |
| P/E | < 25 | 5 |

**คะแนนเต็ม:** 50 คะแนน
**เกณฑ์ผ่าน:** 25 คะแนน

### ผลล่าสุด (2026-03-24)

| รายการ | ค่า |
|--------|-------|
| หุ้นทั้งหมดใน SET | 460 |
| หุ้นที่ผ่าน Wave 1 | **82 ตัว** |
| อัตราผ่าน | 17.8% |

## Wave 2: การประเมินมูลค่า DCF

### การคำนวณ WACC

```
WACC = Rf + (Beta × MRP)
```

### พารามิเตอร์ตลาด SET

| พารามิเตอร์ | ค่า | หมายเหตุ |
|-----------|-------|-------|
| Rf | 2.5% | Bond Yield ไทย 10 ปี |
| MRP | 6% | ส่วนเพิ่มความเสี่ยงของตลาดเกิดใหม่ |
| Tax Rate | 20% | ภาษีนิติบุคคล |
| Ticker Suffix | .BK | รูปแบบของ Yahoo Finance |

### วิธีการประเมินมูลค่า

1. **DCF (Discounted Cash Flow)**
   - คาดการณ์ FCF 10 ปี
   - Terminal Value (Gordon Growth)
   - Discount ด้วย WACC

2. **PE Band**
   - เทียบ PE กับ sector
   - ดูช่วง PE ในอดีต

3. **Multi-Method Cross-Check (Wave 2.5)**
   - ตรวจ DCF เทียบกับ PE
   - Flag ความผิดปกติ

### ระดับ MOS

| MOS | ระดับ | การตัดสินใจ |
|-----|--------|--------|
| >= 30% | **ซื้อแรง** | เฝ้าดูเป็นลำดับแรก |
| 20-29% | ซื้อ | เฝ้าดู |
| 10-19% | ถือ | ติดตาม |
| < 10% | ผ่าน | ข้าม |

## Wave 3: กลยุทธ์การเข้า

### การกำหนดขนาดสถานะ

- อิงตามระดับ conviction
- ความเสี่ยงต่อดีล: 1-3% ของพอร์ต
- คำนวณ stop loss

### โซนเข้า

- ใช้แนวรับจาก technical analysis
- ยืนยันด้วย volume
- Risk/reward ratio > 2:1

## ผลสแกน SC Asset (SC)

SC ผ่าน Wave 1 ด้วยคะแนน 25 (ขั้นต่ำ):

| ตัวชี้วัด | ค่า | คะแนน |
|--------|-------|--------|
| Revenue Growth | 23.4% | 10 ✅ |
| D/E | 130.4x | 0 ❌ |
| Current Ratio | 2.5 | 5 ✅ |
| FCF | 2.4B THB | 5 ✅ |
| P/E | 5.36x | 5 ✅ |
| **รวม** | | **25** |

**หมายเหตุ:** SC ผ่านแบบหวุดหวิด เพราะ D/E สูงมาก (130x) แต่ชดเชยด้วย growth, FCF และ P/E ต่ำ

## โครงสร้างไฟล์

```
alpha-trinity-scanner/
├── README.md                 # Documentation
├── config.py                 # Thresholds and settings
├── wave1_filter.py           # Quick quality filter
├── wave2_valuation.py        # DCF valuation
├── wave2_5_multimethod.py    # Multi-method cross-check
├── wave2_6_advanced.py       # Advanced valuation
├── wave3_entry.py            # Entry strategy
├── batch_scanner.py          # Batch processing
├── batch_wave2.py            # Batch Wave 2
├── data_manager.py           # Data handling
├── export_watchlist_csv.py   # Export results
├── generate_report.py        # Report generation
├── run_scanner.py            # Main entry point
├── utils.py                  # Helper functions
└── results/
    ├── cache/                # Cached data
    ├── wave1/                # Monthly filter results
    ├── wave2/                # Quarterly valuation results
    ├── wave3/                # Entry strategy results
    └── watchlist_*.csv       # Final watchlist
```

## วิธีใช้งาน

```bash
# Run Wave 1 filter (SET market)
python wave1_filter.py

# Run Wave 2 valuation
python wave2_valuation.py

# Run full scanner
python run_scanner.py

# Export watchlist
python export_watchlist_csv.py
```

## แนวคิดที่เกี่ยวข้อง

- [[Quality Swing Investor]] - กรอบการวิเคราะห์
- [[Deep Value]] - สไตล์การลงทุนแบบ value
- [[Dividend Play]] - กลยุทธ์รายได้
- [[DCF Valuation]] - วิธีประเมินมูลค่า
- [[Margin of Safety]] - ส่วนกันความเสี่ยง

## คอร์สที่เกี่ยวข้อง

- [[Damodaran Valuation]] - วิธีการ DCF
- [[Seth Klarman Margin of Safety]] - หลักการ MOS

## ความต่างเมื่อเทียบกับ Quality Swing Investor

| มิติ | Alpha Trinity Scanner | Quality Swing Investor |
|--------|----------------------|------------------------|
| แนวทาง | การคัดกรองอัตโนมัติ | การวิเคราะห์แบบ manual |
| แกนหลัก | DCF valuation | Quality + Catalyst |
| ผลลัพธ์ | Watchlist | Thesis ที่นำไปใช้ได้จริง |
| ความถี่ | รายเดือน/รายไตรมาส | รายตัว |
| ขอบเขต | ทั้งตลาด | หุ้นรายตัว |

## การเชื่อมต่อการใช้งาน

1. **ATS** → คัด 460 หุ้นใน SET → ได้ 82 หุ้นเข้าเกณฑ์
2. **QSI** → เจาะลึกหุ้นเข้าเกณฑ์ → ได้ Score + Thesis
3. **Stock Review** → บันทึกลง BF-Vault
4. **MOC** → ติดตามใน [[Stock Reviews MOC]]

---

*ที่อยู่ Scanner: C:\Users\bfipa\projects\stock-screen\alpha-trinity-scanner\*
