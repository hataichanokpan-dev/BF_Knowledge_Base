---
title: "VQM Model — Backtesting Framework"
aliases: ["VQM Backtesting", "เฟรมเวิร์กการทดสอบ VQM", "Backtesting Protocol"]
tags: [📁/projects, 🏷️/vqm-model, 🏷️/backtesting, 🏷️/validation, status/draft]
created: 2026-04-06
modified: 2026-04-06
type: framework
status: seedling
links:
  - "[[Chapter 3 - Methodology]]"
  - "[[VQM Model - Factor Calculation Formulas]]"
  - "[[Complete Reference List]]"
---

# VQM Model — Backtesting Framework

> [!WARNING] Backtesting Pitfalls
> "Historical performance is not indicative of future results"
>
> This framework aims to minimize common biases: Look-ahead, Survivorship, Overfitting

---

## 1. Framework Overview

### 1.1 Backtesting Objectives

```
┌─────────────────────────────────────────────────────────────┐
│  BACKTESTING GOALS                                          │
│                                                             │
│  1. Validate VQM Model predictive power                    │
│  2. Measure risk-adjusted returns                          │
│  3. Test robustness across market regimes                  │
│  4. Estimate implementation feasibility (costs, turnover)   │
└─────────────────────────────────────────────────────────────┘
```

### 1.2 Period Coverage

| Parameter | Value | Justification |
|-----------|-------|---------------|
| **Start Date** | 2019-01-01 | Pre-COVID baseline |
| **End Date** | 2024-12-31 | Most recent complete data |
| **Total Period** | 6 years | ~24 quarters |
| **Regimes Covered** | Bull, Bear, Recovery, High Inflation | Diversified |

---

## 2. Walk-Forward Architecture

### 2.1 Rolling Window Design

```
┌─────────────────────────────────────────────────────────────────┐
│  WALK-FORWARD ROLLING WINDOW                                   │
│                                                                 │
│  ┌───────────────┬───────────────┬───────────────┬─────────┐   │
│  │   Training    │     Test      │   Training    │  Test   │   │
│  │   (12 months) │   (3 months)  │   (12 months) │ (3 mo)  │   │
│  └───────────────┴───────────────┴───────────────┴─────────┘   │
│         ↓               ↓                 ↓            ↓         │
│      Q1-Q4/19      Q1/20            Q2-Q1/21      Q2/21        │
│      (Calc factors) (Hold portfolio)  (Recalc)     (Hold)       │
│                                                                 │
│  Note: Training rolls forward, not expanding                  │
└─────────────────────────────────────────────────────────────────┘
```

### 2.2 Timeline Details

| Period | Training Window | Test Period | Rebalance Date |
|--------|-----------------|-------------|----------------|
| **Cycle 1** | Jan-Dec 2019 | Q1 2020 (Jan-Mar) | 2020-01-02 |
| **Cycle 2** | Q2 2019 - Q1 2020 | Q2 2020 (Apr-Jun) | 2020-04-01 |
| **Cycle 3** | Q3 2019 - Q2 2020 | Q3 2020 (Jul-Sep) | 2020-07-01 |
| ... | ... | ... | ... |
| **Cycle 24** | Q3 2023 - Q2 2024 | Q4 2024 (Oct-Dec) | 2024-10-01 |

### 2.3 Advantages of Walk-Forward

1. **No Look-ahead Bias** — ใช้เฉพาะข้อมูลที่มีณ วันที่ทดสอบ
2. **Regime Adaptation** — โมเดล adapt กับสภาพตลาดที่เปลี่ยนไป
3. **Realistic Simulation** — เลียนแบบการลงทุนจริง
4. **Robustness Test** — ทดสอบในหลายสภาพตลาด

---

## 3. Portfolio Construction Rules

### 3.1 Selection Process

```
Step 1: Filter Universe
├── Liquidity: ADV > 20M THB
├── Size: Market Cap > 5B THB
└── Data Availability: Complete metrics

Step 2: Calculate VQM Score
├── Compute Value Score (4 metrics)
├── Compute Quality Score (4 metrics)
├── Compute Momentum Score (3 metrics)
└── Composite: 0.45×V + 0.35×Q + 0.20×M

Step 3: Rank & Select
├── Sort by VQM Score (descending)
└── Select Top N (N = 20, 25, 30)

Step 4: Assign Weights
├── Base Case: Equal Weight (1/N)
├── Alt Case 1: Score Weighted
└── Apply Constraints
```

### 3.2 Constraints

```
Maximum Weight per Stock: 5%
Maximum Weight per Sector: 10%
Minimum Portfolio Size: 20 stocks
Maximum Portfolio Size: 30 stocks
```

### 3.3 Sector Classification

