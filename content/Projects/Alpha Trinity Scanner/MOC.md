---
title: "Alpha Trinity Scanner — Map of Content"
aliases: ["ATS MOC", "Alpha Trinity Scanner Index", "แผนที่ความรู้ Alpha Trinity"]
tags: [📁/projects, 🏷️/alpha-trinity-scanner, 🏷️/moc, 🏷️/reverse-dcf, status/evergreen]
created: 2026-04-06
modified: 2026-04-06
type: moc
status: evergreen
links:
  - "[[VQM Model - Thesis Research Plan]]"
  - "[[Alpha Trinity Scanner - Project Summary]]"
  - "[[Investing MOC]]"
  - "[[Neumann Stock Scanner Implementation]]"
  - "[[Quality Swing Investor]]"
---

# Alpha Trinity Scanner — Map of Content

> [!ABSTRACT] **Alpha Trinity Scanner:** Reverse DCF Expectation Gap Analysis สำหรับตลาดหุ้นไทย
>
> **Motto:** "Better roughly right than precisely wrong with broken data" — Aswath Damodaran
> **Status:** ✅ Validated | ⏳ Forward Tracking (24-month)

---

## 🎯 Project Overview

**Objective:** ตรวจสอบสมมติฐาน Expectation Gap สำหรับหุ้นไทย โดยใช้ Reverse DCF Methodology

### Core Hypothesis

```
┌─────────────────────────────────────────────────────────────┐
│  MARKET PRICES → EMBED EXPECTATIONS (growth, margin, ROIC)   │
│                                                             │
│  Growth Traps:    Expectations > Capabilities → Underperform │
│  Value Opps:      Expectations < Capabilities → Outperform   │
└─────────────────────────────────────────────────────────────┘
```

### Signal Definitions (LOCKED)

| Signal | Criteria | Expected Return |
|--------|----------|-----------------|
| **AVOID** | composite > 50% | -2.35% (protected) |
| **CAUTION** | 20% < comp ≤ 50% | +16.59% (sweet spot) |
| **ACCEPTABLE** | composite ≤ 20% | +13.63% (positive) |

**Validation Status:** ✅ HYPOTHESIS SUPPORTED (Correlation: -30.35%)

---

## 🚀 Entry Points

> [!TIP] **เริ่มต้นจากที่นี่** ถ้าใหม่กับโปรเจค

| Entry Point | Description | For |
|-------------|-------------|-----|
| **[[00_Project_Summary]]** | Executive summary และ validation results | ภาพรวมฉับไว |
| **[[สรุปโปรเจกต์]]** | ภาพรวมภาษาไทย | ผู้เริ่มต้นภาษาไทย |
| **[[METHODOLOGY_DEEP_DIVE]]** | วิธีการทำงานลึกๆ | ผู้สนใจเทคนิค |
| **[[THESIS-v2-Professional]]** | วิทยานิพนธ์ฉบับสมบูรณ์ | นักวิจัย |

---

## 📚 Core Concepts

### 1. Reverse DCF Framework

| Concept | Description | Link |
|---------|-------------|------|
| **Implied Growth** | อัตรา growth ที่ตลาดคาดหวัง | [[01_Technical_Documentation]] |
| **Implied Margin** | EBIT Margin ที่ตลาดคาดหวัง | [[01_Technical_Documentation]] |
| **Implied ROIC** | ROIC ที่ตลาดคาดหวัง | [[01_Technical_Documentation]] |
| **Gap Score** = (0.40×growth_gap) + (0.30×margin_gap) + (0.30×roic_gap) | [[03_RISK_FRAMEWORK]] |

### 2. Thai Market Adaptations

| Parameter | Value | Source |
|-----------|-------|--------|
| **Country Risk Premium (CRP)** | 2.07% | Damodaran |
| **PTT WACC** | 7.16% | Calculated |
| **Beta (Unlevered)** | 0.80-1.20 | Industry average |

### 3. Dual-AI Validation

| AI | Focus | Bias |
|----|-------|------|
| **Gemini** | Growth thesis identification | Optimistic on narrative |
| **Codex** | Risk and governance analysis | Conservative, detail-oriented |

---

## 🗂️ Clusters

### Cluster A: Core Documentation

```
CORE_DOCUMENTATION/
├── 00_Project_Summary.md          ← เริ่มต้นที่นี่
├── 01_Technical_Documentation.md   ← วิธีการทำงาน
├── 02_API_Reference.md            ← คู่มือโปรแกรมเมอร์
├── 03_RISK_FRAMEWORK.md           ← กรอบความเสี่ยง
└── 04_LITERATURE_REVIEW.md        ← งานวิจัยสนับสนุน
```

### Cluster B: Thesis Documents

