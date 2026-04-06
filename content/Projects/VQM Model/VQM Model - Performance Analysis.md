---
title: "VQM Model — Performance Analysis"
aliases: ["VQM Performance Analysis", "วิเคราะห์ผลประกอบ VQM", "VQM Factor Attribution"]
tags: [📁/projects, 🏷️/vqm-model, 🏷️/analysis, 🏷️/factor-attribution, 🏷️/regime-analysis]
created: 2026-04-06
modified: 2026-04-06
type: analysis
status: seed
links:
  - "[[VQM Model - Backtest Results]]"
  - "[[Value Factor Papers]]"
  - "[[Quality Factor Papers]]"
  - "[[Momentum Factor Papers]]"
  - "[[Multi-Factor Models]]"
  - "[[Market Regimes Research]]"
---

# VQM Model — Performance Analysis

> [!ABSTRACT] วิเคราะห์ผลประกอบและประสิทธิผลของ VQM Model
> **Status:** 🚧 Waiting for backtest results

---

## 🎯 Analysis Overview

เอกสารนี้วิเคราะห์:
1. **Factor Attribution** — แต่ละปัจจัยส่งผลต่อผลตอบแทนอย่างไร
2. **Regime Analysis** — ผลงานใน market conditions ต่างกัน
3. **Risk Analysis** — ความเสี่ยงและการควบคุม drawdown
4. **Sensitivity Analysis** — ผลของการเปลี่ยนแปลง parameters

---

## 📊 Factor Attribution

### Value Component (45% weight)

> [!INFO] **Hypothesis:** Value stocks ให้ผลตอบแทนดีกว่าระยะยาว แต่มีความผันผวนสูง

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| **Contribution to Return** | Leading factor | TBD | ⏸️ Pending |
| **Best Period** | Bull markets | TBD | ⏸️ Pending |
| **Worst Period** | Momentum crashes | TBD | ⏸️ Pending |
| **Correlation with Quality** | Positive | TBD | ⏸️ Pending |
| **Correlation with Momentum** | **Negative** | TBD | ⏸️ Pending |

**Key Metrics:**
```
Value_Score = 0.40 × FCF_Yield_Rank
            + 0.30 × PE_Relative_Rank
            + 0.30 × EV_EBITDA_Rank
```

### Quality Component (35% weight)

> [!INFO] **Hypothesis:** Quality stocks มี downside protection ดีกว่า

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| **Contribution to Return** | Moderate + steady | TBD | ⏸️ Pending |
| **Drawdown Protection** | **Strongest** | TBD | ⏸️ Pending |
| **Best Period** | Bear markets | TBD | ⏸️ Pending |
| **Worst Period** | Speculative bubbles | TBD | ⏸️ Pending |

**Key Metrics:**
```
Quality_Score = 0.40 × ROIC_WACC_Spread_Rank
              + 0.30 × FCF_Conversion_Rank
              + 0.30 × Debt_EBITDA_Rank
```

### Momentum Component (20% weight)

> [!WARNING] **Hypothesis:** Momentum เพิ่มผลตอบแทนแต่เพิ่มความเสี่ยงด้วย

| Metric | Expected | Actual | Status |
|--------|----------|--------|--------|
| **Contribution to Return** | High + volatile | TBD | ⏸️ Pending |
| **Crash Risk** | **High** | TBD | ⏸️ Pending |
| **Best Period** | Trending markets | TBD | ⏸️ Pending |
| **Worst Period** | Regime switches | TBD | ⏸️ Pending |

**Key Metrics:**
```
Momentum_Score = 0.60 × Price_6M_Rank
               + 0.40 × Volume_Trend_Rank
```

---

## 📈 Regime Analysis

### Bull Market Performance

| Metric | VQM | SET | Best Factor |
|--------|-----|-----|-------------|
| **Return** | TBD | TBD | Expected: Momentum |
| **Volatility** | TBD | TBD | - |
| **Sharpe** | TBD | TBD | - |

