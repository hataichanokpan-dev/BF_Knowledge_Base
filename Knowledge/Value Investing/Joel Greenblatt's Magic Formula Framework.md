---
title: Joel Greenblatt's Magic Formula Framework
note_type: knowledge
created: 2026-03-29
updated: 2026-03-29
tags:
  - note/knowledge
  - investing
  - value
  - quality
  - systematic
aliases:
  - Magic Formula
  - Greenblatt System
  - ROC + EY
---

# Joel Greenblatt's Magic Formula Framework

> **"Buy good businesses at bargain prices - systematically."**
> — Joel Greenblatt, *The Little Book That Beats the Market* (2005)

---

## 🎯 Core Philosophy

### สาระสำคัญ
Magic Formula = **Quality (ROC) + Value (EY)** ในระบบเดียว

| แนวคิด | ต้นแบบ | ที่มา |
|--------|--------|-------|
| **Quality** | หา "good business" | Benjamin Graham → Warren Buffett |
| **Value** | ซื้อ "bargain price" | Benjamin Graham → Seth Klarman |
| **Systematic** | ทำซ้ำได้ ไม่ใช้อารมณ์ | Quant discipline |

### Mental Models

| Model | ความหมาย | การใช้งาน |
|-------|----------|-----------|
| **Mr. Market** | ตลาดเป็นโรคจิต ราคาขึ้นลงตามอารมณ์ | ซื้อตอนกลัว ขายตอนโลภ |
| **Time Arbitrage** | Formula ไม่เวิร์กทุกปี = โอกาส | ทน underperform 1-3 ปี |
| **Margin of Safety** | ซื้อ good business ราคาถูก = ป้องกัน downside | ถ้าพลาด ราคาถูกช่วยได้ |

### 🔥 Key Quotes

> **"The secret to the magic formula's success is that it doesn't always work. If it did, everyone would use it, and it would stop working."**

> **"Choosing individual stocks without any idea of what you're looking for is like running through a dynamite factory with a burning match. You may live, but you're still an idiot."**

> **"I'm not asking you to trust me. I'm asking you to trust the numbers."**

---

## 📐 The Magic Formula: Exact Calculations

### ⭐ ทำไมไม่ใช้ P/E และ ROE?

| Metric | ปัญหา | Magic Formula แก้ยังไง |
|--------|-------|----------------------|
| **P/E** | ไวต่อโครงสร้างหนี้ + tax rate | ใช้ **EBIT/EV** (pre-tax, debt-agnostic) |
| **ROE** | ไวต่อ leverage (หนี้เยอะ = ROE สูงเทียม) | ใช้ **ROC** (capital รวมหนี้) |

---

### 📊 Metric 1: Return on Capital (ROC) → Quality

**วัตถุประสงค์:** หาธุรกิจที่ลงทุนน้อยแล้วได้กำไรมาก = **Moat**

```
ROC = EBIT / (Net Working Capital + Net Fixed Assets)
```

#### ส่วนประกอบ

| Component | Formula | หมายเหตุ |
|-----------|---------|----------|
| **EBIT** | Earnings Before Interest & Taxes | Operating Income จากงบ |
| **Net Working Capital** | `(Current Assets - Excess Cash) - (Current Liabilities - ST Debt)` | เงินหมุนเวียนที่ใช้จริง |
| **Net Fixed Assets** | `Total Assets - Current Assets - Intangibles` | PPE ที่ใช้ดำเนินการ |

#### ⚠️ สิ่งที่ต้องระวัง

| รวม | ตัดออก |
|-----|--------|
| Operating assets | Excess cash |
| PPE ที่ใช้จริง | Goodwill + Intangibles |
| Working capital จำเป็น | Non-operating assets |

#### เกณฑ์ ROC

| ROC Level | ความหมาย | Action |
|-----------|----------|--------|
| **> 50%** | Exceptional moat | ✅ ตรวจสอบว่า denominator ไม่ผิดปกติ |
| **20-50%** | Excellent | ✅ Target zone |
| **10-20%** | Good | ⚠️ พอใช้ |
| **< 10%** | Poor | ❌ ตัดออก |
| **< 0%** | Loss-making | ❌ ตัดทิ้ง |

> 💡 **Best Practice:** ใช้ **ROC เฉลี่ย 5 ปี >= 20%** เป็น baseline

---

### 📊 Metric 2: Earnings Yield (EY) → Value

**วัตถุประสงค์:** วัดว่าหุ้น "ถูก" แค่ไหนเทียบกับราคาซื้อกิจการทั้งหมด

```
EY = EBIT / Enterprise Value (EV)
```

#### Enterprise Value Formula

```
EV = Market Cap + Total Debt + Preferred Stock + Minority Interest - Cash & Equivalents
```

