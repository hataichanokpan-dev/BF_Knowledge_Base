"""
VQM Model - Backtesting Engine
Walk-forward backtesting with quarterly rebalancing
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Tuple
import warnings
warnings.filterwarnings('ignore')


class VQMPortfolioConstructor:
    """Construct VQM portfolios based on scores"""

    def __init__(self, n_stocks=25, max_weight=0.05, max_sector_weight=0.10):
        self.n_stocks = n_stocks
        self.max_weight = max_weight
        self.max_sector_weight = max_sector_weight

    def construct_portfolio(self, score_df: pd.DataFrame) -> pd.DataFrame:
        """Construct portfolio for a given date"""
        # Filter to valid scores
        valid = score_df.dropna(subset=['vqm_score']).copy()

        if len(valid) < self.n_stocks:
            print(f"Warning: Only {len(valid)} valid stocks, using all")
            n = len(valid)
        else:
            n = self.n_stocks

        # Sort by VQM score and select top N
        selected = valid.nlargest(n, 'vqm_score').copy()

        # Equal weight
        selected['weight'] = 1.0 / len(selected)

        # Check sector constraints
        sector_weights = selected.groupby('sector')['weight'].sum()

        # Warn if sector constraint violated (simplified)
        violating_sectors = sector_weights[sector_weights > self.max_sector_weight]
        if len(violating_sectors) > 0:
            pass  # In full implementation, would re-weight

        return selected[['symbol', 'sector', 'vqm_score', 'weight',
                        'value_score', 'quality_score', 'momentum_score']]


class VQMBacktester:
    """Walk-forward backtesting for VQM model"""

    def __init__(self, transaction_cost=0.0050):
        self.transaction_cost = transaction_cost  # 0.50% round-trip

    def run_backtest(self, price_df: pd.DataFrame, benchmark_df: pd.DataFrame,
                     score_df: pd.DataFrame, rebalance_dates: List) -> Dict:
        """Run walk-forward backtest"""
        print("=" * 50)
        print("Running VQM Backtest...")
        print("=" * 50)

        constructor = VQMPortfolioConstructor()

        portfolios = []
        portfolio_returns = []

        for i, rebalance_date in enumerate(rebalance_dates[:-1]):
            # Get score data for this date
            date_scores = score_df[score_df['date'] == rebalance_date]

            if len(date_scores) == 0:
                continue

            # Construct portfolio
            portfolio = constructor.construct_portfolio(date_scores)
            portfolio['rebalance_date'] = rebalance_date

            # Get next rebalance date (for holding period)
            if i + 1 < len(rebalance_dates):
                next_date = rebalance_dates[i + 1]
            else:
                next_date = price_df['date'].max()

            # Calculate portfolio return for holding period
            start_price = price_df[price_df['date'] == rebalance_date][['symbol', 'close']].copy()
            end_price = price_df[price_df['date'] == next_date][['symbol', 'close']].copy()

            if len(start_price) == 0 or len(end_price) == 0:
                continue

            # Merge to get price changes
            price_change = start_price.merge(
                end_price,
                on='symbol',
                suffixes=('_start', '_end')
            )
            price_change['return'] = (price_change['close_end'] - price_change['close_start']) / price_change['close_start']

            # Merge with portfolio weights
            portfolio_return = portfolio.merge(price_change, on='symbol', how='left')
            portfolio_return['return'] = portfolio_return['return'].fillna(0)

            # Calculate portfolio return (weighted average)
            weighted_return = (portfolio_return['weight'] * portfolio_return['return']).sum()

            # Subtract transaction costs
            # Assume 50% turnover per rebalance
            turnover_cost = self.transaction_cost * 0.5
            net_return = weighted_return - turnover_cost

            portfolio_returns.append({
                'date': rebalance_date,
                'period_end': next_date,
                'gross_return': weighted_return,
                'net_return': net_return,
                'n_stocks': len(portfolio),
            })

            portfolios.append(portfolio)

        # Create returns series
        returns_df = pd.DataFrame(portfolio_returns)

        # Generate daily returns (for metrics calculation)
        daily_returns = self._generate_daily_returns(
            price_df, benchmark_df, portfolios, rebalance_dates
        )

        result = {
            'portfolios': portfolios,
            'returns': returns_df,
            'daily_returns': daily_returns,
            'rebalance_dates': rebalance_dates
        }

        print(f"[OK] Backtest complete: {len(portfolios)} periods")

        return result

    def _generate_daily_returns(self, price_df: pd.DataFrame, benchmark_df: pd.DataFrame,
                                portfolios: List, rebalance_dates: List) -> pd.DataFrame:
        """Generate daily returns time series"""
        all_returns = []

        # Ensure date columns are datetime
        price_df = price_df.copy()
        price_df['date'] = pd.to_datetime(price_df['date'])

        benchmark_df = benchmark_df.copy()
        benchmark_df['date'] = pd.to_datetime(benchmark_df['date'])

        for i, portfolio in enumerate(portfolios):
            rebalance_date = pd.to_datetime(portfolio['rebalance_date'].iloc[0])

            if i + 1 < len(rebalance_dates):
                end_date = pd.to_datetime(rebalance_dates[i + 1])
            else:
                end_date = price_df['date'].max()

            # Get daily prices for holding period
            period_mask = (price_df['date'] > rebalance_date) & (price_df['date'] <= end_date)
            period_prices = price_df[period_mask].copy()

            if len(period_prices) == 0:
                continue

            # Calculate daily portfolio returns
            daily_rets = []

            for date in period_prices['date'].unique():
                date_prices = period_prices[period_prices['date'] == date][['symbol', 'close']]
                prev_prices = price_df[price_df['date'] < date].sort_values('date').groupby('symbol').tail(1)[['symbol', 'close']]

                if len(date_prices) == 0 or len(prev_prices) == 0:
                    continue

                # Merge with portfolio
                merged = date_prices.merge(prev_prices, on='symbol', suffixes=('', '_prev'))
                merged = merged.merge(portfolio[['symbol', 'weight']], on='symbol', how='left')

                if len(merged) == 0:
                    continue

                merged['daily_return'] = (merged['close'] - merged['close_prev']) / merged['close_prev']
                merged['weight'] = merged['weight'].fillna(0)

                # Portfolio return
                port_return = (merged['daily_return'] * merged['weight']).sum()

                # Get benchmark return for this date
                bench_row = benchmark_df[benchmark_df['date'] == date]
                if len(bench_row) > 0:
                    bench_return = bench_row['set_return'].values[0]
                else:
                    # Find closest date
                    if len(benchmark_df) > 0:
                        idx = (benchmark_df['date'] - date).abs().idxmin()
                        bench_return = benchmark_df.loc[idx, 'set_return']
                    else:
                        bench_return = 0

                daily_rets.append({
                    'date': date,
                    'portfolio_return': port_return,
                    'benchmark_return': bench_return,
                    'excess_return': port_return - bench_return
                })

            all_returns.extend(daily_rets)

        return pd.DataFrame(all_returns)


class PerformanceMetrics:
    """Calculate performance metrics for backtest results"""

    @staticmethod
    def calculate_metrics(returns_df: pd.DataFrame, benchmark_df: pd.DataFrame,
                          rf_annual: float = 0.025) -> Dict:
        """Calculate comprehensive performance metrics"""
        if len(returns_df) == 0:
            return {}

        # Ensure date columns are same type
        returns_df = returns_df.copy()
        benchmark_df = benchmark_df.copy()
        returns_df['date'] = pd.to_datetime(returns_df['date'])
        benchmark_df['date'] = pd.to_datetime(benchmark_df['date'])

        # Merge with benchmark
        merged = returns_df.merge(benchmark_df, on='date', how='left')
        merged['benchmark_return'] = merged['benchmark_return'].fillna(0)
        merged['excess_return'] = merged['portfolio_return'] - merged['benchmark_return']

        # Daily risk-free rate
        rf_daily = rf_annual / 252

        # Basic metrics
        total_days = len(merged)
        years = total_days / 252

        # Returns
        total_return = (1 + merged['portfolio_return']).prod() - 1
        benchmark_total_return = (1 + merged['benchmark_return']).prod() - 1
        excess_total = total_return - benchmark_total_return

        # CAGR
        cagr = (1 + total_return) ** (1 / years) - 1
        benchmark_cagr = (1 + benchmark_total_return) ** (1 / years) - 1

        # Volatility
        vol = merged['portfolio_return'].std() * np.sqrt(252)
        benchmark_vol = merged['benchmark_return'].std() * np.sqrt(252)

        # Sharpe Ratio
        excess_returns_daily = merged['portfolio_return'] - rf_daily
        sharpe = excess_returns_daily.mean() / excess_returns_daily.std() * np.sqrt(252)

        # Benchmark Sharpe
        benchmark_excess = merged['benchmark_return'] - rf_daily
        benchmark_sharpe = benchmark_excess.mean() / benchmark_excess.std() * np.sqrt(252)

        # Sortino Ratio
        downside_returns = excess_returns_daily[excess_returns_daily < 0]
        if len(downside_returns) > 0:
            sortino = excess_returns_daily.mean() / downside_returns.std() * np.sqrt(252)
        else:
            sortino = sharpe  # No downside

        # Max Drawdown
        cum_returns = (1 + merged['portfolio_return']).cumprod()
        rolling_max = cum_returns.expanding().max()
        drawdown = (cum_returns - rolling_max) / rolling_max
        max_drawdown = drawdown.min()

        # Benchmark Max Drawdown
        bench_cum = (1 + merged['benchmark_return']).cumprod()
        bench_rolling_max = bench_cum.expanding().max()
        bench_dd = (bench_cum - bench_rolling_max) / bench_rolling_max
        benchmark_max_dd = bench_dd.min()

        # Information Ratio
        if merged['excess_return'].std() > 0:
            ir = merged['excess_return'].mean() / merged['excess_return'].std() * np.sqrt(252)
        else:
            ir = 0

        # Alpha & Beta (CAPM regression)
        from scipy import stats
        x = merged['benchmark_return'] - rf_daily
        y = merged['portfolio_return'] - rf_daily

        if len(x) > 0 and x.std() > 0 and len(x.unique()) > 1:
            beta, alpha, r_value, p_value, std_err = stats.linregress(x, y)
            alpha_annual = alpha * 252
        else:
            beta = 1.0
            alpha_annual = 0

        # Hit Rate
        hit_rate = (merged['excess_return'] > 0).mean()

        # Win/Loss ratio
        wins = merged[merged['excess_return'] > 0]['excess_return'].mean()
        losses = merged[merged['excess_return'] < 0]['excess_return'].mean()
        win_loss_ratio = abs(wins / losses) if losses != 0 else 0

        return {
            'period_years': years,
            'total_return': total_return,
            'benchmark_total_return': benchmark_total_return,
            'excess_return': excess_total,
            'cagr': cagr,
            'benchmark_cagr': benchmark_cagr,
            'volatility': vol,
            'benchmark_volatility': benchmark_vol,
            'sharpe_ratio': sharpe,
            'benchmark_sharpe': benchmark_sharpe,
            'sortino_ratio': sortino,
            'max_drawdown': max_drawdown,
            'benchmark_max_drawdown': benchmark_max_dd,
            'information_ratio': ir,
            'alpha': alpha_annual,
            'beta': beta,
            'hit_rate': hit_rate,
            'win_loss_ratio': win_loss_ratio
        }

    @staticmethod
    def print_report(metrics: Dict):
        """Print formatted performance report"""
        print("\n" + "=" * 60)
        print("VQM MODEL BACKTEST RESULTS")
        print("=" * 60)

        print("\n[RETURN METRICS]")
        print("-" * 60)
        print(f"  CAGR:                    {metrics['cagr']:>7.2%}  (Benchmark: {metrics['benchmark_cagr']:>6.2%})")
        print(f"  Total Return:            {metrics['total_return']:>7.2%}  (Benchmark: {metrics['benchmark_total_return']:>6.2%})")
        print(f"  Excess Return:           {metrics['excess_return']:>7.2%}")

        print("\n[RISK METRICS]")
        print("-" * 60)
        print(f"  Volatility:              {metrics['volatility']:>7.2%}  (Benchmark: {metrics['benchmark_volatility']:>6.2%})")
        print(f"  Max Drawdown:            {metrics['max_drawdown']:>7.2%}  (Benchmark: {metrics['benchmark_max_drawdown']:>6.2%})")

        print("\n[RISK-ADJUSTED METRICS]")
        print("-" * 60)
        print(f"  Sharpe Ratio:            {metrics['sharpe_ratio']:>7.2f}  (Benchmark: {metrics['benchmark_sharpe']:>6.2f})")
        print(f"  Sortino Ratio:           {metrics['sortino_ratio']:>7.2f}")
        print(f"  Information Ratio:       {metrics['information_ratio']:>7.2f}")

        print("\n[ALPHA & BETA]")
        print("-" * 60)
        print(f"  Alpha (annual):          {metrics['alpha']:>7.2%}")
        print(f"  Beta:                    {metrics['beta']:>7.2f}")

        print("\n[TRADING STATISTICS]")
        print("-" * 60)
        print(f"  Hit Rate:               {metrics['hit_rate']:>7.2%}")
        print(f"  Win/Loss Ratio:         {metrics['win_loss_ratio']:>7.2f}")

        # Assessment
        print("\n" + "=" * 60)
        print("[ASSESSMENT]")
        print("=" * 60)

        checks = []
        if metrics['cagr'] > metrics['benchmark_cagr']:
            checks.append("[+] OUTPERFORMS benchmark on CAGR")
        else:
            checks.append("[-] Underperforms benchmark on CAGR")

        if metrics['sharpe_ratio'] > metrics['benchmark_sharpe']:
            checks.append("[+] HIGHER Sharpe ratio than benchmark")
        else:
            checks.append("[-] Lower Sharpe ratio than benchmark")

        if metrics['max_drawdown'] > metrics['benchmark_max_drawdown']:
            checks.append("[+] BETTER Max Drawdown than benchmark")
        else:
            checks.append("[-] Worse Max Drawdown than benchmark")

        if metrics['alpha'] > 0.03:
            checks.append("[+] STRONG Alpha (>3%)")
        elif metrics['alpha'] > 0:
            checks.append("[+] Positive Alpha")
        else:
            checks.append("[-] Negative Alpha")

        for check in checks:
            print(f"  {check}")

        print("=" * 60 + "\n")


def regime_analysis(daily_returns: pd.DataFrame) -> Dict:
    """Analyze performance across different market regimes"""
    print("\n" + "=" * 60)
    print("[REGIME ANALYSIS]")
    print("=" * 60)

    # Define regimes based on benchmark returns
    # Bull: positive returns, Bear: negative returns
    daily_returns['regime'] = 'Bull'
    daily_returns.loc[daily_returns['benchmark_return'] < -0.005, 'regime'] = 'Bear'

    # Calculate returns by regime
    regime_stats = []

    for regime in ['Bull', 'Bear']:
        regime_data = daily_returns[daily_returns['regime'] == regime]

        if len(regime_data) > 0:
            regime_return = regime_data['portfolio_return'].mean()
            benchmark_return = regime_data['benchmark_return'].mean()
            excess = regime_return - benchmark_return

            regime_stats.append({
                'regime': regime,
                'days': len(regime_data),
                'portfolio_return': regime_return,
                'benchmark_return': benchmark_return,
                'excess_return': excess,
                'hit_rate': (regime_data['excess_return'] > 0).mean()
            })

    result = pd.DataFrame(regime_stats)

    for _, row in result.iterrows():
        print(f"\n{row['regime']} Market ({row['days']} days):")
        print(f"  Portfolio:    {row['portfolio_return']:>7.4%} per day")
        print(f"  Benchmark:    {row['benchmark_return']:>7.4%} per day")
        print(f"  Excess:       {row['excess_return']:>7.4%} per day")
        print(f"  Hit Rate:     {row['hit_rate']:>7.2%}")

    print("=" * 60 + "\n")

    return result


if __name__ == '__main__':
    print("VQM Backtesting Engine - Ready")
