"""
VQM Model - Main Execution Script
Run complete VQM backtest with mock data
"""

import sys
import os
import pandas as pd
import warnings
warnings.filterwarnings('ignore')

# Add src to path
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from mock_data_generator import MockSETDataGenerator
from factor_calculator import VQMFactorCalculator, VQMScorer, calculate_all_scores
from backtest import VQMBacktester, PerformanceMetrics, regime_analysis, VQMPortfolioConstructor


def main():
    """Run complete VQM backtest"""
    print("=" * 70)
    print(" " * 15 + "VQM MODEL BACKTESTING ENGINE")
    print("=" * 70)
    print("Integrated Value-Quality-Momentum Model for SET")
    print("Period: 2019-2024 | Mock Data Demonstration")
    print("=" * 70)

    # Step 1: Generate mock data
    print("\n[STEP 1] Data Generation")
    print("-" * 70)
    generator = MockSETDataGenerator(start_date='2019-01-01', end_date='2024-12-31', n_stocks=50)
    files = generator.generate_all_data(output_dir='data/processed')

    # Load data
    price_df = pd.read_csv(files['price'])
    financial_df = pd.read_csv(files['financial'])
    benchmark_df = pd.read_csv(files['benchmark'])

    # Ensure date columns are datetime
    price_df['date'] = pd.to_datetime(price_df['date'])
    financial_df['report_date'] = pd.to_datetime(financial_df['report_date'])
    financial_df['period_end'] = pd.to_datetime(financial_df['period_end'])
    benchmark_df['date'] = pd.to_datetime(benchmark_df['date'])

    print(f"\n  [OK] Price data: {len(price_df):,} rows")
    print(f"  [OK] Financial data: {len(financial_df):,} rows")
    print(f"  [OK] Benchmark data: {len(benchmark_df):,} rows")

    # Step 2: Calculate factors
    print("\n[STEP 2] Factor Calculation")
    print("-" * 70)
    calculator = VQMFactorCalculator()
    factor_df = calculator.calculate_all_factors(price_df, financial_df)

    print(f"\n  [OK] Value factors (4): FCF Yield, P/E Rel, P/B Rel, EV/EBITDA")
    print(f"  [OK] Quality factors (4): ROIC Spread, FCF Conv, Debt/EBITDA, GM")
    print(f"  [OK] Momentum factors (3): Price 6M, Earnings Rev, Volume Trend")

    # Step 3: Calculate VQM scores
    print("\n[STEP 3] VQM Score Calculation")
    print("-" * 70)
    score_df, rebalance_dates = calculate_all_scores(factor_df)

    scorer = VQMScorer()
    print(f"\n  [OK] Weights: Value {scorer.weights['value']:.0%}, "
          f"Quality {scorer.weights['quality']:.0%}, "
          f"Momentum {scorer.weights['momentum']:.0%}")
    print(f"  [OK] Rebalancing: Quarterly (~{len(rebalance_dates)} periods)")

    # Show sample scores for latest date
    latest_scores = score_df[score_df['date'] == score_df['date'].max()].nlargest(10, 'vqm_score')
    print(f"\n  Sample Top 10 Stocks ({latest_scores['date'].iloc[0].strftime('%Y-%m-%d')}):")
    print("  " + "-" * 66)
    print(f"  {'Symbol':<8} {'Sector':<15} {'VQM':>6} {'Value':>6} {'Qual':>6} {'Mom':>6}")
    print("  " + "-" * 66)
    for _, row in latest_scores.iterrows():
        print(f"  {row['symbol']:<8} {row['sector']:<15} "
              f"{row['vqm_score']:>6.2f} {row['value_score']:>6.2f} "
              f"{row['quality_score']:>6.2f} {row['momentum_score']:>6.2f}")

    # Step 4: Run backtest
    print("\n[STEP 4] Backtesting")
    print("-" * 70)
    backtester = VQMBacktester(transaction_cost=0.0050)
    results = backtester.run_backtest(price_df, benchmark_df, score_df, rebalance_dates)

    print(f"\n  [OK] Walk-forward backtest complete")
    print(f"  [OK] Periods: {len(results['portfolios'])}")
    print(f"  [OK] Transaction cost: 0.50% round-trip")

    # Step 5: Calculate performance metrics
    print("\n[STEP 5] Performance Analysis")
    print("-" * 70)
    metrics = PerformanceMetrics.calculate_metrics(
        results['daily_returns'],
        benchmark_df,
        rf_annual=0.025
    )

    PerformanceMetrics.print_report(metrics)

    # Step 6: Regime analysis
    regime_stats = regime_analysis(results['daily_returns'])

    # Save results
    print("\n[STEP 6] Saving Results")
    print("-" * 70)

    os.makedirs('results', exist_ok=True)

    # Save metrics
    metrics_df = pd.DataFrame([metrics])
    metrics_df.to_csv('results/performance_metrics.csv', index=False)
    print("  [OK] Performance metrics saved: results/performance_metrics.csv")

    # Save daily returns
    results['daily_returns'].to_csv('results/daily_returns.csv', index=False)
    print("  [OK] Daily returns saved: results/daily_returns.csv")

    # Save portfolio holdings
    all_portfolios = []
    for port in results['portfolios']:
        all_portfolios.append(port)
    if all_portfolios:
        portfolio_df = pd.concat(all_portfolios, ignore_index=True)
        portfolio_df.to_csv('results/portfolio_holdings.csv', index=False)
        print("  [OK] Portfolio holdings saved: results/portfolio_holdings.csv")

    # Save regime analysis
    regime_stats.to_csv('results/regime_analysis.csv', index=False)
    print("  [OK] Regime analysis saved: results/regime_analysis.csv")

    print("\n" + "=" * 70)
    print(" " * 20 + "[COMPLETE] BACKTEST COMPLETE [COMPLETE]")
    print("=" * 70)
    print("\nResults saved in 'results/' directory")
    print("\nKey Findings:")
    print(f"  • CAGR: {metrics['cagr']:.2%} vs Benchmark {metrics['benchmark_cagr']:.2%}")
    print(f"  • Sharpe: {metrics['sharpe_ratio']:.2f} vs Benchmark {metrics['benchmark_sharpe']:.2f}")
    print(f"  • Alpha: {metrics['alpha']:.2%} per year")
    print(f"  • Max Drawdown: {metrics['max_drawdown']:.2%} vs Benchmark {metrics['benchmark_max_drawdown']:.2%}")
    print()

    return results, metrics


if __name__ == '__main__':
    results, metrics = main()
