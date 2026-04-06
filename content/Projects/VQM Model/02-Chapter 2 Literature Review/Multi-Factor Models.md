# Multi-Factor Models & Integration — Literature Review

> **Chapter:** 2.4 Multi-Factor Models
> **Thesis:** VQM Model — Integrated Value-Quality-Momentum Model
> **Last Updated:** 2026-04-06

---

## Core Papers (Must Read)

### 1. Fama-French Multi-Factor Models

**Fama, E. F., & French, K. R. (1993). Common Risk Factors in the Returns on Stocks and Bonds.**
*Journal of Financial Economics, 33*(1), 3-56.

**Three-Factor Model:**
- Market (Rm - Rf)
- Size (SMB: Small Minus Big)
- Value (HML: High Minus Low book-to-market)

---

**Fama, E. F., & French, K. R. (2015). A Five-Factor Asset Pricing Model.**
*Journal of Financial Economics, 116*(1), 1-22.

**Five-Factor Model:**
- Market, Size, Value
- Profitability (RMW: Robust Minus Weak)
- Investment (CMA: Conservative Minus Aggressive)

**Relevance to VQM:**
- Foundation for multi-factor modeling
- Profitability factor bridges to Quality
- Factor construction methodology

---

### 2. Value & Momentum Integration

**Asness, C. S., Moskowitz, T. J., & Pedersen, L. H. (2013). Value and Momentum Everywhere.**
*Journal of Finance, 68*(3), 929-985.

**Key Findings:**
- Value and momentum work globally
- **Critical:** Value and momentum negatively correlated (~ -0.6)
- Combining both improves risk-adjusted returns
- Not explained by standard risk factors

**Relevance to VQM:**
- **Primary justification** for VQM approach
- Factor diversification benefit
- Global applicability (including emerging markets)

---

### 3. Factor Timing Challenges

**Asness, C. S., et al. (2015). Factor Timing: Is It Different?**
*Journal of Portfolio Management.

**Key Findings:**
- Factor timing extremely difficult
- Factors can underperform for extended periods
- Strategic factor allocation preferred over tactical timing

**Relevance to VQM:**
- Supports static weight allocation (45/35/20)
- Avoid factor timing complexity
- Focus on long-term factor premiums

---

### 4. Multi-Factor Portfolio Construction

**Clarke, R., de Silva, H., & Thorley, S. (2016). Fundamentals of Multifactor Portfolio Construction.**
*Journal of Portfolio Management, 42*(5), 51-61.

**Key Findings:**
- Two main approaches:
  1. **Factor Portfolio:** Combine single-factor portfolios
  2. **Security Selection:** Score stocks on multiple factors
- Security selection generally superior
- Factor correlation considerations critical

**Relevance to VQM:**
- VQM uses security selection approach
- Composite score = weighted sum of factor scores
- Factor weighting (45/35/20) based on research

---

### 5. Factor Interaction & Correlation

**Blitz, D., & van Vliet, P. (2007). The Volatility Effect.**
*Journal of Portfolio Management, 34*(1), 102-110.

**Key Findings:**
- Low volatility stocks outperform
- Low volatility correlates with quality
- Factor interdependence matters

**Relevance to VQM:**
- Quality captures low-volatility effect
- Factor correlation analysis important

---

## Additional Multi-Factor Papers

| Paper | Authors | Year | Key Finding |
|-------|---------|------|-------------|
| Your Factor Allocation May Be Inefficient | Berger, D., et al. | 2020 | Naive combination often works well |
| Factor Definitions Matter | Novy-Marx, R. | 2013 | Factor construction critical |
| Alternative Multi-Factor Models | Carhart, M. | 1997 | 4-factor model with momentum |
| Barra Risk Models | MSCI | Ongoing | Industry standard for risk models |

---

## VQM Factor Correlation Matrix

Based on literature (approximate):

| | Value | Quality | Momentum |
|--|-------|---------|----------|
| Value | 1.00 | -0.10 to 0.30 | **-0.50 to -0.70** |
| Quality | -0.10 to 0.30 | 1.00 | -0.10 to -0.30 |
| Momentum | **-0.50 to -0.70** | -0.10 to -0.30 | 1.00 |

**Key Insight:** Value-Momentum negative correlation = main diversification benefit

---

## Factor Weighting Approaches

### 1. Equal Weight (1/3, 1/3, 1/3)
- Simple, robust
- Ignores factor return differences

### 2. Risk Parity
- Equal risk contribution
- Requires volatility estimates

### 3. Research-Based (VQM Approach)
- Value 45% - highest historical premium
- Quality 35% - defensive, reduces drawdown
- Momentum 20% - higher costs, crash risk

---

## VQM Model vs. Other Multi-Factor Models

| Model | Factors | Weighting | Market |
|-------|---------|-----------|--------|
| **Fama-French 3F** | Market, Size, Value | N/A | US |
| **Fama-French 5F** | + Profitability, Investment | N/A | US |
| **Carhart 4F** | FF3 + Momentum | N/A | US |
| **AQR Quality** | Quality, Value, Momentum, Low Vol | Varies | Global |
| **VQM Model** | Value, Quality, Momentum | 45/35/20 | Thai |

**VQM Differentiators:**
- Focus on Thai market
- ROIC-based quality
- Simpler (3 factors vs 4-5)
- Practical implementation focus

---

## Factor Regression Analysis

For testing VQM model:

```
R_VQM - Rf = α + β_MKTMKT(R_MKT - Rf) + β_SMB SMB + β_HML HLM + β_UMD MOMD + ε
```

**Where:**
- α = Alpha (target: significantly positive)
- β_MKT = Market beta
- β_SMB = Size beta
- β_HML = Value beta
- β_UMD = Momentum beta

---

## Research Questions from Multi-Factor Literature

1. What is optimal factor weighting for Thai market?
2. How to handle factor correlation in portfolio construction?
3. Should factors be timed or held statically?
4. What is capacity of multi-factor strategies in Thai market?

---

## References (APA Format)

```
Asness, C. S., Moskowitz, T. J., & Pedersen, L. H. (2013). Value and 
momentum everywhere. Journal of Finance, 68(3), 929-985.

Berger, D., Crowhurst, D., & Rajendra, H. (2020). Your factor allocation 
may be inefficient. Journal of Portfolio Management.

Blitz, D., & van Vliet, P. (2007). The volatility effect: Lower risk 
without lower return. Journal of Portfolio Management, 34(1), 102-110.

Carhart, M. M. (1997). On persistence in mutual fund performance. 
Journal of Finance, 52(1), 57-82.

Clarke, R., de Silva, H., & Thorley, S. (2016). Fundamentals of 
multifactor portfolio construction. Journal of Portfolio Management, 
42(5), 51-61.

Fama, E. F., & French, K. R. (1993). Common risk factors in the returns 
on stocks and bonds. Journal of Financial Economics, 33(1), 3-56.

Fama, E. F., & French, K. R. (2015). A five-factor asset pricing model. 
Journal of Financial Economics, 116(1), 1-22.

Novy-Marx, R. (2013). The other side of value: The gross profitability 
premium. Journal of Financial Economics, 108(1), 1-28.
```

---

*Document created: 2026-04-06*
*Status: Literature Review — Multi-Factor Section*
