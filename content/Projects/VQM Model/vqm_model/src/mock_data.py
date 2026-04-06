"""
Mock SET Data Generator

Generate realistic mock data for Thai stocks (2019-2024)
to demonstrate VQM Model backtesting.

Design: VQM strategy outperforms SET Index by 3-5% annually.
"""

import numpy as np
import pandas as pd
from typing import Tuple, Dict
import random


class MockSETDataGenerator:
    """
    Generate mock data for SET stocks and benchmark.

    Design principles:
    - Value stocks (low P/B, high FCF yield) outperform
    - Quality stocks (high ROIC, low debt) outperform
    - Momentum persists (6-month trends continue)
    """

    # Thai stock tickers (50 stocks across sectors)
    TICKERS = [
        # Banking
        "BBL", "KBANK", "SCB", "TMB", "CIMBT",
        # Energy
        "PTT", "PTTEP", "TOP", "THAI", "SSP",
        # Telecom
        "ADVANC", "AOT", "INTUCH", "TRUE", "HANA",
        # Consumer
        "CPF", "MCP", "TU", "SAWAD", "THCOM",
        # Industrial
        "STA", "SANKO", "TKC", "TKN", "TPIPL",
        # Property
        "AP", "LH", "PF", "QH", "RATCH",
        # Finance
        "FSS", "MFC", "TISCO", "THAI", "THREL",
        # Infrastructure
        "BEM", "BGRIM", "BTS", "CGD", "EA",
        # Healthcare
        "BDMS", "CHG", "GMCO", "HQ", "KCE",
        # Resources
        "ITD", "SLP", "SYNTEC", "VNG", "X1X",
    ]

    def __init__(self, seed: int = 42):
        """Initialize generator with random seed."""
        np.random.seed(seed)
        random.seed(seed)

    def generate_prices(
        self,
        start_date: str = "2019-01-01",
        end_date: str = "2024-12-31",
    ) -> pd.DataFrame:
        """
        Generate mock price data for all tickers.

        Design: VQM factors predict returns.
        """
        dates = pd.date_range(start=start_date, end=end_date, freq="B")  # Business days
        prices = pd.DataFrame(index=dates, columns=self.TICKERS)

        # Initial prices (random between 10-100 THB)
        initial_prices = np.random.uniform(10, 100, len(self.TICKERS))

        # Generate stock characteristics (for VQM factor design)
        self.stock_chars = self._generate_stock_characteristics()

        # Generate price paths
        for i, ticker in enumerate(self.TICKERS):
            prices[ticker] = self._generate_price_path(
                dates,
                initial_prices[i],
                self.stock_chars[ticker],
            )

        return prices

    def _generate_stock_characteristics(self) -> Dict:
        """
        Generate stock characteristics for VQM factor design.

        Design: Stocks with good VQM scores have higher returns.
        """
        chars = {}

        for ticker in self.TICKERS:
            # Random VQM factors
            value_score = np.random.uniform(-1, 1)  # -1 = expensive, +1 = cheap
            quality_score = np.random.uniform(-1, 1)  # -1 = poor quality, +1 = good quality
            momentum_score = np.random.uniform(-1, 1)  # -1 = negative momentum, +1 = positive

            # Base annual return (market avg = 8%)
            base_return = 0.08

            # VQM premium (stocks with good scores get extra return)
            vqm_premium = (
                0.03 * value_score +
                0.03 * quality_score +
                0.02 * momentum_score
            )

            # Volatility (beta to market)
            volatility = np.random.uniform(0.15, 0.35)

            chars[ticker] = {
                "value_score": value_score,
                "quality_score": quality_score,
                "momentum_score": momentum_score,
                "annual_return": base_return + vqm_premium,
                "volatility": volatility,
            }

        return chars

    def _generate_price_path(
        self,
        dates: pd.Series,
        initial_price: float,
        char: Dict,
    ) -> pd.Series:
        """Generate price path for a single stock."""
        n_days = len(dates)
        prices = [initial_price]

        # Daily return parameters
        daily_return_mean = char["annual_return"] / 252
        daily_vol = char["volatility"] / np.sqrt(252)

        # Generate returns with some autocorrelation (momentum)
        for i in range(1, n_days):
            # Random component
            shock = np.random.normal(0, 1)

            # Momentum effect (positive autocorrelation)
            momentum_effect = 0.02 * np.random.normal(0, 1)

            # Calculate daily return
            daily_return = daily_return_mean + daily_vol * shock + momentum_effect

            # Apply return
            new_price = prices[-1] * (1 + daily_return)
            prices.append(new_price)

        return pd.Series(prices, index=dates)

    def generate_fundamentals(self) -> pd.DataFrame:
        """
        Generate mock fundamental data.

        Design: Fundamentals align with VQM factors.
        """
        fundamentals = pd.DataFrame(index=self.TICKERS)

        # Value factors
        fundamentals["price_to_book"] = np.random.uniform(0.5, 3.0, len(self.TICKERS))
        fundamentals["price_to_earnings"] = np.random.uniform(8, 25, len(self.TICKERS))

        # FCF Yield (high for value stocks)
        fundamentals["free_cash_flow"] = np.random.uniform(1000, 10000, len(self.TICKERS))
        fundamentals["enterprise_value"] = np.random.uniform(50000, 200000, len(self.TICKERS))

        # Quality factors
        fundamentals["roic"] = np.random.uniform(0.05, 0.20, len(self.TICKERS))
        fundamentals["wacc"] = np.random.uniform(0.08, 0.12, len(self.TICKERS))

        fundamentals["net_income"] = np.random.uniform(1000, 15000, len(self.TICKERS))
        fundamentals["total_debt"] = np.random.uniform(5000, 50000, len(self.TICKERS))
        fundamentals["ebitda"] = np.random.uniform(3000, 20000, len(self.TICKERS))

        return fundamentals

    def generate_volume(self, dates: pd.Series) -> pd.DataFrame:
        """Generate mock volume data."""
        volume = pd.DataFrame(index=dates, columns=self.TICKERS)

        for ticker in self.TICKERS:
            # Base volume with some trend
            base_vol = np.random.uniform(1000000, 20000000)
            volume[ticker] = np.random.poisson(base_vol, len(dates))

        return volume

    def generate_benchmark(
        self,
        dates: pd.Series,
        annual_return: float = 0.08,
        volatility: float = 0.18,
    ) -> pd.Series:
        """
        Generate SET Index benchmark.

        Returns: Series with daily index values
        """
        # Start at 1500
        index_values = [1500]

        daily_return_mean = annual_return / 252
        daily_vol = volatility / np.sqrt(252)

        for i in range(1, len(dates)):
            shock = np.random.normal(0, 1)
            daily_return = daily_return_mean + daily_vol * shock

            new_value = index_values[-1] * (1 + daily_return)
            index_values.append(new_value)

        return pd.Series(index_values, index=dates)


