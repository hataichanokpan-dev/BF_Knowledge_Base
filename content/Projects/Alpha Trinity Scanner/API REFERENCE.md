---
tags: [finance/investing, thai-stocks, api-reference, python]
project: alpha-trinity-scanner
type: documentation
created: 2026-04-05
updated: 2026-04-05
---

# Alpha Trinity Scanner - API Reference

Complete reference for all Python modules in the project.

---

## Module Index

| Module | Lines | Purpose |
|--------|-------|---------|
| `reverse_dcf_engine.py` | 700+ | Solve implied expectations from market price |
| `gap_scorer.py` | 350+ | Calculate expectation gaps vs realistic caps |
| `macro_guardrails.py` | 650+ | 2x2 regime detection |
| `data_triangulator.py` | 280+ | Extract real financials from statements |
| `realistic_calculator.py` | 200+ | Calculate realistic capability caps |
| `implied_expectations.py` | 300+ | Decompose implied expectations |
| `risk_framework.py` | 400+ | Risk assessment & stress testing |
| `backtest_engine.py` | 400+ | Cross-sectional backtest |
| `forward_tracker.py` | 600+ | 12-24 month paper trading |
| `case_study_analyzer.py` | 450+ | Deep dive stock analysis |
| `value_watchlist.py` | 450+ | Paper trading framework |

---

## Core Modules

### reverse_dcf_engine.py

**Purpose**: Invert DCF to solve for implied growth, margin, ROIC from market price

#### Classes

```python
class ReverseDCFEngine:
    """
    Main engine for Reverse DCF calculations

    Methods:
        solve_implied_growth(market_ev, base_fcf, wacc, terminal_growth)
            Returns: (implied_growth, hit_bracket_limit)

        solve_implied_target_margin(market_ev, revenue, current_margin, ...)
            Returns: (implied_target_margin, margin_expansion_required)

        solve_implied_roic(growth, reinvestment_rate)
            Returns: implied_roic

        calculate_enterprise_value(symbol, price, shares_outstanding)
            Returns: enterprise_value

        calculate_wacc(symbol, risk_free_rate, market_risk_premium)
            Returns: wacc
    """

    def __init__(self, config: Optional[DCFConfig] = None):
        """
        Initialize with default or custom configuration

        Args:
            config: DCFConfig with risk_free_rate, market_risk_premium, etc.
        """

    def calculate_reverse_dcf(
        self,
        symbol: str,
        market_price: float,
        financials: Dict[str, float]
    ) -> ImpliedExpectations:
        """
        Main entry point for Reverse DCF calculation

        Args:
            symbol: Stock symbol
            market_price: Current market price per share
            financials: Dict with revenue, ebit, debt, cash, etc.

        Returns:
            ImpliedExpectations dataclass with:
                - implied_growth
                - implied_target_margin (if negative FCF)
                - implied_roic
                - valuation_method (single_stage vs multi_stage)
        """
```

#### Data Structures

```python
@dataclass
class DCFConfig:
    """Configuration for DCF calculations"""
    risk_free_rate: float = 0.025
    market_risk_premium: float = 0.06
    terminal_growth: float = 0.03
    growth_bracket_min: float = -0.20
    growth_bracket_max: float = 0.40

@dataclass
class ImpliedExpectations:
    """Result of Reverse DCF calculation"""
    symbol: str
    implied_growth: Optional[float]
    implied_target_margin: Optional[float]
    implied_roic: float
    valuation_method: str  # 'single_stage' or 'multi_stage'
    wacc: float
    market_ev: float
```

#### Usage Example

```python
from core.reverse_dcf_engine import ReverseDCFEngine

engine = ReverseDCFEngine()

# For normal FCF companies
result = engine.calculate_reverse_dcf(
    symbol="PTTGC",
    market_price=35.25,
    financials={
        "revenue": 684321000000,
        "ebit": 45234000000,
        "debt": 150000000000,
        "cash": 50000000000,
        "shares": 5600000000,
    }
)

print(f"Implied Growth: {result.implied_growth:.1%}")
# Output: Implied Growth: 2.0%
```

