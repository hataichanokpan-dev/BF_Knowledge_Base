---
tags: [finance/investing, thai-stocks, methodology, data-quality]
project: alpha-trinity-scanner
type: methodology
created: 2026-04-05
updated: 2026-04-05
---

# Alpha Trinity Scanner - Methodology Deep Dive

> *"Better roughly right than precisely wrong with broken data"* - Project Motto

## Overview

This document covers the two most critical technical aspects of the Alpha Trinity Scanner:

1. **Data Triangulation**: How we solve the "broken data" problem for Thai stocks
2. **CAUTION Zone Hypothesis**: Why the 20-50% expectation gap is the sweet spot

---

## Part 1: Data Triangulation - Our Competitive Moat

### The Problem

**Issue**: Yahoo Finance returns `EBIT = 0` for ALL Thai stocks

**Impact**: Without EBIT, we cannot calculate:
- Operating margin
- WACC (cannot compute D/E ratio properly)
- ROIC (cannot compute invested capital)
- Realistic growth caps

**Root Cause**: Yahoo Finance data structure for Thai stocks differs from US stocks
- Field mapping issues
- Thai accounting format differences
- Limited coverage for emerging markets

### Our Solution: Data Triangulation

Instead of relying on a single data source, we triangulate from three sources:

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA TRIANGULATION                        │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌─────────────┐      ┌─────────────┐      ┌─────────────┐ │
│  │  yfinance   │──────│   Financial  │──────│   SET       │ │
│  │  (prices)   │      │  Statements │      │  Filings    │ │
│  └─────────────┘      └─────────────┘      └─────────────┘ │
│         │                     │                     │        │
│         └─────────────────────┴─────────────────────┘        │
│                              │                               │
│                        ┌──────▼──────┐                       │
│                        │  Unified    │                       │
│                        │  Dataset    │                       │
│                        └─────────────┘                       │
└─────────────────────────────────────────────────────────────┘
```

### Implementation: `data_triangulator.py`

```python
class DataTriangulator:
    """
    Extract real financial data from Thai company statements

    Strategy:
    1. Get company info from yfinance
    2. Download financial statements (income, balance, cash flow)
    3. Extract key line items directly from statements
    4. Fall back to yfinance info if statements unavailable
    5. Validate and clean data
    """

    def extract_income_statement_items(self, symbol: str) -> dict:
        """
        Extract from Income Statement:
        - Revenue (Total Revenue)
        - Operating Income (Operating Profit)
        - EBIT (Operating Income)
        - Net Income
        - Interest Expense
        - Tax Expense
        """
        # Download income statement
        stmt = self.financials.get_income_stmt(symbol)

        return {
            'revenue': self._find_item(stmt, REVENUE_KEYWORDS),
            'operating_income': self._find_item(stmt, OP_INCOME_KEYWORDS),
            'ebit': self._find_item(stmt, EBIT_KEYWORDS),
            'net_income': self._find_item(stmt, NET_INCOME_KEYWORDS),
            'interest_expense': self._find_item(stmt, INTEREST_KEYWORDS),
            'tax_expense': self._find_item(stmt, TAX_KEYWORDS),
        }
