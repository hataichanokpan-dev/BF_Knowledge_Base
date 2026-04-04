---
title: "Deep Value - Cheat Sheet"
type: cheatsheet
created: 2026-04-04
tags:
  - thesis
  - quick-reference
  - deep-value
---

# Deep Value - Cheat Sheet

> **Quick Reference สำหรับการตัดสินใจ Deep Value ไทย**

---

## ✅ PASS Criteria (ต้องผ่านทั้งหมด)

| Metric | Threshold | คำนวณ |
|--------|-----------|-------|
| P/BV | < 0.5x | P/BV = Price / Book Value |
| NCAV | Price < 0.67×NCAV | (Current Assets - Liabilities) / Shares |
| D/E Ratio | < 1.5x | D/E = Debt / Equity |
| F-Score | ≥ 6 | 9-item quality check |
| Catalyst | Exists | ต้องระบุได้ภายใน 2-3 ปี |
| MOS | > 30% | MOS = (IV - Price) / IV |

---

## 🚫 REJECT Criteria (พบข้อใดข้อ = หลีเลี่ยง)

| Red Flag | Score | Trigger |
|---------|-------|--------|
| Business Failure | 10 | กำไรขาดทุน 3 ปีติดต่อ |
| No Catalyst | 9 | ไม่มี catalyst ที่ระบุได้ภายใน 2 ปี |
| High Debt | 8 | D/E > 2.0x หรือ Interest Coverage < 1.5x |
| Governance Red | 9 | RPT > 20% หรือ auditor ไม่ใช่ Big 4 |
| Structural Decline | 9 | อุตสาหกรรมอยู่ในช่วง decline |
| Liquidity Risk | 7 | Free Float < 10% |

**DV-VTS ≥ 15 = 🚫 REJECT**

---

## ⚠️ CAUTION Criteria (ตรวจสอบเพิ่ม)

| Yellow Flag | Score | Action |
|------------|-------|--------|
| P/BV 0.3-0.5x | 4 | Moderate discount |
| F-Score 4-6 | 4 | Check business viability |
| Catalyst Timeline > 1 year | 3 | Longer wait required |
| Low Liquidity | 3 | Check trading volume |
| Related Party Transactions | 4 | RPT 10-20% |

**DV-VTS 8-14 = ⚠️ DEEP DIVE REQUIRED**
**DV-VTS < 8 = ✅ PASS**

---

## 📐 Position Sizing

| Tier | Base | Criteria | Conviction Multiplier |
|------|------|----------|----------------------|
| **A** | 5% | P/BV < 0.3x, NCAV, Clear Catalyst < 1 year | 1.0x (High Conviction) |
| **B** | 3% | P/BV 0.3-0.5x, F-Score ≥ 6, Catalyst 1-2 years | 0.75x (Standard) |
| **C** | 2% | P/BV > 0.5x, F-Score 4-6, Catalyst Unclear | 0.5x (Low Conviction) |

**Final Position = Base × Conviction Multiplier × Liquidity Adjustment**

> **Liquidity Adjustment:** Reduce position by 50% if Free Float < 15% or avg daily volume < 5M THB

---

## 🛡️ Stop Loss Rules

| Trigger | Stop Loss | Action |
|---------|-----------|--------|
| **Thesis Break** | ทันที | Sell all |
| **Catalyst Failure** | ทันที | Sell all |
| **Time Stop** (2-3 years) | ทันที | Sell all |
| **Technical Stop** | -20% | Evaluate for thesis break |
| **Price < -30%** | ทันที | Sell all |

---

## 💰 Take Profit Rules

| Trigger | Take Profit | Action |
|---------|-------------|--------|
| **Price ≥ IV** | 50% position | Sell half |
| **Catalyst Realized** | 75% position | Sell partial |
| **Target Price** (IV + 30%) | ทั้งหมด | Sell all |
| **2-3 years passed** | ทบทวน | Re-evaluate thesis |

---

## 📅 Sector Limits

| Rule | Limit | Why |
|------|------|-----|
| Max per Sector | 20% | Deep value stocks often cluster in same sectors |
| Max Single Position | 5% | Illiquidity and concentration risk |
| Min Sectors | 3 | Diversification |
| Cash Reserve | 15% | Opportunity fund for new opportunities |

---

## 🌡️ Macro Sensitivity Quick Check

| Sector | Rate Rising | Rate Falling | Rate Neutral |
|--------|-------------|--------------|--------------|
| **Property** | ⚠️ Caution | ✅ Buy | ✅ Good |
| **Industrial** | ✅ Good | ⚠️ Caution | ⚠️ Caution |
| **Financials** | ✅ Good | ⚠️ Caution | ⚠️ Caution |
| **Energy** | ⚠️ Caution | ✅ Buy | ✅ Good |

---

## 💰 Deep Value Calculator

```
Discount to IV = (IV - Price) / IV × 100%

NCAV = Current Assets - Total Liabilities
NNWC = Cash + 0.75×AR + 0.5×Inv - Total Liabilities
MOS = (IV - Price) / IV
```

---

## 📋 Catalyst Checklist

| Type | Examples | Timeline |
|------|----------|----------|
| **Asset Sale** | Land sale, subsidiary sale | 6-12 months |
| **Restructuring** | Management change, cost reduction | 6-18 months |
| **M&A** | Buyout, take private offer | 3-12 months |
| **Buyback** | Share repurchase program | 6-12 months |
| **Sector Rotation** | Fund rotation into sector | 6-18 months |
| **Dividend Cut** | Company cuts dividend to free up cash | 3-6 months |

---

## 🔗 Quick Links

- [[Deep-Value-Thesis]] - Full Thesis v2.0
- [[Deep-Value-Flow]] - Visual Workflows
- [[Dividend-Play-Thesis]] - Complementary approach
- [[Valuation-Framework]] - Valuation methods
