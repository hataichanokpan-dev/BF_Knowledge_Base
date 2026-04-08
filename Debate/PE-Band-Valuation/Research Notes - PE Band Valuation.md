---
title: "Research Notes - PE Band Valuation"
note_type: research
created: 2026-03-29
updated: 2026-03-30
tags:
  - pe-band
  - valuation
  - research
  - academic
  - set-market
---

## 📖 Research Notes - PE Band Valuation

### Definition
PE Band (Price-to-Earnings Band) คือวิธีประเมินมูลค่าโดย:
1. คำนวณ PE Ratio ย้อนหลัง 5-10 ปี
2. สร้าง Band จาก Percentile (P20/P50/P80)
3. เทียบ PE ปัจจุบันกับ Band เพื่อดูว่าราคาถูก/แพง

---

## 📚 Academic Sources

### 1. Sareewiwatthana (2014) - Backtest หุ้นไทย 2002-2012

| รายละเอียด | ข้อมูล |
|------------|--------|
| **วิธีการ** | คัด 30 หุ้น "PE ต่ำสุด" รีบาลานซ์รายปี |
| **ช่วงเวลา** | 2002-2012 (11 ปี) |
| **Benchmark** | SET TRI |

**ผลลัพธ์:**
| Metric | Low PE Portfolio | SET TRI |
|--------|------------------|---------|
| ชนะตลาด | **8 ใน 11 ปี** | - |
| CAGR | **32.3%/ปี** | 18.6%/ปี |
| เงิน 1M ท้ายช่วง | **37.3M บาท** | 6.5M บาท |

**แหล่งอ้างอิง:** https://www.scirp.org/pdf/TI_2014051514162768.pdf

---

### 2. Perez (2017, MDPI) - Value vs Growth ในไทย 1999-2016

| รายละเอียด | ข้อมูล |
|------------|--------|
| **วิธีการ** | เปรียบเทียบ MSCI Thailand Value vs Growth |
| **ช่วงเวลา** | 1999-2016 (17 ปี) |

**ผลลัพธ์:**
| Metric | Value Index | Growth Index |
|--------|-------------|--------------|
| ผลตอบแทนรวม | **+156%** | +120% |
| ชนะรายปี | **10/17 ปี** | 7/17 ปี |

**แหล่งอ้างอิง:** https://www.mdpi.com/2227-7072/5/4/30

---

### 3. Maharakkhaka et al. (2023) - Predictive Power Study

| รายละเอียด | ข้อมูล |
|------------|--------|
| **ช่วงเวลา** | เม.ย. 1988 - ธ.ค. 2022 (416 จุดข้อมูล) |
| **ตัวแปรทดสอบ** | CAPE, P/E, P/BV |

**ผลลัพธ์ Regression:**
| ตัวแปร | Coefficient | p-value | นัยสำคัญ |
|--------|-------------|---------|----------|
| ΔP/E | **0.002945** | **0.0391** | ✅ มีนัยสำคัญ |
| CAPE | - | - | ❌ ไม่ชัดเจน |
| P/BV | - | - | ❌ ไม่ชัดเจน |

**แหล่งอ้างอิง:** https://ajmi.stamford.edu/index.php/ajmi/article/download/389/212/

---

## 📊 SET Market Data Sources

| แหล่งข้อมูล | URL | ข้อมูล |
|-------------|-----|--------|
| SET Statistics | https://www.set.or.th/en/market/statistics/market-statistics/main | P/E รายเดือน |
| SET Stock Overview | https://www.set.or.th/en/market/product/stock/overview | ข้อมูลหุ้นรายตัว |

---

## ⚠️ Research Limitations

### Survivorship Bias
- Backtest ใช้เฉพาะหุ้นที่ยังอยู่ในตลาด
- ละทิ้งหุ้นที่: เพิกถอน, ล้มละลาย, โดน SP
- ผลลัพธ์ดูดีเกินจริง

### Look-ahead Bias
- สัญญาณซื้อเกิดขึ้นเมื่อ PE ต่ำกว่า band
- แต่งบการเงินจริงยังไม่ได้ประกาศ
- ในอดีต "รู้" E แล้ว แต่ตอนนั้นยังไม่รู้

### Regime Shift
| ยุค | ช่วงเวลา | PE Band ทำงาน |
|-----|----------|----------------|
| ยุคทอง | 2010-2018 | ✅ ดี |
| ยุคปัจจุบัน | 2020-ปัจจุบัน | ❌ ล้มเหลว |

---

## 🔗 Related Concepts

- [[Valuation Methods]]
- [[Mean Reversion Theory]]
- [[Survivorship Bias]]
- [[Value Trap]]
- [[ROIC-WACC Framework]]

---

## 📎 Related Files

- [[PE-Band-Valuation-MOC]] - Map of Content
- [[Debate Thesis - PE Band Valuation]] - Full Thesis
- [[Quick Reference - PE Band Debate]] - Cheat Sheet
- [[Round 1 Summary - Definition & Methodology]] - Round 1 Details

---

#pe-band #valuation #research #academic #set-market #sources
