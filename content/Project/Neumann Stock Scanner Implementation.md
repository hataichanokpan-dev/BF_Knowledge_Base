---
created: 2026-03-29
status: planning
priority: medium
source: "[[Jeffrey Neumann Trading Course]]"
related:
  - "[[Alpha Trinity Scanner]]"
  - "[[Quality Swing Investor]]"
---

# Neumann Stock Scanner Implementation

> "Don't pick stocks. Pick sectors. Then buy the basket." - Jeffrey Neumann

## Overview

Stock scanner ที่ implement **Four Corners Framework** จาก Jeffrey Neumann (Unknown Market Wizard, $2,500 → $50M+)

---

## Core Philosophy

### Four Corners Framework

```
┌─────────────┬─────────────┐
│   CHART     │  STRUCTURE  │
│ (Technical) │ (Low Float) │
├─────────────┼─────────────┤
│   SECTOR    │  CATALYST   │
│   (Theme)   │   (Story)   │
└─────────────┴─────────────┘
```

**ขาด Corner ไหน = ไม่เข้า (รอต่อ)**

---

## Implementation Plan

### Phase 1: Data Infrastructure
- [ ] เลือก data source (Polygon.io vs Yahoo Finance)
- [ ] ตั้งค่า API connection
- [ ] สร้าง data cache layer

### Phase 2: Wave 1 - Structural Filter
- [ ] Float screening (< 200M, ideal < 50M)
- [ ] Insider ownership check (> 15%)
- [ ] Institutional ownership (< 30%)
- [ ] Price range filter ($0.50 - $10)
- [ ] Dilution detection (S-3, ATM keywords)

### Phase 3: Wave 2 - Technical Ignition
- [ ] Basing pattern detection (> 180 days)
- [ ] Price compression (BB Width < 20th %ile)
- [ ] RVOL spike detection (> 5x)
- [ ] RSI historic oversold
- [ ] Downtrend breakout scanner

### Phase 4: Wave 3 - Sector Cluster
- [ ] Sector classification
- [ ] Cluster breakout detection (3+ stocks)
- [ ] Relative Strength calculation
- [ ] Lead Dog identification
- [ ] Sector lifecycle phase

### Phase 5: Wave 4 - Catalyst Audit
- [ ] Hard catalyst calendar (FDA, earnings, legislative)
- [ ] Volume catalyst detection
- [ ] Dilution audit automation
- [ ] News sentiment integration

### Phase 6: Scoring & Output
- [ ] Neumann Score calculation
- [ ] Watchlist generation
- [ ] Alert system
- [ ] Dashboard UI

---

## Scoring System

```
Neumann Score = (W1 × 0.20) + (W2 × 0.30) + (W3 × 0.20) + (W4 × 0.30)

> 75  = HIGH CONVICTION → Deep dive + Enter
60-75 = WATCHLIST → รอ setup
< 60  = DISCARD
```

---

## กฎเหล็ก 5 ข้อ

1. **Never Average Down** - ห้ามเติมขาดทุน
2. **Avoid the Crowd** - หลีกเลี่ยงที่คนพูดถึงเยอะ
3. **No Hard Stops** - ใช้ mental stops ตาม thesis
4. **Know the Filings** - อ่าน SEC filings ให้รู้เรื่อง
5. **Wait for the Turn** - รอ volume + basing + catalyst

---

## Comparison: Alpha Trinity vs Neumann

| Aspect | [[Alpha Trinity Scanner]] | Neumann Scanner |
|--------|---------------------------|-----------------|
| Source | Damodaran + Klarman | Schwager |
| Style | Quality + Value | Momentum + Catalyst |
| Timeframe | Long-term | Swing |
| Focus | Fundamental | Technical + Sector |
| Entry | MOS from IV | Breakout + Volume |
| Status | ✅ Implemented | 📋 Planning |

---

## Resources

- **Course:** [[Jeffrey Neumann Trading Course]] (Episteme, 11 chapters)
- **Book:** Unknown Market Wizards by Jack Schwager
- **Oracle:** `learning-1774762386004-c3l5bz`

---

## Status Log

| Date | Update |
|------|--------|
| 2026-03-29 | Initial plan created, saved to Oracle |
