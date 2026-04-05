---
tags: [finance/investing, thai-stocks, valuation, dcf, technical]
project: alpha-trinity-scanner
type: technical
created: 2026-04-05
---

# Reverse DCF Engine - Technical Documentation

## Overview

**Reverse DCF** inverts the traditional valuation model:

| Traditional DCF | Reverse DCF |
|----------------|-------------|
| Inputs → Fair Value → Compare to Price | Price → Solve for Implied Expectations → Compare to Fundamentals |

## Core Solvers

### 1. Implied Growth Solver

**Purpose:** Given market price, what growth rate is the market assuming?

**Algorithm:** Binary search (goal-seek optimization)

```python
def solve_implied_growth(market_ev, base_fcf, wacc, terminal_growth):
    """
    Find growth rate where PV(FCF) = Market EV
    
    Args:
        market_ev: Enterprise value from market
        base_fcf: Current free cash flow
        wacc: Weighted average cost of capital
        terminal_growth: Perpetual growth rate (≤ GDP)
    
    Returns:
        (implied_growth, hit_bracket_limit)
    """
```

**Constraints:**
- Growth bracket: [-20%, +40%]
- Rationale: >40% sustained growth unprecedented for EM
- Terminal growth: ≤ GDP (~3% for Thailand)

### 2. Implied Target Margin Solver (Negative FCF)

**Purpose:** High-reinvestment companies require different approach

**Insight:** When FCF is negative due to CapEx:
- Don't solve for growth (leads to bracket errors)
- Solve for **target margin** instead
- Use multi-stage DCF with margin convergence

**Method:**

```python
def solve_implied_target_margin(
    market_ev, revenue, current_margin,
    revenue_growth_assumption,  # 12% for EM
    wacc, terminal_growth
):
    """
    For negative FCF companies:
    1. Assume reasonable revenue growth (12% for EM)
    2. Solve for target margin required to justify price
    3. Calculate margin expansion needed
    """
```

### 3. Implied ROIC Solver

**Purpose:** Is expected ROIC sufficient to support growth?

**Sustainable Growth Formula:**
```
g = ROIC × Reinvestment Rate
```

Therefore:
```
ROIC = g / Reinvestment Rate
```

## Multi-Stage DCF

### When to Use?
- Negative FCF companies
- High growth phase (startups, high capex)
- Traditional single-stage fails

### Three Stages

| Stage | Duration | Characteristics |
|-------|----------|----------------|
| **High Growth** | Years 1-5 | Revenue grows, margins converge to target |
| **Transition** | Years 6-10 | Growth slows, margins stabilize |
| **Terminal** | Year 10+ | Stable growth at GDP rate |

### Calculation

```python
def _calc_multistage_ev_from_margin(
    revenue, current_margin, target_margin,
    revenue_growth, wacc, terminal_growth,
    high_growth_years=5,
    transition_years=5
):
    """
    Stage 1: Revenue grows at revenue_growth, margins converge to target
    Stage 2: Growth slows linearly to terminal, margins stable
    Stage 3: Terminal growth at GDP rate
    
    Returns: Enterprise Value from multi-stage DCF
    """
```

## Gap Calculation

### Growth Gap

```python
growth_gap = (implied_growth - realistic_growth) / realistic_growth
```

**Interpretation:**
- Positive: Market expects MORE growth than realistic
- Negative: Market expects LESS growth than realistic (value opportunity)

### Composite Score

Weighted combination of all three gaps:

```python
composite = (0.40 × growth_gap + 
             0.30 × margin_gap + 
             0.30 × roic_gap)
```

### Signal Classification

```python
if composite > 0.50:    → AVOID      # Expectations too high
elif composite > 0.20: → CAUTION    # Moderate expectations  
else:                  → ACCEPTABLE # Reasonable expectations
```

## Epsilon Dampening

**Problem:** Small realistic caps (1-2%) cause infinite gaps

**Solution:**
```python
EPSILON = 0.01  # 1% minimum denominator

gap = (implied - realistic) / max(abs(realistic), EPSILON)
```

## Thai Market Adaptations

### Data Challenges

| Challenge | Solution |
|-----------|----------|
| EBIT = 0 in Yahoo | Data triangulation from financial statements |
| No historical data | Forward tracking only |
| Small caps illiquid | Use SET50 for validation |

### Parameters

```python
# Thailand specific
RISK_FREE_RATE = 0.025      # 2.5% Thai 10Y bond
MARKET_RISK_PREMIUM = 0.06  # 6% EM risk premium
TERMINAL_GROWTH = 0.03       # 3% GDP growth
GROWTH_BRACKET = (-0.20, 0.40)  # -20% to 40%
```

## Examples

### Example 1: PTTGC (Deep Value)

```
Price: 35.25 THB
Implied Growth: 2%
Realistic Growth: 12%
Growth Gap: -83.33%
Composite: -66.77%
Signal: ACCEPTABLE

Interpretation: Market pricing in 2% growth vs 12% realistic = Deep value
```

### Example 2: BTS (Overheated)

```
Price: 2.10 THB  
Valuation Method: multi_stage (negative FCF)
Implied Target Margin: 50%
Current Margin: 57%
Margin Expansion Required: -7pp (decline)
Composite: +78.72%
Signal: AVOID

Interpretation: Market expects margins to stay high, but ROIC too low
```

## Files

- `reverse_dcf_engine.py` - Core implementation (700+ lines)
- `implied_expectations.py` - Expectation decomposition (300+ lines)
- `realistic_calculator.py` - Realistic cap calculation (200+ lines)
- `gap_scorer.py` - Gap calculation & signals (350+ lines)

## References

- Damodaran, A. (2012). *Investment Valuation: Tools and Techniques for Determining the Value of Any Asset*, Wiley.
- Damodaran, A. (2019). *The Dark Side of Valuation*, FT Press.
