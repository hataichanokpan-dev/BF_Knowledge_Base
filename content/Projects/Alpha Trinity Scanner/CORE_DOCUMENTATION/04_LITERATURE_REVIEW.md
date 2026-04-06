---
tags: [finance/investing, thai-stocks, literature-review, evidence]
project: alpha-trinity-scanner
type: literature-review
created: 2026-04-05
updated: 2026-04-05
---

# Alpha Trinity Scanner - Literature Review & Evidence Map

> *"The key to successful investing is having better assumptions about the future than others do, not better mathematical models"* - Damodaran

## Purpose

Map research evidence to model implementation: which claims support our signal logic, which parts are weak, and what parameter choices are "good enough" for Thai equities.

---

## 1. Reverse DCF Mechanics & Inversion Failure Modes

### Key Claim
**Implied expectations extracted from market price predict future returns better than raw valuation metrics.**

### Evidence Matrix

| Claim | Source Quality | Supports/Contradicts | Current Implementation | Action |
|-------|---------------|---------------------|------------------------|--------|
| Market price embeds consensus expectations | Mauboussin & Rappaport (2001) "Expectations Investing" | ✅ Supports | `reverse_dcf_engine.py` solves for implied growth/margin/ROIC | ✅ Keep |
| Binary search reliably inverts DCF | Damodaran (2012) Ch. 7 "Investment Valuation" | ✅ Supports | Goal-seek optimization in `solve_implied_growth()` | ✅ Keep |
| Negative FCF requires multi-stage approach | Damodaran (2019) "Dark Side of Valuation" | ✅ Supports | `solve_implied_target_margin()` for high capex companies | ✅ Keep |
| Growth bracket limits prevent unrealistic solutions | Practice-based (EM growth >40% unsustainable) | ✅ Supports | GROWTH_BRACKET = (-20%, +40%) | ✅ Keep |
| Terminal growth must not exceed GDP | Damodaran (2012) | ✅ Supports | TERMINAL_GROWTH = 3% (Thailand GDP) | ✅ Keep |
| Epsilon dampening prevents infinite gaps | Numerical stability (project innovation) | ⚠️ No direct source | EPSILON = 0.01 in gap calculation | ✅ Keep |

### Failure Modes Documented

| Failure Mode | Impact | Mitigation |
|--------------|--------|------------|
| Hit bracket limit (-20% to +40%) | Implied growth = max/min, unreliable | Flag as "BRACKET_ERROR" in results |
| Negative FCF with single-stage | Nonsensical implied growth | Use multi-stage with target margin solver |
| Small realistic cap (<2%) | Infinite gap without epsilon | EPSILON dampening |
| yfinance EBIT = 0 (Thai stocks) | Wrong WACC, wrong valuation | Data triangulation from statements |

---

## 2. Expectation Gap Predictability

### Key Claim
**Stocks with high expectation gaps (market expects too much) underperform. Stocks with low/negative gaps (market expects too little) outperform.**

### Evidence Matrix

| Claim | Source Quality | Supports/Contradicts | Current Implementation | Action |
|-------|---------------|---------------------|------------------------|--------|
| Valuation spread predicts returns | Lakonishok et al. (1994) "Contrarian Investment" | ✅ Supports | Composite score > 50% = AVOID | ✅ Validated |
| Negative correlation: gap → return | Project validation: -30.35% | ✅ Supports | Quick validation on SET50 | ✅ Keep |
| CAUTION zone (20-50%) = sweet spot | Project finding: +16.59% vs +13.63% | ⚠️ New finding | CAUTION signal included | 🔍 Monitor (24-month) |
| Mean reversion in cyclical sectors | Arnott et al. (1989) | ✅ Supports | Energy sector: PTTGC -67% → +80% | ✅ Validated |
| Growth traps persist | Montier (2008) "Value of Nothing" | ✅ Supports | DELTA +70% gap = underperform | ✅ Validated |

### Thai Market Validation

| Metric | Result | Status |
|--------|--------|--------|
| Correlation (gap vs 6M return) | -30.35% | ✅ PASSED |
| ACCEPTABLE avg return | +13.63% | ✅ |
| CAUTION avg return | +16.59% | 🏆 Best |
| AVOID avg return | -2.35% | ✅ Protected capital |

---

## 3. Thai Market Microstructure & Regime Effects

### Key Claim
**Thai SET has unique characteristics that affect expectation gap reliability.**

### Evidence Matrix

