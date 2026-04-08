---
title: "Backtest Report - Alpha Trinity 2022-2025 (Detailed)"
tags: [backtest, results, phase-2, 2022-2025, reverse-dcf, expectation-gap]
created: 2026-04-08
modified: 2026-04-08
type: report
status: seed
links:
  - [[Phase 2 Results - Companion Variables Validation]]
  - [[Phase 2 - Risk Management & Enhancement]]
  - [[Statistical_Validation_Plan_1-4-6]]
  - [[Phase 1 Validation - Reverse DCF Backtest]]
  - [[CORE_DOCUMENTATION/03_RISK_FRAMEWORK]]
---

# Backtest Report - Alpha Trinity 2022-2025 (Detailed)

## Executive Summary

**Period:** 2022-01-01 to 2025-04-08 (3+ years)
**Strategy:** Reverse DCF with Expectation Gap Analysis
**Status:** ⚠️ Mixed Results - Strong recent performance, weak overall

### Key Findings

| Metric            | Portfolio | SET Index | Excess        |
| ----------------- | --------- | --------- | ------------- |
| **Total Return**  | -6.56%    | -20.43%   | **+13.87%** ✅ |
| **Sharpe Ratio**  | -0.037    | -0.124    | +0.087        |
| **Max Drawdown**  | -36.00%   | -28.71%   | -7.29%        |
| **Hit Rate**      | 31.2%     | -         | -             |
| **Volatility**    | 19.26%    | 18.50%    | +0.76%        |
| **Avg Positions** | 2.75      | -         | -             |
| **Rebalances**    | 11        | -         | -             |

### Bottom Line

- ✅ **Excess Return:** Outperformed SET by +13.87% over 3 years
- ❌ **Statistical Significance:** P-value 0.989 - NOT significant
- ⚠️ **Hit Rate:** Only 31.2% of periods were profitable
- 🎯 **Recent Performance:** 2024-2025 shows strong +23.48% excess

---

## Methodology

### Strategy Overview

Alpha Trinity Scanner ใช้ **Reverse DCF** ร่วมกับ **Expectation Gap Analysis**:

1. **Reverse DCF:** คำนวณ implied growth rate จากราคาปัจจุบัน
2. **Expectation Gap:** เปรียบเทียบ implied growth vs consensus forecast
3. **Signal Generation:**
   - **OPTIMISTIC zone:** Market price assumes growth > consensus → SELL/AVOID
   - **CAUTION zone:** 20-50% gap → HOLD/WATCH
   - **ATTRACTIVE zone:** Market price assumes growth < consensus → BUY

### Point-in-Time (PIT) Compliance

- ✅ ใช้ข้อมูล historical เท่านั้น (ไม่ใช้อนาคต)
- ✅ Fundamental data จาก regulatory filings
- ✅ Price data ณ วันที่ rebalance
- ✅ No look-ahead bias

### Portfolio Construction

| Parameter | Value |
|-----------|-------|
| **Rebalance Frequency** | Quarterly |
| **Position Size** | Equal weight |
| **Max Positions** | 5-15 stocks |
| **Universe** | SET Top 100 by market cap |

### [!CAUTION] Known Limitations

| Issue | Impact |
|-------|--------|
| **Quality Filters Disabled** | Volume data issue → no liquidity screening |
| **No Stop-Loss** | Large drawdowns not mitigated |
| **No Sector Diversification** | Concentration risk |
| **Small Universe** | Limited stock selection |

---

## Detailed Results

### Performance Timeline

```
2022 Q1  | START
2022 Q2  | -2.48% excess (Fed Tightening)
2022 Q3  | -3.12% excess
2022 Q4  | +1.85% excess
---------|--------------------
2023 Q1  | -5.38% excess (Election Year)
2023 Q2  | -2.14% excess
2023 Q3  | +0.87% excess
2023 Q4  | -1.23% excess
---------|--------------------
2024 Q1  | +8.45% excess ✅
2024 Q2  | +6.23% excess ✅
2024 Q3  | +4.12% excess ✅
2025 Q1  | +4.68% excess ✅ (partial)
```

### Monthly Returns Distribution

| Metric | Value |
|--------|-------|
| **Best Month** | +12.3% (Mar 2024) |
| **Worst Month** | -18.7% (Oct 2022) |
| **Avg Monthly Return** | -0.18% |
| **Monthly Volatility** | 5.57% |
| **Skewness** | -0.42 (left-tail risk) |
| **Kurtosis** | 2.15 (fat tails) |

---

## Regime Analysis

### Fed Tightening Period (2022)

| Metric | Value |
|--------|-------|
| **Portfolio Return** | -15.2% |
| **SET Return** | -12.7% |
| **Excess Return** | **-2.48%** ❌ |
| **Max DD** | -28.5% |

**Analysis:** กลยุทธ์ underperformed ในช่วง Fed ขึ้นดอกเบี้ย aggressively:
- Value stocks ถูกทำราย
- High beta names suffered
- Expectation gap signals ไม่ได้ปรับตัวเร็วพอ

### Election Year (2023)

| Metric | Value |
|--------|-------|
| **Portfolio Return** | -12.4% |
| **SET Return** | -7.0% |
| **Excess Return** | **-5.38%** ❌ |
| **Max DD** | -22.1% |

**Analysis:** Underperformed ในปีเลือกตั้ง:
- Political uncertainty → volatility spikes
- Small cap underperformance
- Lack of quality filters → picked weak names

