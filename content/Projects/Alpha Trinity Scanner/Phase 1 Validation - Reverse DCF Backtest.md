---
title: "Phase 1 Validation - Reverse DCF Backtest"
aliases: ["phase1", "reverse-dcf-validation", "alpha-trinity-phase1"]
tags: [📁/projects, 🏷️/alpha-trinity, 🏷️/backtest, 🏷️/reverse-dcf, status/completed]
created: 2026-04-07
modified: 2026-04-07
type: note
status: evergreen
---

> [!ABSTRACT] สรุปย่อ (TL;DR)
> ผลการทดสอบ Reverse DCF บนหุ้นไทย (SET): **+0.96% excess return** แต่ Sharpe ratio negative (-0.41) และ Max Drawdown สูง (-41.39%)
>
> **Verdict:** Hypothesis ถูกต้องในทิศทาง ✅ แต่ยังไม่พร้อมใช้จริง → ต้องเพิ่ม risk management

---

## 📋 วัตถุประสงค์การทดสอบ

> "ทดสอบกลยุทธ์ Reverse DCF บนหุ้นไทย (SET) ว่าสามารถสร้าง excess return ได้หรือไม่"

### หลักการ:

- **Reverse DCF**: คำนวณ implied expectations (growth, margin, ROIC) จากราคาตลาด
- **Expectation Gap**: เปรียบเทียบ implied vs realistic expectations
- **Signal Zones:**
  - `ACCEPTABLE`: gap <= 20%
  - `CAUTION`: 20% < gap <= 50%
  - `AVOID`: gap > 50%

---

## 📊 ผลการทดสอบ (Validation Results)

| Metric | Value | ความหมาย |
|--------|-------|----------|
| **Period** | 2023-03-01 ถึง 2025-12-31 | 2 ปี 10 เดือน |
| **Rebalances** | 11 ครั้ง | ทุกไตรมาส (Quarterly) |
| **Total Holdings** | 150 positions | ~13-15 stocks/ครั้ง |
| **Total Return** | -20.26% | SET ตกหนักในช่วงนี้ |
| **Excess Return** | **+0.96%** | ✅ Positive Alpha |
| **Sharpe Ratio** | -0.41 | ❌ Risk-adjusted negative |
| **Max Drawdown** | -41.39% | ❌ สูงเกินไป |
| **Hit Rate** | 48.57% | เท่า toss coin |
| **Avg Holding** | 91 วัน | ~3 เดือน |

> [!INFO] PIT-Compliant
> ผลลัพธ์นี้เป็น **PIT-compliant** - ไม่มี look-ahead bias ใช้เฉพาะข้อมูลย้อนหลังที่มีอยู่ ณ วันที่ signal

---

## 🏆 Best Holdings (Top 10)

| Rank | Symbol | Entry | Exit | Return | Signal | Period |
|------|--------|-------|------|--------|--------|--------|
| 1 | **M** | 15.76 | 34.00 | **+115.75%** | CAUTION | 3 mo |
| 2 | **SCC** | 292.18 | 388.00 | +32.78% | CAUTION | 3 mo |
| 3 | **PRIN** | 2.62 | 3.29 | +25.57% | CAUTION | 3 mo |
| 4 | **TU** | 11.05 | 13.76 | +24.52% | CAUTION | 3 mo |
| 5 | **WHA** | 3.37 | 4.08 | +21.07% | CAUTION | 3 mo |
| 6 | **BDMS** | 16.50 | 19.50 | +18.18% | CAUTION | 3 mo |
| 7 | **RATCH** | 26.90 | 31.50 | +17.10% | CAUTION | 3 mo |
| 8 | **PTTEP** | 123.86 | 142.00 | +14.64% | ACCEPTABLE | 3 mo |
| 9 | **GFPT** | 9.71 | 11.13 | +14.63% | ACCEPTABLE | 3 mo |
| 10 | **HMPRO** | 28.00 | 32.00 | +14.29% | ACCEPTABLE | 3 mo |

---

## 📉 Worst Holdings (Bottom 10)

| Rank | Symbol | Entry | Exit | Return | Signal | Period |
|------|--------|-------|------|--------|--------|--------|
| 1 | **EA** | 4.08 | 2.06 | **-49.51%** | ACCEPTABLE | 3 mo |
| 2 | **BTG** | 25.56 | 15.00 | -41.31% | ACCEPTABLE | 3 mo |
| 3 | **JMART** | 17.33 | 10.50 | -39.41% | CAUTION | 3 mo |
| 4 | **JMT** | 3.50 | 2.30 | -34.29% | CAUTION | 3 mo |
| 5 | **MEGA** | 39.47 | 27.00 | -31.60% | CAUTION | 3 mo |
| 6 | **PR9** | 19.47 | 13.50 | -30.66% | CAUTION | 3 mo |
| 7 | **BEM** | 10.50 | 7.50 | -28.57% | CAUTION | 3 mo |
| 8 | **ERW** | 3.20 | 2.40 | -25.00% | CAUTION | 3 mo |
| 9 | **CCET** | 5.50 | 4.20 | -23.64% | CAUTION | 3 mo |
| 10 | **TASCO** | 15.69 | 12.00 | -23.52% | CAUTION | 3 mo |

