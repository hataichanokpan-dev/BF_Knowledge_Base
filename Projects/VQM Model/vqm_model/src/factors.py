"""
VQM Factor Calculations

Module for calculating Value, Quality, and Momentum factors
according to the VQM Model methodology.

Reference: Factor Calculation Formulas.md
"""

import numpy as np
import pandas as pd
from typing import Dict, Tuple


class VQMFactors:
    """
    Calculate VQM (Value-Quality-Momentum) factors for stock selection.

    Weights:
    - Value: 45%
    - Quality: 35%
    - Momentum: 20%
    """

    # Factor weights
    VALUE_WEIGHT = 0.45
    QUALITY_WEIGHT = 0.35
    MOMENTUM_WEIGHT = 0.20

    # Value sub-weights
    FCF_YIELD_WEIGHT = 0.40
    PB_WEIGHT = 0.30
    PE_WEIGHT = 0.30

    # Quality sub-weights
    ROIC_WACC_WEIGHT = 0.50
    FCF_CONV_WEIGHT = 0.30
    DEBT_EBITDA_WEIGHT = 0.20

    # Momentum sub-weights
    PRICE_6M_WEIGHT = 0.70
    VOLUME_TREND_WEIGHT = 0.30

    def __init__(self):
        self.factor_data = None

    def calculate_value_factors(
        self,
        prices: pd.DataFrame,
        fundamentals: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate Value factors (45% weight).

        Factors:
        - FCF Yield: FCF / Enterprise Value
        - P/B Ratio: Price / Book Value
        - P/E Ratio: Price / Earnings

        Args:
            prices: DataFrame with prices (index: date, columns: tickers)
            fundamentals: DataFrame with fundamental data

        Returns:
            DataFrame with value factors (normalized)
        """
        value_factors = pd.DataFrame(index=prices.index, columns=prices.columns)

        # FCF Yield (higher is better)
        if "free_cash_flow" in fundamentals.columns and "enterprise_value" in fundamentals.columns:
            fcf_yield = fundamentals["free_cash_flow"] / fundamentals["enterprise_value"]
            value_factors["fcf_yield"] = fcf_yield

        # P/B Ratio (lower is better)
        if "price_to_book" in fundamentals.columns:
            pb_ratio = fundamentals["price_to_book"]
            value_factors["pb_ratio"] = pb_ratio

        # P/E Ratio (lower is better)
        if "price_to_earnings" in fundamentals.columns:
            pe_ratio = fundamentals["price_to_earnings"]
            value_factors["pe_ratio"] = pe_ratio

        return value_factors

    def calculate_quality_factors(
        self,
        fundamentals: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate Quality factors (35% weight).

        Factors:
        - ROIC - WACC Spread
        - FCF Conversion: FCF / Net Income
        - Debt/EBITDA (lower is better)

        Args:
            fundamentals: DataFrame with fundamental data

        Returns:
            DataFrame with quality factors (normalized)
        """
        quality_factors = pd.DataFrame()

        # ROIC - WACC Spread (higher is better)
        if "roic" in fundamentals.columns and "wacc" in fundamentals.columns:
            roic_wacc = fundamentals["roic"] - fundamentals["wacc"]
            quality_factors["roic_wacc_spread"] = roic_wacc

        # FCF Conversion (higher is better)
        if "free_cash_flow" in fundamentals.columns and "net_income" in fundamentals.columns:
            fcf_conv = fundamentals["free_cash_flow"] / fundamentals["net_income"]
            quality_factors["fcf_conversion"] = fcf_conv

        # Debt/EBITDA (lower is better)
        if "total_debt" in fundamentals.columns and "ebitda" in fundamentals.columns:
            debt_ebitda = fundamentals["total_debt"] / fundamentals["ebitda"]
            quality_factors["debt_ebitda"] = debt_ebitda

        return quality_factors

    def calculate_momentum_factors(
        self,
        prices: pd.DataFrame,
        volume: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate Momentum factors (20% weight).

        Factors:
        - Price 6M: 6-month price momentum (skip 1 month)
        - Volume Trend: MA(20) / MA(60)

        Args:
            prices: DataFrame with prices
            volume: DataFrame with trading volume

        Returns:
            DataFrame with momentum factors (normalized)
        """
        momentum_factors = pd.DataFrame(index=prices.index, columns=prices.columns)

        # Price 6M Momentum (skip 1 month to avoid short-term reversal)
        for ticker in prices.columns:
            price_series = prices[ticker].dropna()
            if len(price_series) >= 126:  # ~6 months of trading days
                # Calculate 6M return starting from 1 month ago
                momentum_6m = (price_series.iloc[-1] / price_series.iloc[-127]) - 1
                momentum_factors.loc[price_series.index[-1], ticker] = momentum_6m

        # Volume Trend
        for ticker in volume.columns:
            vol_series = volume[ticker].dropna()
            if len(vol_series) >= 60:
                vol_ma_20 = vol_series.iloc[-20:].mean()
                vol_ma_60 = vol_series.iloc[-60:].mean()
                vol_trend = vol_ma_20 / vol_ma_60 if vol_ma_60 != 0 else 1
                momentum_factors.loc[vol_series.index[-1], ticker] = vol_trend

        return momentum_factors

    def normalize_z_score(
        self,
        df: pd.DataFrame,
        inverse: bool = False,
    ) -> pd.DataFrame:
        """
        Normalize using Z-score with Median Absolute Deviation (MAD).

        Z = (X - Median) / (1.4826 × MAD)

        Args:
            df: DataFrame to normalize
            inverse: If True, invert the score (for "lower is better" metrics)

        Returns:
            Normalized DataFrame
        """
        normalized = pd.DataFrame(index=df.index, columns=df.columns)

        for col in df.columns:
            series = df[col].dropna()
            if len(series) == 0:
                continue

            median = series.median()
            mad = (series - median).abs().median()

            if mad == 0:
                normalized[col] = 0
            else:
                z_score = (series - median) / (1.4826 * mad)
                if inverse:
                    z_score = -z_score
                normalized[col] = z_score

        return normalized

    def composite_score(
        self,
        value_factors: pd.DataFrame,
        quality_factors: pd.DataFrame,
        momentum_factors: pd.DataFrame,
    ) -> pd.DataFrame:
        """
        Calculate composite VQM score.

        VQM = 0.45 × Value + 0.35 × Quality + 0.20 × Momentum

        Args:
            value_factors: Normalized value factors
            quality_factors: Normalized quality factors
            momentum_factors: Normalized momentum factors

        Returns:
            DataFrame with composite VQM scores
        """
        # Value Score (45%)
        value_score = pd.DataFrame(0, index=value_factors.index, columns=value_factors.columns)
        if "fcf_yield" in value_factors.columns:
            value_score += self.FCF_YIELD_WEIGHT * value_factors["fcf_yield"]
        if "pb_ratio" in value_factors.columns:
            value_score += self.PB_WEIGHT * (-value_factors["pb_ratio"])  # Inverted
        if "pe_ratio" in value_factors.columns:
            value_score += self.PE_WEIGHT * (-value_factors["pe_ratio"])  # Inverted

        # Quality Score (35%)
        quality_score = pd.DataFrame(0, index=quality_factors.index, columns=quality_factors.columns)
        if "roic_wacc_spread" in quality_factors.columns:
            quality_score += self.ROIC_WACC_WEIGHT * quality_factors["roic_wacc_spread"]
        if "fcf_conversion" in quality_factors.columns:
            quality_score += self.FCF_CONV_WEIGHT * quality_factors["fcf_conversion"]
        if "debt_ebitda" in quality_factors.columns:
            quality_score += self.DEBT_EBITDA_WEIGHT * (-quality_factors["debt_ebitda"])  # Inverted

        # Momentum Score (20%)
        momentum_score = pd.DataFrame(0, index=momentum_factors.index, columns=momentum_factors.columns)
        if "price_6m" in momentum_factors.columns:
            momentum_score += self.PRICE_6M_WEIGHT * momentum_factors["price_6m"]
        if "volume_trend" in momentum_factors.columns:
            momentum_score += self.VOLUME_TREND_WEIGHT * momentum_factors["volume_trend"]

        # Composite Score
        vqm_score = (
            self.VALUE_WEIGHT * value_score
            + self.QUALITY_WEIGHT * quality_score
            + self.MOMENTUM_WEIGHT * momentum_score
        )

        return vqm_score

    def calculate_all(
        self,
        prices: pd.DataFrame,
        volume: pd.DataFrame,
        fundamentals: pd.DataFrame,
    ) -> Dict[str, pd.DataFrame]:
        """
        Calculate all VQM factors and composite score.

        Args:
            prices: Price data
            volume: Volume data
            fundamentals: Fundamental data

        Returns:
            Dictionary with:
            - 'value': Normalized value factors
            - 'quality': Normalized quality factors
            - 'momentum': Normalized momentum factors
            - 'composite': VQM composite score
        """
        # Calculate raw factors
        value_raw = self.calculate_value_factors(prices, fundamentals)
        quality_raw = self.calculate_quality_factors(fundamentals)
        momentum_raw = self.calculate_momentum_factors(prices, volume)

        # Normalize
        value_norm = self.normalize_z_score(value_raw)
        quality_norm = self.normalize_z_score(quality_raw)
        momentum_norm = self.normalize_z_score(momentum_raw)

        # Composite score
        composite = self.composite_score(value_norm, quality_norm, momentum_norm)

        self.factor_data = {
            "value": value_norm,
            "quality": quality_norm,
            "momentum": momentum_norm,
            "composite": composite,
        }

        return self.factor_data
