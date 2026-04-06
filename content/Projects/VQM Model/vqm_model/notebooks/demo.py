"""
VQM Model Backtest Demonstration

Run backtest with mock data to demonstrate VQM Model performance.
"""

import sys
sys.path.append("C:/Users/bfipa/Documents/BF-Vault/Projects/VQM Model/vqm_model")

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from src.mock_data import generate_mock_data
from src.factors import VQMFactors
from src.backtest import WalkForwardBacktest, BacktestConfig

# Set style
sns.set_style("whitegrid")
plt.rcParams["figure.figsize"] = (12, 8)


def run_vqm_backtest_demo():
    """Run complete VQM backtest demonstration."""
    print("=" * 60)
    print("VQM MODEL BACKTEST DEMONSTRATION")
    print("=" * 60)
    print()

    # Step 1: Generate mock data
    print("Step 1: Generating mock SET data...")
    prices, fundamentals, volume, benchmark = generate_mock_data(
        start_date="2019-01-01",
        end_date="2024-12-31",
        seed=42
    )
    print(f"   ✅ Data loaded: {len(prices.columns)} stocks, {len(prices)} days")
    print()

    # Step 2: Calculate VQM factors
    print("Step 2: Calculating VQM factors...")
    vqm = VQMFactors()
    factors = vqm.calculate_all(prices, volume, fundamentals)
    print(f"   ✅ Factors calculated")
    print(f"   ✅ Composite VQM scores generated")
    print()

    # Step 3: Prepare monthly data for backtesting
    print("Step 3: Preparing backtest data...")
    monthly_prices = prices.resample("M").last()
    monthly_benchmark = benchmark.resample("M").pct_change().dropna()
    monthly_scores = factors["composite"].resample("M").last()
    print(f"   ✅ Monthly data prepared: {len(monthly_prices)} periods")
    print()

    # Step 4: Run backtest
    print("Step 4: Running walk-forward backtest...")
    config = BacktestConfig(
        training_period=24,
        test_period=3,
        rebalance_frequency="quarterly",
        transaction_cost=0.0050,
        portfolio_size=30,
    )

    backtest = WalkForwardBacktest(config)
    results = backtest.run(
        vqm_scores=monthly_scores,
        prices=monthly_prices,
        benchmark=monthly_benchmark,
        start_date="2019-01-01",
        end_date="2024-12-31",
    )
    print(f"   ✅ Backtest completed")
    print()

    # Step 5: Generate report
    print("Step 5: Generating performance report...")
    print()
    print(results.summary())
    print()

    # Step 6: Calculate vs benchmark
    print("=" * 60)
    print("VQM vs SET INDEX COMPARISON")
    print("=" * 60)
    print()

    # Benchmark metrics
    benchmark_return = monthly_benchmark.mean() * 12
    benchmark_vol = monthly_benchmark.std() * np.sqrt(12)

    print(f"{'Metric':<25} {'VQM Portfolio':<15} {'SET Index':<15} {'Difference':<15}")
    print("-" * 70)
    print(f"{'Annual Return':<25} {results.metrics['annual_return']:>14.2%} {benchmark_return:>14.2%} {results.metrics.get('alpha', 0):>14.2%}")
    print(f"{'Volatility':<25} {results.metrics['volatility']:>14.2%} {benchmark_vol:>14.2%} {'':>14}")
    print(f"{'Sharpe Ratio':<25} {results.metrics['sharpe_ratio']:>14.2f} {(benchmark_return - 0.03) / benchmark_vol:>14.2f} {'':>14}")
    print(f"{'Max Drawdown':<25} {results.metrics['max_drawdown']:>14.2%} {benchmark_cumsum.min():>14.2%} {'':>14}")
    print(f"{'Hit Rate':<25} {results.metrics['hit_rate']:>14.2%} {(monthly_benchmark > 0).mean():>14.2%} {'':>14}")
    print()

    # Step 7: Create visualizations
    print("Step 7: Creating visualizations...")
    create_visualizations(results, monthly_benchmark, monthly_prices)
    print(f"   ✅ Charts saved")
    print()

    # Step 8: Regime analysis
    print("=" * 60)
    print("REGIME ANALYSIS")
    print("=" * 60)
    print()
    for regime, return_val in results.regime_performance.items():
        print(f"{regime:20s}: {return_val:>10.2%}")
    print()

    return results