```
SET Sectors (11 sectors):
1. Agri & Food        7. Property
2. Consumer           8. Resources
3. Financials         9. Services
4. Industrials       10. Technology
5. Petrochem & Chem   11. Tourism
6. Health Care
```

---

## 4. Execution & Cost Model

### 4.1 Transaction Cost Assumptions

| Component | Cost | Basis |
|-----------|------|-------|
| **Broker Commission** | 0.10% | SET fee + broker |
| **VAT** | 0.025% | 7% of commission |
| **Stamp Duty** | 0.10% | Buy side only (Thailand) |
| **Slippage** | 0.15% | Market impact (avg stock) |
| **Total (buy)** | 0.35% | Round trip |
| **Total (sell)** | 0.15% | Round trip |
| **Round-trip** | 0.50% | Full cycle |

### 4.2 Execution Model

```
Assumptions:
- Execute at OPEN price on rebalance date
- All trades execute same day
- No partial fills
- No market impact beyond slippage assumption

Reality Check:
- Large caps: 0.30% round-trip realistic
- Mid caps: 0.50-0.75% round-trip realistic
- Small caps: 0.75-1.00% round-trip realistic
```

### 4.3 Turnover Calculation

```
Turnover (%) = (Σ|Δw_i|) / 2

เมื่อ:
Δw_i = w_i,t - w_i,t-1 (change in weight for stock i)
Sum over all stocks in portfolio

Example:
- Portfolio has 25 stocks
- Each quarter, 8 stocks changed (32%)
- Avg weight change: 2%
- Turnover = 8 × 2% × 2 = 32%
- Annual turnover ≈ 128%
```

---

## 5. Performance Metrics

### 5.1 Return Metrics

| Metric | Formula | Description |
|--------|---------|-------------|
| **Total Return** | (P_t - P_0) / P_0 | Cumulative return |
| **Annualized Return** | (1 + Total_R)^(1/n) - 1 | Per-year return |
| **Quarterly Return** | (P_t - P_t-1) / P_t-1 | Per-period return |
| **CAGR** | (P_t / P_0)^(1/n) - 1 | Compound annual growth |

### 5.2 Risk-Adjusted Metrics

| Metric | Formula | Benchmark |
|--------|---------|-----------|
| **Sharpe Ratio** | (R_p - R_f) / σ_p | SET Index |
| **Sortino Ratio** | (R_p - R_f) / σ_downside | SET Index |
| **Information Ratio** | α_p / Tracking Error | N/A |
| **Treynor Ratio** | (R_p - R_f) / β_p | SET Index |
| **Omega** | ∫(1-F(r))dr / ∫F(r)dr | MAR = 0% |

### 5.3 Risk Metrics

| Metric | Formula | Description |
|--------|---------|-------------|
| **Volatility** | StdDev(returns) × √12 | Annualized |
| **Max Drawdown** | Max(Peak - Trough) / Peak | Largest decline |
| **Downside Deviation** | StdDev(negative returns) | Risk of bad outcomes |
| **VaR (95%)** | Percentile(returns, 5%) | Worst 5% outcome |
| **CVaR** | Mean(returns < VaR) | Expected loss beyond VaR |

### 5.4 Benchmark-Adjusted Metrics

```
Alpha (Jensen's) = R_p - R_f - β_p × (R_m - R_f)

Tracking Error = StdDev(R_p - R_m)

Information Ratio = (R_p - R_m) / Tracking_Error

Up Capture = Mean(R_p | R_m > 0) / Mean(R_m | R_m > 0)

Down Capture = Mean(R_p | R_m < 0) / Mean(R_m | R_m < 0)
```

---

## 6. Statistical Significance Tests

### 6.1 Alpha Significance

```
Hypothesis:
H0: α = 0 (No skill)
H1: α ≠ 0 (Skill exists)

Test:
t-stat = α̂ / SE(α̂)

Critical Value:
- t_crit = 1.96 (for 95% confidence, two-tailed)
- t_crit = 2.58 (for 99% confidence, two-tailed)

Decision:
- Reject H0 if |t-stat| > t_crit
```

### 6.2 Comparison Tests

| Test | Purpose | When to Use |
|------|---------|-------------|
| **Paired t-test** | VQM vs SET returns | Normal distribution |
| **Wilcoxon Signed** | VQM vs SET (non-parametric) | Non-normal data |
| **F-test** | Compare variance | Risk comparison |
| **Kolmogorov-Smirnov** | Distribution comparison | Return distribution |

---

## 7. Regime Analysis

### 7.1 Regime Classification