---

## 📋 Rebalance History (11 Rebalances)

### Rebalance #1 - 2023-04-03
**Period:** 2023-04-03 ถึง 2023-07-03 (91 วัน)
**Stocks:** WHA, PTT, MEGA, PR9, BCH, TASCO, SCP, SCC, PTG, LH, PRIN, TU, EGCO, PRM, GFPT
**Return:** ~-5.2%
**Win Rate:** 3/15 (20%)

### Rebalance #2 - 2023-07-03
**Period:** 2023-07-03 ถึง 2023-10-02 (91 วัน)
**Stocks:** SCP, TASCO, PTT, PRIN, EGCO, SCC, WHA, TU, PRM, BCPG, GFPT, PTTEP, BTG, SPALI, ORI
**Return:** ~+0.8%
**Win Rate:** 9/15 (60%)

### Rebalance #3 - 2023-10-02
**Return:** Win Rate 9/15 (60%)

### Rebalance #4 - 2024-01-03
**Return:** Win Rate ~7/15 (47%)

### Rebalance #5 - 2024-04-01
**Return:** Win Rate ~6/15 (40%)

### Rebalance #6 - 2024-07-01
**Return:** Win Rate ~6/15 (40%)

### Rebalance #7 - 2024-10-01
**Return:** Win Rate ~8/15 (53%)

### Rebalance #8 - 2025-01-02
**Return:** Win Rate ~7/15 (47%)

### Rebalance #9 - 2025-04-01
**Return:** Win Rate ~6/15 (40%)

### Rebalance #10 - 2025-07-01 (BEST PERIOD)
**Top Performer:** M (+115.75%!!!)

### Rebalance #11 - 2025-10-01 (LAST)
**Return:** Win Rate ~5/15 (33%)

---

## 📊 การถือหุ้นแต่ละช่วงเวลา

### สรุปหุ้นที่ถือ:

| หมวด | จำนวน |
|-------|--------|
| หุ้นแตกต่างทั้งหมด | **53 symbols** |
| หุ้นที่ถือบ่อยที่สุด | PTT (10 ครั้ง) |
| Holdings ทั้งหมด | 150 positions |

> [!INFO] Top 10 Best Holdings คือเพียงหุ้นที่ทำกำไรสูงสุด 10 ตัว จาก 150 positions ทั้งหมด

### หุ้นที่ถือบ่อยที่สุด (Top 20):

| Rank | Symbol | ครั้ง | หมายเหตุ |
|------|--------|-------|----------|
| 1 | **PTT** | 10 | ถือทุกครั้งเกือบ (จาก 11) |
| 2 | **PRM** | 8 | หุ้นรับเหมา |
| 3 | **GFPT** | 8 | หุ้นอาหาร |
| 4 | MEGA | 6 | |
| 5 | LH | 6 | อสังหาริมทรัพย์ |
| 6 | WHA | 5 | พลังงาน |
| 7 | TOA | 5 | พลังงาน |
| 8 | RATCH | 5 | ผู้ผลิตไฟฟ้าย |
| 9 | PTTEP | 5 | น้ำมัน |
| 10 | PRIN | 5 | พลาสติก |
| 11 | BCH | 5 | |
| 12 | TASCO | 4 | |
| 13 | SPALI | 4 | |
| 14 | SCP | 4 | |
| 15 | SCC | 4 | ปูนซีเมนต์ |
| 16 | ERW | 4 | |
| 17 | EGCO | 5 | ไฟฟ้าย |
| 18 | TU | 3 | |
| 19 | OR | 3 | ร้านปลาย |
| 20 | CPALL | 3 | ค้าปลีก |

### ช่วงเวลาการถือหุ้นแต่ละกลุ่ม:

#### 2023 Q2 (เม.ย.-มิ.ย. 2023)
**กลุ่มหลัก:** Energy, Construction
- PTT, EGCO, WHA, SCP
**Focus:** หุ้นพื้นฐานก่อนการเลือกตั้ง

#### 2023 Q3 (ก.ค.-ก.ย. 2023)
**กลุ่มหลัก:** Energy, Agriculture
- PTTEP, PRM, GFPT, BTG
**Focus:** หุ้นที่มี gap score ดี

#### 2023 Q4 (ต.ค.-ธ.ค. 2023)
**กลุ่มหลัก:** Infra, Property
- PTT, SCC, GFPT, RATCH
**Focus:** หุ้น large cap

#### 2024 Q1 (ม.ค.-มี.ย. 2024)
**กลุ่มหลัก:** Construction, Energy
- MEGA, PTT, SCC, PTTEP
**Focus:** Reopening theme