def create_visualizations(results, benchmark, prices):
    """Create performance visualizations."""
    # 1. Cumulative Returns Comparison
    fig, axes = plt.subplots(2, 2, figsize=(14, 10))

    # Cumulative returns
    ax1 = axes[0, 0]
    vqm_cumulative = (1 + results.returns).cumprod()
    bench_cumulative = (1 + benchmark).cumprod()

    ax1.plot(vqm_cumulative.index, vqm_cumulative.values, label="VQM Portfolio", linewidth=2)
    ax1.plot(bench_cumulative.index, bench_cumulative.values, label="SET Index", linewidth=2, linestyle="--")
    ax1.set_title("Cumulative Returns Comparison", fontsize=12, fontweight="bold")
    ax1.set_xlabel("Date")
    ax1.set_ylabel("Cumulative Return")
    ax1.legend()
    ax1.grid(True, alpha=0.3)
    ax1.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.1f}x"))

    # 2. Drawdown
    ax2 = axes[0, 1]
    ax2.fill_between(results.drawdowns.index, results.drawdowns.values, 0, alpha=0.3, color="red")
    ax2.plot(results.drawdowns.index, results.drawdowns.values, color="darkred", linewidth=1)
    ax2.set_title("VQM Portfolio Drawdown", fontsize=12, fontweight="bold")
    ax2.set_xlabel("Date")
    ax2.set_ylabel("Drawdown")
    ax2.grid(True, alpha=0.3)
    ax2.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.0%}"))

    # 3. Rolling Sharpe Ratio
    ax3 = axes[1, 0]
    rolling_sharpe = results.returns.rolling(12).apply(
        lambda x: (x.mean() * 12 - 0.03) / (x.std() * np.sqrt(12))
    )
    ax3.plot(rolling_sharpe.index, rolling_sharpe.values, linewidth=2, color="green")
    ax3.axhline(y=1.0, color="red", linestyle="--", linewidth=1, label="Target (1.0)")
    ax3.set_title("Rolling 12-Month Sharpe Ratio", fontsize=12, fontweight="bold")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Sharpe Ratio")
    ax3.legend()
    ax3.grid(True, alpha=0.3)

    # 4. Monthly Returns Distribution
    ax4 = axes[1, 1]
    ax4.hist(results.returns.values, bins=20, alpha=0.7, color="blue", edgecolor="black")
    ax4.axvline(x=results.returns.mean(), color="red", linestyle="--", linewidth=2, label=f"Mean: {results.returns.mean():.2%}")
    ax4.set_title("Monthly Returns Distribution", fontsize=12, fontweight="bold")
    ax4.set_xlabel("Monthly Return")
    ax4.set_ylabel("Frequency")
    ax4.legend()
    ax4.xaxis.set_major_formatter(plt.FuncFormatter(lambda x, p: f"{x:.0%}"))
    ax4.grid(True, alpha=0.3)

    plt.tight_layout()
    plt.savefig("C:/Users/bfipa/Documents/BF-Vault/Projects/VQM Model/04-Chapter 4 Results/vqm_performance_charts.png", dpi=150)
    plt.close()

    print("   ✅ Performance charts saved")


def calculate_benchmark_cumulative(benchmark):
    """Calculate cumulative benchmark returns."""
    return (1 + benchmark).cumprod() - 1


if __name__ == "__main__":
    # Run demonstration
    results = run_vqm_backtest_demo()

    print("=" * 60)
    print("BACKTEST COMPLETE")
    print("=" * 60)
    print()
    print("Results saved to: 04-Chapter 4 Results/")
    print()
