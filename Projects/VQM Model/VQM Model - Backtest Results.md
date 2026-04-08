---
title: "VQM Model — Backtest Results (2019-2024)"
aliases: ["VQM Backtest Results", "ผลการทดสอบ VQM", "VQM Performance Report"]
tags: [📁/projects, 🏷️/vqm-model, 🏷️/backtest, 🏷️/results, 🏷️/validation]
created: 2026-04-06
modified: 2026-04-06
type: results
status: seed
links:
  - "[[VQM Model - Detailed Thesis Research Plan]]"
  - "[[VQM Model - Performance Analysis]]"
  - "[[VQM Model - Literature Research Compilation]]"
  - "[[Complete Reference List]]"
---

# VQM Model — Backtest Results (2019-2024)

> [!ABSTRACT] ผลการทดสอบ VQM Model กับข้อมูลจริง/จำลอง
> **Period:** 2019-2024 (5 years) | **Universe:** SET Main Board | **Rebalancing:** Quarterly

---

## 🎯 Executive Summary

> [!INFO] **Status:** 🚧 Waiting for backtest execution
> **Assigned:** Codex (Python implementation) | **QA:** Gemini

### Test Objectives

1. ✅ ทดสอบว่า VQM สร้าง Alpha > 3% ต่อปี
2. ✅ ทดสอบว่า Sharpe Ratio > SET Index
3. ✅ ทดสอบว่า Max Drawdown < SET Index
4. ✅ วิเคราะห์ผลประกอบตาม regime

---

## 📊 Performance Metrics (Pending Results)

| Metric | VQM Portfolio | SET Index | Alpha | Assessment |
|--------|---------------|-----------|-------|------------|
| **CAGR** | TBD | TBD | TBD | Target: > 3% |
| **Volatility** | TBD | TBD | - | Target: Lower |
| **Sharpe Ratio** | TBD | TBD | - | Target: > 1.0 |
| **Max Drawdown** | TBD | TBD | - | Target: < -25% |
| **Hit Rate** | TBD | - | - | Target: > 55% |

---

## 🧪 Hypotheses Testing Results

| Hypothesis | Expected | Result | Status |
|------------|----------|--------|--------|
| **H1:** VQM Sharpe > SET Sharpe | Sharpe_VQM > Sharpe_SET | TBD | ⏸️ Pending |
| **H2:** VQM outperforms single-factor | ΔSharpe > 0.15 | TBD | ⏸️ Pending |
| **H3:** Quality reduces downside | ΔMaxDD < -5% | TBD | ⏸️ Pending |
| **H4:** Robust across regimes | α > 0 in 3/4 regimes | TBD | ⏸️ Pending |
| **H5:** Net return positive after costs | NetAlpha > 2% | TBD | ⏸️ Pending |

---

## 📈 Regime Analysis (Pending)

### Regime Definitions

| Regime | Criteria | Periods (2019-2024) |
|--------|----------|---------------------|
| **Bull** | SET > 0% (6M) | 2019, 2021, 2023+ |
| **Bear** | SET < -10% (6M) | 2020 Q1-Q2 |
| **Neutral** | Between | 2022 |

### Performance by Regime

| Regime | VQM Return | SET Return | Alpha | Assessment |
|--------|------------|------------|-------|------------|
| **Bull** | TBD | TBD | TBD | ⏸️ Pending |
| **Bear** | TBD | TBD | TBD | ⏸️ Pending |
| **Neutral** | TBD | TBD | TBD | ⏸️ Pending |

---

## 🔍 Factor Attribution Analysis

### Value Component (45% weight)

| Metric | Value | Notes |
|--------|-------|-------|
| Contribution to Return | TBD | % of total return |
| Best Period | TBD | When value shined |
| Worst Period | TBD | When value lagged |

### Quality Component (35% weight)

| Metric | Quality | Notes |
|--------|---------|-------|
| Contribution to Return | TBD | % of total return |
| Drawdown Protection | TBD | Max DD reduction |
| Best Period | TBD | When quality shined |

### Momentum Component (20% weight)

| Metric | Momentum | Notes |
|--------|----------|-------|
| Contribution to Return | TBD | % of total return |
| Crash Risk | TBD | Did momentum crash? |
| Best Period | TBD | When momentum shined |

---

## 📂 Data Sources

| Data Type | Source | Period | Notes |
|-----------|--------|--------|-------|
| **Price Data** | SET / Mock | 2019-2024 | Daily close |
| **Fundamental** | SET / Mock | 2019-2024 | Quarterly |
| **Corporate Actions** | SET / Mock | 2019-2024 | Splits, dividends |
| **Risk-free Rate** | BOT | 2019-2024 | 3-month T-bill |

---

## 🔧 Methodology Notes

### Portfolio Construction

```
1. Filter: ADV > 20M THB (3-month avg)
2. Calculate VQM Score for all stocks
3. Rank by VQM Score (descending)
4. Select Top 20-30 stocks
5. Equal-weight with constraints:
   - Max 5% per stock
   - Max 30% per sector
```

### Rebalancing Rules

```
Frequency: Quarterly (Mar 31, Jun 30, Sep 30, Dec 31)
Execution: First trading day + 45 days lag
Turnover Cap: Max 50% per quarter
Transaction Cost: 0.35% one-way (0.70% round-trip)
```

### Scoring Formula

```
VQM_Score = 0.45 × Rank(Value) + 0.35 × Rank(Quality) + 0.20 × Rank(Momentum)

Where:
- Value = FCF Yield, P/E Relative, EV/EBITDA
- Quality = ROIC - WACC, FCF Conversion, Debt/EBITDA
- Momentum = 6-Month Price Return, Volume Trend
```

---

## 📝 Execution Log

| Date | Action | Owner | Status |
|------|--------|-------|--------|
| 2026-04-06 | Template created | obb | ✅ Complete |
| 2026-04-06 | Mock data generation | Codex | 🚧 In Progress |
| 2026-04-06 | Backtest execution | Codex | 📋 Pending |
| 2026-04-06 | QA review | Gemini | 📋 Pending |
| 2026-04-06 | Results interpretation | Damodaran | 📋 Pending |
| 2026-04-06 | Documentation update | obb | 📋 Pending |

---

## 🔗 Linked References

- [[VQM Model - Detailed Thesis Research Plan]] — แผนวิจัยรายละเอียด
- [[VQM Model - Performance Analysis]] — วิเคราะห์ผลประกอบ
- [[VQM Model - Literature Research Compilation]] — ทบทวนวรรณกรรม
- [[Complete Reference List]] — รายการอ้างอิงครบถ้วน

---

## 📚 แหล่งข้อมูล

- SET Historical Data
- Python: `factors.py`, `backtest.py`, `test_factors.py`
- Mock Data Generator (Codex)

---

*Document created: 2026-04-06*
*Last updated: 2026-04-06*
*Status: 🚧 Waiting for backtest execution*