---

### gap_scorer.py

**Purpose**: Calculate expectation gaps between implied and realistic capabilities

#### Classes

```python
class GapScorer:
    """
    Calculate expectation gap scores for individual stocks

    Methods:
        calculate_gap_score(symbol: str) -> GapScore
        calculate_growth_gap(implied, realistic) -> float
        calculate_margin_gap(implied, realistic) -> float
        calculate_roic_gap(implied, realistic) -> float
        calculate_composite(growth, margin, roic) -> float
        classify_signal(composite) -> str  # 'AVOID', 'CAUTION', 'ACCEPTABLE'
    """

    # LOCKED THRESHOLDS (pre-registered)
    AVOID_THRESHOLD = 0.50
    CAUTION_THRESHOLD = 0.20
```

#### Data Structures

```python
@dataclass
class GapScore:
    """Complete gap score for a stock"""
    symbol: str

    # Gaps
    growth_gap: float      # (implied - realistic) / realistic
    margin_gap: float
    roic_gap: float
    composite_gap: float   # Weighted combination

    # Signals
    signal: str            # 'AVOID', 'CAUTION', 'ACCEPTABLE'
    signal_strength: float # How confident (0-1)

    # Components
    implied: ImpliedExpectations
    realistic: RealisticCapabilities
```

#### Usage Example

```python
from core.gap_scorer import GapScorer

scorer = GapScorer()

score = scorer.calculate_gap_score("PTTGC")

print(f"Growth Gap: {score.growth_gap:.1%}")
print(f"Composite: {score.composite_gap:.1%}")
print(f"Signal: {score.signal}")

# Output:
# Growth Gap: -83.3%  (Market expects 2%, realistic 12%)
# Composite: -66.8%
# Signal: ACCEPTABLE
```

---

### macro_guardrails.py

**Purpose**: Detect macro regime (2x2: Growth x Liquidity)

#### Classes

```python
class MacroGuardrails:
    """
    Detect current macro regime for signal adjustment

    Regimes:
        GOLDEN_LOCK: High Growth + High Liquidity
        GROWTH_SLOWDOWN: Low Growth + High Liquidity
        LIQUIDITY_CRUNCH: High Growth + Low Liquidity
        STAGFLATION: Low Growth + Low Liquidity

    Methods:
        detect_regime() -> MacroRegime
        get_growth_signals() -> GrowthRegime
        get_liquidity_signals() -> LiquidityRegime
        adjust_signals_for_regime(signals, regime) -> Dict
    """
```

#### Data Structures

```python
class MacroRegime(Enum):
    GOLDEN_LOCK = "GOLDEN_LOCK"
    GROWTH_SLOWDOWN = "GROWTH_SLOWDOWN"
    LIQUIDITY_CRUNCH = "LIQUIDITY_CRUNCH"
    STAGFLATION = "STAGFLATION"

@dataclass
class RegimeIndicators:
    """Current regime indicators"""
    growth_regime: str  # 'HIGH' or 'LOW'
    liquidity_regime: str  # 'HIGH' or 'LOW'
    regime: MacroRegime
    confidence: float  # 0-1
```

#### Usage Example

```python
from core.macro_guardrails import MacroGuardrails

guardrails = MacroGuardrails()
regime = guardrails.detect_regime()

print(f"Current Regime: {regime.regime.value}")
print(f"Confidence: {regime.confidence:.0%}")

# Adjust signals for regime
adjusted = guardrails.adjust_signals_for_regime(
    signals={'PTTGC': 'ACCEPTABLE', ...},
    regime=regime.regime
)
```

---

### data_triangulator.py

**Purpose**: Extract real financial data from Thai company statements

#### Classes