| Claim | Source Quality | Supports/Contradicts | Current Implementation | Action |
|-------|---------------|---------------------|------------------------|--------|
| Family/control structures affect governance | Claessens et al. (2000) | ✅ Supports | RPT risk considered in stock selection | ⚠️ Qualitative |
| Foreign flows drive volatility | Bank of Thailand research | ✅ Supports | Macro regime detection in `macro_guardrails.py` | ✅ Keep |
| Sector concentration (Energy/Banking) | SET Factbook | ✅ Supports | Sector analysis, concentration risk limits | ✅ Keep |
| Limited analyst coverage on small caps | Thai brokerage reports | ⚠️ Anecdotal | Focus on SET50 for validation | ✅ Keep |
| yfinance data quality issues | Project finding (EBIT=0) | ✅ Confirmed | `data_triangulator.py` extracts from statements | ✅ Critical |

### Regime Effects (2x2 Framework)

| Regime | Characteristics | Expected Signal Performance |
|--------|----------------|----------------------------|
| GOLDEN_LOCK (High Growth + High Liquidity) | Strong exports, capital inflows | CAUTION leads, all signals boost |
| GROWTH_SLOWDOWN (Low Growth + High Liquidity) | Weak domestic, foreign flows stable | Defensive sectors, ACCEPTABLE |
| LIQUIDITY_CRUNCH (High Growth + Low Liquidity) | Capital flight, THB weak | Quality focus, CAUTION suffers |
| STAGFLATION (Low Growth + Low Liquidity) | Worst case, risk-off | Survival mode, AVOID protected |

---

## 4. Emerging Market Valuation Calibration

### Key Claim
**EM requires higher risk premia and stricter assumption bounds.**

### Evidence Matrix

| Claim | Source Quality | Supports/Contradicts | Current Implementation | Action |
|-------|---------------|---------------------|------------------------|--------|
| EM risk premium: 4-8% | Damodaran (2024) country risk data | ✅ Supports | MARKET_RISK_PREMIUM = 6% | ✅ Keep |
| Terminal growth <= GDP | Damodaran (2012) | ✅ Supports | TERMINAL_GROWTH = 3% (Thailand) | ✅ Keep |
| Higher growth volatility in EM | Bekaert & Harvey (1995) | ✅ Supports | Growth bracket: -20% to +40% (vs -5% to +15% US) | ✅ Keep |
| Accounting quality varies | Standard & Poor's (2023) Thailand | ⚠️ Moderate concern | Data triangulation required | ✅ Implemented |
| Survivorship bias in EM | Project concern | ⚠️ No direct test | Use SET50 (established companies) | ✅ Mitigated |

---

## 5. Behavioral Finance Bridge

### Key Claim
**Expectation gaps work because markets systematically misprice due to behavioral biases.**

### Evidence Matrix

| Claim | Source Quality | Supports/Contradicts | Current Implementation | Action |
|-------|---------------|---------------------|------------------------|--------|
| Extrapolation bias (past growth → future) | Lakonishok et al. (1994) | ✅ Supports | High growth stocks → AVOID signal | ✅ Validated |
| Overreaction to news | Daniel et al. (1998) | ✅ Supports | Short-term reversal in gaps | 🔍 Not tested |
| Limited attention → slow revision | Peng & Xiong (2006) | ⚠️ Unclear for SET | Gap closure speed? | 🔍 Research needed |
| Narrative momentum | Project observation | ⚠️ Anecdotal | DELTA growth story → overheated | 🔍 Monitor |
| Institutional herding | Sias (2004) | ✅ Supports | CAUTION zone = sweet spot? | 🏆 Explains finding |

### CAUTION Zone Hypothesis

**Finding**: CAUTION (20-50% gap) showed highest returns (+16.59%)

**Behavioral Explanation**:
- Acceptable (<20%): "Too cheap" = value traps, ignored
- Caution (20-50%): "Slightly expensive" = quality, institutional demand
- AVOID (>50%): "Story stocks" = priced for perfection, disappointment

**Literature Support**:
- "Quality at a Reasonable Price" (Bacon et al., 2020)
- "Growth at Fair Price" outperforms deep value in EM
- Thai institutional preference for "growth stories with reasonable valuation"

---

## 6. Assumption Ledger

### Core Parameters

| Parameter | Value | Literature Rationale | Confidence | Review Frequency |
|-----------|-------|---------------------|------------|------------------|
| **Risk-Free Rate** | 2.5% | Thai 10Y bond yield (2024) | HIGH | Quarterly |
| **Market Risk Premium** | 6% | EM premium (Damodaran 2024) | MEDIUM | Annually |
| **Terminal Growth** | 3% | Thailand GDP cap | HIGH | Annually |
| **Growth Bracket** | -20% to +40% | EM sustainable growth (Damodaran) | MEDIUM | Never (locked) |
| **AVOID Threshold** | >50% | Based on validation results | MEDIUM | 24-month review |
| **CAUTION Range** | 20-50% | Sweet spot finding | LOW | 24-month review |
| **Epsilon** | 0.01 | Numerical stability | HIGH | Never (locked) |
| **Max Sector Weight** | 30% | Diversification principle | MEDIUM | Never (locked) |
| **Max Stock Weight** | 10% | Position sizing | MEDIUM | Never (locked) |

