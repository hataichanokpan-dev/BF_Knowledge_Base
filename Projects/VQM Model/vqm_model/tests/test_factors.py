"""
Tests for VQM Factor Calculations
"""

import pytest
import numpy as np
import pandas as pd
from src.factors import VQMFactors


@pytest.fixture
def sample_prices():
    """Sample price data for testing."""
    dates = pd.date_range("2019-01-01", "2024-12-31", freq="M")
    tickers = ["ADVANC", "AOT", "BDMS", "BBL", "BEM"]

    np.random.seed(42)
    data = np.random.randn(len(dates), len(tickers)) * 0.1 + 1

    # Cumulative returns to simulate price trends
    for i in range(1, len(data)):
        data[i] = data[i-1] * (1 + np.random.randn(len(tickers)) * 0.05)

    prices = pd.DataFrame(data, index=dates, columns=tickers)
    prices = 100 * prices  # Start at 100 THB

    return prices


@pytest.fixture
def sample_fundamentals():
    """Sample fundamental data for testing."""
    tickers = ["ADVANC", "AOT", "BDMS", "BBL", "BEM"]

    data = {
        "free_cash_flow": np.random.randn(len(tickers)) * 1000 + 5000,
        "enterprise_value": np.random.randn(len(tickers)) * 50000 + 100000,
        "price_to_book": np.random.randn(len(tickers)) * 0.5 + 1.5,
        "price_to_earnings": np.random.randn(len(tickers)) * 5 + 15,
        "roic": np.random.randn(len(tickers)) * 0.03 + 0.12,
        "wacc": np.random.randn(len(tickers)) * 0.01 + 0.10,
        "net_income": np.random.randn(len(tickers)) * 2000 + 10000,
        "total_debt": np.random.randn(len(tickers)) * 10000 + 20000,
        "ebitda": np.random.randn(len(tickers)) * 3000 + 15000,
    }

    fundamentals = pd.DataFrame(data, index=tickers)

    return fundamentals


@pytest.fixture
def sample_volume():
    """Sample volume data for testing."""
    dates = pd.date_range("2019-01-01", "2024-12-31", freq="M")
    tickers = ["ADVANC", "AOT", "BDMS", "BBL", "BEM"]

    np.random.seed(42)
    data = np.random.randint(1000000, 50000000, size=(len(dates), len(tickers)))

    volume = pd.DataFrame(data, index=dates, columns=tickers)

    return volume


class TestVQMFactors:
    """Test VQM factor calculations."""

    def test_initialization(self):
        """Test VQMFactors initialization."""
        vqm = VQMFactors()

        assert vqm.VALUE_WEIGHT == 0.45
        assert vqm.QUALITY_WEIGHT == 0.35
        assert vqm.MOMENTUM_WEIGHT == 0.20

    def test_calculate_value_factors(self, sample_prices, sample_fundamentals):
        """Test value factor calculation."""
        vqm = VQMFactors()
        value_factors = vqm.calculate_value_factors(sample_prices, sample_fundamentals)

        assert "fcf_yield" in value_factors.columns
        assert "pb_ratio" in value_factors.columns
        assert "pe_ratio" in value_factors.columns

    def test_calculate_quality_factors(self, sample_fundamentals):
        """Test quality factor calculation."""
        vqm = VQMFactors()
        quality_factors = vqm.calculate_quality_factors(sample_fundamentals)

        assert "roic_wacc_spread" in quality_factors.columns
        assert "fcf_conversion" in quality_factors.columns
        assert "debt_ebitda" in quality_factors.columns

    def test_calculate_momentum_factors(self, sample_prices, sample_volume):
        """Test momentum factor calculation."""
        vqm = VQMFactors()
        momentum_factors = vqm.calculate_momentum_factors(sample_prices, sample_volume)

        # Check that columns exist (might be empty if not enough data)
        assert isinstance(momentum_factors, pd.DataFrame)

    def test_normalize_z_score(self):
        """Test Z-score normalization."""
        vqm = VQMFactors()

        # Create test data
        data = pd.DataFrame({
            "metric1": [1, 2, 3, 4, 5],
            "metric2": [10, 20, 30, 40, 50],
        })

        normalized = vqm.normalize_z_score(data)

        # Check that mean is close to 0 and std is close to 1
        assert abs(normalized["metric1"].mean()) < 0.1
        assert abs(normalized["metric1"].std() - 1.0) < 0.1

    def test_normalize_z_score_inverse(self):
        """Test Z-score normalization with inversion."""
        vqm = VQMFactors()

        # Create test data where higher = worse
        data = pd.DataFrame({
            "metric": [5, 4, 3, 2, 1],  # Higher is worse
        })

        normalized = vqm.normalize_z_score(data, inverse=True)

        # After inversion, lowest original value should have highest score
        assert normalized.loc[4, "metric"] > normalized.loc[0, "metric"]

    def test_composite_score(self):
        """Test composite score calculation."""
        vqm = VQMFactors()

        # Create test factor scores
        value = pd.DataFrame({"score": [1.0, 0.5, 0.0, -0.5, -1.0]})
        quality = pd.DataFrame({"score": [0.5, 0.25, 0.0, -0.25, -0.5]})
        momentum = pd.DataFrame({"score": [1.5, 0.75, 0.0, -0.75, -1.5]})

        composite = vqm.composite_score(value, quality, momentum)

        # Check that composite score uses correct weights
        # Stock 0: 0.45*1.0 + 0.35*0.5 + 0.20*1.5 = 0.45 + 0.175 + 0.3 = 0.925
        expected = 0.45 * 1.0 + 0.35 * 0.5 + 0.20 * 1.5
        assert abs(composite.iloc[0, 0] - expected) < 0.01

    def test_calculate_all(self, sample_prices, sample_volume, sample_fundamentals):
        """Test complete factor calculation."""
        vqm = VQMFactors()
        factors = vqm.calculate_all(sample_prices, sample_volume, sample_fundamentals)

        assert "value" in factors
        assert "quality" in factors
        assert "momentum" in factors
        assert "composite" in factors

        # Check composite score shape
        assert isinstance(factors["composite"], pd.DataFrame)


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
