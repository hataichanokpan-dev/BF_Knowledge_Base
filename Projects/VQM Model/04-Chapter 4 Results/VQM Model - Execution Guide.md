---
title: "VQM Model — Execution Guide"
aliases: ["VQM Execution", "คู่มือรัน VQM", "VQM Backtesting Guide"]
tags: [📁/projects, 🏷️/vqm-model, 🏷️/execution, 🏷️/backtesting, status/draft]
created: 2026-04-06
modified: 2026-04-06
type: guide
status: seedling
links:
  - "[[VQM Model - Implementation Plan]]"
  - "[[Chapter 3 - Methodology]]"
  - "[[VQM Model - Backtesting Framework]]"
---

# VQM Model — Execution Guide

> [!INFO] Phase 4: Data Collection & Backtesting
> **Objective:** Execute VQM backtest on SET data (2019-2024) and analyze results

---

## 1. Data Collection

### 1.1 Data Sources

| Data Type | Source | API/Method | Notes |
|-----------|--------|------------|-------|
| **Stock Prices** | SET, Yahoo Finance | `yfinance` | Daily OHLCV |
| **Financials** | SET Filing | Manual/Scraping | Quarterly PIT |
| **Index Data** | SET Index | `yfinance` | Benchmark |
| **Risk-free Rate** | BOT | Static/Online | 10-yr bond |

### 1.2 Data Requirements

```
Universe Filter (applied at each rebalance date):
- Market Cap > 5,000M THB
- Average Daily Volume > 20M THB
- Listed for at least 12 months
- Exclude: Insurance, REITs, Preferred shares

Expected Universe Size: ~250 stocks
```

### 1.3 Point-in-Time (PIT) Data Format

```csv
Date,Symbol,Revenue,EBITDA,NetIncome,FCF,Debt,Cash,Equity,MarketCap,...
2019-03-31,ADVANC,185000,45000,32000,28000,120000,15000,420000,520000,...
2019-03-31,AOT,65000,18000,12000,10000,25000,8000,180000,220000,...
...
```

---

## 2. Execution Steps

### Step 1: Setup Environment

```bash
# Create virtual environment
python -m venv vqm-env
source vqm-env/bin/activate  # Linux/Mac
# or
vqm-env\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt
```

### Step 2: Prepare Data

```bash
# Download price data
python src/data_loader.py --download-prices --start 2019-01-01 --end 2024-12-31

# Load financial data (manual or API)
python src/data_loader.py --load-financials --source data/raw/financials/

# Create PIT dataset
python src/data_loader.py --create-pit --output data/processed/pit_data.csv
```

### Step 3: Run Backtest

```bash
# Run full backtest
python main.py --config config.yaml --output results/backtest_2019_2024.csv

# Run with sensitivity analysis
python main.py --config config.yaml --sensitivity --output results/sensitivity/
```

### Step 4: Generate Report

```bash
# Generate performance report
python src/metrics.py --input results/backtest_2019_2024.csv --output reports/

# Generate visualizations
python notebooks/plot_results.py --input results/backtest_2019_2024.csv
```

---

## 3. Expected Output Files

```
results/
├── backtest_2019_2024.csv           # Full backtest results
├── portfolio_holdings/              # Quarterly holdings
│   ├── 2019Q1_portfolio.csv
│   ├── 2019Q2_portfolio.csv
│   └── ...
├── returns/
│   ├── daily_returns.csv
│   └── monthly_returns.csv
└── metrics/
    ├── performance_summary.csv     # Key metrics table
    ├── regime_analysis.csv          # Bull/Bear performance
    └── factor_attribution.csv       # Factor contributions
```

---

## 4. Performance Metrics to Track

### 4.1 Key Metrics (Expected Targets)

| Metric | Target | Benchmark (SET) |
|--------|--------|-----------------|
| **CAGR** | > 10% | ~5-8% |
| **Volatility** | < 20% | ~18-22% |
| **Sharpe Ratio** | > 1.0 | ~0.4-0.6 |
| **Max Drawdown** | < -25% | ~-30% (COVID) |
| **Alpha** | > 3% | 0% |
| **Hit Rate** | > 55% | 50% |

### 4.2 Regime Analysis

```
Expected VQM behavior:
- Bull markets: Outperform (momentum helps)
- Bear markets: Protect downside (quality helps)
- High volatility: Resilient (value + quality)
```

