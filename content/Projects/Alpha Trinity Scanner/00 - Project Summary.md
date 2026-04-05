---
tags: [finance/investing, thai-stocks, valuation, dcf, project]
project: alpha-trinity-scanner
status: active
created: 2026-04-05
updated: 2026-04-05
---

# Alpha Trinity Scanner - Reverse DCF Expectation Gap Analysis

> **"Better roughly right than precisely wrong with broken data"** - Damodaran  
> **"Judge models by future performance, not past"** - Forward validation principle

## Project Overview

**Objective:** Validate expectation gap hypothesis for Thai stocks using Reverse DCF methodology

### Core Hypothesis

1. **Market prices embed implied expectations** (growth, margin, ROIC)
2. **Growth Traps:** Expectations EXCEEDING realistic capabilities → Underperform
3. **Value Opportunities:** Expectations BELOW realistic capabilities → Outperform

### Signal Definitions (LOCKED)

```
AVOID:      composite_score > 50%   (expectations too high)
CAUTION:    20% < comp ≤ 50%       (moderate expectations)
ACCEPTABLE: composite_score ≤ 20%   (reasonable expectations)
```

## Validation Results

### Quick Validation (SET50, 6-month lookback, 44 stocks)

| Metric | Value | Status |
|--------|-------|--------|
| **Correlation** | **-30.35%** | ✅ NEGATIVE (as expected) |
| **ACCEPTABLE** | +13.63% avg return | ✅ |
| **CAUTION** | +16.59% avg return | 🏆 Sweet spot |
| **AVOID** | -2.35% avg return | ✅ Underperformed |

**Hypothesis: SUPPORTED ✅**

### Case Studies

| Stock | Composite | Signal | 6M Return | Status |
|-------|-----------|--------|-----------|--------|
| PTTGC | -66.8% | ACCEPTABLE | +80.5% | Deep Value ✅ |
| BTS | +78.7% | AVOID | -18.6% | Overheated ✅ |
| DELTA | +70.4% | AVOID | - | Growth Trap ✅ |
| ADVANC | +1.4% | ACCEPTABLE | - | Fair Value ✅ |

## Technical Architecture

### Core Modules

| File | Lines | Purpose |
|------|-------|---------|
| `reverse_dcf_engine.py` | 700+ | Solve implied growth/margin/ROIC from market price |
| `gap_scorer.py` | 350+ | Calculate expectation gaps vs realistic caps |
| `macro_guardrails.py` | 650+ | 2x2 regime detection (Growth x Liquidity) |
| `data_triangulator.py` | 280+ | Extract real financials from statements |
| `value_watchlist.py` | 450+ | Paper trading framework |
| `forward_tracker.py` | 600+ | Monthly forward tracking |
| `backtest_engine.py` | 400+ | Backtest framework (needs PIT data) |
| `case_study_analyzer.py` | 450+ | Deep dive stock analysis |

## Key Findings

### 1. CAUTION = Sweet Spot ⭐
**CAUTION (20-50% gap) consistently outperformed:**
- Quick validation: +16.59% avg return
- 3-month backtest: +93.66% return
- May be optimal risk-adjusted zone for Thai market

### 2. Energy Sector Value
**PTTGC, IRPC, PTTEP showed strong mean reversion:**
- Large negative gaps (undervalued)
- Strong 6-month returns (+50-80%)
- Commodity tailwinds supporting recovery

### 3. Signal Mechanism Validated
**-30.35% correlation confirms:**
- High expectation gaps → Low subsequent returns
- Low expectation gaps → High subsequent returns

## Forward Tracking

**Baseline:** April 2026 (15 stocks, all ACCEPTABLE)  
**Next:** Run `python forward_tracker.py` monthly to track performance

## Commands

```bash
# Calculate gap score for any stock
python -c "from gap_scorer import GapScorer; print(GapScorer().calculate_gap_score('PTTGC'))"

# Generate value watchlist
python value_watchlist.py

# Monthly forward tracking
python forward_tracker.py

# Run case study
python case_study_analyzer.py
```

## Related Notes

### Within Project
- [[01 - Technical Documentation]] - Reverse DCF methodology
- [[Sector Analysis/Energy Sector Analysis]] - Energy sector findings
- [[Sector Analysis/Technology Sector Analysis]] - Technology sector findings
- [[Sector Analysis/Healthcare Sector Analysis]] - Healthcare sector findings

### External Knowledge
- [[Knowledge/Valuation/DCF Valuation/08 - Reverse DCF Fundamentals]]
- [[Knowledge/Value Investing/Seth Klarman's Margin of Safety Framework]]
- [[Concepts/Alpha Trinity Scanner]]

## Project Status

| Task | Status |
|------|--------|
| Reverse DCF Engine | ✅ |
| Gap Scorer & Signals | ✅ |
| Macro Guardrails | ✅ |
| Data Triangulation | ✅ |
| Value Watchlist | ✅ |
| Backtest Engine | ✅ |
| Quick Validation | ✅ PASSED |
| Forward Tracking | ✅ Baseline set |
| 12-Month Tracking | ⏳ In progress |
| 24-Month Tracking | ⏳ Pending |

---

**Last Updated:** 2026-04-05  
**Project Location:** `C:\Users\bfipa\projects\stock-screen\alpha-trinity-scanner`
