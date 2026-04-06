---
project: VQM Model
tags: [thesis, research, multi-factor, vqm, stock-selection]
created: 2026-04-06
status: planning
type: project-plan
---

# VQM Model — Thesis Research Plan

> **Formerly:** Alpha Trinity Scanner
> **New Official Name:** Integrated Value-Quality-Momentum Model (VQM Model)

---

## Executive Summary

โปรเจควิจัยนี้มุ่งพัฒนาและทดสอบ **VQM Model (Value-Quality-Momentum)** — กรอบการคัดเลือกหุ้นแบบหลายปัจจัยสำหรับตลาดหุ้นไทย โดยผสาน 3 แกนหลัก:

```
┌────────────────────────────────────────────────────────────┐
│  VQM MODEL CORE FACTORS                                    │
│                                                            │
│  VALUE (45%)       │  QUALITY (35%)    │  MOMENTUM (20%)  │
│  • FCF Yield       │  • ROIC - WACC    │  • Price 6M      │
│  • P/E x P/B       │  • FCF Conversion │  • Earnings Rev  │
│  • EV/EBITDA       │  • Debt/EBITDA    │  • Volume        │
└────────────────────────────────────────────────────────────┘
```

---

## Part 1: Project Naming Decision

### Team Voting Results

| ชื่อโปรเจค | เสนอโดย | คะแนน | หมายเหตุ |
|-------------|----------|--------|----------|
| **Integrated Value-Quality-Momentum Model (VQM Model)** | Codex | ★★★★★ | แนะนำให้ใช้ — ตรงประเด็น, ใช้ใน thesis ได้ดี |
| Tri-Factor Equity Selection Framework | Codex | ★★★☆☆ | ดีแต่ยาวไป |
| Systematic VQM Stock Selection Model | Codex | ★★★★☆ | เน้น systematic ดี |
| Factor Fusion Equity Ranking System | Codex | ★★★☆☆ | Fusion ไม่ค่อยโดดเด่น |
| Quantitative Trinity Factor Framework | Codex | ★★★☆☆ | เก็บ Trinity แต่ไม่โฟกัส VQM |

### Final Decision

**Official Project Name:** `Integrated Value-Quality-Momentum Model (VQM Model)`

**เหตุผล:**
- ตรงประเด็น สื่อถึงหลักการทำงานครบ
- เป็นทางการ เหมาะกับ thesis/academic
- จำง่าย ใช้เป็น acronym ได้
- อ้างอิงในงานวิจัยได้สะดวก

---

## Part 2: Thesis Structure

### Chapter 1: Introduction

**1.1 Background**
- ปัญหาของ Single-factor investing
- ความต้องการกรอบหลายปัจจัยที่เชื่อถือได้

**1.2 Research Gap**
- ขาด framework ที่รวม Value+Quality+Momentum อย่างเป็นระบบสำหรับ Thai market
- งานวิจัย existing ส่วนใหญ่ focus ตลาด developed

**1.3 Research Objectives**
1. พัฒนา VQM Model สำหรับตลาดหุ้นไทย
2. ทดสอบประสิทธิภาพเทียบกับ benchmark
3. วิเคราะห์ความทนทานของโมเดลใน market regimes ต่างกัน

**1.4 Scope**
- **Market:** SET (Stock Exchange of Thailand)
- **Period:** 2019-2024 (5 ปี ครอบคลุมหลาย regime)
- **Universe:** หุ้นที่มีสภาพคล่องดี (ADV > 20M THB)
- **Rebalancing:** Quarterly

**1.5 Contributions**
- VQM Model framework
- หลักฐานเชิงประจักษ์จาก Thai market
- แนวทางใช้งานจริงสำหรับนักลงทุน

---

### Chapter 2: Literature Review

**2.1 Value Investing**
- Fama & French (1992, 1993, 2015)
- Graham & Dodd Security Analysis
- หลักฐานเชิงประจักษ์ใน Thai market

**2.2 Quality Factor**
- Novy-Marx (2013) — Profitability as value
- ROIC และ Economic Value Added
- Cash Flow quality metrics

**2.3 Momentum Factor**
- Jegadeesh & Titman (1993, 2001)
- ปรากฏการณ์ momentum ในตลาด emerging

**2.4 Multi-Factor Models**
- Fama-French 3-factor, 5-factor models
- Barra risk models
- Factor interaction และ correlation

**2.5 Market Regimes**
- Risk-on vs Risk-off periods
- Volatility regimes
- Sector rotation effects

---

### Chapter 3: Methodology

**3.1 Data & Sample Design**
- แหล่งข้อมูล: [TBD]
- Data cleaning procedures
- Point-in-Time (PIT) data handling
- Survivorship bias controls

**3.2 Factor Definitions**

| Factor | Formula | Source |
|--------|---------|--------|
| FCF Yield | FCF / EV | Calculated |
| P/E Relative | P/E / Median(P/E, Sector) | Calculated |
| P/B Relative | P/B / Median(P/B, Sector) | Calculated |
| EV/EBITDA | EV / EBITDA | Calculated |
| ROIC - WACC | NOPAT / IC - WACC | Calculated |
| FCF Conversion | FCF / Net Income | Calculated |
| Debt/EBITDA | Total Debt / EBITDA | Financials |
| Price Momentum (6M) | (Price_t / Price_t-6) - 1 | Calculated |
| Earnings Revision | Estimate Revision Score | Analyst data |
| Volume Trend | Volume_MA(20) / Volume_MA(60) | Calculated |