**Expected Behavior:**
- Momentum เป็น driver หลัก
- Value สมดุลผล
- Quality ไม่โดดเด่น

### Bear Market Performance

| Metric | VQM | SET | Best Factor |
|--------|-----|-----|-------------|
| **Return** | TBD | TBD | Expected: Quality |
| **Max DD** | TBD | TBD | Expected: Lower |
| **Recovery** | TBD | TBD | - |

**Expected Behavior:**
- Quality เป็น protector หลัก
- Value เริ่มทำงานหลัง crash
- Momentum อาจ crash

### Volatility Regime

| Metric | VQM | SET | Best Factor |
|--------|-----|-----|-------------|
| **Return** | TBD | TBD | Expected: Mixed |
| **Volatility** | TBD | TBD | Expected: Lower |
| **Hit Rate** | TBD | TBD | - |

---

## 🔍 Risk Analysis

### Drawdown Analysis

| Metric | VQM | SET | Improvement |
|--------|-----|-----|-------------|
| **Max Drawdown** | Target: < -25% | -35% (2020) | TBD |
| **Avg Drawdown** | Target: < SET | TBD | TBD |
| **Recovery Time** | Target: < SET | TBD | TBD |

### Volatility Analysis

| Metric | VQM | SET | Assessment |
|--------|-----|-----|------------|
| **Annual Volatility** | TBD | TBD | Target: Lower |
| **Downside Volatility** | TBD | TBD | Target: Significantly lower |
| **Sortino Ratio** | TBD | TBD | Target: > SET |

### Correlation Analysis

| Factor Pair | Correlation | Interpretation |
|-------------|-------------|----------------|
| **Value × Quality** | Slightly Positive | Diversified |
| **Value × Momentum** | **Strongly Negative** | Excellent diversification |
| **Quality × Momentum** | Slightly Negative | Good diversification |

---

## 🧪 Sensitivity Analysis

### Weight Variations

| Scenario | Value | Quality | Momentum | Expected Sharpe |
|----------|-------|---------|----------|-----------------|
| **Baseline** | 45% | 35% | 20% | TBD |
| **Value-Heavy** | 55% | 25% | 20% | TBD |
| **Quality-Heavy** | 35% | 45% | 20% | TBD |
| **Momentum-Heavy** | 40% | 30% | 30% | TBD |
| **Equal Weight** | 33% | 33% | 34% | TBD |

### Parameter Variations

| Parameter | Baseline | Alternative | Impact |
|-----------|----------|-------------|--------|
| **Rebalancing** | Quarterly | Monthly | Higher turnover |
| **Universe Size** | 20-30 stocks | 40-50 stocks | Diversification |
| **ADV Filter** | 20M THB | 10M THB | More small caps |
| **Sector Cap** | 30% | 20% | Lower concentration |

---

## 📝 Key Findings Template

> [!NOTE] **จะเติมเมื่อมีผล backtest**

### Finding 1: [Title]

**Observation:**
-

**Explanation:**
-

**Implication:**
-

### Finding 2: [Title]

**Observation:**
-

**Explanation:**
-

**Implication:**
-

---

## 🔗 Linked References

- [[VQM Model - Backtest Results]] — ผลการทดสอบหลัก
- [[Value Factor Papers]] — เอกสารปัจจัยมูลค่า
- [[Quality Factor Papers]] — เอกสารปัจจัยคุณภาพ
- [[Momentum Factor Papers]] — เอกสารปัจจัยโมเมนตัม
- [[Multi-Factor Models]] — โมเดลหลายปัจจัย
- [[Market Regimes Research]] — กลุ่มตลาดและความเสี่ยง

---

## 📚 แหล่งข้อมูล

- Asness et al. (2013). Value and momentum everywhere.
- Clarke et al. (2016). Fundamentals of multifactor portfolio construction.
- Daniel & Moskowitz (2016). Momentum crashes.

---

*Document created: 2026-04-06*
*Last updated: 2026-04-06*
*Status: 🚧 Waiting for backtest results*