---

## 5. Validation Checks

### 5.1 Data Quality

```python
# Check for missing data
assert df.isnull().sum().sum() == 0, "Missing data detected"

# Check for look-ahead bias
assert all(df['date'] <= df['report_date']), "Look-ahead bias detected"

# Check for outliers
assert (df['fcf_yield'] > -0.5).all() & (df['fcf_yield'] < 1.0).all(), "Invalid FCF Yield"
```

### 5.2 Portfolio Constraints

```python
# Check max weight per stock
assert all(portfolio['weight'] <= 0.05), "Max weight exceeded"

# Check max weight per sector
sector_weights = portfolio.groupby('sector')['weight'].sum()
assert all(sector_weights <= 0.10), "Sector weight exceeded"

# Check portfolio size
assert 20 <= len(portfolio) <= 30, "Portfolio size out of range"
```

### 5.3 Backtesting Integrity

```python
# No future data used
assert all(training_end < test_start for ...)

# Transaction costs applied
assert costs > 0, "No transaction costs applied"

# Rebalancing frequency correct
assert len(rebalance_dates) == 24, "Wrong number of rebalances"
```

---

## 6. Troubleshooting

### 6.1 Data Issues

| Problem | Solution |
|---------|----------|
| Missing price data | Use forward fill for gaps < 5 days |
| Wrong financials | Verify PIT format (report date vs data date) |
| Invalid universe | Re-apply filters at each rebalance |

### 6.2 Calculation Issues

| Problem | Solution |
|---------|----------|
| Extreme z-scores | Use MAD-based (robust) z-score |
| Zero/negative FCF | Winsorize at 1st/99th percentile |
| Missing metrics | Use sector median for imputation |

### 6.3 Performance Issues

| Problem | Solution |
|---------|----------|
| Underperforming SET | Check factor weights, try sensitivity |
| High turnover | Increase portfolio size to 30 |
| Large drawdowns | Check value trap filtering |

---

## 7. Sample Execution Flow

```python
# main.py

import yaml
from src.data_loader import SETDataLoader
from src.factor_calculator import VQMFactorCalculator
from src.scoring import VQMScorer
from src.portfolio import VQMPortfolioConstructor
from src.backtest import VQMBacktester
from src.metrics import PerformanceMetrics

# Load configuration
with open('config.yaml') as f:
    config = yaml.safe_load(f)

# Initialize components
loader = SETDataLoader(config['data']['start_date'],
                      config['data']['end_date'])
calculator = VQMFactorCalculator()
scorer = VQMScorer(config['factors'])
constructor = VQMPortfolioConstructor(config['portfolio'])
backtester = VQMBacktester(config['backtest'])

# Load data
data = loader.load_all_data()

# Run backtest
results = backtester.run(data, calculator, scorer, constructor)

# Calculate metrics
metrics = PerformanceMetrics()
report = metrics.generate_report(
    results['vqm_returns'],
    results['set_returns'],
    config['risk_free']['rate']
)

# Save results
report.to_csv('results/performance_report.csv')
print(report)
```

---

## 8. Expected Timeline

| Step | Duration | Notes |
|------|----------|-------|
| **Data Collection** | 1-2 days | Manual effort for financials |
| **Data Cleaning** | 1 day | PIT formatting |
| **Factor Calculation** | 1-2 hours | Automated |
| **Backtesting** | 2-4 hours | 24 quarters |
| **Analysis** | 1 day | Regime, attribution |
| **Documentation** | 1 day | Write results |
| **Total** | ~1 week | From start to results |

---

## 9. Next Steps After Execution

1. **Review Results** — Compare with targets
2. **Regime Analysis** — Bull vs Bear performance
3. **Sensitivity Tests** — Vary weights, portfolio size
4. **Interpret Findings** — What drives performance?
5. **Write Chapter 4** — Results section
6. **Prepare Defense** — Key findings, Q&A prep

---

## 🔗 Linked References

- [[VQM Model - Implementation Plan]] — Python framework
- [[Chapter 3 - Methodology]] — Methodology reference
- [[VQM Model - Backtesting Framework]] — Backtesting protocol

---

*Document created: 2026-04-06*
*Status: Execution Guide — Ready to run*
