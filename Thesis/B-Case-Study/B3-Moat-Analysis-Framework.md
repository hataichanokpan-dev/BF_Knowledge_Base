# B3: Moat Analysis Framework

> **Research Question:** วิธีระบุและวัด Economic Moat จาก Financial Statements
> **Purpose:** Practical toolkit สำหรับ Thai stock analysis
> **Date:** 2026-04-01

---

## Executive Summary

> [!tip] Core Principle
> **Moat = Sustainable Competitive Advantage that protects ROIC > WACC over time**

Moat ไม่ใช่เรื่อง "story" แต่ต้องเห็นได้ในตัวเลข Framework นี้ใช้:
- **Quantitative Metrics** — วัดได้จากงบการเงิน
- **Financial Statement Analysis** — ตรวจจับจาก 3 งบ
- **Red Flags Detection** — สัญญาณเตือนจาก footnotes

---

## Part 1: Quantitative Moat Indicators

### 1.1 Primary Moat Metrics

| Metric | Formula | Moat Threshold | Interpretation |
|--------|---------|----------------|----------------|
| **ROIC-WACC Spread** | ROIC - WACC | > 3% sustained | Primary indicator of moat |
| **ROIC (5Y Avg)** | NOPAT / Invested Capital | > 15% | High quality business |
| **Gross Margin Stability** | StdDev(GM) < 2% | Low volatility | Pricing power indicator |
| **Operating Margin vs Industry** | OM - Industry OM | > 5% premium | Cost/pricing advantage |

### 1.2 ROIC Decomposition (DuPont for Moat)

```
ROIC = NOPAT Margin × Capital Turnover
     = (NOPAT / Revenue) × (Revenue / Invested Capital)
```

| Component | What It Measures | High Moat Signal |
|-----------|------------------|------------------|
| **NOPAT Margin** | Pricing power + Cost efficiency | > 15% and stable |
| **Capital Turnover** | Asset efficiency | > 1.0x (varies by industry) |

**Insight:**
- High Margin + Low Turnover = Pricing Power Moat (e.g., luxury brands, software)
- Low Margin + High Turnover = Cost Advantage Moat (e.g., retailers, commodities)
- High Margin + High Turnover = Dual Moat (rare, extremely valuable)

### 1.3 Moat Strength Scorecard

| Indicator | Weight | Score 0-3 | Calculation |
|-----------|--------|-----------|-------------|
| ROIC-WACC Spread (5Y avg) | 25% | 0: <0%, 1: 0-3%, 2: 3-6%, 3: >6% | Spread × 25% |
| Margin Stability (5Y StdDev) | 20% | 0: >5%, 1: 3-5%, 2: 1-3%, 3: <1% | Inverse scale |
| Excess Return Persistence | 20% | 0: <3Y, 1: 3-5Y, 2: 5-7Y, 3: >7Y | Years of ROIC>WACC |
| FCF Conversion | 15% | 0: <50%, 1: 50-70%, 2: 70-90%, 3: >90% | FCF/NOPAT |
| Capital Discipline | 20% | 0: Dilutive, 1: Neutral, 2: Accretive, 3: Strong buyback | Qualitative |

**Total Score Interpretation:**
- **2.5-3.0:** Wide Moat
- **1.5-2.5:** Narrow Moat
- **<1.5:** No Moat

---

## Part 2: Pricing Power Measurement

### 2.1 What is Pricing Power?

> [!definition] Pricing Power
> ความสามารถในการ (1) ขึ้นราคาโดยไม่เสียลูกค้า หรือ (2) รักษาราคาไว้ได้เมื่อ competitor ลดราคา

### 2.2 Financial Statement Indicators

#### From Income Statement

| Indicator | Formula | Pricing Power signal |
|-----------|---------|---------------------|
| **Gross Margin Trend** | (Revenue - COGS) / Revenue | Stable or rising over 5Y |
| **Gross Margin vs Peers** | GM - Industry Avg | Premium > 5% indicates power |
| **Price Realization** | Revenue Growth vs Volume Growth | Revenue > Volume = price increase |
| **SG&A Efficiency** | SG&A / Revenue | Declining = brand leverage |

#### From Balance Sheet

| Indicator | Formula | Pricing power signal |
|-----------|---------|---------------------|
| **Receivables Quality** | DSO trend | Stable/declining despite price increases |
| **Inventory Turnover** | COGS / Avg Inventory | High turnover + high margin = strong |
| **Intangible Assets** | Goodwill + Intangibles / Assets | High ratio may indicate brand value |