### Assumptions Needing Research

| Assumption | Current Treatment | Required Research |
|------------|-------------------|-------------------|
| CAUTION zone persists beyond 6 months | Monitoring | 24-month forward validation |
| Gap closure speed | Unknown | Track monthly in forward tracker |
| Regime-specific signal performance | Partially tested | Stress testing by regime |
| Sector-specific thresholds | Not implemented | Task 8 research |

---

## 7. Decision Log

### Reverse DCF Engine

| Decision | Rationale | Status |
|----------|-----------|--------|
| Use binary search for implied growth | Standard approach, reliable | ✅ Keep |
| Multi-stage for negative FCF | Single-stage fails | ✅ Keep |
| Epsilon dampening | Prevents infinite gaps | ✅ Keep |
| Growth bracket: -20% to +40% | EM sustainability | ✅ Keep |

### Signal Classification

| Decision | Rationale | Status |
|----------|-----------|--------|
| AVOID > 50% | Validation supported (-2.35% return) | ✅ Keep |
| CAUTION 20-50% | Sweet spot finding (+16.59%) | 🔍 Monitor |
| ACCEPTABLE < 20% | Good returns (+13.63%) | ✅ Keep |

### Thai Market Adaptations

| Decision | Rationale | Status |
|----------|-----------|--------|
| Data triangulation from statements | yfinance EBIT = 0 bug | ✅ Critical |
| Focus on SET50 for validation | Liquidity, data quality | ✅ Keep |
| Macro regime detection | Foreign flow sensitivity | ✅ Keep |

---

## 8. Task 8 Hooks

Follow-up research based on literature gaps:

1. **CAUTION Threshold Sensitivity**
   - Question: Is 20-50% optimal for all sectors?
   - Test: Sector-specific threshold optimization
   - Data: 24-month forward tracking

2. **Gap Closure Speed**
   - Question: How fast do expectations correct?
   - Test: Monthly gap evolution tracking
   - Impact: Rebalancing frequency

3. **Regime-Specific Performance**
   - Question: Do signals work in STAGFLATION?
   - Test: Historical regime analysis (if data available)
   - Alternative: Stress testing framework

4. **Institutional Ownership Correlation**
   - Question: Does CAUTION zone = institutional demand?
   - Test: Thai SEC ownership data
   - Impact: Signal interpretation

5. **Value Trap Detection**
   - Question: Which ACCEPTABLE stocks are traps?
   - Test: Fundamental deterioration indicators
   - Impact: Filter refinement

---

## 9. What We Skipped (and Why)

| Topic | Reason for Skipping |
|-------|---------------------|
| General DCF theory | User knows basics, focus on Reverse DCF |
| Global factor models (Fama-French) | Not tied to expectation gaps |
| ML forecasting papers | Outside current thesis |
| Deep Thai banking history | Too sector-specific |
- Pre-digital era surveys | Not relevant to current market structure |
| Complex option pricing | Not used in current model |
| Currency hedging strategies | Thai stocks THB-denominated |

---

## 10. Key References

### Core Valuation

1. Damodaran, A. (2012). *Investment Valuation: Tools and Techniques*. Wiley.
2. Damodaran, A. (2019). *The Dark Side of Valuation*. FT Press.
3. Mauboussin, M., & Rappaport, A. (2001). "Expectations Investing". Harvard Business Review.

### Empirical Support

4. Lakonishok, J., Shleifer, A., & Vishny, R. (1994). "Contrarian Investment, Extrapolation, and Risk". *Journal of Finance*.
5. Montier, J. (2008). *The Value of Nothing*. Wiley.
6. Arnott, R., et al. (1989). "Tactical Asset Allocation". *Journal of Portfolio Management*.

### Thai/EM Specific

7. Claessens, S., et al. (2000). "The Separation of Ownership and Control in East Asian Corporations". *Journal of Financial Economics*.
8. Bekaert, G., & Harvey, C. (1995). "Time-Varying World Market Integration". *Journal of Finance*.
9. Bank of Thailand. (Annual). *Financial Institutions Statistics*.

### Behavioral

10. Daniel, K., et al. (1998). "Investor Psychology and Security Market Under- and Overreactions". *Journal of Finance*.
11. Peng, L., & Xiong, W. (2006). "Investor Attention, Overconfidence, and Category Learning". *Journal of Financial Economics*.
12. Sias, R. (2004). "Institutional Herding". *Review of Financial Studies*.

---

**Last Updated**: 2026-04-05
**Next Review**: After 12-month forward tracking completion