```
Method 1: Moving Average Cross
- Bull: MA(6) > MA(12) + 5%
- Bear: MA(6) < MA(12) - 5%
- Sideways: Other

Method 2: Volatility-Based
- Low Vol: VIX < 15
- Normal Vol: 15 ≤ VIX < 25
- High Vol: VIX ≥ 25

Method 3: Drawdown-Based
- Bull: Drawdown from peak < 10%
- Correction: 10% ≤ DD < 20%
- Bear: Drawdown ≥ 20%
```

### 7.2 Regime Periods (2019-2024)

| Regime | Period | Characteristics |
|--------|--------|-----------------|
| **Bull 2019** | Jan-Dec 2019 | Recovery from 2018 |
| **COVID Crash** | Feb-Mar 2020 | -35% drawdown |
| **Recovery** | Apr-Dec 2020 | V-shape recovery |
| **Bull 2021** | Jan-Dec 2021 | Easing cycle |
| **Rate Hike** | Jan-Oct 2022 | Fed tightening |
| **Recovery 2023** | Nov 2022-Dec 2023 | China reopening |
| **Election Year** | Jan-Dec 2024 | Political uncertainty |

---

## 8. Sensitivity Analysis

### 8.1 Parameter Variations

| Parameter | Base | Low | High |
|-----------|------|-----|------|
| **Portfolio Size** | 25 | 20 | 30 |
| **Value Weight** | 45% | 40% | 50% |
| **Quality Weight** | 35% | 30% | 40% |
| **Momentum Weight** | 20% | 15% | 25% |
| **Rebalance Freq** | Quarterly | Semi-annual | Monthly |
| **Transaction Cost** | 0.50% | 0.30% | 0.75% |

### 8.2 Robustness Checks

```
1. Sub-period Analysis
   ├── Period A: 2019-2021 (COVID + Recovery)
   ├── Period B: 2022-2024 (Rate hike + Recovery)
   └── Compare: Is VQM consistent?

2. Sector-Neutral Test
   ├── Construct sector-matched benchmark
   └── Test: Does VQM add value beyond sector bet?

3. Liquidity Filter Test
   ├── Base: ADV > 20M THB
   ├── Test 1: ADV > 10M THB (smaller universe)
   └── Test 2: ADV > 50M THB (larger caps only)

4. Alternative Benchmarks
   ├── SET Index (market cap weighted)
   ├── SET50 (blue chips)
   └── Equal-weight SET (size neutral)
```

---

## 9. Overfitting Prevention

### 9.1 Out-of-Sample Testing

```
In-Sample (Training): 2019-2022
Out-of-Sample (Testing): 2023-2024

Rule: ไม่ปรับ parameters หลังดูผล Out-of-Sample
```

### 9.2 Cross-Validation

```
K-Fold Time Series CV:
- Split data into K blocks (e.g., K=5)
- Train on blocks 1 to k-1, test on block k
- Roll forward, repeat
- Average performance across folds

Benefit: ป้องกัน overfitting ต่อ period ใด period หนึ่ง
```

### 9.3 Model Simplicity Principle

```
"Do not add parameters unless they significantly improve performance"

Criteria:
- Adjusted R² increase
- Out-of-sample Sharpe improvement
- Economic intuition exists
```

---

## 10. Reporting Template

### 10.1 Performance Table

| Metric | VQM (Gross) | VQM (Net) | SET Index | Excess |
|--------|-------------|-----------|-----------|--------|
| **CAGR** | - | - | - | - |
| **Volatility** | - | - | - | - |
| **Sharpe** | - | - | - | - |
| **Max DD** | - | - | - | - |
| **Alpha** | - | - | - | - |
| **Hit Rate** | - | - | - | - |

### 10.2 Regime Performance Table

| Regime | VQM Return | SET Return | Excess | VQM Vol | SET Vol |
|--------|------------|------------|--------|---------|---------|
| **Bull** | - | - | - | - | - |
| **Bear** | - | - | - | - | - |
| **High Vol** | - | - | - | - | - |

### 10.3 Drawdown Analysis

```
Top 5 Drawdowns:
1. Date: DD: XX% | Recovery: XX days
2. Date: DD: XX% | Recovery: XX days
...
```

---

## 11. Implementation Checklist

- [ ] Data pipeline setup (PIT data)
- [ ] Factor calculation engine
- [ ] Scoring & ranking module
- [ ] Portfolio construction logic
- [ ] Walk-forward framework
- [ ] Performance calculation
- [ ] Statistical tests
- [ ] Regime classification
- [ ] Sensitivity tests
- [ ] Report generation

---

## 🔗 Linked References

- [[Chapter 3 - Methodology]] — ระเบียบวิธีวิจัย
- [[VQM Model - Factor Calculation Formulas]] — สูตรคำนวณ
- [[Complete Reference List]] — อ้างอิง backtesting literature

---

*Document created: 2026-04-06*
*Status: Framework Draft — Ready for implementation*
