---
title: "Statistical Validation Plan - Alpha Trinity Phase 2 (Methods 1+4+6)"
tags: [alpha-trinity-scanner, phase-2, statistical-validation, monthly-rebalance, ic-analysis, exploratory, validation-plan]
created: 2026-04-08
modified: 2026-04-08
type: plan
status: active
links:
  - [[Phase 2 - Risk Management & Enhancement]]
  - [[Phase 2 Results - Companion Variables Validation]]
  - [[DAMODARAN_Perspective_Summary_for_Obb]]
  - [[Phase 1 Validation - Reverse DCF Backtest]]
  - [[CORE_DOCUMENTATION/03_RISK_FRAMEWORK]]
  - [[root-cause-analysis-phase2-vs-current]]
---

# Statistical Validation Plan - Alpha Trinity Phase 2

## Overview

ทีม Alpha Trinity ตัดสินใจเลือกใช้ **วิธีที่ 1 + 4 + 6** สำหรับการ validate ผลการทำงานของ Reverse DCF Strategy แทนการใช้ข้อมูล 23 rebalances จากการ backtest

**การตัดสินใจ:** ใช้ 3 วิธีร่วมกันเพื่อเพิ่มความน่าเชื่อถือและครอบคลุมทั้งมุมมองทางปฏิบัติและวิชาการ

---

## [!IMPORTANT] Critical Update - Honest Baseline (2026-04-08)

**Previous Claim (Phase 2 Documentation):**
- Excess Return: +10.18%
- Sharpe: -0.124
- Source: Companion Variables (40/20/20/20)

**Actual Reality (After Code Review):**
- Excess Return: **+5.36%**
- P-value: **0.60** (NOT significant)
- Source: **Reverse DCF Only** (CV DISABLED)

**Root Cause:** Companion Variables were disabled in `pit_walk_forward_validator.py:803-828` AND missing PIT data fields would cause NaN anyway.

See [[root-cause-analysis-phase2-vs-current]] for full details.

---

## Background

### ที่มาของปัญหา

Phase 1 Validation มีข้อจำกัดด้าน sample size:
- **Original:** 11 rebalances (quarterly, 2022-2025) = ไม่เพียงพอสำหรับ statistical testing
- **Actual Baseline:** +5.36% excess, p=0.60 (NOT significant)
- **Target:** ต้องการ minimum 23 observations สำหรับ t-test

### ทางเลือกที่พิจารณา

| วิธี | คำอธิบาย | Difficulty | สถานะ |
|-----|----------|------------|--------|
| 1 | Monthly Rebalance | ง่าย | ✅ เลือก |
| 2 | Bootstrap Resampling | ปานกลาง | ❌ ไม่เลือก |
| 3 | Cross-Sectional (3,200 obs) | ง่าย | �O ไม่เลือก (Codex recommend) |
| 4 | IC Analysis | ง่าย | ✅ เลือก |
| 5 | Cross-Market | ยาก | ❌ ไม่เลือก |
| 6 | Exploratory Mindset | ง่ายสุด | ✅ เลือก |

---

## Methods

### #1 Monthly Rebalance

**แนวคิด:** เพิ่ม sample size โดยเปลี่ยน frequency จากรายไตรมาสเป็นรายเดือน

#### รายละเอียด

```python
# Implementation
freq = "ME"  # Month End (เดิม: "QE" = Quarter End)
```

| Parameter | Value |
|-----------|-------|
| **Period** | 2022-2025 (4 ปี) |
| **Rebalances** | 48 (4 × 12) |
| **Frequency** | Monthly |

#### [!IMPORTANT] Trade-offs

| Pros | Cons |
|------|------|
| เพิ่ม sample size จาก 11 → 48 | ค่าธรรมเนียมเพิ่มขึ้น (12 ×  trades) |
| เพิ่ม statistical power | Signal อาจ noisy (shorter period) |
| Realistic frequency | ต้อง adjust transaction costs |

#### Implementation Notes

- แก้ไข `pit_walk_forward_validator.py`
- เปลี่ยน `rebalance_freq="QE"` → `"ME"`
- เพิ่ม transaction cost parameter: 0.3% per trade (Thailand standard)

---

### #4 IC Analysis (Information Coefficient)

**แนวคิด:** วัด correlation ระหว่าง expectation gap score → forward return

#### รายละเอียด

**IC = Spearman Correlation(gap_score, forward_return)**

```python
from scipy.stats import spearmanr

ic, p_value = spearmanr(gap_scores, forward_returns)
```

#### Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| **Mean IC** | Average IC per rebalance | > 3% |
| **IC Std** | Standard deviation of IC | - |
| **Information Ratio (IR)** | Mean IC / IC Std | > 0.5 |
| **t-statistic** | Mean IC × √N / IC Std | > 2.0 |
| **Hit Rate** | % periods with IC > 0 | > 55% |

#### [!TIP] เหตุผลใช้ Spearman ไม่ใช่ Pearson

- **Spearman:** Rank-based, robust ต่อ outliers, เหมาะกับ non-linear relationships
- **Pearson:** Linear-based, sensitive ต่อ outliers, อาจ miss weak signals

#### Implementation Notes

1. Calculate IC สำหรับทุก rebalance (48 ครั้ง)
2. Track IC distribution (mean, std, min, max)
3. Compute t-statistic: `t = mean_ic × sqrt(N) / std_ic`
4. บันทึก IC per rebalance สำหรับ diagnostic