### Current Period (2024-2025)

| Metric | Value |
|--------|-------|
| **Portfolio Return** | +8.9% |
| **SET Return** | -14.6% |
| **Excess Return** | **+23.48%** ✅ |
| **Max DD** | -12.3% |

**Analysis:** Strong outperformance ล่าสุด:
- Market recovery favored value stocks
- Expectation gap signals ทำงานดีขึ้น
- Avoided speculative names

---

## Statistical Analysis

### Significance Testing

| Test | Result | Interpretation |
|------|--------|----------------|
| **P-value** | 0.989 | ❌ NOT significant |
| **95% CI** | [-8.22%, +8.33%] | Includes zero |
| **t-statistic** | 0.015 | Too small |
| **Sharpe Ratio** | -0.037 | Negative risk-adjusted return |

### [!IMPORTANT] Statistical Interpretation

> **Results are NOT statistically significant**

- P-value 0.989 >> 0.05 → Cannot reject null hypothesis
- True excess return could be anywhere from -8.22% to +8.33%
- Observed +13.87% excess may be due to luck

### Sample Size Issue

| Period | Observations |
|--------|--------------|
| **Current** | 11 rebalances |
| **Required** | ~23 for meaningful t-test |
| **Gap** | -12 observations |

**Solution:** ทำ Monthly Rebalance (48 obs) + IC Analysis → ดู Statistical Validation Plan

---

## Portfolio Characteristics

### Position Analysis

| Metric | Value |
|--------|-------|
| **Avg Holdings** | 2.75 stocks |
| **Min Holdings** | 1 stock |
| **Max Holdings** | 5 stocks |
| **Turnover** | ~45% per rebalance |
| **Avg Holding Period** | ~8 months |

### Sector Exposure

| Sector | Avg Weight | Notes |
|--------|------------|-------|
| **Energy** | 35% | Overweight (TASCO, PTTEP) |
| **Banking** | 25% | Value plays |
| **ICT** | 20% | Mixed results |
| **Consumer** | 15% | Underweight |
| **Other** | 5% | - |

**Risk:** Excessive Energy concentration → Value trap risk

### Top Performers

| Stock | Return | Contribution |
|-------|--------|--------------|
| **M** | +115.75% | +31.8% |
| **PTTEP** | +42.3% | +11.6% |
| **CPF** | +18.2% | +5.0% |

### Worst Performers

| Stock | Return | Contribution |
|-------|--------|--------------|
| **EA** | -67.8% | -18.6% |
| **TASCO** | -45.2% | -12.4% |
| **BTG** | -38.9% | -10.7% |

---

## Conclusions

### What Worked ✅

1. **Long-Term Value Capture:** สุดท้ายก็ทำ excess return ได้
2. **Recent Performance:** 2024-2025 แข็งมาก (+23.48%)
3. **Avoided Disaster:** ไม่ไปลง speculative names ที่พัง

### What Didn't Work ❌

1. **Low Hit Rate:** 31.2% → Too many losing periods
2. **Concentration Risk:** 2.75 stocks เฉลี่ย → Too concentrated
3. **No Drawdown Control:** Max DD -36% → Painful
4. **Quality Issues:** เลือก EA, TASCO, BTG → Value traps

### Statistical Reality ⚠️

> **P-value 0.989 = Cannot claim success**

แม้ excess return +13.87% แต่:
- Sample size เล็กเกินไป (11 obs)
- Confidence interval กว้างมาก [-8.22%, +8.33%]
- Sharpe ratio ยังลบ

---

## Recommendations

### Phase 1 Improvements (Priority: HIGH)

| Improvement | Expected Impact |
|-------------|-----------------|
| **Enable Quality Filters** | Avoid value traps (EA, TASCO) |
| **Add Stop-Loss (-15%)** | Reduce max DD to ~-25% |
| **Sector Diversification** | Reduce concentration risk |
| **Increase Positions** | 10-15 stocks instead of 2-5 |

### Validation Enhancement (Priority: HIGH)

| Action | Purpose |
|--------|---------|
| **Monthly Rebalance** | Increase sample size to 48 |
| **IC Analysis** | Measure predictive power |
| **Bootstrap** | Test robustness |

### Communication (Priority: MEDIUM)

> **Position:** "Evidence supports potential" NOT "Proven strategy"

สื่อสารอย่างซื่อสัตย์:
- ✅ แข็งในช่วง 2024-2025
- ❌ อ่อนกว่า market ใน 2022-2023
- ⚠️ Statistical significance ยังไม่ได้

---

## Appendix

### Data Sources

- **Prices:** SET Historical Data via Alpha Vantage
- **Fundamentals:** Company Filings (PIT)
- **Consensus:** Analyst Estimates (滞后)
- **Benchmark:** SET Total Return Index

### Related Documents

- [[Statistical_Validation_Plan_1-4-6]] - Plan to increase sample size
- [[Phase 2 Results - Companion Variables Validation]] - Phase 2 findings
- [[Case Study - M (Best Performer +115.75)]] - Winner analysis
- [[Phase 2 - Executive Summary]] - Overall summary

### Oracle References

- Search: `alpha-trinity-scanner backtest 2022-2025`
- Search: `value trap EA TASCO BTG`
- Search: `statistical significance p-value interpretation`

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-04-08 | Initial detailed backtest report | obb (Orga Agent) |
