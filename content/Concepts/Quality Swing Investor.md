---
title: Quality Swing Investor
note_type: concept
status: evergreen
created: 2026-03-27
updated: 2026-03-27
tags:
  - note/concept
  - framework/investing
  - strategy/stock-picking
aliases:
  - QSI
  - Quality Swing
  - QSI Framework
source: 7-round deep dive with Gemini (2026-03-26)
---

# Quality Swing Investor

> Investment framework combining quality fundamentals with swing timing


## Overview

Quality Swing Investor (QSI) เป็น framework วิเคราะห์หุ้นที่ผสมผสาน:
- **Quality** - พื้นฐานธุรกิจที่แข็งแกร่ง
- **Swing** - จังหวะเข้าซื้อตามเทคนิคัล
- **Catalyst** - ปัจจัยกระตุ้นราคา

## Triple Score System (0-100)

### 1. Quality Score (คะแนนคุณภาพ)

| Component | Weight | Criteria |
|-----------|--------|----------|
| **Moat** | 20 | Competitive advantage, barriers to entry |
| **Financial Health** | 20 | D/E ratio, cash flow, balance sheet |
| **Growth** | 20 | Revenue growth, earnings trajectory |
| **Management** | 20 | Track record, capital allocation |
| **Valuation** | 20 | P/E, P/BV vs sector/intrinsic value |

**Quality Indicators:**
- ROE > 15%
- D/E < 1.0x
- Positive operating cash flow
- Consistent dividend history
- P/BV < 1x (value)

### 2. Swing Score (คะแนนจังหวะ)

| Component | Weight | Criteria |
|-----------|--------|----------|
| **Trend** | 25 | Price vs MA50/MA200, overall direction |
| **Momentum** | 25 | RSI (30-70 range), MACD signals |
| **Support/Resistance** | 25 | Clear levels defined, bounce history |
| **Volume** | 25 | Accumulation patterns, breakout volume |

**Swing Indicators:**
- Price above MA50
- RSI not overbought (<70)
- Clear support level identified
- Volume confirmation on moves

### 3. Catalyst Score (คะแนนปัจจัยกระตุ้น)

| Component | Weight | Criteria |
|-----------|--------|----------|
| **Events** | 25 | Dividends (XD dates), earnings, corporate actions |
| **Industry** | 25 | Sector trends, regulatory changes, macro tailwinds |
| **Sentiment** | 25 | Analyst upgrades, market perception, news flow |
| **Risk Profile** | 25 | Downside protection, known risks quantified |

**Catalyst Types:**
- Dividend announcements (XD dates)
- Rate cuts (beneficial for property, REITs)
- New product launches
- Sector rotation
- Earnings surprises

## Composite Formula

```
Composite Score = (Quality × 0.5) + (Catalyst × 0.3) + (Swing × 0.2)
```

**Why This Weighting:**
- Quality dominates (50%) - fundamentals drive long-term
- Catalyst secondary (30%) - timing matters for swing
- Swing supporting (20%) - technical confirms entry

## Decision Matrix

| Score | Action | Meaning |
|-------|--------|---------|
| **>85** | BUY | Strong quality + catalyst + timing |
| **70-85** | WATCH | Good but wait for better entry |
| **50-69** | SPECULATIVE | High risk, small position only |
| **<50** | PASS | Insufficient quality or catalyst |

## Sector Adjustments

Different sectors require different emphasis:

| Sector | Adjustment | Notes |
|--------|------------|-------|
| **REIT** | Weight yield higher | Dividend sustainability key |
| **Tech** | Weight growth higher | Accept higher P/E for growth |
| **Bank** | Weight cycle position | NIM, credit cost cycle matters |
| **Cyclical** | Weight timing higher | Entry/exit timing critical |
| **Property** | Weight P/BV higher | Book value provides floor |

## Market Regime Filter

Adjust scoring based on market conditions:

| Regime | Adjustment |
|--------|------------|
| **Bull** | Standard weights |
| **Bear** | Increase Quality weight (+10%) |
| **Volatile** | Increase Catalyst weight (+10%) |
| **Recovery** | Increase Swing weight (+10%) |

## Application Process

### Step 1: Data Collection
- Current price, 52W high/low
- P/E, P/BV, ROE, D/E
- Dividend yield, XD date
- Recent news, sector trends

### Step 2: Score Each Pillar
- Quality: Score 0-100 based on 5 components
- Swing: Score 0-100 based on 4 components
- Catalyst: Score 0-100 based on 4 components

### Step 3: Calculate Composite
```
Composite = Q×0.5 + C×0.3 + S×0.2
```

### Step 4: Apply Decision Matrix
- >85: Buy
- 70-85: Add to watchlist
- 50-69: Small speculative position
- <50: Pass

### Step 5: Define Action Plan
- Entry zone (support level)
- Stop loss (invalidation level)
- Targets (base/bull/bear cases)
- Position size (based on conviction)

## Example Scoring

### SPVI Analysis (2026-03-27)
| Pillar | Score | Breakdown |
|--------|-------|-----------|
| Quality | 69/100 | Moat 11, Financial Health 16, Growth 12, Management 15, Valuation 15 |
| Swing | 66/100 | Trend 18, Momentum 15, Volume 10, Structure 16, Volatility 7 |
| Catalyst | 55/100 | Events 18, Industry 14, Sentiment 11, Risk 12 |

**Composite:** 69×0.5 + 55×0.3 + 66×0.2 = **63.7** → SPECULATIVE

### MCS Analysis (2026-03-27)
| Pillar | Score | Notes |
|--------|-------|-------|
| Quality | 80/100 | ROE สูง, Margin ดี, หนี้ต่ำ ⚠️ พึ่งญี่ปุ่น 99% |
| Swing | 60/100 | ถูกมาก ⚠️ ราคาใกล้ 52W High |
| Catalyst | 60/100 | กำไรโต 41.5%, ปันผลใกล้ตัว |

**Composite:** 80×0.5 + 60×0.3 + 60×0.2 = **70** → WATCH

## Related Concepts

- [[Alpha Trinity Scanner]] - Automated screening tool (82 SET stocks passed Wave 1)
- [[Deep Value]] - Extreme discount focus
- [[Quality GARP]] - Quality at reasonable price
- [[Value Swing]] - Value + timing combo
- [[Dividend Play]] - Yield-focused strategy
- [[CAN SLIM]] - Growth stock system
- [[Jesse Stine's Superstock System]] - Microcap momentum

## Related Frameworks

- [[Value Investing]] - Fundamental approach
- [[Technical Analysis]] - Chart-based timing
- [[Moat]] - Competitive advantage analysis
- [[Catalyst]] - Price driver identification

## Key Takeaways

1. **Quality First** - Fundamentals drive long-term returns
2. **Time Your Entry** - Don't buy at random prices
3. **Catalyst Required** - Need a reason for price to move
4. **Score Objectively** - Remove emotion from decisions
5. **Size Appropriately** - Match position to conviction

---

*Framework developed through 7-round deep dive with Gemini, 2026-03-26*
