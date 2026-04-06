# Market Regimes & Risk Management — Literature Review

> **Chapter:** 2.5 Market Regimes
> **Thesis:** VQM Model — Integrated Value-Quality-Momentum Model
> **Last Updated:** 2026-04-06

---

## Core Papers

### 1. Momentum Crashes & Regimes

**Daniel, K., & Moskowitz, T. J. (2016). Momentum Crashes.**
*Journal of Financial Economics, 122*(2), 221-247.

**Key Findings:**
- Momentum crashes during market rebounds (after bear markets)
- Crashes related to market regime changes
- Time-varying momentum premium

**Relevance to VQM:**
- Risk management for momentum component
- Quality factor may mitigate crash risk
- Regime-aware rebalancing considerations

---

### 2. Volatility Regimes

**[TBD — Volatility Regimes Research]**

**Key Concepts:**
- High vs. low volatility periods
- Factor performance varies across regimes
- Risk management implications

**Relevance to VQM:**
- Adjust factor weights by regime?
- Stop-loss during high volatility?
- Sector rotation considerations

---

### 3. Business Cycle & Factors

**[TBD — Business Cycle Factor Research]**

**Key Concepts:**
- Value performs better in recoveries
- Quality defensive in recessions
- Momentum regime-dependent

**Relevance to VQM:**
- Regime-based factor allocation?
- Static vs. dynamic weighting

---

## VQM Model Regime Analysis Framework

### Regime Classification

| Regime | Definition | Expected VQM Performance |
|--------|------------|-------------------------|
| **Bull Market** | SET Index > MA(200), rising | Value & Momentum strong |
| **Bear Market** | SET Index < MA(200), falling | Quality defensive |
| **High Volatility** | VIX > threshold | Quality outperforms |
| **Low Volatility** | VIX < threshold | Momentum strong |

### Factor Performance by Regime (Literature-Based)

| Factor | Bull | Bear | High Vol | Low Vol |
|--------|------|------|----------|---------|
| Value | ++ | - | - | + |
| Quality | + | ++ | ++ | + |
| Momentum | ++ | -- | - | ++ |

**Legend:** ++ strong outperform, + mild outperform, - underperform, -- crash risk

---

## Risk Management Considerations

### 1. Maximum Drawdown Control

**Approaches:**
- Stop-loss on individual positions (e.g., -20%)
- Portfolio-level drawdown limits (e.g., -15% from peak)
- Reduce momentum exposure in high volatility

### 2. Position Sizing

**Constraints:**
- Max 5% per stock
- Max 10% per sector
- Equal-weight or score-weighted

### 3. Rebalancing Strategy

**Options:**
- **Quarterly** (VQM baseline) — balances costs and signal decay
- **Monthly** — better momentum signals, higher costs
- **Regime-triggered** — rebalance on regime change

---

## Thailand Market Regimes (2019-2024)

### Period Classification

| Period | Regime | SET Performance | Notes |
|--------|--------|-----------------|-------|
| 2019 | Bull + Volatile | +7% | Trade war tensions |
| 2020 | Bear → Bull | -13% → +28% | COVID crash, rebound |
| 2021 | Bull | +15% | Recovery |
| 2022 | Sideways/Bear | -10% | Fed rate hikes |
| 2023 | Recovery | +18% | China reopening |
| 2024 (YTD) | Bull | +8% | Easing expectations |

**Relevance to VQM:**
- Backtest covers multiple regimes
- Test robustness across conditions

---

## Research Questions

1. How does VQM perform in bull vs. bear markets?
2. Does quality protect during momentum crashes?
3. Optimal rebalancing frequency by regime?
4. Should factor weights be dynamic?

---

## References (APA Format)

```
Daniel, K., & Moskowitz, T. J. (2016). Momentum crashes. Journal of 
Financial Economics, 122(2), 221-247.

[Additional references TBD]
```

---

*Document created: 2026-04-06*
*Status: Literature Review — Market Regimes Section*
