---
title: "VQM Model — Implementation Plan"
aliases: ["VQM Implementation", "แผนพัฒนา VQM", "VQM Python Implementation"]
tags: [📁/projects, 🏷️/vqm-model, 🏷️/implementation, 🏷️/python, status/draft]
created: 2026-04-06
modified: 2026-04-06
type: plan
status: seedling
links:
  - "[[Chapter 3 - Methodology]]"
  - "[[VQM Model - Factor Calculation Formulas]]"
  - "[[VQM Model - Backtesting Framework]]"
---

# VQM Model — Implementation Plan

> [!INFO] Phase 3: Data Collection & Implementation
> **Objective:** Build working VQM Model with Python, backtest 2019-2024, generate results

---

## 1. Project Structure

```
vqm-model/
├── data/
│   ├── raw/                    # Raw data from SET/Bloomberg
│   ├── processed/              # Cleaned, PIT data
│   └── external/               # Benchmark indices, risk-free rate
├── src/
│   ├── data_loader.py          # Data ingestion
│   ├── factor_calculator.py    # VQM factor calculations
│   ├── scoring.py              # Z-score, composite scoring
│   ├── portfolio.py            # Portfolio construction
│   ├── backtest.py             # Walk-forward testing
│   └── metrics.py              # Performance metrics
├── tests/
│   ├── test_factors.py         # Factor calculation tests
│   ├── test_scoring.py         # Scoring logic tests
│   └── test_backtest.py        # Backtesting framework tests
├── notebooks/
│   ├── 01_data_exploration.ipynb
│   ├── 02_factor_analysis.ipynb
│   └── 03_backtest_results.ipynb
├── config.yaml                 # Configuration parameters
├── requirements.txt            # Python dependencies
└── main.py                     # Entry point
```

---

## 2. Data Requirements

### 2.1 Data Sources

| Data | Source | Frequency | Notes |
|------|--------|-----------|-------|
| **Price, Volume** | SET Data, Alpha Vantage | Daily | Adjusted close |
| **Financials** | SET Filing, RapidAPI | Quarterly | PIT format |
| **Index Data** | SET Index, SET50 | Daily | Benchmark |
| **Risk-free Rate** | BOT | Daily | 10-year bond |
| **Sector Info** | SET | Static | GICS mapping |

### 2.2 API & Libraries

```python
# requirements.txt
pandas>=2.0.0
numpy>=1.24.0
yfinance>=0.2.0
requests>=2.31.0
pyyaml>=6.0
scipy>=1.11.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0
plotly>=5.17.0
openpyxl>=3.1.0
```

### 2.3 Alternative Data Sources (Free)

| Source | URL | Data Available |
|--------|-----|----------------|
| **SET Data** | set.or.th | Historical prices, financials |
| **Yahoo Finance** | finance.yahoo.com | Prices (limited Thai stocks) |
| **Alpha Vantage** | alphavantage.co | Global stock data |
| **Investing.com** | investing.com | Thai stocks, indices |
| **Thai Stock API** | (research needed) | Local data provider |

---

## 3. Implementation Phases

### Phase 3.1: Data Pipeline (Week 1-2)

```python
# src/data_loader.py

class SETDataLoader:
    """Load and process SET stock data"""

    def __init__(self, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.universe = self._load_universe()

    def _load_universe(self):
        """Load SET stock universe with filters"""
        # Criteria:
        # - Market Cap > 5B THB
        # - ADV > 20M THB
        # - Listed before start_date
        pass

    def load_price_data(self, symbols):
        """Load daily OHLCV for symbols"""
        pass

    def load_financial_data(self, symbols):
        """Load quarterly financials (PIT format)"""
        pass

    def create_pit_dataset(self):
        """Create Point-in-Time dataset"""
        pass
```

### Phase 3.2: Factor Calculator (Week 2-3)

```python
# src/factor_calculator.py

class VQMFactorCalculator:
    """Calculate VQM factors for all stocks"""

    def __init__(self, pit_data):
        self.data = pit_data

    # Value Factors
    def calculate_fcf_yield(self):
        """FCF / Enterprise Value"""
        pass

    def calculate_pe_relative(self):
        """P/E / Sector Median P/E"""
        pass

    def calculate_pb_relative(self):
        """P/B / Sector Median P/B"""
        pass

    def calculate_ev_ebitda(self):
        """EV / EBITDA"""
        pass

    # Quality Factors
    def calculate_roic_spread(self):
        """ROIC - WACC"""
        pass

    def calculate_fcf_conversion(self):
        """FCF / Net Income"""
        pass

    def calculate_debt_ebitda(self):
        """Total Debt / EBITDA"""
        pass

    def calculate_gross_margin(self):
        """Gross Profit / Revenue"""
        pass

    # Momentum Factors
    def calculate_price_6m(self):
        """(Price_t / Price_t-6M) - 1"""
        pass

    def calculate_earnings_revision(self):
        """EPS Estimate revision (3-month)"""
        pass

    def calculate_volume_trend(self):
        """Volume_MA(20) / Volume_MA(60)"""
        pass

    def calculate_all_factors(self, date):
        """Calculate all 11 factors for given date"""
        pass
```

