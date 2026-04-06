---
tags: [finance/investing, thai-stocks, valuation, reverse-dcf, project-moc]
project: alpha-trinity-scanner
type: MOC
created: 2026-04-05
updated: 2026-04-05
---

# Alpha Trinity Scanner - Map of Content

> **"Better roughly right than precisely wrong with broken data"** - Damodaran

## Project Overview

**Objective**: Validate expectation gap hypothesis for Thai stocks using Reverse DCF methodology

**Core Hypothesis**:
1. Market prices embed implied expectations (growth, margin, ROIC)
2. **Growth Traps**: Expectations EXCEEDING realistic → Underperform
3. **Value Opportunities**: Expectations BELOW realistic → Outperform

**Validation Status**: ✅ HYPOTHESIS SUPPORTED
- Correlation: -30.35% (high gaps → low returns)
- CAUTION signal: +16.59% avg return (sweet spot)
- AVOID signal: -2.35% avg return (protected capital)

---

## Documentation Structure

### 00 - Project Summary
**File**: [[00_Project_Summary]]

**Contents**:
- Quick validation results (6-month lookback)
- Signal definitions (LOCKED)
- Technical architecture overview
- Key findings and case studies
- Forward tracking status

**When to read**: First stop for understanding the project

---

### 01 - Technical Documentation
**File**: [[01_Technical_Documentation]]

**Contents**:
- Reverse DCF methodology explained
- Core solvers (implied growth, target margin, ROIC)
- Multi-stage DCF for negative FCF
- Gap calculation formulas
- Thai market adaptations

**When to read**: Understanding how the engine works

---

### 02 - Risk Framework
**File**: [[03_RISK_FRAMEWORK]]

**Contents**:
- 5 Risk categories (Signal, Concentration, Liquidity, Model, Regime)
- Stress testing scenarios (Recession, Liquidity Crunch, Commodity Crash)
- Risk management rules (Entry, Exit, Rebalancing)
- Integration with forward tracking

**When to read**: Managing portfolio risk and stress testing

---

### 03 - Literature Review
**File**: [[04_LITERATURE_REVIEW]]

**Contents**:
- Evidence matrix (claim → source → validation → action)
- Assumption ledger (all parameters with rationale)
- Decision log (keep/adjust/monitor for each module)
- Task 8 hooks (follow-up research)

**When to read**: Understanding research backing and parameter choices

---

### 04 - Methodology Deep Dive
**File**: [[METHODOLOGY_DEEP_DIVE]]

**Contents**:
- Data triangulation (solving yfinance EBIT=0 bug)
- CAUTION zone hypothesis (why 20-50% gap = sweet spot)
- Thai market microstructure effects
- Integration with forward tracking

**When to read**: Understanding our competitive moat and key findings

---

### 05 - API Reference
**File**: [[02_API_REFERENCE]]

**Contents**:
- Complete module index with line counts
- Class and method signatures
- Usage examples for all core modules
- Configuration and utilities reference

**When to read**: Code documentation and maintenance

---

### Sector Analysis
**Directory**: [[Sector Analysis]]

#### Energy Sector
**File**: [[Sector Analysis/Energy Sector Analysis]]

**Key Findings**:
- Average composite: -22% (deep value)
- PTTGC: -67% → +80% return
- IRPC: -78% → +75% return
- Opportunity: High mean reversion potential

#### Technology Sector
**File**: [[Sector Analysis/Technology Sector Analysis]]

**Key Findings**:
- Average composite: +28% (slightly overvalued)
- DELTA: +70% (growth trap risk)
- TRUE: +11% → +36% return (hidden value)
- Opportunity: Selective (TRUE, ADVANC)

#### Healthcare Sector
**File**: [[Sector Analysis/Healthcare Sector Analysis]]

**Key Findings**:
- Average composite: +174% (severely overheated)
- BDMS: +174% → +5% return (underperformed)
- Opportunity: AVOID, look elsewhere

---

### Thai Documentation (เอกสารภาษาไทย)

#### สรุปโปรเจกต์
**File**: [[สรุปโปรเจกต์]]

**Contents**:
- ภาพรวมโปรเจกต์ภาษาไทย
- ผลการตรวจสอบ
- การวิเคราะห์แต่ละ Sector
- วิธีใช้งาน

#### วิธี Sync Vercel
**File**: [[วิธีSyncVercel]]

**Contents**:
- วิธี sync เนื้อหาไป BF-Knowledge-Base
- คำสั่ง PowerShell
- การแก้ปัญหาที่พบบ่อย

---

### Sector Analysis
**Directory**: [[Sector Analysis]]

#### Energy Sector
**File**: [[Sector Analysis/Energy Sector Analysis]]

**Key Findings**:
- Average composite: -22% (deep value)
- PTTGC: -67% → +80% return
- IRPC: -78% → +75% return
- Opportunity: High mean reversion potential

#### Technology Sector
**File**: [[Sector Analysis/Technology Sector Analysis]]

**Key Findings**:
- Average composite: +28% (slightly overvalued)
- DELTA: +70% (growth trap risk)
- TRUE: +11% → +36% return (hidden value)
- Opportunity: Selective (TRUE, ADVANC)

#### Healthcare Sector
**File**: [[Sector Analysis/Healthcare Sector Analysis]]

**Key Findings**:
- Average composite: +174% (severely overheated)
- BDMS: +174% → +5% return (underperformed)
- Opportunity: AVOID, look elsewhere

---

## Quick Reference

### Signal Definitions (LOCKED)

```
AVOID:      composite > 50%    (expectations too high)
CAUTION:    20% < comp ≤ 50%   (moderate expectations)
ACCEPTABLE: composite ≤ 20%    (reasonable expectations)
```

### Composite Score Formula

```
composite = (0.40 × growth_gap) +
           (0.30 × margin_gap) +
           (0.30 × roic_gap)
```

### Key Commands

```bash
# Calculate gap score for any stock
python -c "from core.gap_scorer import GapScorer; print(GapScorer().calculate_gap_score('PTTGC'))"

# Generate value watchlist
python analysis/value_watchlist.py

# Monthly forward tracking
python validation/forward_tracker.py
```

---

## Related Knowledge

### Damodaran Valuation Course
- [[Knowledge/Valuation/DCF Valuation/00 - DCF Valuation Course MOC]]
- [[Knowledge/Valuation/DCF Valuation/08 - Reverse DCF Fundamentals]]
- [[Knowledge/Valuation/DCF Valuation/10 - Reverse DCF Practical Application]]

### Investment Frameworks
- [[Knowledge/Value Investing/Seth Klarman's Margin of Safety Framework]]
- [[Knowledge/Value Investing/Howard Marks' Market Cycle & Risk Framework]]

### Concepts
- [[Concepts/Alpha Trinity Scanner]]

---

## Project Status (2026-04-05)

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
| Risk Framework | ✅ Complete |
| Literature Review & Documentation | ✅ Complete (Task 7) |

---

**Last Updated**: 2026-04-05
**Project Location**: `C:\Users\bfipa\projects\stock-screen\alpha-trinity-scanner`