#### From Cash Flow Statement

| Indicator | Formula | Pricing power signal |
|-----------|---------|---------------------|
| **Cash Conversion** | OCF / NOPAT | > 90% = quality earnings |
| **Capex Intensity** | Capex / Depreciation | < 1.5x = maintenance mode (moat protected) |
| **Free Cash Flow Margin** | FCF / Revenue | > 10% = strong pricing power |

### 2.3 Pricing Power Test

```
Pricing Power Test (5 Questions):
==================================
1. Gross Margin > Industry Average?  [Y/N]
2. Gross Margin stable/rising 5Y?    [Y/N]
3. Revenue growth > Volume growth?   [Y/N]
4. DSO stable despite price increases? [Y/N]
5. FCF Margin > 10%?                 [Y/N]

Score: 4-5 Yes = Strong Pricing Power
       2-3 Yes = Moderate
       0-1 Yes = No Pricing Power
```

---

## Part 3: Moat Types and Financial Fingerprints

### 3.1 Five Moat Types (Morningstar Framework)

| Moat Type | Definition | Financial Fingerprint | Thai Examples |
|-----------|------------|----------------------|---------------|
| **Intangible Assets** | Brand, patents, licenses | High margin, low asset intensity | ADVANC, CPALL |
| **Switching Costs** | Costly to change providers | High retention, stable revenue | SAP (enterprise) |
| **Network Effect** | Value grows with users | Accelerating revenue, margin expansion | None in TH |
| **Cost Advantage** | Lower cost structure | High gross margin vs peers, scale | CPF |
| **Efficient Scale** | Market only supports few players | High ROIC, limited competition, regulated | BBL, EGCO |

### 3.2 Financial Fingerprints by Moat Type

#### Intangible Assets (Brand/Patents)

```
Income Statement:
- High Gross Margin (>40%)
- High Operating Margin (>20%)
- High SG&A (marketing) but leverage over time

Balance Sheet:
- Low PP&E / Total Assets
- High Intangibles (brands, goodwill)

Cash Flow:
- High FCF conversion
- Low maintenance capex
```

#### Switching Costs

```
Income Statement:
- Stable/declining COGS as % of revenue (scale)
- High recurring revenue
- Low customer acquisition cost over time

Balance Sheet:
- High deferred revenue (subscriptions)
- Low receivables (auto-pay)

Cash Flow:
- Highly predictable OCF
- Low capex intensity
```

#### Network Effect

```
Income Statement:
- Accelerating revenue growth
- Expanding margins as scale increases
- Low incremental cost per user

Balance Sheet:
- Low asset intensity
- Growing deferred revenue

Cash Flow:
- OCF grows faster than revenue
- Minimal capex needed for growth
```

#### Cost Advantage

```
Income Statement:
- Gross margin premium vs peers
- Lower COGS per unit
- SG&A leverage at scale

Balance Sheet:
- High inventory turnover
- Efficient working capital

Cash Flow:
- Strong cash conversion
- Capex focused on efficiency
```

#### Efficient Scale (Regulated/Natural Monopoly)

```
Income Statement:
- Stable, moderate margins
- Predictable revenue
- Limited pricing power but protected returns

Balance Sheet:
- High PP&E (infrastructure)
- Regulated asset base

Cash Flow:
- Strong, predictable OCF
- High maintenance capex
- Dividend-focused
```

---

## Part 4: Red Flags for Moat Deterioration

### 4.1 Income Statement Red Flags

| Red Flag | What to Look For | Moat Implication |
|----------|------------------|------------------|
| **Margin Compression** | GM declining 3+ consecutive years | Pricing pressure, competition |
| **SG&A Inflation** | SG&A growing faster than revenue | Brand investment failing |
| **Revenue Quality** | Receivables > Revenue growth | Channel stuffing, weak demand |
| **One-time Gains** | Frequent "exceptional" items | Core business deteriorating |
| **R&D Decline** | R&D % falling vs peers | Innovation lagging |

### 4.2 Balance Sheet Red Flags

| Red Flag | What to Look For | Moat Implication |
|----------|------------------|------------------|
| **Goodwill Impairment** | Large write-offs | Acquisition moat failing |
| **Inventory Build** | Inventory > Sales growth | Demand weakening |
| **Receivables Aging** | DSO increasing | Customer quality declining |
| **Asset Lightening** | Sale-leaseback, asset sales | Desperation for cash |
| **Equity Dilution** | Frequent capital raises | Value destruction |

