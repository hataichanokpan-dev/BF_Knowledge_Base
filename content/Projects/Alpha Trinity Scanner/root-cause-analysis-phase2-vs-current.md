---
title: "Root Cause Analysis - Phase 2 vs Current Performance Gap"
tags: [root-cause, phase-2, companion-variables, contradiction, qa]
created: 2026-04-08
modified: 2026-04-08
type: analysis
status: critical
links:
  - [[Phase 2 Results - Companion Variables Validation]]
  - [[Backtest_Report_2022-2025_Detailed]]
  - [[Statistical_Validation_Plan_1-4-6]]
  - [[CORE_DOCUMENTATION/03_RISK_FRAMEWORK]]
---

# Root Cause Analysis - Phase 2 vs Current Performance Gap

> **Date:** 2026-04-08
> **Status:** CRITICAL - Companion Variables DISABLED
> **QA by:** Gemini (testlon)

---

## Executive Summary

**The +10.18% excess return claim is FALSE.**

Companion Variables (PEG, P/B-ROE, EV/EBITDA) are **disabled in production code**, and even if enabled, they would produce NaN due to missing data fields.

---

## The Contradiction

| Source | Claim | Reality |
|--------|-------|---------|
| **Phase 2 Documentation** | +10.18% excess return | ✅ Written |
| **Actual Code** | CV DISABLED | ❌ Not implemented |
| **Real Results** | +10.18% | **+5.36% (p=0.60)** |

---

## Root Cause (3 Layers)

### Layer 1: Companion Variables DISABLED in Code

**File:** `analysis/pit_walk_forward_validator.py`, lines 803-828

```python
# Step 8: Companion Variables - DISABLED
# comp = self.companion_scorer.score(...)  <-- COMMENTED OUT

# Step 9: Use Reverse DCF ONLY
composite_signal_100 = reverse_dcf_score  # 100% Reverse DCF
```

**Impact:** Strategy runs with 100% Reverse DCF, 0% Companion Variables

---

### Layer 2: Missing Data (Would produce NaN anyway)

The PIT data cache is missing required fields:

| CV Score | Required Field | Available? |
|-----------|----------------|------------|
| **PEG** | Net Income, Shares Outstanding | ❌ Missing |
| **P/B-ROE** | Book Value, ROE | ❌ Missing |
| **EV/EBITDA** | EBITDA | ❌ Missing |

**Impact:** Even if enabled, CV scores would be NaN and get filtered out

---

### Layer 3: The +10.18% Claim Has No Evidence

| Search Target | Result |
|---------------|--------|
| Codebase for "10.18" | Found ONLY in documentation |
| JSON results | No trace |
| CSV exports | No trace |
| Git history | No A/B test ever run |

**Conclusion:** +10.18% appears to be **theoretical/projected**, not empirical

---

## Current Honest Baseline

```
Total Return: -15.80%
Benchmark: -21.16% (SET)
Excess Return: +5.36%
Sharpe Ratio: -0.208
P-value: 0.60
Statistical Significance: NO (cannot reject null hypothesis)
```

**Translation:** Performance is indistinguishable from random luck

---

## Performance Comparison

| Metric | Phase 2 (Documentation) | Reality (Code) | Gap |
|--------|-------------------------|----------------|-----|
| **Excess Return** | +10.18% | **+5.36%** | **-4.82%** |
| **Signal Source** | 40/20/20/20 | **100/0/0/0** | CV missing |
| **Statistical Sig** | Not stated | **p=0.60** | Not significant |
| **Avg Positions** | 10.3 | **2.75** | Fewer signals |

---

## What Actually Happened

1. Phase 2 document was written with **projected/expected** results
2. Companion Variables were **disabled** before running actual backtest
3. Actual results (+5.36%) were **worse than projection** (+10.18%)
4. Documentation was **never updated** with real numbers
5. Team believed the +10.18% claim without verification

---

## Recommendations

### Immediate Actions (Priority: CRITICAL)

| # | Action | Owner | Timeline |
|---|--------|-------|----------|
| 1 | **Update documentation** with real numbers | obb | Today |
| 2 | **Fix data pipeline** for CV fields | codex | 1-2 days |
| 3 | **Run proper A/B test** (CV vs no CV) | codex | 2-3 days |
| 4 | **Achieve statistical significance** (need 23+ rebalances) | codex | TBD |

### How to Fix Companion Variables

**Step 1: Fix Data Pipeline**
- Add Net Income, Shares, Equity, EBITDA to PIT snapshots
- Update JSON statements loader

**Step 2: Verify CV Scoring**
- Run `verify_companion_scoring.py`
- Run `diagnose_companion_scoring.py`
- Confirm all 3 CV scores return valid values

**Step 3: Build Proper A/B Test**

```
Config A: Reverse DCF only (100/0/0/0) -- baseline
Config B: Full model (40/20/20/20) -- with CV
Config C: Equal weight (25/25/25/25) -- sensitivity
```

**Step 4: Be Honest About Baseline**

> Current: +5.36% excess with p=0.60
> Meaning: Cannot reject null hypothesis (zero alpha)
> Any CV improvement must measure against THIS baseline

---

## Communication Guidelines

### DO Say ✅

- "Current results show +5.36% excess return"
- "Not statistically significant (p=0.60)"
- "Companion Variables are disabled pending data fixes"
- "We are working to enable CV properly"

### DON'T Say ❌

- "We achieved +10.18% excess return"
- "Companion Variables improved performance"
- "Results are statistically significant"
- "Strategy is proven"

---

## Key Files

- `analysis/pit_walk_forward_validator.py:803-828` - CV disabled
- `analysis/companion_variables.py` - CV scorer implementation
- `results/extended_validation_report.json` - Real results
- `QA_REPORT_Phase2_Contradiction.md` - Gemini QA report

---

## Oracle Update

```bash
# Save learning to Oracle
oracle_learn "Companion Variables were DISABLED in Phase 2 code despite documentation claiming +10.18% improvement. Real excess return was +5.36% with p=0.60 (not significant). Always verify documentation against actual code."
```

---

## Changelog

| Date | Change | Author |
|------|--------|--------|
| 2026-04-08 | Initial root cause analysis | obb (based on Gemini QA) |
