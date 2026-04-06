---
project: VQM Model
tags: [thesis, research, multi-factor, vqm, detailed-plan]
created: 2026-04-06
updated: 2026-04-06
status: planning
type: detailed-research-plan
version: 2.0
---

# VQM Model — Detailed Thesis Research Plan v2.1

> **Integrated Value-Quality-Momentum Model for Thai Stock Market**
>
> **Updated:** 2026-04-06
> **Status:** Detailed Planning Phase

---

## Table of Contents

1. [Executive Summary](#executive-summary)
2. [Research Framework](#research-framework)
3. [Detailed Chapter Breakdown](#detailed-chapter-breakdown)
4. [Methodology Specifications](#methodology-specifications)
5. [Implementation Checklist](#implementation-checklist)
6. [Timeline with Buffer](#timeline-with-buffer)
7. [Risk Management](#risk-management)

---

## Executive Summary

### Problem Statement (One Sentence)

> **"Develop a quantifiable multi-factor stock selection model for the Thai market that generates statistically significant alpha (α > 3% p.a., p < 0.05) with lower downside risk than the SET Index benchmark."**

### Why This Matters

Thai institutional investors face a critical challenge:
- **Active managers underperform** SET Index by 2-4% annually after fees
- **Single-factor approaches** (value-only, momentum-only) suffer from long drawdowns
- **No comprehensive multi-factor framework** exists for Thai market with Point-in-Time data

**This thesis fills that gap.**

### Core Hypothesis

> **H₀:** VQM Portfolio Sharpe Ratio ≤ SET Index Sharpe Ratio
> **H₁:** VQM Portfolio Sharpe Ratio > SET Index Sharpe Ratio (p < 0.05)

**How It Works:** Combining Value (45%), Quality (35%), and Momentum (20%):
1. **Value** → Undervalued stocks with margin of safety
2. **Quality** → Companies with sustainable competitive advantages
3. **Momentum** → Price trends reflecting information diffusion

### Target Market

| Parameter | Value |
|-----------|-------|
| **Market** | SET (Stock Exchange of Thailand) |
| **Period** | 2019-2024 (5 years) — covering COVID, Recovery, High-rate regimes |
| **Universe** | Stocks with ADV > 20M THB (3-month average) |
| **Portfolio Size** | 20-30 stocks |
| **Rebalancing** | Quarterly (Mar, Jun, Sep, Dec) |
| **Rebalance Day** | First working day after earnings filing + 45 days lag |
| **Constraints** | Max 5% per stock, Max 30% per sector |

### Success Goals (SMART)

| Goal | Metric | Target | Why It Matters |
|------|--------|--------|----------------|
| **G1** | Gross Alpha | > 5% p.a. | Before costs, proves model validity |
| **G2** | Net Alpha | > 3% p.a. | After costs, proves practical value |
| **G3** | Sharpe Ratio | > 1.0 | Risk-adjusted outperformance |
| **G4** | Max Drawdown | < -25% | Downside protection vs SET (-35% in 2020) |
| **G5** | Statistical Significance | p < 0.05 | Not luck, but systematic edge |

---

## Research Framework

### Research Questions (Aligned with Academic Standards)

| ID | Research Question | Null Hypothesis (H₀) | Alternative (H₁) | Measurable Outcome |
|----|-------------------|---------------------|------------------|-------------------|
| **RQ1** | Does the VQM model generate statistically significant alpha compared to the SET Index? | α = 0 | α > 0 | Alpha > 3% p.a., t-stat > 1.96 |
| **RQ2** | Does multi-factor combination outperform single-factor strategies? | Sharpe_VQM ≤ Sharpe_BestSingle | Sharpe_VQM > Sharpe_BestSingle | ΔSharpe > 0.15 |
| **RQ3** | Does the Quality factor reduce downside risk during market stress? | MaxDD_VQM ≥ MaxDD_Momentum | MaxDD_VQM < MaxDD_Momentum | ΔMaxDD < -5% |
| **RQ4** | Is the model robust across different market regimes? | Alpha differs across regimes | Alpha consistent | α > 0 in 3/4 regimes |
| **RQ5** | Does the model generate positive returns after realistic transaction costs? | NetReturn ≤ 0 | NetReturn > 0 | Net Alpha > 2% p.a. |

### Why These Three Factors?

| Factor | Weight | What It Captures | Key Metric |
|--------|--------|------------------|------------|
| **Value** | 45% | Undervaluation relative to fundamentals | FCF Yield, P/E Relative |
| **Quality** | 35% | Sustainable competitive advantage | ROIC - WACC, FCF Conversion |
| **Momentum** | 20% | Price trend persistence | 6-Month Price Return |

---

## Detailed Chapter Breakdown

### Chapter 1: Introduction

**Action Items (Checklist)**

- [ ] **1.1 Problem Statement** (1 paragraph)
  - เขียนปัญหาเป็น 1 ประโยควัดผลได้
  - ระบุ gap: ขาด multi-factor framework สำหรับ Thai market

- [ ] **1.2 Research Background** (2-3 pages)
  - [ ] Evolution of factor investing (CAPM → Fama-French → Multi-factor)
  - [ ] Thai market characteristics (concentration, volatility, foreign flows)
  - [ ] Current practices among Thai institutional investors

- [ ] **1.3 Research Objectives** (SMART)
  - **O1:** Develop VQM Model for SET with quantifiable rules
  - **O2:** Achieve Alpha > 3% p.a. with Sharpe > 1.0
  - **O3:** Demonstrate Max DD < -25% through full cycle
  - **O4:** Validate robustness across 3+ market regimes

- [ ] **1.4 Scope & Boundaries**
  - **In Scope:** SET main board, 2019-2024, Thai-listed companies only
  - **Out of Scope:** mai (Market for Alternative Investment), Preferred shares, ETFs, Derivatives
  - **Data Constraints:** Use only publicly available data (Bloomberg, SETSMART, Financials)

- [ ] **1.5 Expected Contributions**
  - **Academic:** First comprehensive VQM study on Thai market with PIT data
  - **Practical:** Actionable stock selection framework for Thai investors
  - **Methodological:** Demonstrates regime-aware factor weighting

---

### Chapter 2: Literature Review

**Action Items (Checklist)**

- [ ] **2.1 Value Investing Literature**
  - [ ] Graham & Dodd (1934) — Security Analysis principles
  - [ ] Fama & French (1992, 1993, 2015) — Value factor definition
  - [ ] Lakonishok et al. (1994) — Contrarian investment
  - [ ] **Thai-specific:** [Search for SET value studies]

- [ ] **2.2 Quality Factor Literature**
  - [ ] Novy-Marx (2013) — Gross profitability premium
  - [ ] Piotroski (2000) — F-score methodology
  - [ ] Quality definitions: ROIC, FCF conversion, earnings quality

- [ ] **2.3 Momentum Literature**
  - [ ] Jegadeesh & Titman (1993, 2001) — Momentum definitions
  - [ ] emerging markets evidence
  - [ ] **Thai-specific:** [Search for SET momentum studies]

- [ ] **2.4 Multi-Factor Models**
  - [ ] Fama-French 3-factor, 5-factor models
  - [ ] Barra risk model methodology
  - [ ] Factor interaction and correlation studies
  - [ ] Optimal factor combination research

- [ ] **2.5 Market Regime Literature**
  - [ ] Bull/Bear market definitions
  - [ ] VIX/VSET as regime indicators
  - [ ] Sector rotation across regimes

- [ ] **2.6 Gap Analysis Table**

| Area | Existing Research | Gap | This Study Addresses |
|------|------------------|-----|---------------------|
| Thai VQM | Limited | No comprehensive PIT study | ✓ Full PIT backtest |
| Regime analysis | US-focused | No Thai regime study | ✓ 3-regime analysis |
| Transaction costs | Often ignored | Unrealistic assumptions | ✓ 35 bps cost model |
| Practicality | Academic focus | Not investor-friendly | ✓ Implementation guide |

- [ ] **2.7 Conceptual Framework**
  - Draw input → model → output diagram
  - Define factor interactions
  - Specify portfolio construction logic

---

### Chapter 3: Methodology

**Action Items (Checklist)**

- [ ] **3.1 Data Collection & Governance**

  **Data Sources:**
  - [ ] Primary: [TBD — Bloomberg / SETSMART / Datastream]
  - [ ] Backup: P/E, P/B from company filings
  - [ ] Price: Daily close from SET
  - [ ] Corporate actions: Splits, dividends, delistings

  **Data Governance:**
  - [ ] Point-in-Time (PIT) fundamental data
  - [ ] Lag rule: Use earnings 45 days after fiscal year-end
  - [ ] Include delisted stocks (no survivorship bias)
  - [ ] Handle missing data: Exclude if > 20% missing
  - [ ] Outlier treatment: Winsorize at 1%/99%

- [ ] **3.2 Factor Definitions (Exact Formulas)**

  **Value Factors (45%):**
  ```
  FCF Yield = Free Cash Flow / Enterprise Value
  P/E Relative = (P/E) / Median(P/E, Sector)
  P/B Relative = (P/B) / Median(P/B, Sector)
  EV/EBITDA = Enterprise Value / EBITDA
  ```
  - [ ] Implement FCF Yield calculation
  - [ ] Implement sector-relative P/E, P/B
  - [ ] Implement EV/EBITDA (exclude Financials)

  **Quality Factors (35%):**
  ```
  ROIC - WACC = (NOPAT / Invested Capital) - WACC
  FCF Conversion = Free Cash Flow / Net Income
  Debt/EBITDA = Total Debt / EBITDA
  Gross Margin Trend = (GM_t - GM_t-1) / GM_t-1
  ```
  - [ ] Implement ROIC calculation
  - [ ] Estimate WACC per company (CAPM + CRP)
  - [ ] Implement FCF Conversion (exclude negative NI)
  - [ ] Calculate Debt/EBITDA

  **Momentum Factors (20%):**
  ```
  Price 6M = (Price_t / Price_t-126) - 1
  Earnings Revision = (Estimate_t - Estimate_t-1) / |Price|
  Volume Trend = Volume_MA(20) / Volume_MA(60)
  ```
  - [ ] Implement 6-month price momentum
  - [ ] Get analyst estimate revisions (if available)
  - [ ] Implement volume trend indicator

- [ ] **3.3 Factor Scoring & Normalization**

  **Normalization:**
  ```
  1. Cross-sectional ranking within universe
  2. Convert to percentile (0-100)
  3. Winsorize at 5th/95th percentile
  4. Alternative: Robust Z-score with ±3 clip
  ```
  - [ ] Implement ranking method
  - [ ] Implement winsorization
  - [ ] Verify distributions (check for skewness)

  **Composite Score:**
  ```
  VQM_Score = 0.45 × Rank(Value) + 0.35 × Rank(Quality) + 0.20 × Rank(Momentum)
  ```
  - [ ] Implement weighted scoring
  - [ ] Add tie-breaker: Use smallest market cap first

- [ ] **3.4 Portfolio Construction**

  **Selection Rules:**
  - [ ] Filter: ADV > 20M THB (3-month avg)
  - [ ] Rank all stocks by VQM_Score
  - [ ] Select Top 20-30 stocks
  - [ ] Apply constraints

  **Weighting Scheme:**
  ```
  Option A: Equal-weight (simpler, more robust)
  Option B: Score-weighted (higher score = higher weight)

  Default: Equal-weight with max 5% per stock
  ```
  - [ ] Implement equal-weighting
  - [ ] Apply position limits (5% max per stock)
  - [ ] Apply sector limits (30% max per sector)

  **Rebalancing Rules:**
  - [ ] Frequency: Quarterly (Mar 31, Jun 30, Sep 30, Dec 31)
  - [ ] Execution: First trading day + 45 days lag
  - [ ] Rebalance threshold: Only trade if weight deviation > 2%
  - [ ] Turnover cap: Max 50% portfolio turnover per quarter

- [ ] **3.5 Backtesting Framework**

  **Benchmark Specification:**
  - [ ] Primary: SET Index Total Return
  - [ ] Secondary: SET50 Index Total Return
  - [ ] Control: Equal-weight universe

  **Cost Model:**
  ```
  Commission: 0.15% (Thai standard)
  Slippage: 0.10% (estimated)
  Market Impact: 0.10% (for larger trades)
  Total: ~0.35% per trade (0.70% round-trip)
  ```
  - [ ] Implement 35 bps one-way cost
  - [ ] Adjust for liquidity (higher cost for low ADV stocks)

  **Backtest Protocol:**
  - [ ] No look-ahead: Use only data available at rebalance date
  - [ ] Include delisted stocks (handle -100% returns correctly)
  - [ ] Reinvest dividends
  - [ ] Log all trades for analysis

- [ ] **3.6 Statistical Testing**

  **Performance Metrics:**
  ```
  - CAGR (Compound Annual Growth Rate)
  - Volatility (annualized standard deviation)
  - Sharpe Ratio = (R - Rf) / σ
  - Sortino Ratio = (R - Rf) / σ_downside
  - Max Drawdown
  - Calmar Ratio = CAGR / |Max DD|
  - Alpha (vs SET)
  - Beta
  - Information Ratio = Alpha / Tracking Error
  - Hit Rate (% of positive months)
  - Turnover (% of portfolio traded per year)
  ```

  **Statistical Tests:**
  - [ ] t-test for alpha significance
  - [ ] Bootstrap confidence intervals for Sharpe
  - [ ] Factor regression (expose to Fama-French factors)
  - [ ] Granger causality test (if exploring lead-lag)

---

### Chapter 4: Results

**Action Items (Checklist)**

- [ ] **4.1 Descriptive Statistics**
  - [ ] Factor distribution histograms
  - [ ] Correlation matrix (Value vs Quality vs Momentum)
  - [ ] Sector allocation over time
  - [ ] Portfolio turnover analysis

- [ ] **4.2 Performance Analysis**

  **Cumulative Returns:**
  - [ ] Plot VQM vs SET vs Single-factors
  - [ ] Log-scale chart for clarity
  - [ ] Mark key events (COVID crash, recovery, rate hikes)

  **Annual Performance:**
  ```
  | Year | VQM | SET | Alpha |
  |------|-----|-----|-------|
  | 2019 |     |     |       |
  | 2020 |     |     |       |
  | 2021 |     |     |       |
  | 2022 |     |     |       |
  | 2023 |     |     |       |
  | 2024 |     |     |       |
  ```
  - [ ] Calculate yearly returns
  - [ ] Calculate yearly alpha

  **Risk-Adjusted Metrics:**
  ```
  | Metric | VQM | SET | Best Single-Factor |
  |--------|-----|-----|-------------------|
  | CAGR   |     |     |                   |
  | Vol    |     |     |                   |
  | Sharpe |     |     |                   |
  | Max DD |     |     |                   |
  ```
  - [ ] Calculate all metrics
  - [ ] Perform t-tests

- [ ] **4.3 Regime Analysis**

  **Regime Definition:**
  ```
  Bull: SET > 0% in trailing 6 months
  Bear: SET < -10% in trailing 6 months
  Neutral: Between Bull and Bear
  ```
  - [ ] Identify regime periods
  - [ ] Calculate regime-specific returns

  **Expected Regimes (2019-2024):**
  - 2019 H1: Pre-COVID (Bull)
  - 2020 Q1-Q2: COVID crash (Bear)
  - 2020 Q3-2021: Recovery (Bull)
  - 2022: Rate hike concerns (Neutral)
  - 2023-2024: [Depends on market conditions]

- [ ] **4.4 Factor Attribution**
  - [ ] Decompose returns by factor contribution
  - [ ] Analyze factor timing (when each factor added value)
  - [ ] Correlation heatmap by year

- [ ] **4.5 Sensitivity Analysis**

  **Weight Sensitivity:**
  ```
  | Scenario | Value | Quality | Momentum | Sharpe |
  |----------|-------|---------|----------|--------|
  | Baseline | 45%   | 35%     | 20%      |        |
  | Alt 1    | 50%   | 30%     | 20%      |        |
  | Alt 2    | 40%   | 40%     | 20%      |        |
  | Alt 3    | 40%   | 35%     | 25%      |        |
  ```
  - [ ] Run backtests for alternative weights
  - [ ] Compare Sharpe ratios

  **Parameter Sensitivity:**
  - [ ] Portfolio size: 15, 20, 25, 30, 40 stocks
  - [ ] Rebalancing: Monthly, Quarterly, Semi-annual
  - [ ] Universe: ADV > 10M, 20M, 50M THB

- [ ] **4.6 Practical Feasibility**

  **Capacity Analysis:**
  - [ ] Calculate average trade size vs ADV
  - [ ] Estimate market impact at different scales
  - [ ] Determine max AUM before significant slippage

  **Transaction Cost Impact:**
  ```
  | Cost Assumption | Gross Return | Net Return | Delta |
  |-----------------|--------------|------------|-------|
  | 0%              |              |            |       |
  | 0.35%           |              |            |       |
  | 0.70%           |              |            |       |
  ```
  - [ ] Calculate returns at different cost levels

- [ ] **4.7 Negative Findings**
  - [ ] Report periods where VQM underperformed
  - [ ] Analyze reasons (regime mismatch, factor rotation)
  - [ ] Discuss limitations honestly

---

### Chapter 5: Conclusion

**Action Items (Checklist)**

- [ ] **5.1 Summary of Findings**
  - [ ] Answer each Research Question with evidence
  - [ ] Accept/reject each Hypothesis with statistics
  - [ ] One-page executive summary table

- [ ] **5.2 Academic Implications**
  - [ ] Contribution to factor investing literature
  - [ ] Insights on Thai market efficiency
  - [ ] Methodological contributions (PIT, regime analysis)

- [ ] **5.3 Practical Implications**
  - [ ] How Thai investors can implement VQM
  - [ ] Required resources (data, tools)
  - [ ] Expected performance range (with confidence intervals)

- [ ] **5.4 Limitations**
  - [ ] Sample size (5 years, one market)
  - [ ] Data constraints (analyst estimates availability)
  - [ ] Model assumptions (static weights, linear combination)
  - [ ] Transaction cost estimation uncertainty

- [ ] **5.5 Future Research**
  - [ ] Dynamic factor weighting based on regimes
  - [ ] Machine learning enhancement (non-linear relationships)
  - [ ] Cross-market validation (ASEAN, emerging markets)
  - [ ] Inclusion of ESG factors
  - [ ] Short-side implementation

---

## Methodology Specifications

### Data Requirements

| Data Type | Source | Frequency | History Required |
|-----------|--------|-----------|------------------|
| Price | SET | Daily | 2018-2019 (pre-period) |
| Volume | SET | Daily | 2018-2019 |
| Fundamentals | Bloomberg/SETSMART | Quarterly | 2018-2024 |
| Corporate Actions | SET | Event-driven | 2019-2024 |
| Sector Classification | SET | Static/Updates | 2019-2024 |
| Risk-free Rate | BOT | Monthly | 2019-2024 |

### Technical Specifications

**Programming Environment:**
- Language: Python 3.12+
- Core Libraries: pandas, numpy, scipy, statsmodels
- Backtesting: [vectorbt / backtrader / custom]
- Visualization: matplotlib, seaborn, plotly
- Data Storage: DuckDB + Parquet files

**Computational Requirements:**
- Memory: 16GB+ recommended
- Storage: 10GB+ for data
- Processing: Single-core sufficient (backtest is parallelizable)

---

## Implementation Checklist

### Phase 0: Setup (Week 1-2)

- [ ] Set up development environment
  - [ ] Install Python + required packages
  - [ ] Set up Git repository
  - [ ] Create project structure
- [ ] Secure data access
  - [ ] Bloomberg API / SETSMART account
  - [ ] Download historical data
  - [ ] Validate data quality
- [ ] Define baseline parameters
  - [ ] Lock factor definitions
  - [ ] Lock portfolio rules
  - [ ] Lock backtest assumptions

### Phase 1: Data & Factors (Week 3-7)

- [ ] **Week 3-4: Data Pipeline**
  - [ ] Build data ingestion script
  - [ ] Implement PIT data logic
  - [ ] Handle corporate actions
  - [ ] Create data quality checks

- [ ] **Week 5-6: Factor Engine**
  - [ ] Implement all 10 factors
  - [ ] Create factor scoring function
  - [ ] Build composite score calculator
  - [ ] Test factor distributions

- [ ] **Week 7: Portfolio Construction**
  - [ ] Implement stock selection logic
  - [ ] Build rebalance engine
  - [ ] Apply constraints
  - [ ] Test with sample data

### Phase 2: Backtesting (Week 8-11)

- [ ] **Week 8: Base Backtest**
  - [ ] Run 2019-2024 backtest
  - [ ] Generate performance metrics
  - [ ] Create baseline visualizations

- [ ] **Week 9: Regime Analysis**
  - [ ] Identify regime periods
  - [ ] Calculate regime-specific returns
  - [ ] Compare across regimes

- [ ] **Week 10: Sensitivity Tests**
  - [ ] Weight variations
  - [ ] Parameter variations
  - [ ] Cost sensitivity

- [ ] **Week 11: Statistical Analysis**
  - [ ] t-tests for alpha
  - [ ] Sharpe confidence intervals
  - [ ] Factor regression

### Phase 3: Writing (Week 12-16)

- [ ] **Week 12:** Draft Chapters 1-2
- [ ] **Week 13-14:** Complete Chapter 3
- [ ] **Week 15:** Complete Chapter 4
- [ ] **Week 16:** Complete Chapter 5

### Phase 4: Revision (Week 17-20)

- [ ] **Week 17-18:** Advisor feedback incorporation
- [ ] **Week 19:** Final polish
- [ ] **Week 20:** Defense preparation

---

## Timeline with Buffer

### Summary Timeline

| Phase | Duration | Buffer | Total |
|-------|----------|--------|-------|
| Setup | 2 weeks | 0 | 2 weeks |
| Data & Factors | 5 weeks | 1 | 6 weeks |
| Backtesting | 4 weeks | 1 | 5 weeks |
| Writing | 5 weeks | 2 | 7 weeks |
| Revision | 4 weeks | 2 | 6 weeks |
| **Total** | **20 weeks** | **6 weeks** | **26 weeks (~6 months)** |

### Detailed Gantt Chart

```
Week:  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26
Setup  ████
Data               ██████████████
Backtest                           ██████████████
Writing                                        ████████████████████████
Revision                                                          ████████████████████████
Buffer                                                              ████ ████ ████ ████ ████ ████
```

### Milestones

| Week | Milestone | Deliverable |
|------|-----------|-------------|
| 2 | Environment ready | Running code skeleton |
| 7 | Factor engine complete | All factors calculated |
| 11 | Backtest complete | Full results report |
| 16 | First draft complete | Full thesis draft |
| 20 | Revision complete | Defense-ready thesis |

---

## Risk Management

### Project Risks

| Risk | Probability | Impact | Mitigation |
|------|-------------|--------|------------|
| Data access issues | Medium | High | Have backup data sources |
| Factor implementation bugs | High | Medium | Extensive unit testing |
| Insufficient alpha | Medium | High | Have alternative factor combinations |
| Timeline overrun | High | Medium | Built-in buffer weeks |
| Advisor rejection of approach | Low | High | Early validation of methodology |

### Model Risks

| Risk | Description | Mitigation |
|------|-------------|------------|
| Look-ahead bias | Using future data | Strict PIT enforcement |
| Survivorship bias | Excluding delisted stocks | Include all historical stocks |
| Overfitting | Too many parameters | Simple baseline, robustness tests |
| Data mining | Testing many combinations | Pre-specify hypotheses |
| Implementation gap | Paper returns not achievable | Conservative cost assumptions |

---

## Success Criteria

### Must-Have (Non-negotiable)

- [ ] Alpha > 0 with p < 0.05
- [ ] Sharpe ratio > SET Sharpe
- [ ] Complete 5-year backtest
- [ ] Chapter 3 methodology reproducible
- [ ] All hypotheses tested

### Nice-to-Have

- [ ] Alpha > 3% p.a.
- [ ] Sharpe > 1.0
- [ ] Max DD < -20%
- [ ] Hit rate > 60%
- [ ] Publication-worthy results

---

## Appendix

### A. Factor Formulas Reference

[Detailed mathematical formulas for each factor]

### B. Data Dictionary

[Field names, types, sources for all data]

### C. Code Repository Structure

```
vqm-model/
├── data/
│   ├── raw/
│   ├── processed/
│   └── pit/
├── src/
│   ├── factors.py
│   ├── scoring.py
│   ├── portfolio.py
│   ├── backtest.py
│   └── metrics.py
├── notebooks/
│   ├── 01_exploration.ipynb
│   ├── 02_factors.ipynb
│   └── 03_backtest.ipynb
├── tests/
├── figures/
└── thesis/
    └── chapters/
```

---

*Document Version: 2.1*
*Last Updated: 2026-04-06*
*Next Review: After Phase 1 completion*

---

## Change Log

| Date | Version | Changes |
|------|---------|---------|
| 2026-04-06 | 2.1 | Improved clarity: added SMART success goals, simplified research framework, clearer problem statement |
| 2026-04-06 | 2.0 | Added detailed chapter checklists, specifications, timeline after Codex/Gemini review |
| 2026-04-06 | 1.0 | Initial version from team meeting |