### 4.3 Cash Flow Red Flags

| Red Flag | What to Look For | Moat Implication |
|----------|------------------|------------------|
| **FCF Negative** | OCF < Capex consistently | Capital hungry, no moat |
| **Earnings-Cash Gap** | Net Income > OCF persistently | Low quality earnings |
| **Dividend Cut** | Dividend reduced or suspended | Cash preservation needed |
| **Buyback Pause** | Buybacks stopped | Management sees better uses |

### 4.4 Footnote Red Flags (Critical)

| Footnote Item | Red Flag | Moat Warning |
|---------------|----------|--------------|
| **Related Party Transactions (RPT)** | High % of revenue, increasing trend | Governance risk, value leakage |
| **Revenue Recognition** | Policy changes, aggressive timing | Quality deterioration |
| **Leases** | Operating → Finance lease shift | Hidden leverage |
| **Pension/OPEB** | Rising obligations, underfunded | Future cash drain |
| **Legal/Regulatory** | New lawsuits, regulatory actions | Moat under attack |
| **Segment Reporting** | Declining segments hidden in aggregates | Core erosion |
| **Customer Concentration** | Top 5 customers > 30% revenue | Switching cost risk |
| **Key Person Risk** | Founder/CEO departure | Intangible moat at risk |

---

## Part 5: Moat Analysis Checklist

### 5.1 Quantitative Checklist

```
MOAT QUANTITATIVE CHECKLIST
============================

ROIC ANALYSIS:
[ ] ROIC (5Y avg) > 15%
[ ] ROIC > WACC for 5+ consecutive years
[ ] ROIC-WACC spread > 3%
[ ] ROIC stable or improving (StdDev < 3%)

MARGIN ANALYSIS:
[ ] Gross Margin > Industry average
[ ] Gross Margin stable/improving (5Y trend)
[ ] Operating Margin > Industry average
[ ] EBITDA Margin stable

CAPITAL EFFICIENCY:
[ ] Capital Turnover > 1.0x
[ ] Asset Turnover stable/improving
[ ] Working Capital efficient (CCC stable)
[ ] Capex/Depreciation < 1.5x (maintenance mode)

CASH FLOW QUALITY:
[ ] FCF positive 4 of 5 years
[ ] FCF/NOPAT > 80%
[ ] OCF > Net Income consistently
[ ] Dividend sustainable from FCF
```

### 5.2 Qualitative Checklist

```
MOAT QUALITATIVE CHECKLIST
===========================

PRICING POWER:
[ ] Can raise prices without losing customers
[ ] Brand recognition strong
[ ] Premium positioning sustainable
[ ] Customer switching costs exist

COMPETITIVE POSITION:
[ ] Market share stable/growing
[ ] Barriers to entry high
[ ] No existential disruption threat
[ ] Regulatory environment stable/favorable

CAPITAL ALLOCATION:
[ ] Management track record good
[ ] M&A disciplined (accretive)
[ ] Buybacks at reasonable prices
[ ] Dividend policy sustainable

GOVERNANCE:
[ ] Related Party Transactions minimal
[ ] Independent board oversight
[ ] Alignment with minority shareholders
[ ] No major scandals or issues
```

### 5.3 Moat Erosion Warning Checklist

```
MOAT EROSION WARNING SIGNS
==========================

FINANCIAL WARNINGS:
[ ] ROIC declining 2+ years
[ ] Gross margin compression
[ ] FCF turning negative
[ ] Debt/Equity rising
[ ] Inventory building

STRATEGIC WARNINGS:
[ ] New formidable competitor
[ ] Technology disruption
[ ] Regulatory change negative
[ ] Customer consolidation
[ ] Supplier power increasing

MANAGEMENT WARNINGS:
[ ] Key executive departures
[ ] Strategy confusion
[ ] Empire-building M&A
[ ] Aggressive accounting
[ ] Poor communication
```

---

## Part 6: Case Examples of Moat Erosion

### 6.1 Classic Moat Erosion Patterns

#### Pattern 1: Technology Disruption