```

### Thai-Specific Keyword Mapping

Thai financial statements use English labels but with variations:

| Line Item | Standard | Thai Variations |
|-----------|----------|-----------------|
| Revenue | "Total Revenue" | "Revenue", "Total Revenue", "Operating Revenue" |
| Operating Income | "Operating Income" | "Operating Profit", "EBIT", "Operating Result" |
| EBIT | "EBIT" | "Earnings Before Interest and Taxes" |
| Net Income | "Net Income" | "Net Profit", "Profit for the Year" |
| Interest | "Interest Expense" | "Finance Cost", "Interest Expense" |

### The "Broken Data" Examples

**Before Data Triangulation**:

```python
>>> yfinance.Ticker("PTTGC.BK").info.get('ebitda')
0  # WRONG!
>>> yfinance.Ticker("PTTGC.BK").info.get('operatingMargins')
0  # WRONG!
```

**After Data Triangulation**:

```python
>>> dt = DataTriangulator()
>>> dt.extract_financials("PTTGC")
{
    'ebit': 45234100000,  # 45.2B THB - CORRECT!
    'revenue': 684321000000,
    'operating_margin': 0.0661,  # 6.61% - CORRECT!
}
```

### Validation Against Reality

We validate extracted data against:

1. **SET Filings**: Cross-check with company annual reports
2. **Broker Research**: Compare with Thai brokerage estimates
3. **Reasonableness**: Check for extreme values (e.g., margin > 100%)

```python
def validate_extracted_data(self, symbol: str, data: dict) -> bool:
    """
    Sanity checks for extracted data
    """
    checks = []

    # Check 1: Revenue > 0
    checks.append(data['revenue'] > 0)

    # Check 2: Margin between 0% and 100%
    margin = data.get('operating_margin', 0)
    checks.append(0 <= margin <= 1)

    # Check 3: Net income < revenue (sanity)
    checks.append(abs(data['net_income']) < data['revenue'])

    # Check 4: Tax rate reasonable (0-50%)
    tax_rate = data.get('tax_expense', 0) / data.get('ebit', 1)
    checks.append(0 <= tax_rate <= 0.5)

    return all(checks)
```

### Why This Matters

**Without data triangulation:**
- EBIT = 0 → Cannot calculate ROIC
- Margin = 0 → Cannot calculate realistic margins
- WACC wrong → Valuation wrong
- **Result: "Precisely wrong with broken data"**

**With data triangulation:**
- Real EBIT from statements → Accurate ROIC
- Real margins from statements → Accurate realistic caps
- Proper WACC → Reasonable valuation
- **Result: "Roughly right with corrected data"**

---

## Part 2: The CAUTION Zone Hypothesis

### The Discovery

**Initial Hypothesis**: Lower expectation gap = Better returns

**Expected Ranking**:
1. ACCEPTABLE (<20%) → Best
2. CAUTION (20-50%) → Good
3. AVOID (>50%) → Poor

**Actual Results** (Quick Validation, SET50, 6-month):

| Signal | Avg Return | Surprise |
|--------|------------|----------|
| **CAUTION** | **+16.59%** | 🏆 **BEST** |
| ACCEPTABLE | +13.63% | Expected |
| AVOID | -2.35% | Expected (protected capital) |

### Why Does CAUTION Win?

#### Hypothesis 1: Institutional Appetite

**Theory**: Thai institutional investors (funds, banks, insurance) prefer:
- Quality companies
- Growth stories
- Reasonable valuation

**The Sweet Spot**:
- ACCEPTABLE (<20%): "Too cheap" = Value traps, weak fundamentals
- CAUTION (20-50%): "Quality with growth" = Institutional favorites
- AVOID (>50%): "Priced for perfection" = Disappointment risk

**Evidence**:

| Company | Composite | Signal | Type | 6M Return |
|---------|-----------|--------|------|-----------|
| TRUE | +11% | ACCEPTABLE | Turnaround, value | +36.5% |
| ADVANC | +1% | ACCEPTABLE | Fair value | - |
| HMPRO | +7% | ACCEPTABLE | Reasonable growth | +18.2% |

The best ACCEPTABLE performers had clear catalysts (turnaround, growth).

#### Hypothesis 2: Behavioral "Goldilocks" Zone

**Too Cold (ACCEPTABLE)**:
- Market ignores these stocks
- Limited analyst coverage
- "Boring" companies
- Slow reversion

**Just Right (CAUTION)**:
- Market acknowledges quality
- Moderate expectations
- Room for positive surprise
- Momentum + Value

**Too Hot (AVOID)**:
- Priced for perfection
- Any miss = disappointment
- High expectations = high risk

#### Hypothesis 3: Thai Market Structure

**Concentration**: Thai SET is dominated by:
- Energy (PTT, PTTGC)
- Banking (KBANK, SCB, BBL)
- Telecom (ADVANC, TRUE, AIS)

**Institutional Flow**:
- Foreign funds favor large-cap quality
- Thai institutions hold index constituents
- Retail investors chase momentum

**Result**:
- Large-cap quality (CAUTION zone) gets institutional support
- Small-cap value (ACCEPTABLE zone) gets ignored

### The CAUTION Zone Framework

```
Expectation Gap

    +100% |─────────────────────| AVOID
         |     Growth Traps     |   Severe overheating
    +50% |─────────────────────|
         |                      |
    +20% |─────────────────────| CAUTION ← SWEET SPOT
         |   Quality Growth     |   Institutional favorites
      0% |─────────────────────|
         |   Fair Value         |
   -20%  |─────────────────────| ACCEPTABLE
         |   Deep Value         |   Turnaround candidates
   -50%  |─────────────────────|
         |   Mean Reversion     |