#### เปรียบเทียบ EY vs P/E

| Metric | Formula | Pros | Cons |
|--------|---------|------|------|
| **P/E** | Price / Net Income | ง่าย คุ้นเคย | ไวต่อ debt + tax |
| **EY** | EBIT / EV | Debt-agnostic, Pre-tax | ซับซ้อนกว่า |

**ตัวอย่าง:**
- Company A: Market Cap $100M, Debt $0, EBIT $10M → EY = 10%
- Company B: Market Cap $100M, Debt $500M, EBIT $10M → EY = 10/600 = **1.67%**

> ถ้าดู P/E เท่ากัน แต่ EY ต่างกันมาก = Company B แพงกว่าเพราะหนี้เยอะ

#### EY vs Bond Yield

```
EY Spread = EY - 10Y Treasury Yield
```

| EY Spread | ความหมาย |
|-----------|----------|
| **> 6%** | ถูกมาก vs พันธบัตร |
| **3-6%** | ถูกปานกลาง |
| **0-3%** | แพง |
| **< 0%** | แพงมาก (ควรหลีกเลี่ยง) |

---

## 🔄 The Ranking System

### ขั้นตอนการจัดอันดับ

```
Step 1: คำนวณ ROC ทุกตัวใน universe → จัด rank (สูงสุด = 1)
Step 2: คำนวณ EY ทุกตัวใน universe → จัด rank (สูงสุด = 1)
Step 3: Combined Rank = ROC Rank + EY Rank
Step 4: เลือกตัวที่ Combined Rank ต่ำสุด
```

### ตัวอย่าง

| หุ้น | ROC | ROC Rank | EY | EY Rank | Combined | Result |
|------|-----|----------|-----|---------|----------|--------|
| **A** | 45% | 5 | 15% | 10 | **15** | ✅ #1 |
| **B** | 60% | 1 | 8% | 50 | 51 | |
| **C** | 30% | 20 | 12% | 15 | **35** | ✅ #2 |
| **D** | 25% | 35 | 18% | 5 | 40 | |

> 💡 **Key Insight:** หุ้นที่ดีที่สุดไม่จำเป็นต้อง ROC สูงสุดหรือ EY สูงสุด แต่เป็น **balance ที่ดีทั้งสองด้าน**

---

## 📈 Backtest Results

### Original Claim (1988-2004)

| Strategy | CAGR | Notes |
|----------|------|-------|
| **Magic Formula** | **30.8%** | 17 ปี backtest |
| **S&P 500** | 12.4% | Benchmark |

### ⚠️ ความเป็นจริงที่ต้องรู้

| ประเด็น | ข้อเท็จจริง |
|---------|------------|
| **Volatility** | ผลตอบแทนรายปีกว้างมาก (ติดลบถึง +80%) |
| **Realistic Return** | Independent studies = 20-26% before costs |
| **Recent Period** | 2014-2024 underperform S&P (growth bull market) |
| **Rolling 3-Year** | Outperform ~65-70% of the time |

### Performance by Period

| Period | Magic Formula | S&P 500 | Status |
|--------|---------------|---------|--------|
| 1988-2004 | 30.8% | 12.4% | ✅ Golden era |
| 2005-2013 | ~18% | ~8% | ✅ Still good |
| 2014-2024 | ~10% | ~13% | ⚠️ Underperform |

> 🔥 **Critical:** Strategy เจ็บได้หลายปีติด ต้องทนได้

---

## 🛠️ Implementation Guide

### Universe Definition

| Criteria | Setting | เหตุผล |
|----------|---------|--------|
| **Market Cap** | > $200M | สภาพคล่อง |
| **Exclude** | Financials, Utilities, REITs | โครงสร้างงบต่าง |
| **Exclude** | Foreign ADRs | Data quality |
| **Exclude** | Negative EBIT | ขาดทุน |

### Portfolio Construction

| Parameter | Setting | เหตุผล |
|-----------|---------|--------|
| **Number of Stocks** | **20-30** | กระจายความเสี่ยงพอ |
| **Position Sizing** | Equal weight | ไม่ predict ว่าตัวไหนจะดีกว่า |
| **Holding Period** | 1 year | Tax optimization |
| **Rebalancing** | Annual | ลด transaction costs |

### 🧠 Tax Hack: 51/53 Week Rule

| Stock Type | Action | Timing |
|------------|--------|--------|
| **Losers** | ขายก่อนครบ 1 ปี | ~51 weeks → Short-term loss |
| **Winners** | ขายหลังครบ 1 ปี | ~53 weeks → Long-term gain (tax ต่ำกว่า) |

### Accumulation Strategy

