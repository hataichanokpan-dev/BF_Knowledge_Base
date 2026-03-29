---
title: QSI Quick Filter
note_type: template
framework: Quality Swing Investor
version: "2.0"
created: 2026-03-28
tags:
  - note/template
  - framework/qsi
---

# QSI Quick Filter (1 หน้า)

> ใช้คัดหุ้นเร็ว 3 ชั้น

---

## ⚡ ชั้น 1: Kill Switch (30 วินาที)

**ตัดทิ้งทันทีถ้า:**
- [ ] มี sign: `SP / NC / CB / CS / CF / CC`
- [ ] Audit: Qualified / Adverse / Disclaimer
- [ ] มูลค่าซื้อขาย < 10 ลบ./วัน
- [ ] ต่ำกว่า EMA200 (ถ้าเล่น swing)

**ถ้าผ่าน → ไปชั้น 2**

---

## 🔍 ชั้น 2: 5 Metrics (2 นาที)

| # | Metric | Pass | Fail |
|---|--------|------|------|
| 1 | **ROE** | > 12% | < 8% |
| 2 | **Net D/E** | < 1.0x | > 2.0x |
| 3 | **CFO** | บวก | ติดลบ |
| 4 | **P/E vs Sector** | ต่ำกว่า | สูงกว่า 2x |
| 5 | **Catalyst 1-2Q** | มีชัด | ไม่มี |

**ถ้าผ่าน >= 4/5 → ไปชั้น 3**

---

## 📊 ชั้น 3: Technical (2 นาที)

| # | Check | Pass | Fail |
|---|-------|------|------|
| 1 | **Trend** | > EMA50 > EMA200 | < EMA200 |
| 2 | **RSI** | 50-70 | >80 หรือ <40 |
| 3 | **Volume** | Breakout >= 1.5x | < 1x |
| 4 | **RS vs SET** | ชนะ 3M | แพ้ >5ppt |

---

## 🚦 Decision

| Result | Action |
|--------|--------|
| ผ่านทุกชั้น | **Full QSI Deep Dive** |
| ผ่าน 2/3 ชั้น | **Add Watchlist** |
| ติด Kill Switch | **PASS** |

---

## 📐 Position Size Quick

| Conviction | Size | Stop |
|------------|------|------|
| High (QSI 85+) | 8-12% | -2ATR หรือ EMA50 |
| Medium (75-84) | 5-8% | -2ATR |
| Low (65-74) | 3-5% | Tight |

---

**Full Checklist:** [[QSI Deep Dive Checklist]]
