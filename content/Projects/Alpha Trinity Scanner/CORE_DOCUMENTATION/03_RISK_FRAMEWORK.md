---
tags: [finance/investing, thai-stocks, risk-management, stress-testing, framework]
project: alpha-trinity-scanner
type: documentation
created: 2026-04-05
updated: 2026-04-05
---

# Alpha Trinity Scanner - Risk Framework & Stress Testing

> *"Risk means more things can happen than will happen"* - Elroy Dimson
> *"The greatest risk is taking no risks"* - Mark Zuckerberg (misattributed to Damodaran)

## Overview

The Risk Framework provides comprehensive risk assessment for portfolios built using expectation gap signals. It integrates Damodaran's risk-adjusted valuation principles, Howard Marks' market cycle framework, and Klarman's margin of safety approach.

---

## Risk Categories

### 1. Signal Risk

**Definition**: Risk that expectation gap signals fail to predict returns

**Metrics**:
- Signal age (days since last validation)
- Performance decay (recent vs historical returns)
- Signal composition (AVOID/CAUTION/ACCEPTABLE mix)

**Risk Levels**:
- **LOW**: Signals recently validated, < 6 months old, < 20% decay
- **MEDIUM**: Signals 6-12 months old, 20-40% decay
- **HIGH**: Signals > 12 months old, > 40% decay
- **CRITICAL**: AVOID signals in portfolio, significant decay

**Mitigation**:
- Monthly forward tracking
- Re-validate signals quarterly
- Remove AVOID signals immediately
- Monitor signal degradation

### 2. Concentration Risk

**Definition**: Risk from excessive exposure to specific sectors or stocks

**Limits**:
- Max sector weight: 30%
- Max single stock weight: 10%

**Metrics**:
- Sector weights (percentage per sector)
- Stock weights (percentage per stock)
- Herfindahl-Hirschman Index (HHI) for concentration

**Risk Levels**:
- **LOW**: All weights within limits, HHI < 0.10
- **MEDIUM**: One limit breached, HHI 0.10-0.15
- **HIGH**: Multiple limits breached, HHI > 0.15
- **CRITICAL**: Sector > 50% or Stock > 20%

**Mitigation**:
- Diversify across 5+ sectors
- Limit single stock positions to 10%
- Rebalance when concentrations exceed limits

### 3. Liquidity Risk

**Definition**: Risk of being unable to exit positions without excessive slippage

**Thai Market Context**:
- Many SET stocks are illiquid
- Average daily value varies widely
- Small caps can have < 10M THB daily volume

**Limits**:
- Minimum average daily value: 50M THB
- Portfolio liquidity ratio: > 50%

**Risk Levels**:
- **LOW**: All stocks liquid, ratio > 70%
- **MEDIUM**: Some illiquid stocks, ratio 50-70%
- **HIGH**: > 30% illiquid, ratio < 50%
- **CRITICAL**: > 50% illiquid, ratio < 30%

**Mitigation**:
- Focus on SET50/SET100 stocks
- Check average daily volume before entry
- Scale out of illiquid positions gradually

### 4. Model Risk

**Definition**: Risk from incorrect assumptions or model failures

**Key Assumptions**:
- Risk-free rate: 2.5% (Thai 10Y bond)
- Market risk premium: 6% (EM premium)
- Terminal growth: 3% (GDP growth cap)

**Stress Ranges**:
- Risk-free: 1.5% - 4.0%
- MRP: 4% - 8%
- Terminal growth: 1% - 5%

**Risk Levels**:
- **LOW**: Assumptions within historical norms
- **MEDIUM**: Some assumptions at range boundaries
- **HIGH**: Multiple assumptions stressed
- **CRITICAL**: Assumptions outside historical ranges

**Mitigation**:
- Regular assumption review
- Sensitivity analysis on key inputs
- Document rationale for all assumptions

### 5. Regime Risk

**Definition**: Risk that signals perform differently across macro regimes

**2x2 Regime Framework**:
| | High Liquidity | Low Liquidity |
|---|---|---|
| **High Growth** | GOLDEN_LOCK | LIQUIDITY_CRUNCH |
| **Low Growth** | GROWTH_SLOWDOWN | STAGFLATION |

**Expected Performance by Regime**:
- **GOLDEN_LOCK**: All signals boost, CAUTION leads
- **GROWTH_SLOWDOWN**: Moderate returns, defensive sectors
- **LIQUIDITY_CRUNCH**: Reduced returns, quality focus
- **STAGFLATION**: Severe reduction, survival mode

**Risk Levels**:
- **LOW**: Portfolio positioned for current regime
- **MEDIUM**: Some regime mismatch
- **HIGH**: Significant regime mismatch
- **CRITICAL**: Portfolio exposed to worst regime

**Mitigation**:
- Monitor macro indicators monthly
- Adjust sector weights based on regime
- Maintain defensive posture in uncertain regimes