```python
class DataTriangulator:
    """
    Extract financial data from statements (not yfinance info)

    Methods:
        extract_financials(symbol: str) -> Dict
        extract_income_statement_items(symbol) -> Dict
        extract_balance_sheet_items(symbol) -> Dict
        extract_cash_flow_items(symbol) -> Dict
        validate_extracted_data(symbol, data) -> bool
    """

    # Thai-specific keywords
    REVENUE_KEYWORDS = ['revenue', 'total revenue', 'operating revenue']
    EBIT_KEYWORDS = ['ebit', 'operating income', 'operating profit']
    NET_INCOME_KEYWORDS = ['net income', 'net profit', 'profit for the year']
```

#### Usage Example

```python
from core.data_triangulator import DataTriangulator

dt = DataTriangulator()
financials = dt.extract_financials("PTTGC")

print(f"EBIT: {financials['ebit']:,.0f} THB")
print(f"Operating Margin: {financials['operating_margin']:.1%}")

# Output:
# EBIT: 45,234,100,000 THB
# Operating Margin: 6.6%
```

---

### realistic_calculator.py

**Purpose**: Calculate realistic capability caps for companies

#### Classes

```python
class RealisticCalculator:
    """
    Calculate realistic growth/margin/ROIC caps

    Methods:
        calculate_realistic_growth(symbol, financials) -> float
        calculate_realistic_margin(symbol, sector) -> float
        calculate_realistic_roic(symbol, sector) -> float
        get_sector_benchmarks(sector) -> SectorBenchmarks
    """
```

#### Data Structures

```python
@dataclass
class SectorBenchmarks:
    """Sector-specific realistic caps"""
    sector: str
    median_growth: float
    median_margin: float
    median_roic: float
    growth_std: float
    margin_std: float
```

---

### risk_framework.py

**Purpose**: Risk assessment and stress testing

#### Classes

```python
class RiskFramework:
    """
    Comprehensive risk assessment

    Methods:
        assess_portfolio_risk(portfolio, signals, ...) -> Dict[str, RiskLevel]
        _assess_signal_risk(...) -> RiskLevel
        _assess_concentration_risk(...) -> RiskLevel
        _assess_liquidity_risk(...) -> RiskLevel
        _assess_model_risk(...) -> RiskLevel
    """

class StressTester:
    """
    Stress testing framework

    Methods:
        run_stress_test(portfolio, signals, ...) -> List[StressTestResult]
        generate_risk_report(results, risks) -> str
    """
```

#### Usage Example

```python
from core.risk_framework import RiskFramework, StressTester

rf = RiskFramework()
tester = StressTester(rf)

# Assess risk
risks = rf.assess_portfolio_risk(
    portfolio={'PTTGC': 0.20, 'TRUE': 0.15, ...},
    signals={'PTTGC': 'ACCEPTABLE', ...},
    sector_mapping={'PTTGC': 'Energy', ...},
    price_data=price_df,
    volume_data=volume_df
)

# Run stress tests
results = tester.run_stress_test(
    portfolio=portfolio,
    signals=signals,
    sector_mapping=sector_mapping,
    current_prices=prices
)

# Generate report
report = tester.generate_risk_report(results, risks)
print(report)
```

---

## Validation Modules

### backtest_engine.py

**Purpose**: Cross-sectional backtest framework

#### Classes

```python
class BacktestEngine:
    """
    Cross-sectional backtest (no look-ahead bias)

    Methods:
        run() -> BacktestResult
        generate_signals(date) -> Dict
        calculate_returns(signals, start_date, end_date) -> Dict
        analyze_results() -> BacktestAnalysis
    """

class BacktestConfig:
    """Backtest configuration"""
    avoid_threshold: float = 0.50
    caution_threshold: float = 0.20
    rebalance_frequency_months: int = 1
```

### forward_tracker.py

**Purpose**: 12-24 month forward paper trading

#### Classes

```python
class ForwardPaperTrader:
    """
    Monthly forward tracking

    Methods:
        create_initial_snapshot() -> MonthlySnapshot
        take_monthly_snapshot() -> Optional[MonthlySnapshot]
        generate_report() -> str
    """

# LOCKED RULES (pre-registered)
RULES = {
    "avoid_threshold": 0.50,
    "caution_threshold": 0.20,
    "rebalance_frequency": "monthly",
}
```