```
THESIS/
├── THESIS-v2-Professional.md      ← วิทยานิพนธ์ภาษาอังกฤษ
├── THESIS-v2-Thai.md              ← วิทยานิพนธ์ภาษาไทย
└── 00_INDEX.md                    ← ดัชนีเอกสารวิทยานิพนธ์
```

### Cluster C: Research & Analysis

```
RESEARCH/
├── METHODOLOGY_DEEP_DIVE.md       ← วิธีวิจัยลึก
├── Sector Analysis/               ← วิเคราะห์แต่ละภาค
│   ├── Energy Sector Analysis.md
│   ├── Technology Sector Analysis.md
│   └── Healthcare Sector Analysis.md
└── MOC.md                         ← MOC เดิม (จะถูกแทนที่)
```

### Cluster D: Thai Documents

```
THAI_DOCUMENTS/
├── สรุปโปรเจกต์.md                ← สรุปภาษาไทย
├── เอกสารตกผลึก.md               ← สิ่งที่ได้เรียนรู้
├── แผนการปรึกษาAI.md             ← แนวทางใช้งาน AI
├── วิธีSyncVercel.md               ← วิธี sync เว็บ
└── 00_INDEX.md                    ← ดัชนีเอกสารไทย
```

### Cluster E: Archive

```
ARCHIVE/
├── THESIS-v1-Thai.md               ← ฉบับเก่า (ถูกแทนที่)
├── THESIS-v1-Expectation-Gap-Analysis.md
└── 00_INDEX.md
```

---

## 📋 Indexes

### Index by Topic

| Topic | Documents |
|-------|-----------|
| **Methodology** | Technical Documentation, Methodology Deep Dive |
| **Risk** | Risk Framework, Literature Review |
| **Validation** | Project Summary, Thesis v2 |
| **Sector Analysis** | Energy, Technology, Healthcare |
| **Thai** | สรุปโปรเจกต์, เอกสารตกผลึก, แผนการปรึกษาAI |

### Index by Status

| Status | Documents |
|--------|-----------|
| ✅ Complete | Core Documentation, Thesis v2, Risk Framework |
| ⏳ In Progress | Forward Tracking (12-month), Sector Analysis |
| 📋 Planned | Forward Tracking (24-month), ML Enhancement |

### Index by Signal Type

| Signal | Description | Example |
|--------|-------------|---------|
| **AVOID** | Expectations too high | BDMS (+174% → +5%) |
| **CAUTION** | Moderate expectations | TRUE (+11% → +36%) |
| **ACCEPTABLE** | Reasonable expectations | PTTGC (-67% → +80%) |

---

## 🔗 Meta

### Version History

| Date | Version | Changes |
|------|---------|---------|
| 2026-04-06 | 2.0 | MOC recreated with Obsidian format |
| 2026-04-05 | 1.0 | Original MOC created |
| 2026-04-04 | 0.x | Project started |

### Project Statistics

| Metric | Value |
|--------|-------|
| **Total Documents** | 18+ |
| **Test Coverage** | 99/99 passing |
| **Validation Period** | 6 months |
| **Tracking Period** | 24 months (in progress) |
| **Correlation** | -30.35% |

### Related Projects

| Project | Relationship |
|---------|--------------|
| [[VQM Model]] | โปรเจควิจัยถัดไป (Multi-factor) |
| [[Neumann Stock Scanner Implementation]] | ระบบ scanner อื่นๆ |
| [[Quality Swing Investor]] | กรอบการลงทุนแบบ swing |
| [[Investing MOC]] | MOC หลักการลงทุน |

### Key Knowledge Links

| Area | Link |
|------|------|
| **DCF Valuation** | [[Knowledge/Valuation/DCF Valuation/00 - DCF Valuation Course MOC]] |
| **Reverse DCF** | [[Knowledge/Valuation/DCF Valuation/08 - Reverse DCF Fundamentals]] |
| **Margin of Safety** | [[Knowledge/Value Investing/Seth Klarman's Margin of Safety Framework]] |
| **Market Cycles** | [[Knowledge/Value Investing/Howard Marks' Market Cycle & Risk Framework]] |

---

## 🔗 Linked References

- [[VQM Model - Thesis Research Plan]] — โปรเจควิจัยถัดไป
- [[Alpha Trinity Scanner - Project Summary]] — สรุปโปรเจค
- [[Investing MOC]] — MOC การลงทุน
- [[Neumann Stock Scanner Implementation]] — ระบบ scanner
- [[Quality Swing Investor]] — Quality Swing Framework
- [[Concepts/Alpha Trinity Scanner]] — แนวคิดหลัก

---

## 📚 แหล่งข้อมูล

- Damodaran, A. (2022). Investment Valuation: Tools and Techniques.
- Damodaran, A. (n.d.). Reverse DCF Fundamentals. NYU Stern.
- Thai Stock Market Data (SET)

---

*Document created: 2026-04-06*
*Last updated: 2026-04-06*
*Status: Evergreen — Forward tracking in progress*
