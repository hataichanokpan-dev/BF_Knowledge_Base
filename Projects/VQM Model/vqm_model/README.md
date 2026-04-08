# VQM Model — Python Implementation

> **Integrated Value-Quality-Momentum Model for Thai Stock Market**
>
> **Version:** 1.0.0
> **Python:** 3.10+

---

## Project Overview

VQM Model is a multi-factor stock selection model combining:
- **Value (45%)**: FCF Yield, P/B Ratio, P/E Ratio
- **Quality (35%)**: ROIC-WACC Spread, FCF Conversion, Debt/EBITDA
- **Momentum (20%)**: 6-Month Price Momentum, Volume Trend

---

## Project Structure

```
vqm_model/
├── data/
│   ├── raw/           # Raw data from SET/Bloomberg
│   ├── processed/     # Processed PIT data
│   └── external/      # Benchmark data (SET Index)
├── src/
│   ├── __init__.py
│   ├── data_loader.py     # Load and clean data
│   ├── factors.py         # Calculate VQM factors
│   ├── portfolio.py       # Portfolio construction
│   └── backtest.py        # Walk-forward backtesting
├── notebooks/
│   └── 00_exploration.ipynb
├── tests/
│   └── test_factors.py
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Create Virtual Environment

```bash
# Windows (PowerShell)
python -m venv venv
.\venv\Scripts\activate

# Windows (Git Bash)
python -m venv venv
source venv/Scripts/activate
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### 1. Data Preparation

```python
from src.data_loader import SETDataLoader

# Load price data
loader = SETDataLoader()
prices = loader.load_prices(start_date="2017-01-01", end_date="2024-12-31")

# Load financial statements
financials = loader.load_financials()
```

### 2. Calculate VQM Factors

```python
from src.factors import VQMFactors

# Calculate factors
vqm = VQMFactors()
factors = vqm.calculate_all(prices, financials)

# Get composite scores
scores = vqm.composite_score(factors)
```

### 3. Backtesting

```python
from src.backtest import WalkForwardBacktest

# Run backtest
backtest = WalkForwardBacktest(
    training_period=24,  # months
    test_period=3,       # months
    rebalance="quarterly"
)

results = backtest.run(
    prices=prices,
    factors=factors,
    start_date="2019-01-01",
    end_date="2024-12-31"
)

# Performance summary
print(results.summary())
```

---

## Factor Formulas

### Value Factors (45%)

| Factor | Formula | Direction |
|--------|---------|-----------|
| FCF Yield | FCF / Enterprise Value | Higher is better |
| P/B Ratio | Price / Book Value | Lower is better |
| P/E Ratio | Price / Earnings | Lower is better |

### Quality Factors (35%)

| Factor | Formula | Direction |
|--------|---------|-----------|
| ROIC-WACC | ROIC - WACC | Higher is better |
| FCF Conversion | FCF / Net Income | Higher is better |
| Debt/EBITDA | Total Debt / EBITDA | Lower is better |

### Momentum Factors (20%)

| Factor | Formula | Direction |
|--------|---------|-----------|
| Price 6M | (P_t / P_t-6) - 1 | Higher is better |
| Volume Trend | Vol_MA(20) / Vol_MA(60) | Higher is better |

---

## Backtest Parameters

| Parameter | Value |
|-----------|-------|
| Period | 2019-2024 |
| Rebalancing | Quarterly |
| Training Window | 24 months |
| Test Window | 3 months |
| Transaction Cost | 0.50% round-trip |
| Portfolio Size | Top 30 stocks |

---

## Output

### Performance Metrics

- CAGR (Compound Annual Growth Rate)
- Alpha (vs SET Index)
- Sharpe Ratio
- Sortino Ratio
- Max Drawdown
- Hit Rate

### Files Generated

```
data/processed/
├── vqm_scores.csv        # Monthly VQM scores
├── portfolio_returns.csv # Portfolio returns
└── backtest_results.pkl  # Full backtest results
```

---

## Testing

```bash
# Run all tests
pytest tests/

# Run with coverage
pytest --cov=src tests/
```

---

## References

- Fama, E. F., & French, K. R. (2015). A five-factor asset pricing model.
- Asness, C. S., et al. (2013). Value and momentum everywhere.
- Lopez de Prado, M. (2020). Advances in financial machine learning.

---

## License

MIT License

---

*Created: 2026-04-06*
*Status: Development Phase*