**3.3 Scoring & Weighting**
```
Z_score(i,k,t) = (X(i,k,t) - Median) / (1.4826 × MAD)
Composite_Score(i,t) = 0.45×Value + 0.35×Quality + 0.20×Momentum
```

**3.4 Portfolio Construction**
- Top 20-30 stocks by score
- Equal-weight or Score-weighted
- Constraints: Max 10% per sector, Max 5% per stock

**3.5 Backtesting Protocol**
- Walk-forward analysis
- Transaction costs: 0.5% round-trip
- Slippage model

**3.6 Statistical Tests**
- t-test for alpha significance
- Sharpe ratio comparison
- Max Drawdown analysis
- Factor regression analysis

---

### Chapter 4: Results

**4.1 Descriptive Statistics**
- Factor distributions
- Correlation matrix
- Portfolio characteristics

**4.2 Performance Analysis**
- vs SET Index benchmark
- vs Single-factor portfolios
- Risk-adjusted metrics

**4.3 Risk Analysis**
- Max Drawdown
- Downside deviation
- Sortino ratio

**4.4 Regime Analysis**
- Bull market performance
- Bear market performance
- High volatility periods

**4.5 Sensitivity Analysis**
- Weight variations
- Rebalancing frequency
- Universe size

**4.6 Practical Feasibility**
- Turnover analysis
- Capacity constraints
- Net returns after costs

---

### Chapter 5: Conclusion

**5.1 Summary of Findings**
- คำตอบตาม Research Questions
- หลักฐานสนับสนุน/คัดค้าน Hypotheses

**5.2 Implications**
- Academic implications
- Practical implications for investors

**5.3 Limitations**
- Data constraints
- Model assumptions
- Market frictions

**5.4 Future Research**
- Dynamic weighting schemes
- ML overlay
- Cross-market validation

---

## Part 3: Research Questions & Hypotheses

### Primary Research Question

**RQ:** โมเดล VQM ที่ผสานปัจจัย Value, Quality และ Momentum สามารถสร้างผลตอบแทนที่ดีกว่าตลาดและกลยุทธ์ Single-factor ได้หรือไม่?

### Hypotheses

| ID | Hypothesis | Variable | Test |
|----|-----------|----------|------|
| **H1** | พอร์ต VQM ให้ค่า Sharpe ratio และ alpha สูงกว่า benchmark อย่างมีนัยสำคัญ | Sharpe, Alpha | t-test |
| **H2** | พอร์ต VQM มีผลตอบแทนปรับความเสี่ยงสูงกว่า Value-only, Quality-only, Momentum-only | Risk-adjusted return | Comparison |
| **H3** | การเพิ่ม Quality ทำให้ Max Drawdown และ downside volatility ลดลงอย่างมีนัยสำคัญ | Max DD, Downside vol | Paired test |
| **H4** | โมเดล VQM ยังคงให้ excess return ในหลาย market regimes | Regime returns | Sub-period analysis |
| **H5** | ผลตอบแทนสุทธิหลังหัก transaction costs ยังเป็นบวกและสูงกว่า benchmark | Net return | Cost-adjusted analysis |

---

## Part 4: Development Roadmap

### Phase 1: Data & Factor Foundation (Month 1-2)
- [ ] Data pipeline setup
- [ ] PIT data store
- [ ] Factor calculation engine
- [ ] Data quality validation

### Phase 2: Backtest & Validation (Month 3-4)
- [ ] Walk-forward framework
- [ ] Historical backtest (2019-2024)
- [ ] Regime analysis
- [ ] Sensitivity testing

### Phase 3: Thesis Writing (Month 5-8)
- [ ] Chapter 1: Introduction
- [ ] Chapter 2: Literature Review
- [ ] Chapter 3: Methodology
- [ ] Chapter 4: Results
- [ ] Chapter 5: Conclusion

### Phase 4: Defense Preparation (Month 9-10)
- [ ] Presentation slides
- [ ] Q&A preparation
- [ ] Committee review

---

## Part 5: Success Metrics

### Quantitative Targets

| Metric | Target | Benchmark |
|--------|--------|-----------|
| Alpha (p.a.) | > 3% | SET Index |
| Sharpe Ratio | > 1.0 | SET Index |
| Max Drawdown | < -25% | N/A |
| Hit Rate | > 55% | N/A |
| Net Return (after cost) | Positive | N/A |

### Academic Criteria

- [ ] Literature review ครอบคลุม (50+ references)
- [ ] Methodology เชื่อถือได้ (PIT data, walk-forward)
- [ ] Results มีนัยสำคัญทางสถิติ (p < 0.05)
- [ ] Contributions ชัดเจน (theoretical + practical)

---

## Meeting Notes

**Date:** 2026-04-06
**Attendees:** Damodaran (Lead), Codex (Technical), Gemini (Quant/Business)
**Decisions Made:**
1. Project renamed to **VQM Model**
2. Thesis structure approved (5 chapters)
3. Research questions finalized (5 hypotheses)
4. Target: Thai market, 2019-2024 period

**Next Steps:**
1. Lock data sources
2. Define factor formulas (baseline version)
3. Set up development environment

---

## References

- Fama, E. F., & French, K. R. (1992). The cross-section of expected stock returns.
- Jegadeesh, N., & Titman, S. (1993). Returns to buying winners and selling losers.
- Novy-Marx, R. (2013). The other side of value: The gross profitability premium.
- Asness, C. S., et al. (2015). Factor timing: Is it different?

---

*Document created: 2026-04-06*
*Last updated: 2026-04-06*
*Status: Planning Phase — Pending Data Setup*
