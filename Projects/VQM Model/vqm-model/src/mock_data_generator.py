"""
VQM Model - Mock Data Generator
Generates realistic mock SET data for backtesting demonstration
"""

import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)


class MockSETDataGenerator:
    """Generate mock SET stock data for VQM backtesting"""

    # SET sectors (11 sectors)
    SECTORS = [
        'Agri & Food', 'Consumer', 'Financials', 'Industrials',
        'Petrochem & Chem', 'Property', 'Health Care', 'Resources',
        'Services', 'Technology', 'Tourism'
    ]

    # Sample stock symbols (Thai naming convention)
    STOCK_PREFIXES = [
        'ADVANC', 'AOT', 'BDMS', 'BBL', 'BEM', 'BGRIM', 'BH', 'BJC',
        'BTS', 'CBG', 'CPF', 'CPN', 'DELTA', 'EA', 'EGCO', 'EP', 'ERT',
        'GFPT', 'GULF', 'HMPRO', 'INTUCH', 'IRPC', 'JAS', 'KBANK', 'KCE',
        'KTB', 'LH', 'M', 'MAJOR', 'MFEC', 'MFC', 'MG', 'MO', 'MPT',
        'OR', 'OSP', 'PTT', 'PTTEP', 'QPAC', 'RATCH', 'SAWAD', 'SCC',
        'SCGP', 'SIRI', 'SPALI', 'SPRC', 'STA', 'STGT', 'TISCO', 'TISCO',
        'TLI', 'TOP', 'TRUE', 'TU', 'VNG', 'WHA', 'WPG'
    ]

    def __init__(self, start_date='2019-01-01', end_date='2024-12-31', n_stocks=50):
        self.start_date = pd.to_datetime(start_date)
        self.end_date = pd.to_datetime(end_date)
        self.n_stocks = n_stocks
        self.trading_days = pd.date_range(start_date, end_date, freq='B')  # Business days

        # Select stocks
        self.symbols = self.STOCK_PREFIXES[:n_stocks]

        # Generate stock characteristics
        self.stock_chars = self._generate_stock_characteristics()

    def _generate_stock_characteristics(self):
        """Generate persistent characteristics for each stock"""
        chars = []

        for i, symbol in enumerate(self.symbols):
            # Assign sector (try to distribute evenly)
            sector = self.SECTORS[i % len(self.SECTORS)]

            # Base market cap (log-normal distribution)
            base_mcap = np.random.lognormal(11, 1) * 1e6  # 5B to 500B THB

            # Stock type: Quality, Value, Growth, or Balanced
            stock_type = np.random.choice(
                ['Quality', 'Value', 'Momentum', 'Balanced'],
                p=[0.25, 0.25, 0.25, 0.25]
            )

            # Base characteristics
            chars.append({
                'symbol': symbol,
                'sector': sector,
                'base_mcap': base_mcap,
                'base_roic': np.random.uniform(0.05, 0.20),  # 5% to 20%
                'base_fcf_yield': np.random.uniform(0.02, 0.12),  # 2% to 12%
                'base_debt_ebitda': np.random.uniform(0.5, 5.0),
                'base_pe': np.random.uniform(8, 25),
                'base_pb': np.random.uniform(0.8, 3.0),
                'stock_type': stock_type,
                'beta': np.random.uniform(0.7, 1.5),
                'volatility': np.random.uniform(0.15, 0.35),
            })

        return pd.DataFrame(chars)

    def generate_price_data(self):
        """Generate daily price and volume data"""
        print(f"Generating price data for {len(self.symbols)} stocks...")

        all_data = []

        for char in self.stock_chars.to_dict('records'):
            symbol = char['symbol']
            beta = char['beta']
            volatility = char['volatility']
            stock_type = char['stock_type']

            # Initial price
            initial_price = np.random.uniform(10, 100)

            # Generate price path (Geometric Brownian Motion with regime shifts)
            prices = [initial_price]
            volumes = []

            # Regime parameters
            bull_return = 0.08 / 252  # 8% annual
            bear_return = -0.15 / 252  # -15% annual
            bull_vol = volatility
            bear_vol = volatility * 1.5

            # Define regimes (simplified)
            regimes = {
                'bull_2019': slice(0, 250),
                'covid_crash': slice(250, 280),
                'recovery': slice(280, 500),
                'bull_2021': slice(500, 750),
                'rate_hike': slice(750, 900),
                'recovery_2023': slice(900, 1150),
                '2024': slice(1150, len(self.trading_days))
            }

            for i in range(1, len(self.trading_days)):
                prev_price = prices[-1]

                # Determine regime
                day_idx = i
                if day_idx < 250:  # 2019
                    drift = bull_return
                    vol = bull_vol
                elif day_idx < 280:  # COVID crash
                    drift = bear_return * 1.5
                    vol = bear_vol * 2
                elif day_idx < 500:  # Recovery
                    drift = bull_return * 1.2
                    vol = bull_vol * 1.2
                elif day_idx < 750:  # 2021 bull
                    drift = bull_return
                    vol = bull_vol
                elif day_idx < 900:  # 2022 rate hike
                    drift = -0.05 / 252
                    vol = volatility * 1.3
                elif day_idx < 1150:  # 2023 recovery
                    drift = bull_return * 0.8
                    vol = bull_vol
                else:  # 2024
                    drift = bull_return * 0.7
                    vol = bull_vol

                # Add stock-type specific alpha
                type_alpha = 0
                if stock_type == 'Quality':
                    type_alpha = 0.02 / 252  # 2% annual alpha
                elif stock_type == 'Value':
                    type_alpha = 0.015 / 252  # 1.5% annual alpha
                elif stock_type == 'Momentum':
                    type_alpha = 0.01 / 252  # 1% annual alpha

                # Generate return
                random_shock = np.random.normal(0, 1)
                daily_return = drift + type_alpha + vol * random_shock / np.sqrt(252)

                # Apply return
                new_price = prev_price * (1 + daily_return)
                prices.append(max(new_price, 0.5))  # Minimum price

                # Generate volume (log-normal with trend)
                base_volume = char['base_mcap'] * 0.002 / initial_price  # 0.2% of mcap daily
                volume_multiplier = 1 + 0.3 * np.random.normal(0, 1)
                volumes.append(int(base_volume * 1e6 * volume_multiplier))

            # Create price series
            price_series = pd.Series(prices, index=self.trading_days)

            # Calculate returns
            returns = price_series.pct_change()

            # Create volume series (add initial)
            volume_series = pd.Series([volumes[0]] + volumes, index=self.trading_days)

            # Calculate momentum metrics
            for date in self.trading_days:
                all_data.append({
                    'date': date,
                    'symbol': symbol,
                    'sector': char['sector'],
                    'open': price_series.loc[date] * (1 + np.random.uniform(-0.005, 0.005)),
                    'high': price_series.loc[date] * (1 + abs(np.random.normal(0, 0.01))),
                    'low': price_series.loc[date] * (1 - abs(np.random.normal(0, 0.01))),
                    'close': price_series.loc[date],
                    'volume': volume_series.loc[date],
                    'market_cap': char['base_mcap'] * (price_series.loc[date] / initial_price),
                })

        df = pd.DataFrame(all_data)
        return df

    def generate_financial_data(self):
        """Generate quarterly financial data (Point-in-Time format)"""
        print("Generating financial data...")

        # Quarterly dates
        quarterly_dates = pd.date_range(
            self.start_date, self.end_date, freq='Q'
        )

        all_data = []

        for q_date in quarterly_dates:
            # Report date is ~45 days after quarter end
            report_date = q_date + timedelta(days=45)

            for char in self.stock_chars.to_dict('records'):
                symbol = char['symbol']

                # Get current price from around this time
                price_idx = pd.Index(self.trading_days).get_indexer([q_date], method='nearest')[0]

                if price_idx > 0:
                    # Add some randomness to financials (business cycle + noise)
                    cycle_factor = 1 + 0.1 * np.sin(price_idx / 125)  # Business cycle
                    noise = np.random.normal(1, 0.05)

                    # Base metrics with some evolution
                    roic = char['base_roic'] * cycle_factor * noise
                    fcf_yield = char['base_fcf_yield'] * cycle_factor * noise
                    debt_ebitda = char['base_debt_ebitda'] * (2 - cycle_factor) * noise
                    pe = char['base_pe'] * (1 + 0.2 * np.random.normal(0, 1))
                    pb = char['base_pb'] * (1 + 0.2 * np.random.normal(0, 1))

                    # Calculate derived metrics
                    revenue = char['base_mcap'] * 0.5 * cycle_factor * noise  # Revenue ~ 50% of mcap
                    ebitda = revenue * np.random.uniform(0.15, 0.30)  # 15-30% margin
                    net_income = ebitda * np.random.uniform(0.50, 0.80) * 0.8  # After tax
                    operating_cf = net_income * np.random.uniform(1.0, 1.5)  # CF conversion
                    capex = revenue * np.random.uniform(0.03, 0.10)
                    fcf = operating_cf - capex

                    # Balance sheet items
                    total_debt = revenue * char['base_debt_ebitda'] / ebitda * revenue
                    cash = revenue * np.random.uniform(0.1, 0.5)
                    equity = char['base_mcap'] * 0.6
                    invested_capital = debt_ebitda * ebitda * 5  # Rough approximation

                    # WACC
                    risk_free = 0.025 + np.random.uniform(-0.005, 0.01)
                    market_premium = 0.07
                    cost_equity = risk_free + char['beta'] * market_premium
                    cost_debt = 0.05 + np.random.uniform(-0.01, 0.02)
                    wacc = (equity / (equity + total_debt)) * cost_equity + \
                           (total_debt / (equity + total_debt)) * cost_debt * 0.8

                    all_data.append({
                        'report_date': report_date,
                        'period_end': q_date,
                        'symbol': symbol,
                        'sector': char['sector'],
                        'revenue': revenue,
                        'ebitda': ebitda,
                        'net_income': net_income,
                        'operating_cf': operating_cf,
                        'capex': capex,
                        'fcf': fcf,
                        'total_debt': total_debt,
                        'cash': cash,
                        'equity': equity,
                        'invested_capital': invested_capital,
                        'roic': max(0, roic),
                        'wacc': wacc,
                        'fcf_conversion': max(-0.5, min(2, fcf / max(net_income, 1))),
                        'debt_ebitda': max(0, debt_ebitda),
                        'gross_margin': np.random.uniform(0.20, 0.45),
                        'pe': max(5, pe),
                        'pb': max(0.5, pb),
                        'ev_ebitda': ebitda * np.random.uniform(6, 15) / ebitda,
                    })

        df = pd.DataFrame(all_data)
        return df

    def generate_benchmark_data(self):
        """Generate SET Index benchmark data"""
        print("Generating benchmark data...")

        # SET Index starts at ~1600 in 2019
        initial_value = 1600

        # Generate index path with regimes
        values = [initial_value]

        for i in range(1, len(self.trading_days)):
            prev = values[-1]

            # Regime-based drift
            if i < 250:  # 2019
                drift = 0.06 / 252
                vol = 0.15
            elif i < 280:  # COVID crash
                drift = -0.40 / 30  # Sharp drop
                vol = 0.40
            elif i < 500:  # Recovery
                drift = 0.15 / 252
                vol = 0.20
            elif i < 750:  # 2021
                drift = 0.10 / 252
                vol = 0.15
            elif i < 900:  # 2022
                drift = -0.08 / 252
                vol = 0.18
            elif i < 1150:  # 2023
                drift = 0.12 / 252
                vol = 0.16
            else:  # 2024
                drift = 0.08 / 252
                vol = 0.15

            daily_return = drift + vol * np.random.normal(0, 1) / np.sqrt(252)
            new_value = prev * (1 + daily_return)
            values.append(max(new_value, 800))  # Floor

        df = pd.DataFrame({
            'date': self.trading_days,
            'set_index': values,
            'risk_free_rate': 0.025 / 252  # 2.5% annual
        })

        # Calculate returns and fill first row
        df['set_return'] = df['set_index'].pct_change()
        df['set_return'] = df['set_return'].fillna(0)

        return df

    def generate_all_data(self, output_dir='data/processed'):
        """Generate all mock data and save to files"""
        import os
        os.makedirs(output_dir, exist_ok=True)

        print("=" * 50)
        print("VQM Model - Mock Data Generator")
        print("=" * 50)

        # Generate price data
        price_df = self.generate_price_data()
        price_file = f'{output_dir}/price_data.csv'
        price_df.to_csv(price_file, index=False)
        print(f"[OK] Price data saved: {price_file} ({len(price_df):,} rows)")

        # Generate financial data
        financial_df = self.generate_financial_data()
        financial_file = f'{output_dir}/financial_data.csv'
        financial_df.to_csv(financial_file, index=False)
        print(f"[OK] Financial data saved: {financial_file} ({len(financial_df):,} rows)")

        # Generate benchmark data
        benchmark_df = self.generate_benchmark_data()
        benchmark_file = f'{output_dir}/benchmark_data.csv'
        benchmark_df.to_csv(benchmark_file, index=False)
        print(f"[OK] Benchmark data saved: {benchmark_file} ({len(benchmark_df):,} rows)")

        # Save stock characteristics
        chars_file = f'{output_dir}/stock_characteristics.csv'
        self.stock_chars.to_csv(chars_file, index=False)
        print(f"[OK] Stock characteristics saved: {chars_file}")

        print("=" * 50)
        print(f"Mock data generation complete!")
        print(f"  - Stocks: {len(self.symbols)}")
        print(f"  - Period: {self.start_date.date()} to {self.end_date.date()}")
        print(f"  - Trading days: {len(self.trading_days)}")
        print("=" * 50)

        return {
            'price': price_file,
            'financial': financial_file,
            'benchmark': benchmark_file,
            'characteristics': chars_file
        }


if __name__ == '__main__':
    # Generate mock data
    generator = MockSETDataGenerator(n_stocks=50)
    files = generator.generate_all_data()

    print("\nFiles ready for VQM backtesting!")