```
Stage 1: Incumbent dominates, high margins
Stage 2: New technology emerges, dismissed by incumbent
Stage 3: New technology improves, crosses tipping point
Stage 4: Incumbent margins compress, share losses
Stage 5: Incumbent becomes irrelevant or adapts

Financial Signals:
- R&D spending declining as % of revenue
- New product pipeline thin
- Gross margins compressing
- Market share losses accelerating
```

#### Pattern 2: Commodity Trap

```
Stage 1: Industry has pricing power, high margins
Stage 2: New entrants attracted, capacity builds
Stage 3: Oversupply, prices collapse
Stage 4: Margins compress, weakest players exit
Stage 5: Rationalization, but lower equilibrium margins

Financial Signals:
- Industry capacity growing > demand
- New entrants appearing
- Gross margins declining industry-wide
- Capex cycle peaking
```

#### Pattern 3: Customer Concentration Risk

```
Stage 1: Large customer provides stable revenue
Stage 2: Dependency grows, customer gains leverage
Stage 3: Customer demands price concessions
Stage 4: Margins compress, customer may leave
Stage 5: Revenue cliff if customer exits

Financial Signals:
- Top customer > 10% of revenue
- Customer growing faster than company
- Gross margins lower for large customer
- Contract renewal risk approaching
```

### 6.2 Thai Market Examples

| Company | Moat Type | Erosion Signal | Outcome |
|---------|-----------|----------------|---------|
| **Traditional Retail** | Location/Scale | E-commerce disruption | Store closures, margin compression |
| **Print Media** | Content/Brand | Digital disruption | Revenue collapse, restructuring |
| **Fixed-line Telecom** | Infrastructure | Mobile substitution | Business model obsolete |
| **Conventional Banks** | Relationship/FDIC | Fintech disruption | Under pressure, adapting |

---

## Part 7: Practical Application for Thai Stocks

### 7.1 Sector-Specific Moat Considerations

| Sector | Primary Moat Type | Key Metric to Watch | Thai Context |
|--------|-------------------|---------------------|--------------|
| **Banking** | Cost of Funds, Scale | ROE vs CoE, NIM | Regulatory moat strong |
| **Telecom** | Network Effect, Switching | ARPU, Churn | Spectrum as barrier |
| **Retail** | Scale, Location, Brand | SSG, Store ROIC | Real estate critical |
| **Energy** | Efficient Scale, Regulation | ROIC vs WACC | PPA provides moat |
| **Property** | Land Bank, Brand | ROIC, Pre-sales | Location, location, location |
| **Agribusiness** | Vertical Integration, Scale | ROIC, Margin stability | Commodity exposure |
| **Industrial** | Cost Position, Scale | Gross Margin vs Peers | Global competition |

### 7.2 Thai Market Moat Challenges

> [!warning] Thailand-Specific Risks

1. **Family Control** — Related Party Transactions common, governance risk
2. **Concentration** — Many industries dominated by few players
3. **Regulatory Uncertainty** — Policy changes can erode moats
4. **Technology Lag** — Digital disruption accelerating
5. **Political Risk** — Can affect regulated businesses

### 7.3 Red Flags Specific to Thai Market

| Red Flag | Thai Context | Where to Find |
|----------|--------------|---------------|
| **RPT with Group Companies** | CP, SCG, etc. have extensive related parties | Notes to financial statements |
| **Land/Asset Transfers** | Related party at non-market prices | Related party disclosure |
| **Executive Compensation** | High vs company performance | Proxy statements, Annual Report |
| **Dividend Policy** | Irregular, despite earnings | Dividend history |
| **Share Pledging** | Major shareholders pledging shares | SET announcements |

---

## Part 8: Integration with ROIC-WACC Thesis

### 8.1 Moat as ROIC Protector

```
ROIC Sustainability Framework:
==============================

                    ┌─────────────────────┐
                    │  ROIC > WACC        │
                    │  (Value Creation)   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │  ECONOMIC MOAT      │
                    │  (Protects ROIC)    │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│  Pricing      │    │  Cost         │    │  Regulatory/  │
│  Power        │    │  Advantage    │    │  Structural   │
│               │    │               │    │               │
│  High Margin  │    │  High Turn    │    │  Protected    │
│  Low Turn     │    │  Low Margin   │    │  Position     │
└───────────────┘    └───────────────┘    └───────────────┘
```

### 8.2 Moat + ROIC-WACC Decision Matrix