```
Month 1: ซื้อ top 2-3 stocks
Month 2: ซื้อ top 2-3 stocks (อาจซ้ำหรือใหม่)
...
Month 10-12: ครบ 20-30 stocks
→ Dollar-cost averaging ลด timing risk
```

---

## 🧠 Psychology: Why Investors Fail

### 4 Psychological Killers

| Trap | อาการ | ผลลัพธ์ |
|------|-------|---------|
| **Tracking Error Regret** | เห็นคนรวยจาก NVDA/TSLA ขณะที่ตัวเองตาม | เลิกกลางทาง |
| **Ugly Stock Bias** | ขยะแขยงหุ้นใน list แล้วข้าม | ทำลาย formula |
| **Recency Bias** | คิดว่า underperform 18 เดือน = broken | เลิกก่อน mean revert |
| **Loss Aversion** | เจ็บ -20% มากกว่าดีใจ +20% | Panic sell |

### 📊 The "Ugly Stock" Problem

> **หุ้นถูกเพราะตลาดเกลียด = ข่าวร้าย อื้อฉาว วิกฤต**

**ตัวอย่างหุ้นที่ Magic Formula เลือก:**
- บริษัทฟ้องล้มละลายแล้วฟื้น
- อุตสาหกรรมตกต่ำ (coal, steel, retail)
- มี scandal / lawsuit

> 💡 **Key:** ถ้าเลือกเอง (cherry-pick) = ทำลาย edge ของ formula

### กฎเหล็ก

```
1. ซื้อทุกตัวใน list ไม่มีข้อยกเว้น
2. ไม่ดู portfolio ทุกวัน
3. ตั้ง reminder รีบาลานซ์ 1 ปี
4. ประเมินผล rolling 3-5 ปี ไม่ใช่ปีเดียว
```

---

## ⚡ Modern Enhancements

### 🔥 Enhancement 1: Momentum Filter

**ปัญหา:** Magic Formula = falling knives (หุ้นถูกแต่ยังตกอยู่)

**แก้ไข:** เพิ่ม momentum เข้าไป

```
Step 1: หา top 50-100 Magic Formula stocks
Step 2: Sort by 6-Month Price Return
Step 3: เลือก top 20-30 with highest momentum
```

**ผลลัพธ์:**
- ลด drawdown
- เพิ่ม returns
- หลีกเลี่ยง catching falling knives

---

### 🔥 Enhancement 2: Quality Overlay

**ปัญหา:** ROC ปีเดียวอาจโดน one-off windfall

**แก้ไข:** เพิ่ม quality screens

| Screen | Formula | Threshold |
|--------|---------|-----------|
| **Gross Margin** | Gross Profit / Revenue | Top 70% of universe |
| **FCF/Debt** | Free Cash Flow / Total Debt | > 0.1 |
| **Accruals** | (Net Income - CFO) / Assets | Bottom 30% = exclude |

---

### 🔥 Enhancement 3: Multi-Factor Integration

```
Modern Formula = Value (EY) + Quality (ROC) + Momentum (6M) + Low Volatility
```

| Factor | Weight | Evidence |
|--------|--------|----------|
| Value | 30% | Fama-French |
| Quality | 30% | Novy-Marx |
| Momentum | 25% | Asness et al. |
| Low Vol | 15% | Betting Against Beta |

---

## ⚠️ Limitations & Criticism

### Critical Issues

| Issue | คำอธิบาย | แก้ไข |
|-------|----------|-------|
| **Small-cap Bias** | Backtest ใช้หุ้นเล็กที่ซื้อจริงยาก | ตั้ง min market cap $500M+ |
| **Value Traps** | ถูกเพราะกำไรจะหาย | เพิ่ม quality overlay |
| **Drawdown** | เจ็บได้หลายปีติด | ทน 3-5 ปี หรือเพิ่ม momentum |
| **Accounting Risk** | EBIT โดนตกแต่งงบได้ | ตรวจ accruals, cash flow |
| **Crowding** | สูตรดัง = edge บางลง | ใช้ modern adaptations |
| **Tax Drag** | Turnover สูง = tax มาก | ใช้ใน IRA / tax-advantaged |

### เมื่อไหร่ Magic Formula ไม่เวิร์ก

| Market Regime | ผลลัพธ์ |
|---------------|---------|
| **Secular Bull (FAANG era)** | Underperform |
| **Low Interest Rate** | Growth > Value |
| **High Liquidity** | Risk-on = cheap stocks lag |

### เมื่อไหร่ Magic Formula เวิร์กดี

| Market Regime | ผลลัพธ์ |
|---------------|---------|
| **Sideways/Choppy** | Outperform |
| **Rising Rates** | Cash flows matter |
| **Post-Crisis** | Value rebounds |

---

## 📋 Practical Checklist