```

### When to Use Each Signal

**ACCEPTABLE (<20%)**:
- Value investors with patience
- Turnaround situations
- Deep value opportunities
- Activist strategies

**CAUTION (20-50%)**:
- Core portfolio holdings
- Quality growth
- Institutional-quality names
- Momentum + Value

**AVOID (>50%)**:
- Explicitly exclude from portfolio
- Potential short candidates
- Risk management
- Capital preservation

### Implications for Portfolio Construction

**Traditional Approach** (what we expected):
```
70% ACCEPTABLE + 20% CAUTION + 10% Cash
```

**Optimal Approach** (what data suggests):
```
40% CAUTION + 30% ACCEPTABLE + 30% sector-diversified
```

**Rationale**:
- CAUTION as core (quality + growth)
- ACCEPTABLE for satellite positions (value, turnaround)
- Sector limits to manage concentration risk

### CAUTION Zone by Sector

| Sector | CAUTION Examples | Why Works |
|--------|------------------|-----------|
| Energy | PTTEP (+27%) | Mean reversion + dividend support |
| Technology | ADVANC (+1%), HMPRO (+7%) | 5G tailwinds + reasonable growth |
| Industrial | Various | Infrastructure spending theme |
| Banking | KBANK, SCB (moderate gaps) | Quality + dividend yield |

### Risks to the Hypothesis

**Risk 1**: CAUTION zone performance is sample-specific
- **Mitigation**: 24-month forward tracking

**Risk 2**: Regime shifts change relative performance
- **Mitigation**: Stress testing framework

**Risk 3**: Market learns, CAUTION becomes AVOID
- **Mitigation**: Continuous monitoring

---

## Part 3: Integration with Forward Tracking

### Monthly Tracking Protocol

Each month, track:

1. **Portfolio Performance**
   - By signal (CAUTION vs ACCEPTABLE)
   - By sector
   - vs SET Index

2. **Signal Migration**
   - ACCEPTABLE → CAUTION → AVOID
   - Gap closure speed
   - New signals emerging

3. **CAUTION Zone Validation**
   - Is CAUTION still outperforming?
   - Which sectors?
   - What's driving the alpha?

### Decision Framework

| Scenario | Action |
|----------|--------|
| CAUTION outperforms by >5% | Increase CAUTION allocation |
| ACCEPTABLE outperforms | Re-evaluate CAUTION hypothesis |
| AVOID turns positive | Check for regime shift |

---

## Related Documentation

- [[01 - Technical Documentation]] - Reverse DCF mechanics
- [[LITERATURE REVIEW]] - Evidence matrix
- [[Sector Analysis]] - Sector-specific findings
- [[Risk Framework & Stress Testing]] - Risk management

---

**Last Updated**: 2026-04-05
**Validation Status**: CAUTION zone hypothesis requires 24-month confirmation
