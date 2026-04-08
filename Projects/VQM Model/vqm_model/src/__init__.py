"""
VQM Model — Integrated Value-Quality-Momentum Model

A multi-factor stock selection model for the Thai stock market.
"""

__version__ = "1.0.0"
__author__ = "VQM Research Team"

from .data_loader import SETDataLoader
from .factors import VQMFactors
from .portfolio import PortfolioConstructor
from .backtest import WalkForwardBacktest

__all__ = [
    "SETDataLoader",
    "VQMFactors",
    "PortfolioConstructor",
    "WalkForwardBacktest",
]