### Phase 1: Universe Setup
- [ ] Market Cap > $200M (หรือ $500M สำหรับ liquidity)
- [ ] Exclude: Financials, Utilities, REITs
- [ ] Exclude: Foreign ADRs
- [ ] Exclude: Negative EBIT

### Phase 2: Quality Filter
- [ ] ROC เฉลี่ย 5 ปี >= 20%
- [ ] Gross Margin >= industry median
- [ ] FCF/Total Debt > 0.1
- [ ] Accruals ratio ไม่สูงผิดปกติ

### Phase 3: Magic Ranking
- [ ] คำนวณ ROC = EBIT / (NWC + Net Fixed Assets)
- [ ] คำนวณ EY = EBIT / EV
- [ ] Rank ROC จากสูงไปต่ำ
- [ ] Rank EY จากสูยไปต่ำ
- [ ] Combined Rank = ROC Rank + EY Rank

### Phase 4: Momentum Trigger (Optional but Recommended)
- [ ] เลือก top 50 Combined Rank
- [ ] Sort by 6-Month Price Return
- [ ] เลือก top 20-30

### Phase 5: Execution
- [ ] Equal dollar weight
- [ ] Accumulate 2-3 stocks/month (ไม่ซื้อทีเดียว)
- [ ] Set calendar: 51 weeks (losers) / 53 weeks (winners)
- [ ] ไม่ check portfolio ทุกวัน

### Phase 6: Discipline Rules
- [ ] ซื้อทุกตัวใน list (no cherry-picking)
- [ ] ทน underperform 1-3 ปี
- [ ] ประเมินผล rolling 3-5 ปี
- [ ] Rebalance ปีละครั้ง

---

## 🔗 Special Situations

### Spin-Offs (Greenblatt's Other Expertise)

| Evidence | Return | Period |
|----------|--------|--------|
| Cusatis et al. (1993) | +20% abnormal | 3 years post-spin |
| Desai & Jain (1999) | +10% abnormal | 3 years post-spin |

**เหตุผลที่ spin-offs ได้ผล:**
- Forced selling (index funds ขายออก)
- Analyst coverage ต่ำ
- Management มี incentive แรงขึ้น

### Value-Weighted Index (Gotham ETFs)

| ETF | Approach |
|-----|----------|
| **GSPY** | S&P 500 reweighted by value |
| **GVLU** | Large-cap value reweighted |

> แนวคิด: ถ่วงน้ำหนักตาม "ความถูก" ไม่ใช่ market cap

---

## 🔗 Related Concepts

- [[Value Investing]] - รากฐานของ Magic Formula
- [[Quality GARP]] - Growth at Reasonable Price variant
- [[Margin of Safety]] - ซื้อถูกป้องกัน downside
- [[Moat]] - ROC สูง = competitive advantage
- [[CAN SLIM]] - Momentum complement
- [[Howard Marks' Market Cycle & Risk Framework]] - Cycle awareness
- [[Seth Klarman's Margin of Safety Framework]] - Deep value approach
- [[Alpha Trinity Scanner]] - Quant screening application

---

## 📚 References

- *The Little Book That Beats the Market* (2005) - Joel Greenblatt
- *The Big Secret for the Small Investor* (2011) - Joel Greenblatt
- [MagicFormulaInvesting.com](https://www.magicformulainvesting.com/) - Official screener
- MIT Monograph: [Lee & So Part 1](https://eso.scripts.mit.edu/docs/LeeSoPart1.pdf)
- Novy-Marx (2013): "The Other Side of Value" - Profitability premium
- Asness et al. (2013): "Value and Momentum Everywhere"
- Gotham ETFs: [GSPY](https://gothametfs.com/gspy) | [GVLU](https://gothametfs.com/gvlu)

---

## 📊 Quick Reference Card

### Formulas

| Metric | Formula |
|--------|---------|
| **ROC** | `EBIT / (Net Working Capital + Net Fixed Assets)` |
| **EY** | `EBIT / Enterprise Value` |
| **EV** | `Market Cap + Debt + Preferred + Minority Interest - Cash` |
| **Combined Rank** | `Rank(ROC) + Rank(EY)` |

### Thresholds

| Metric | Good | Warning |
|--------|------|---------|
| ROC | > 20% | < 10% |
| EY | > 10% | < 5% |
| EY Spread vs 10Y | > 6% | < 2% |
| Portfolio Size | 20-30 stocks | < 15 stocks |

### Key Numbers

| Item | Value |
|------|-------|
| Original CAGR (1988-2004) | 30.8% |
| Realistic CAGR (post-2010) | 10-15% |
| Holding Period | 1 year |
| Rebalancing | Annual |
| Min Market Cap | $200-500M |

---

*สร้าง: 2026-03-29 | อัปเดต: 2026-03-29*