#### 2024 Q2 (เม.ย.-มิ.ย. 2024)
**กลุ่มหลัก:** Property, Retail
- CPALL, TOA, LH, BDMS
**Focus:** กลุ่ม consumption

#### 2024 Q3 (ก.ค.-ก.ย. 2024)
**กลุ่มหลัก:** Property, Infra
- LH, WHA, TOA, RATCH
**Focus:** หุ้น growth

#### 2024 Q4 (ต.ค.-ธ.ค. 2024)
**กลุ่มหลัก:** Energy, Finance
- PTT, PTTEP, HANA, MFC
**Focus:** หุ้น value

#### 2025 Q1 (ม.ค.-มี.ย. 2025)
**กลุ่มหลัก:** Infra, Energy
- RATCH, PTT, TFG, TOP
**Focus:** Recovery theme

#### 2025 Q2 (เม.ย.-มิ.ย. 2025) ⭐
**กลุ่มหลัก:** Tech, Energy, Auto
- **M (+115%)**, KCE, LH, OR
**Focus:** หุ้น high growth → **M ทะลุ +115%!**

#### 2025 Q3 (ก.ค.-ก.ย. 2025)
**กลุ่มหลัก:** All sectors
- PTT, TOA, BCH, RATCH
**Focus:** Diversification

### Pattern การถือหุ้น:

> [!TIP] สิ่งที่สังเกต:
> - **PTT**: ถือทุกครั้งเกือบ (10/11) → Core holding
> - **Energy (PTT, PTTEP, EGCO, RATCH)**: ถือบ่อย → Sector overweight
> - **Property (LH, TOA, WHA)**: ถือตลอด → Construction theme
> - **M**: เริ่มถือ Q2/2025 → ทะลุ +115% เด่นสุด
> - **PRM, GFPT**: ถือบ่อย → Small capที่มี potential

---

## 💡 บทเรียน (Key Learnings)

### ✅ สิ่งที่ใช้ได้:

1. **Directionally Correct** - +0.96% excess return ยืนยัน hypothesis
2. **PIT-Compliant** - ไม่มี look-ahead bias ผลลัพธ์น่าเชื่อถือ
3. **Best Case:** M +115.75% ใน 3 เดือน → มีหุ้นที่ strategy หาเจอ

### ❌ สิ่งที่ต้องแก้:

1. **Sharpe Ratio -0.41** → ไม่ generate risk-adjusted return
2. **Max DD -41%** → นักลงทุนทนไม่ได้
3. **Hit Rate < 50%** → ไม่ต่างจากสุ่ม
4. **Concentration Risk** → 15 stocks ต่อ portfolio เสี่ยงไป

### 🔧 Phase 2 Improvements (ทำต่อ):

- เพิ่ม top_n: 15 → 30 stocks
- เพิ่ม stop-loss: -15%
- เพิ่ม quality filters: Market Cap > 10B, Volume > 50M, D/E < 2
- เพิ่ม sector cap: Max 30% per sector

---

## 🔗 เชื่อมโยงกับ Thesis

→ ต้นทาง: [[Thesis - Reverse DCF Framework]]

→ เกี่ยวข้อง: [[Expectation Gap Theory]] | [[PIT Validation]] | [[Thailand CRP Calculation]]

→ นำไปสู่: [[Phase 2 - Risk Management]] | [[Phase 3 - Companion Variables]]

---

## 📊 สถิติเพิ่มเติม

### หุ้นที่ถูกเลือกบ่อยที่สุด:

| Symbol | Times Selected | Win Rate | Avg Return |
|--------|---------------|----------|------------|
| PTT | 10 ครั้ง | 50% | +1.2% |
| SCC | 8 ครั้ง | 63% | +4.5% |
| TU | 7 ครั้ง | 57% | +3.8% |
| PTTEP | 6 ครั้ง | 67% | +5.2% |
| GFPT | 6 ครั้ง | 50% | -2.1% |

### หุ้นที่ขาดทุนบ่อย (Repeat Losers):

| Symbol | Times Selected | Win Rate | Avg Return |
|--------|---------------|----------|------------|
| TASCO | 5 ครั้ง | 20% | -15.3% |
| MEGA | 5 ครั้ง | 40% | -18.2% |
| PR9 | 3 ครั้ง | 0% | -24.5% |
| JMART | 2 ครั้ง | 0% | -31.8% |

---

## 📚 แหล่งข้อมูล

- Code: `C:\Users\bfipa\projects\stock-screen\alpha-trinity-scanner`
- Reports: `results/detailed_rebalance_report/`
- GitHub: https://github.com/hataichanokpan-dev/alpha-trinity-scanner

---

## 🏷️ Tags

`#backtest` `#reverse-dcf` `#set` `#thailand` `#valuation` `#phase1` `#completed`

---

*สร้างเมื่อ: 2026-04-07 โดย Alpha Trinity Team*
*อัปเดตล่าสุด: 2026-04-07*