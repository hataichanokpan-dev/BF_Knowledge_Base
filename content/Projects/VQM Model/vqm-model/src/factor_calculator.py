"""
VQM Model - Factor Calculator
Calculates Value, Quality, and Momentum factors for SET stocks
"""

import numpy as np
import pandas as pd
from typing import Dict, List
import warnings
warnings.filterwarnings('ignore')


class VQMFactorCalculator:
    """Calculate VQM factors for all stocks"""

    def __init__(self):
        self.factors = {
            'value': ['fcf_yield', 'pe_relative', 'pb_relative', 'ev_ebitda_inv'],
            'quality': ['roic_spread', 'fcf_conversion', 'debt_ebitda_inv', 'gross_margin'],
            'momentum': ['price_6m', 'earnings_revision', 'volume_trend']
        }

    def calculate_value_factors(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate Value factor metrics"""
        print("Calculating Value factors...")

        result = df.copy()

        # Ensure sector column exists
        if 'sector_y' in result.columns:
            result['sector'] = result['sector_y'].fillna(result['sector_x'])
        elif 'sector_x' in result.columns:
            result['sector'] = result['sector_x']

        # FCF Yield = FCF / Enterprise Value
        # Approximate: FCF / (Market Cap + Debt - Cash)
        result['fcf_yield'] = result['fcf'] / (
            result['market_cap'] + result['total_debt'] - result['cash']
        )
        result['fcf_yield'] = result['fcf_yield'].fillna(0).replace([np.inf, -np.inf], 0)

        # P/E Relative = P/E / Sector Median P/E
        # Use reported PE
        result['pe_relative'] = result.groupby(['date', 'sector'])['pe'].transform(
            lambda x: x / x.median() if x.median() > 0 else 1
        )

        # P/B Relative = P/B / Sector Median P/B
        result['pb_relative'] = result.groupby(['date', 'sector'])['pb'].transform(
            lambda x: x / x.median() if x.median() > 0 else 1
        )

        # EV/EBITDA (invert for scoring: lower is better)
        result['ev_ebitda_inv'] = -1 / result['ev_ebitda'].replace(0, np.nan).fillna(result['ev_ebitda'].median())

        return result

    def calculate_quality_factors(self, df: pd.DataFrame) -> pd.DataFrame:
        """Calculate Quality factor metrics"""
        print("Calculating Quality factors...")

        result = df.copy()

        # ROIC Spread = ROIC - WACC
        result['roic_spread'] = result['roic'] - result['wacc']

        # FCF Conversion = FCF / Net Income
        result['fcf_conversion'] = result['fcf_conversion'].fillna(0)

        # Debt/EBITDA (invert: lower is better)
        result['debt_ebitda_inv'] = -1 / result['debt_ebitda'].replace(0, np.nan)

        # Gross Margin
        result['gross_margin'] = result['gross_margin'].fillna(0)

        return result

    def calculate_momentum_factors(self, price_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate Momentum factor metrics"""
        print("Calculating Momentum factors...")

        result = price_df.copy()

        # Price 6-Month Momentum = (Price_t / Price_t-126) - 1
        # ~126 trading days = 6 months
        result['price_6m'] = result.groupby('symbol')['close'].transform(
            lambda x: (x / x.shift(126)) - 1
        )

        # Volume Trend = MA(20) / MA(60)
        result['volume_ma20'] = result.groupby('symbol')['volume'].transform(
            lambda x: x.rolling(20).mean()
        )
        result['volume_ma60'] = result.groupby('symbol')['volume'].transform(
            lambda x: x.rolling(60).mean()
        )
        result['volume_trend'] = result['volume_ma20'] / result['volume_ma60']

        # Earnings Revision (simplified: use recent ROIC trend)
        # In real implementation, would use analyst estimate revisions
        result['earnings_revision'] = result.groupby('symbol')['roic'].transform(
            lambda x: (x.fillna(method='ffill') - x.shift(63).fillna(method='ffill'))
        )

        # Fill NaN momentum with 0
        momentum_cols = ['price_6m', 'volume_trend', 'earnings_revision']
        for col in momentum_cols:
            result[col] = result[col].fillna(0)

        return result

    def calculate_all_factors(self, price_df: pd.DataFrame, financial_df: pd.DataFrame) -> pd.DataFrame:
        """Calculate all VQM factors"""
        print("=" * 50)
        print("Calculating all VQM factors...")
        print("=" * 50)

        # Merge price and financial data
        # For each date, use the most recent financial data available
        financial_df['report_date'] = pd.to_datetime(financial_df['report_date'])
        price_df['date'] = pd.to_datetime(price_df['date'])

        # Sort and merge with asof to get latest financials
        financial_sorted = financial_df.sort_values('report_date')
        price_sorted = price_df.sort_values('date')

        merged = pd.merge_asof(
            price_sorted,
            financial_sorted,
            left_on='date',
            right_on='report_date',
            by='symbol',
            direction='backward'
        )

        # Calculate factor groups
        merged = self.calculate_value_factors(merged)
        merged = self.calculate_quality_factors(merged)
        merged = self.calculate_momentum_factors(merged)

        # Filter to complete data
        factor_cols = (
            self.factors['value'] +
            self.factors['quality'] +
            self.factors['momentum']
        )

        # Replace inf with NaN
        for col in factor_cols:
            if col in merged.columns:
                merged[col] = merged[col].replace([np.inf, -np.inf], np.nan)

        print(f"[OK] Calculated {len(factor_cols)} factors")
        print(f"[OK] Data points: {len(merged):,}")

        return merged


class VQMScorer:
    """Calculate VQM composite scores using robust z-scores"""

    def __init__(self, weights=None):
        self.weights = weights or {
            'value': 0.45,
            'quality': 0.35,
            'momentum': 0.20
        }

    def robust_z_score(self, series: pd.Series) -> pd.Series:
        """Calculate MAD-based robust z-score"""
        median = series.median()
        mad = (series - median).abs().median()

        if mad == 0:
            return pd.Series([0] * len(series), index=series.index)

        return (series - median) / (1.4826 * mad)

    def calculate_group_score(self, df: pd.DataFrame, columns: List[str], date: str) -> pd.Series:
        """Calculate composite score for a factor group"""
        subset = df[df['date'] == date].copy()

        # Handle missing columns
        available_cols = [c for c in columns if c in subset.columns]
        if not available_cols:
            return pd.Series([0] * len(subset), index=subset.index)

        # Calculate z-scores for each metric
        z_scores = pd.DataFrame(index=subset.index)

        for col in available_cols:
            z_scores[col] = self.robust_z_score(subset[col].fillna(subset[col].median()))

        # Average z-scores
        score = z_scores.mean(axis=1)

        return score

    def calculate_vqm_score(self, df: pd.DataFrame, date: str) -> pd.DataFrame:
        """Calculate VQM composite score for a specific date"""
        subset = df[df['date'] == date].copy()

        # Calculate group scores
        value_score = self.calculate_group_score(
            df,
            ['fcf_yield', 'pe_relative', 'pb_relative', 'ev_ebitda_inv'],
            date
        )
        quality_score = self.calculate_group_score(
            df,
            ['roic_spread', 'fcf_conversion', 'debt_ebitda_inv', 'gross_margin'],
            date
        )
        momentum_score = self.calculate_group_score(
            df,
            ['price_6m', 'earnings_revision', 'volume_trend'],
            date
        )

        # Composite VQM score
        subset['value_score'] = value_score.values
        subset['quality_score'] = quality_score.values
        subset['momentum_score'] = momentum_score.values
        subset['vqm_score'] = (
            self.weights['value'] * subset['value_score'] +
            self.weights['quality'] * subset['quality_score'] +
            self.weights['momentum'] * subset['momentum_score']
        )

        return subset


def calculate_all_scores(factor_df: pd.DataFrame) -> pd.DataFrame:
    """Calculate VQM scores for all dates"""
    print("=" * 50)
    print("Calculating VQM scores for all dates...")
    print("=" * 50)

    scorer = VQMScorer()
    all_scores = []

    unique_dates = sorted(factor_df['date'].unique())

    # Only calculate at rebalancing points (quarterly)
    # Approximate quarterly dates
    rebalance_dates = []
    for i in range(0, len(unique_dates), 63):  # ~63 trading days per quarter
        if i < len(unique_dates):
            rebalance_dates.append(unique_dates[i])

    print(f"Rebalancing dates: {len(rebalance_dates)}")

    for date in rebalance_dates:
        score_df = scorer.calculate_vqm_score(factor_df, date)
        all_scores.append(score_df)

    result = pd.concat(all_scores, ignore_index=True)

    print(f"[OK] Calculated scores for {len(result)} stock-date observations")

    return result, rebalance_dates


if __name__ == '__main__':
    # Test the calculator
    print("VQM Factor Calculator - Ready")
    print("Use this module with price and financial data")