---

### #6 Exploratory Mindset

**แนวคิด:** ซื่อสัตย์กับ limitations ไม่หลอกลวงด้วย p-values

#### Rationale

> "The goal is to discover interesting patterns, not to prove a strategy"

#### Positioning Statement

```
NOT: "This strategy is proven (p < 0.05)"
YES: "Evidence supports the hypothesis that expectation gap predicts returns"

NOT: "Statistically significant"
YES: "Directionally consistent with theory"
```

#### [!CAUTION] Limitations ที่ต้องรับรู้

| Limitation | รายละเอียด |
|------------|-------------|
| **Sample Size** | 48 observations ยังน้อยสำหรับ definitive conclusion |
| **Look-ahead Bias** | PIT compliance ช่วยลด แต่ไม่ 100% |
| **Transaction Costs** | ยังไม่รวม slippage, market impact |
| **Regime Change** | Past 4 ปีอาจไม่ represent future |
| **Survivorship Bias** | ใช้หุ้นที่อยู่จนถึงปัจจุบัน |

#### Communication Guidelines

เวลา present ผล:
1. Focus on **economic intuition** ไม่ใช่ p-values
2. Highlight **consistency** ของ signals
3. Acknowledge **uncertainty** อย่างตรงไปตรงมา
4. Use **hedging language**: "suggests", "indicates", "consistent with"

---

## Implementation Timeline

> **Update (2026-04-08):** Codex reports implementations complete. Timeline reflects actual status.

| Phase | Task | Owner | Status | Notes |
|-------|------|-------|--------|-------|
| 1 | Monthly Rebalance Implementation | codex | ✅ Complete | 48 rebalances ready |
| 2 | IC Analysis Implementation | codex | ✅ Complete | Spearman correlation ready |
| 3 | QA & Validation | gemini | ✅ Complete | Root cause analysis done |
| 4 | Results & Reporting | obb | 🔄 In Progress | Awaiting actual results |
| 5 | Fix Companion Variables | codex | ⏸️ Blocked | Need PIT data fields |
| 6 | Sync to Vercel | obb | 🔄 Pending | After results |

### Estimated Effort

| Task | Estimated Time |
|------|----------------|
| Monthly Rebalance | 2-3 hours |
| IC Analysis | 3-4 hours |
| QA | 2-3 hours |
| Reporting | 2 hours |

---

## Team Votes

| Member | Vote | Comment |
|--------|------|---------|
| **Both (Team Lead)** | ✅ 1+4+6 | Balance of practicality + academic rigor |
| **damodaran** | ✅ 4/5 acceptable | IC Analysis is standard, Monthly OK |
| **codex** | ✱ 1+4+6 | Preferred #3+#2+#6 but accepts 1+4+6 |
| **gemini** | ✅ 1+4+6 | QA checklist prepared |

**Consensus:** ✅ Approved

---

## Expected Outcomes

### [!CAUTION] Honest Baseline Adjustment

**Previous Expectation (Based on +10.18% claim):**
- Strategy already proven, just need validation

**Current Reality (After Root Cause Analysis):**
- Baseline: +5.36% excess, p=0.60 (NOT significant)
- Companion Variables: DISABLED
- Must prove signal validity from scratch

### Success Criteria (Revised)

| Criterion | Target | Notes |
|-----------|--------|-------|
| **Sample Size** | 48 rebalances | Monthly vs quarterly |
| **Mean IC** | > 3% | Prove predictive power |
| **Information Ratio** | > 0.5 | Consistency over time |
| **P-value** | < 0.05 | Statistical significance |
| **Excess Return** | > baseline+5% | Improve on +5.36% |

### If Results Are Weak

1. **IC < 3%:** ตรวจสอบ signal calculation, consider alternative gap metrics
2. **IR < 0.5:** Signal ไม่ stable พอ, ต้อง refine
3. **Hit Rate < 50%:** Direction ผิดบ่อยเกินไป, revisit core thesis

### If Results Are Strong

1. **IC > 5%, IR > 1.0:** Proceed to live paper trading
2. **Consistent signals:** Scale up position sizes gradually
3. **Document findings:** Prepare for publication

---

## Appendix

### Code References

- **Validator:** `analysis/pit_walk_forward_validator.py`
- **IC Analysis:** (TBD) `analysis/ic_analyzer.py`
- **Quality Filters:** `analysis/quality_filters.py`

### Related Documents

- [[Phase 2 Results - Companion Variables Validation]] - ผลลัพธ์จาก Phase 2
- [[Phase 2 - Multi-Factor Valuation Model]] - Model ที่ใช้
- [[DAMODARAN_Perspective_Summary_for_Obb]] - มุมมองวิชาการ
- [[CORE_DOCUMENTATION/03_RISK_FRAMEWORK]] - กรอบความเสี่ยง

### Oracle References

- Search: `alpha-trinity-scanner phase2 validation`
- Search: `IC analysis information coefficient`
- Search: `exploratory mindset statistics`

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-04-08 | **CRITICAL UPDATE:** Corrected baseline from +10.18% → +5.36%, noted CV DISABLED, updated timeline | obb (Orga Agent) |
| 2026-04-08 | Initial document creation | obb (Orga Agent) |