#### Data Structures

```python
@dataclass
class MonthlySnapshot:
    """Portfolio state at a point in time"""
    date: pd.Timestamp
    portfolio: Dict[str, float]  # symbol -> weight
    signals: Dict[str, str]
    set_index_value: float
    portfolio_value: float
    return_since_start: float
    set_return_since_start: float
```

---

## Analysis Modules

### case_study_analyzer.py

**Purpose**: Deep dive analysis of individual stocks

#### Classes

```python
class CaseStudyAnalyzer:
    """
    Deep dive into individual stocks

    Methods:
        analyze(symbol: str) -> CaseStudyReport
        generate_breakdown(symbol) -> Dict
        compare_with_sector(symbol) -> Dict
        identify_red_flags(symbol) -> List[str]
    """
```

### value_watchlist.py

**Purpose**: Paper trading framework

#### Classes

```python
class ValueWatchlist:
    """
    Generate and maintain value watchlist

    Methods:
        generate_watchlist() -> List[str]
        update_watchlist() -> None
        get_watchlist_summary() -> Dict
    """
```

---

## Configuration

### config.py

```python
"""Global configuration for Alpha Trinity Scanner"""

# Thai Market Parameters
RISK_FREE_RATE = 0.025      # 2.5% Thai 10Y Bond
MARKET_RISK_PREMIUM = 0.06  # 6% EM Premium
TERMINAL_GROWTH = 0.03      # 3% Thailand GDP

# Signal Thresholds (LOCKED)
AVOID_THRESHOLD = 0.50
CAUTION_THRESHOLD = 0.20

# Growth Bracket
GROWTH_BRACKET_MIN = -0.20
GROWTH_BRACKET_MAX = 0.40

# Risk Limits
MAX_SECTOR_WEIGHT = 0.30
MAX_STOCK_WEIGHT = 0.10
MIN_DAILY_VOLUME = 50_000_000  # 50M THB

# Data Sources
YFINANCE_TICKER_SUFFIX = ".BK"
SET50_SYMBOLS = [
    "ADVANC", "AOT", "AWC", "BBL", "BDMS", "BEM", ...
]
```

---

## Utilities

### utils.py

```python
"""Utility functions"""

def calculate_cagr(start_value, end_value, periods):
    """Calculate Compound Annual Growth Rate"""

def calculate_wacc(
    risk_free_rate,
    beta,
    market_risk_premium,
    cost_of_debt,
    tax_rate,
    debt_ratio
):
    """Calculate Weighted Average Cost of Capital"""

def format_number(num, decimals=2):
    """Format number with thousand separators"""

def thai_baht_to_usd(amount_thb, exchange_rate):
    """Convert THB to USD"""

def is_trading_day(date):
    """Check if date is a Thai trading day"""
```

---

## Error Handling

### Custom Exceptions

```python
class ReverseDCFError(Exception):
    """Base exception for Reverse DCF errors"""

class BracketLimitError(ReverseDCFError):
    """Implied growth hit bracket limit"""

class DataValidationError(ReverseDCFError):
    """Extracted data failed validation"""

class InsufficientDataError(ReverseDCFError):
    """Not enough data for calculation"""
```

---

## Quick Start

```python
# 1. Calculate gap score for a single stock
from core.gap_scorer import GapScorer
score = GapScorer().calculate_gap_score("PTTGC")

# 2. Generate watchlist
from analysis.value_watchlist import ValueWatchlist
watchlist = ValueWatchlist().generate_watchlist()

# 3. Run forward tracking
from validation.forward_tracker import ForwardPaperTrader
tracker = ForwardPaperTrader()
snapshot = tracker.take_monthly_snapshot()

# 4. Assess portfolio risk
from core.risk_framework import RiskFramework
risks = RiskFramework().assess_portfolio_risk(...)

# 5. Run stress test
from core.risk_framework import StressTester
results = StressTester(rf).run_stress_test(...)
```

---

**Last Updated**: 2026-04-05
**Python Version**: 3.12+
**Dependencies**: yfinance, pandas, numpy