### Phase 3.3: Scoring Engine (Week 3)

```python
# src/scoring.py

class VQMScorer:
    """Calculate VQM composite scores"""

    def __init__(self, weights={'value': 0.45, 'quality': 0.35, 'momentum': 0.20}):
        self.weights = weights

    def robust_z_score(self, series):
        """MAD-based Z-score (resistant to outliers)"""
        median = series.median()
        mad = (series - median).abs().median()
        return (series - median) / (1.4826 * mad)

    def calculate_value_score(self, factor_df):
        """Composite value score from 4 metrics"""
        # Apply robust z-score
        # Invert metrics where lower = better
        # Average the 4 z-scores
        pass

    def calculate_quality_score(self, factor_df):
        """Composite quality score from 4 metrics"""
        pass

    def calculate_momentum_score(self, factor_df):
        """Composite momentum score from 3 metrics"""
        pass

    def calculate_vqm_score(self, factor_df):
        """VQM composite score"""
        value = self.calculate_value_score(factor_df)
        quality = self.calculate_quality_score(factor_df)
        momentum = self.calculate_momentum_score(factor_df)

        return (self.weights['value'] * value +
                self.weights['quality'] * quality +
                self.weights['momentum'] * momentum)
```

### Phase 3.4: Portfolio Constructor (Week 4)

```python
# src/portfolio.py

class VQMPortfolioConstructor:
    """Construct VQM portfolios"""

    def __init__(self, n_stocks=25, max_weight=0.05, max_sector=0.10):
        self.n_stocks = n_stocks
        self.max_weight = max_weight
        self.max_sector = max_sector

    def construct_portfolio(self, scores_df, date):
        """Construct portfolio for given date"""
        # Rank by VQM score
        # Select top N stocks
        # Apply constraints (max weight, sector)
        # Return portfolio with weights
        pass

    def equal_weight(self, selected_stocks):
        """Equal-weight portfolio"""
        pass

    def score_weight(self, selected_stocks, scores):
        """Weight by VQM score"""
        pass
```

### Phase 3.5: Backtesting Engine (Week 5-6)

```python
# src/backtest.py

class VQMBacktester:
    """Walk-forward backtesting for VQM model"""

    def __init__(self, start_date, end_date, rebalance_freq='Q'):
        self.start_date = start_date
        self.end_date = end_date
        self.rebalance_freq = rebalance_freq
        self.rebalance_dates = self._generate_rebalance_schedule()

    def _generate_rebalance_schedule(self):
        """Generate quarterly rebalance dates"""
        # Quarterly: First trading day of each quarter
        pass

    def run_backtest(self, data_loader, calculator, scorer, constructor):
        """Run walk-forward backtest"""
        results = []

        for rebalance_date in self.rebalance_dates:
            # Get training period data (12 months prior)
            # Calculate factors on training data
            # Score stocks
            # Construct portfolio
            # Hold for test period (3 months)
            # Record returns

        return pd.DataFrame(results)

    def calculate_transaction_costs(self, old_portfolio, new_portfolio):
        """Calculate transaction costs (0.50% round-trip)"""
        pass

    def apply_slippage(self, trades):
        """Apply slippage model (0.15%)"""
        pass
```

### Phase 3.6: Performance Metrics (Week 6)

```python
# src/metrics.py

class PerformanceMetrics:
    """Calculate performance metrics for backtest results"""

    @staticmethod
    def total_return(returns):
        """Total cumulative return"""
        return (1 + returns).prod() - 1

    @staticmethod
    def cagr(returns, years):
        """Compound Annual Growth Rate"""
        return (1 + returns).prod() ** (1/years) - 1

    @staticmethod
    def volatility(returns):
        """Annualized volatility"""
        return returns.std() * np.sqrt(252)

    @staticmethod
    def sharpe_ratio(returns, rf_rate):
        """Sharpe Ratio"""
        excess_returns = returns - rf_rate / 252
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    @staticmethod
    def sortino_ratio(returns, rf_rate):
        """Sortino Ratio (downside deviation)"""
        excess_returns = returns - rf_rate / 252
        downside = excess_returns[excess_returns < 0]
        return excess_returns.mean() / downside.std() * np.sqrt(252)

    @staticmethod
    def max_drawdown(returns):
        """Maximum drawdown"""
        cum_returns = (1 + returns).cumprod()
        rolling_max = cum_returns.expanding().max()
        drawdown = (cum_returns - rolling_max) / rolling_max
        return drawdown.min()

    @staticmethod
    def information_ratio(returns, benchmark_returns):
        """Information Ratio"""
        excess_returns = returns - benchmark_returns
        return excess_returns.mean() / excess_returns.std() * np.sqrt(252)

    @staticmethod
    def alpha_beta(returns, benchmark_returns, rf_rate):
        """Jensen's Alpha and Beta (CAPM regression)"""
        excess_returns = returns - rf_rate / 252
        excess_benchmark = benchmark_returns - rf_rate / 252

        from scipy import stats
        beta, alpha, r_value, p_value, std_err = stats.linregress(
            excess_benchmark, excess_returns
        )

        alpha_annual = alpha * 252
        return alpha_annual, beta

    def generate_report(self, portfolio_returns, benchmark_returns, rf_rate):
        """Generate full performance report"""
        report = {
            'Total Return': self.total_return(portfolio_returns),
            'CAGR': self.cagr(portfolio_returns, len(portfolio_returns)/252),
            'Volatility': self.volatility(portfolio_returns),
            'Sharpe Ratio': self.sharpe_ratio(portfolio_returns, rf_rate),
            'Sortino Ratio': self.sortino_ratio(portfolio_returns, rf_rate),
            'Max Drawdown': self.max_drawdown(portfolio_returns),
            'Information Ratio': self.information_ratio(portfolio_returns, benchmark_returns),
            'Alpha': self.alpha_beta(portfolio_returns, benchmark_returns, rf_rate)[0],
            'Beta': self.alpha_beta(portfolio_returns, benchmark_returns, rf_rate)[1],
        }
        return pd.Series(report)
```