| ROIC-WACC Spread | Moat Strength | Investment Action |
|------------------|---------------|-------------------|
| High (>6%) | Wide | **Strong Buy** — Compounder |
| High (>6%) | Narrow | **Buy** — But monitor moat |
| Moderate (3-6%) | Wide | **Buy** — Undervalued opportunity |
| Moderate (3-6%) | Narrow | **Hold** — Requires catalyst |
| Low (0-3%) | Wide | **Watch** — Turnaround candidate |
| Low (0-3%) | Narrow | **Avoid** — No competitive advantage |
| Negative | Any | **Avoid** — Value destruction |

---

## Appendix A: Formulas Reference

### ROIC Calculation

```
ROIC = NOPAT / Invested Capital

Where:
NOPAT = EBIT × (1 - Tax Rate)
      = Operating Income × (1 - Tax Rate)

Invested Capital = Total Equity + Total Debt - Cash & Equivalents
                 = Total Assets - Current Liabilities + Short-term Debt - Cash

Adjustments:
- Add back operating leases (if material)
- Remove excess cash
- Capitalize R&D (if material)
- Adjust for one-time items
```

### WACC Calculation

```
WACC = (E/V × Re) + (D/V × Rd × (1 - Tc))

Where:
E = Market value of equity
D = Market value of debt
V = E + D
Re = Cost of Equity (via CAPM: Rf + β × (Rm - Rf))
Rd = Cost of Debt (YTM or interest rate)
Tc = Corporate tax rate

Thai Market Assumptions:
- Rf (Risk-free) = 2-3% (Thai 10Y bond)
- Rm (Market return) = 8-10% (SET historical)
- Beta = From regression or industry average
```

### Margin Formulas

```
Gross Margin = (Revenue - COGS) / Revenue
Operating Margin = Operating Income / Revenue
EBITDA Margin = EBITDA / Revenue
FCF Margin = Free Cash Flow / Revenue
NOPAT Margin = NOPAT / Revenue
```

### Turnover Formulas

```
Asset Turnover = Revenue / Total Assets
Capital Turnover = Revenue / Invested Capital
Inventory Turnover = COGS / Average Inventory
Receivables Turnover = Revenue / Average Receivables
```

---

## Appendix B: Data Sources for Thai Stocks

| Data Point | Source | Notes |
|------------|--------|-------|
| Financial Statements | SETSMART, Company IR | Annual reports, 56-1 |
| Stock Prices | SET, Yahoo Finance | For beta calculation |
| Industry Data | SET Sector Indices | For peer comparison |
| Risk-free Rate | Bank of Thailand | Thai government bonds |
| Market Data | SET | Market cap, trading data |
| Footnotes | Annual Report Notes | Critical for red flags |

---

## Appendix C: Quick Reference Card

```
MOAT ANALYSIS QUICK REFERENCE
=============================

STEP 1: Calculate ROIC-WACC Spread
- ROIC = NOPAT / Invested Capital
- WACC = Cost of Equity × Weight + Cost of Debt × Weight
- Spread = ROIC - WACC
- Threshold: >3% sustained = Moat likely

STEP 2: Identify Moat Type
- High Margin + Low Turnover = Pricing Power
- Low Margin + High Turnover = Cost Advantage
- High Margin + High Turnover = Dual Moat (rare)

STEP 3: Check Moat Health
- Margin trend: Stable or improving?
- ROIC persistence: 5+ years?
- FCF conversion: >80%?

STEP 4: Scan for Red Flags
- Income: Margin compression, revenue quality
- Balance: Goodwill impairment, inventory build
- Cash Flow: Negative FCF, earnings-cash gap
- Footnotes: RPT, revenue recognition, leases

STEP 5: Assess Sustainability
- Barriers to entry still high?
- Disruption risk?
- Management quality?
- Governance sound?

DECISION:
- Wide Moat + High Spread = Compounder
- Narrow Moat + Moderate Spread = Quality play
- No Moat + Low Spread = Avoid/Speculative
```

---

## Related Notes

- [[ROIC-WACC Research Design]]
- [[B1-High-Spread-Companies]]
- [[B2-Negative-Spread-Companies]]
- [[A1-EVA-Literature-Review]]
- [[A2-Data-Methodology]]
- [[Quality Swing Investor]]
- [[Capital Allocation]]
- [[Investing MOC]]

---

*Framework: Based on Morningstar, Damodaran, Greenblatt methodologies*
*Adapted for: Thai Stock Market Analysis*
*Created: 2026-04-01*