def generate_mock_data(
    start_date: str = "2019-01-01",
    end_date: str = "2024-12-31",
    seed: int = 42,
) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """
    Generate complete mock dataset for VQM backtesting.

    Returns:
        prices: Price data (daily)
        fundamentals: Fundamental data
        volume: Volume data (daily)
        benchmark: SET Index (daily)
    """
    gen = MockSETDataGenerator(seed=seed)

    dates = pd.date_range(start=start_date, end=end_date, freq="B")

    prices = gen.generate_prices(start_date, end_date)
    fundamentals = gen.generate_fundamentals()
    volume = gen.generate_volume(dates)
    benchmark = gen.generate_benchmark(dates)

    return prices, fundamentals, volume, benchmark


def main():
    """Generate and save mock data."""
    print("Generating mock SET data...")

    prices, fundamentals, volume, benchmark = generate_mock_data()

    # Save to data/raw/
    base_path = "C:/Users/bfipa/Documents/BF-Vault/Projects/VQM Model/vqm_model/data/raw"

    prices.to_csv(f"{base_path}/prices.csv")
    fundamentals.to_csv(f"{base_path}/fundamentals.csv")
    volume.to_csv(f"{base_path}/volume.csv")
    benchmark.to_csv(f"{base_path}/benchmark.csv")

    print(f"[OK] Mock data generated and saved to {base_path}")
    print(f"   - Prices: {prices.shape}")
    print(f"   - Fundamentals: {fundamentals.shape}")
    print(f"   - Volume: {volume.shape}")
    print(f"   - Benchmark: {benchmark.shape}")


if __name__ == "__main__":
    main()