---

## 4. Configuration File

```yaml
# config.yaml

data:
  start_date: "2019-01-01"
  end_date: "2024-12-31"
  min_market_cap: 5000  # million THB
  min_adv: 20  # million THB
  universe_path: "data/universe/set_stocks.csv"

factors:
  value_weight: 0.45
  quality_weight: 0.35
  momentum_weight: 0.20

portfolio:
  n_stocks: 25
  max_weight_per_stock: 0.05
  max_weight_per_sector: 0.10
  weighting_method: "equal"  # equal, score_weighted

backtest:
  rebalance_frequency: "Q"  # Q=Quarterly, M=Monthly
  training_period_months: 12
  test_period_months: 3
  transaction_cost_buy: 0.0035  # 0.35%
  transaction_cost_sell: 0.0015  # 0.15%
  slippage: 0.0015  # 0.15%

risk_free:
  rate: 0.025  # 2.5% annual (BOT 10-year bond)
```

---

## 5. Testing Strategy

### 5.1 Unit Tests

```python
# tests/test_factors.py

def test_fcf_yield_calculation():
    """Test FCF Yield calculation"""
    # Create sample data
    # Calculate FCF Yield
    # Assert expected result
    pass

def test_roic_spread_calculation():
    """Test ROIC - WACC calculation"""
    pass

# tests/test_scoring.py

def test_robust_z_score():
    """Test MAD-based z-score handles outliers"""
    # Create data with outliers
    # Compare robust vs standard z-score
    pass

def test_composite_score_weights():
    """Test VQM score uses correct weights"""
    pass
```

### 5.2 Integration Tests

```python
# tests/test_backtest.py

def test_walk_forward_structure():
    """Test walk-forward has correct structure"""
    # Verify no look-ahead bias
    # Verify training period precedes test period
    pass

def test_portfolio_constraints():
    """Test portfolio respects constraints"""
    # Max 5% per stock
    # Max 10% per sector
    pass
```

---

## 6. Expected Outputs

### 6.1 Performance Tables

| Metric | VQM (Gross) | VQM (Net) | SET Index | Excess |
|--------|-------------|-----------|-----------|--------|
| CAGR | - | - | - | - |
| Volatility | - | - | - | - |
| Sharpe | - | - | - | - |
| Max DD | - | - | - | - |
| Alpha | - | - | - | - |

### 6.2 Visualizations

- Cumulative returns chart (VQM vs SET)
- Drawdown chart
- Factor performance attribution
- Regime analysis (Bull vs Bear)
- Monthly returns heatmap
- Rolling Sharpe ratio

### 6.3 Documentation

- Code documentation (docstrings)
- Methodology writeup
- Results summary
- Investment insights

---

## 7. Timeline

| Week | Tasks | Deliverables |
|------|-------|--------------|
| **1-2** | Data pipeline, API integration | Clean PIT dataset |
| **2-3** | Factor calculator | 11 factors computed |
| **3** | Scoring engine | VQM scores for all stocks |
| **4** | Portfolio constructor | Portfolio selection logic |
| **5-6** | Backtesting engine | Walk-forward results |
| **6** | Performance metrics | Full report |
| **7** | Testing, validation | QA sign-off |
| **8** | Documentation, writeup | Chapter 4 draft |

---

## 8. Next Steps

**Immediate Actions:**
1. [ ] Set up project structure
2. [ ] Identify data sources (SET, API keys)
3. [ ] Create data loader skeleton
4. [ ] Implement first factor calculator

**For Team:**
- **Codex:** Start implementation with Python
- **Gemini:** Review code for bugs/security
- **Damodaran:** Interpret results, validate methodology
- **OBB:** Document findings

---

## 🔗 Linked References

- [[Chapter 3 - Methodology]] — Methodology reference
- [[VQM Model - Factor Calculation Formulas]] — Formula reference
- [[VQM Model - Backtesting Framework]] — Backtesting protocol

---

*Document created: 2026-04-06*
*Status: Implementation Plan — Ready for coding*