---

## Stress Testing

### Scenarios

| Scenario | Regime | Description | Key Shock |
|----------|--------|-------------|-----------|
| Global Recession | STAGFLATION | US/EU recession, exports -15% | Beta +30%, returns -70% |
| Liquidity Crunch | LIQUIDITY_CRUNCH | Capital flows reverse, THB -20% | Rates spike, beta +20% |
| Commodity Crash | GROWTH_SLOWDOWN | Oil -50%, energy crashes | Energy -50% |
| Recovery | GOLDEN_LOCK | Global recovery, exports +20% | All +50% |

### Stress Test Results Interpretation

| Portfolio Return | Risk Level | Action |
|-----------------|------------|--------|
| > +10% | LOW | No action needed |
| 0% to +10% | LOW-MEDIUM | Monitor |
| -10% to 0% | MEDIUM | Review positioning |
| -20% to -10% | HIGH | Reduce risk |
| < -20% | CRITICAL | Defensive repositioning |

---

## Usage

### Basic Risk Assessment

```python
from core.risk_framework import RiskFramework

rf = RiskFramework()

risks = rf.assess_portfolio_risk(
    portfolio={'PTTGC': 0.20, 'TRUE': 0.15, ...},
    signals={'PTTGC': 'ACCEPTABLE', 'TRUE': 'ACCEPTABLE', ...},
    sector_mapping={'PTTGC': 'Energy', 'TRUE': 'Technology', ...},
    price_data=price_df,
    volume_data=volume_df
)

for risk_cat, risk_level in risks.items():
    print(f"{risk_cat}: {risk_level.name}")
```

### Stress Testing

```python
from core.risk_framework import RiskFramework, StressTester

rf = RiskFramework()
tester = StressTester(rf)

results = tester.run_stress_test(
    portfolio=portfolio,
    signals=signals,
    sector_mapping=sector_mapping,
    current_prices=prices
)

for result in results:
    print(f"{result.scenario_name}: {result.portfolio_return:.2%}")
```

---

## Risk Management Rules

### Entry Rules

1. **Signal Check**: Only ACCEPTABLE and CAUTION signals
2. **Liquidity Filter**: Average daily value > 50M THB
3. **Concentration Limit**: Max 10% per stock, 30% per sector
4. **Regime Alignment**: Adjust sector weights based on regime

### Exit Rules

1. **Signal Migration**: ACCEPTABLE → AVOID → Exit immediately
2. **Stop Loss**: -20% from entry price
3. **Target Achievement**: Gap closes (composite < -20%)
4. **Regime Shift**: Reduce exposure if regime turns adverse

### Rebalancing Rules

1. **Frequency**: Monthly review, quarterly rebalancing
2. **Drift Tolerance**: Allow +/- 5% drift before rebalancing
3. **New Signals**: Add only if signal improves sector balance
4. **Winners**: Trim positions that exceed concentration limits

---

## Integration with Forward Tracking

The risk framework integrates with monthly forward tracking:

1. **Monthly Snapshot**: Assess all risk categories
2. **Stress Test**: Run 4 scenarios
3. **Report**: Generate risk report with recommendations
4. **Action**: Implement any required adjustments

```python
# In forward_tracker.py monthly snapshot
risk_assessment = rf.assess_portfolio_risk(...)
stress_results = tester.run_stress_test(...)
risk_report = tester.generate_risk_report(stress_results, risk_assessment)
```

---

## Case Studies

### Case 1: Energy Concentration Risk

**Portfolio**: PTTGC (20%), IRPC (15%), PTTEP (10%), TOP (10%)

**Issue**: 55% in Energy sector (exceeds 30% limit)

**Stress Test Result**:
- Commodity Crash: -25% portfolio return
- Risk Level: HIGH

**Recommendation**: Reduce Energy to 30%, diversify to other sectors

### Case 2: AVOID Signal in Portfolio

**Portfolio**: BDMS (10%), others (90%)

**Issue**: BDMS has AVOID signal (+174% composite gap)

**Historical Validation**: AVERAGE AVOID return = -2.35%

**Recommendation**: Remove BDMS immediately, replace with ACCEPTABLE signal

### Case 3: Liquidity Risk

**Portfolio**: MIX, SAWAD, LH (all small caps)

**Issue**: Average daily value < 20M THB each

**Risk**: Cannot exit without significant slippage

**Recommendation**: Replace with SET50 stocks in same sectors

---

## Related Notes

- [[00_Project_Summary]] - Overall project status
- [[01_Technical_Documentation]] - Reverse DCF methodology
- [[Sector Analysis/Energy Sector Analysis]] - Energy sector findings
- [[Knowledge/Value Investing/Howard Marks' Market Cycle & Risk Framework]]

---

**Last Updated**: 2026-04-05
**File**: `core/risk_framework.py` (400+ lines)
**Demo**: `examples/stress_test_demo.py`
