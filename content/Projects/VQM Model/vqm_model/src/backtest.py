"""
Walk-Forward Backtesting Engine

Module for backtesting the VQM Model using walk-forward analysis.

Reference: Backtesting Framework.md
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
from dataclasses import dataclass


@dataclass
class BacktestConfig:
    """Configuration for walk-forward backtest."""

    training_period: int = 24  # months
    test_period: int = 3  # months
    rebalance_frequency: str = "quarterly"  # monthly, quarterly
    transaction_cost: float = 0.0050  # 0.50% round-trip
    portfolio_size: int = 30  # number of stocks
    max_weight_per_stock: float = 0.05  # 5%
    max_weight_per_sector: float = 0.10  # 10%


@dataclass
class BacktestResults:
    """Results from backtesting."""

    returns: pd.Series
    portfolio_weights: pd.DataFrame
    metrics: Dict[str, float]
    drawdowns: pd.Series
    regime_performance: Dict[str, float]


class WalkForwardBacktest:
    """
    Walk-forward backtesting for VQM Model.

    Process:
    1. Train: Calculate VQM scores using N months of data
    2. Test: Hold top M stocks for T months
    3. Roll: Move forward and repeat
    """

    def __init__(self, config: BacktestConfig = None):
        self.config = config or BacktestConfig()
        self.results = None

    def run(
        self,
        vqm_scores: pd.DataFrame,
        prices: pd.DataFrame,
        benchmark: pd.Series = None,
        start_date: str = "2019-01-01",
        end_date: str = "2024-12-31",
    ) -> BacktestResults:
        """
        Run walk-forward backtest.

        Args:
            vqm_scores: VQM composite scores (index: dates, columns: tickers)
            prices: Price data for returns calculation
            benchmark: Benchmark returns (e.g., SET Index)
            start_date: Backtest start date
            end_date: Backtest end date

        Returns:
            BacktestResults object
        """
        # Initialize
        dates = pd.date_range(start=start_date, end=end_date, freq="M")
        portfolio_returns = pd.Series(index=dates, dtype=float)
        portfolio_weights = pd.DataFrame(index=dates, columns=prices.columns)

        # Walk-forward loop
        for i, test_date in enumerate(dates):
            # Training period (lookback)
            train_start = test_date - pd.DateOffset(months=self.config.training_period)
            train_end = test_date - pd.DateOffset(months=1)

            # Get training scores
            train_scores = vqm_scores.loc[train_start:train_end]

            if len(train_scores) == 0:
                continue

            # Use latest available scores
            latest_scores = train_scores.iloc[-1]

            # Select top stocks
            top_stocks = self._select_top_stocks(latest_scores)

            # Calculate test period returns
            test_end = test_date + pd.DateOffset(months=self.config.test_period)
            test_prices = prices.loc[test_date:test_end]

            if len(test_prices) < 2:
                continue

            # Calculate returns
            stock_returns = test_prices[top_stocks].pct_change().dropna()

            # Equal-weight portfolio
            if len(stock_returns) > 0:
                port_return = stock_returns.mean(axis=1).sum()
                port_return -= self.config.transaction_cost  # Apply transaction costs

                if test_date in portfolio_returns.index:
                    portfolio_returns[test_date] = port_return

                # Record weights
                portfolio_weights.loc[test_date, top_stocks] = 1.0 / len(top_stocks)

        # Calculate metrics
        metrics = self._calculate_metrics(portfolio_returns, benchmark)

        # Calculate drawdowns
        drawdowns = self._calculate_drawdowns(portfolio_returns)

        # Regime analysis
        regime_performance = self._analyze_regimes(
            portfolio_returns, benchmark
        )

        self.results = BacktestResults(
            returns=portfolio_returns,
            portfolio_weights=portfolio_weights,
            metrics=metrics,
            drawdowns=drawdowns,
            regime_performance=regime_performance,
        )

        return self.results

    def _select_top_stocks(
        self,
        scores: pd.Series,
    ) -> List[str]:
        """Select top N stocks by VQM score."""
        # Drop NaN values
        valid_scores = scores.dropna()

        # Sort descending and get top N
        top_stocks = valid_scores.nlargest(self.config.portfolio_size).index.tolist()

        return top_stocks

    def _calculate_metrics(
        self,
        returns: pd.Series,
        benchmark: pd.Series = None,
    ) -> Dict[str, float]:
        """Calculate performance metrics."""
        if len(returns) == 0:
            return {}

        metrics = {}

        # Basic returns
        metrics["total_return"] = (1 + returns).prod() - 1
        metrics["annual_return"] = (1 + returns).mean() * 12

        # Volatility
        metrics["volatility"] = returns.std() * np.sqrt(12)

        # Sharpe Ratio (assume 3% risk-free rate)
        rf = 0.03
        metrics["sharpe_ratio"] = (metrics["annual_return"] - rf) / metrics["volatility"]

        # Sortino Ratio
        downside_returns = returns[returns < 0]
        if len(downside_returns) > 0:
            downside_dev = downside_returns.std() * np.sqrt(12)
            metrics["sortino_ratio"] = (metrics["annual_return"] - rf) / downside_dev

        # Alpha vs Benchmark
        if benchmark is not None and len(benchmark) > 0:
            # Align benchmark with portfolio returns
            aligned_bench = benchmark.loc[returns.index]
            bench_annual_return = aligned_bench.mean() * 12
            metrics["alpha"] = metrics["annual_return"] - bench_annual_return

            # Beta
            cov_matrix = np.cov(returns, aligned_bench)
            beta = cov_matrix[0, 1] / cov_matrix[1, 1]
            metrics["beta"] = beta

        # Max Drawdown
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdown = (cumulative - running_max) / running_max
        metrics["max_drawdown"] = drawdown.min()

        # Hit Rate
        metrics["hit_rate"] = (returns > 0).sum() / len(returns)

        return metrics

    def _calculate_drawdowns(
        self,
        returns: pd.Series,
    ) -> pd.Series:
        """Calculate drawdown series."""
        cumulative = (1 + returns).cumprod()
        running_max = cumulative.expanding().max()
        drawdowns = (cumulative - running_max) / running_max

        return drawdowns

    def _analyze_regimes(
        self,
        returns: pd.Series,
        benchmark: pd.Series = None,
    ) -> Dict[str, float]:
        """Analyze performance across market regimes."""
        regimes = {}

        if benchmark is None:
            return regimes

        # Define regimes based on benchmark returns
        aligned_bench = benchmark.loc[returns.index]

        # Bull market: benchmark > 10% annualized
        bull_mask = aligned_bench > 0.10 / 12
        if bull_mask.sum() > 0:
            regimes["bull_market"] = returns[bull_mask].mean() * 12

        # Bear market: benchmark < -10% annualized
        bear_mask = aligned_bench < -0.10 / 12
        if bear_mask.sum() > 0:
            regimes["bear_market"] = returns[bear_mask].mean() * 12

        # High volatility: benchmark std > 15% annualized
        bench_vol = aligned_bench.rolling(12).std()
        high_vol_mask = bench_vol > 0.15 / np.sqrt(12)
        if high_vol_mask.sum() > 0:
            regimes["high_volatility"] = returns[high_vol_mask].mean() * 12

        return regimes

    def summary(self) -> str:
        """Generate backtest summary report."""
        if self.results is None:
            return "No backtest results available."

        r = self.results
        output = []

        output.append("=" * 60)
        output.append("VQM MODEL BACKTEST RESULTS")
        output.append("=" * 60)
        output.append("")

        output.append("PERFORMANCE METRICS")
        output.append("-" * 40)
        for key, value in r.metrics.items():
            if isinstance(value, float):
                output.append(f"{key:20s}: {value:10.2%}")
        output.append("")

        output.append("REGIME ANALYSIS")
        output.append("-" * 40)
        for regime, value in r.regime_performance.items():
            output.append(f"{regime:20s}: {value:10.2%}")
        output.append("")

        output.append("=" * 60)

        return "\n".join(output)


def main():
    """Example usage."""
    # This would be replaced with actual data loading
    print("VQM Model Backtesting Engine")
    print("Load data and run backtest using WalkForwardBacktest class")


if __name__ == "__main__":
    main()
