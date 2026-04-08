# Methodology: การเก็บข้อมูล ROIC-WACC สำหรับ SET

> **วัตถุประสงค์:** ออกแบบวิธีการเก็บและคำนวณข้อมูล ROIC-WACC สำหรับหุ้นไทย
> **Source:** Codex Research
> **Date:** 2026-04-01

---

## 1. Scope และ Dataset Design

### Universe การศึกษา

| รายการ | รายละเอียด |
|--------|------------|
| **ตลาด** | SET + mai |
| **ช่วงเวลา** | FY2016 - FY2025 (10 ปี) |
| **ข้อมูล** | Consolidated Annual Statements (Audited) |
| **สกุลเงิน** | THB |

### Sector Classification

```
┌── Non-Financial (ใช้ ROIC-WACC ได้)
│   ├── Industrial
│   ├── Property
│   ├── Consumer
│   └── Technology
│
├── Financial (ต้องใช้ framework อื่น)
│   ├── Banks → ROE vs Cost of Equity
│   └── Insurance → Excess Return on Regulatory Capital
│
└── Special Cases
    ├── Holding Companies → Sum-of-Parts
    └── REITs/Property Funds → Different framework
```

### Flags สำหรับ Comparability

| Flag | ใช้เมื่อ |
|------|----------|
| `pre/post lease standard` | TFRS 16 เริ่ม 2020 |
| `M&A-heavy` | Goodwill สำคัญ |
| `restructuring` | มีการปรับโครงสร้างครั้งใหญ่ |

---

## 2. ROIC Methodology

### สูตรหลัก

$$
\text{ROIC}_t = \frac{\text{NOPAT}_t}{\text{Avg Invested Capital}_t}
$$

$$
\text{Avg Invested Capital}_t = \frac{\text{IC}_{t-1} + \text{IC}_t}{2}
$$

### NOPAT Calculation

$$
\text{NOPAT} = \text{EBIT}_{\text{adj}} \times (1 - T_{\text{op}})
$$

#### NOPAT Adjustments สำหรับบริษัทไทย

> [!important] รายการที่ต้องปรับปรุง
> 1. **ลบ Non-operating items:**
>    - FX translation gains/losses
>    - Asset revaluation gains
>    - Gain/loss on asset sales
>    - Litigation one-offs
>    - Insurance recoveries
>
> 2. **Operating Tax Rate:**
>    - Preferred: 3-year normalized cash tax rate
>    - Fallback: Effective tax rate (capped at 20-30%)

### Invested Capital Construction

**Operating Approach:**

$$
\text{Invested Capital} = \text{Operating Assets} - \text{Operating Liabilities}
$$

**Practical Build:**

| รวม (Include) | ไม่รวม (Exclude) |
|---------------|-------------------|
| Net PP&E | Non-operating investments |
| Right-of-use assets | Excess cash |
| Operating intangibles | Assets held for sale |
| Working capital | Treasury investments |
| Lease liabilities | - |

### Adjustments ที่สำคัญ

#### 1. Goodwill

> [!tip] แนวทางปฏิบัติ
> รายงาน **2 ค่า ROIC**:
> - `ROIC (incl goodwill)` = มุมมองประสิทธิภาพการ acquire
> - `ROIC (ex goodwill)` = มุมมองประสิทธิภาพ operating assets

สำหรับ serial acquirers ในไทย ทั้งสองค่ามีประโยชน์

#### 2. Operating Leases (TFRS 16)

| ช่วงเวลา | แนวทาง |
|----------|--------|
| **Post-2020** | Lease liabilities/ROU assets อยู่ใน balance sheet แล้ว → ระวัง double count |
| **Pre-2020** | Capitalize lease commitments ถ้าเปิดเผย หรือใช้ reported accounting พร้อม flag |

> [!warning] สำคัญ
> ต้อง consistent ระหว่าง NOPAT (EBIT basis) และ Capital base

#### 3. Cash Holdings

$$
\text{Excess Cash} = \text{Total Cash} - \text{Operating Cash}
$$

**Operating Cash Proxy:**
- % of sales (เช่น 2-3%)
- หรือ working cash based on industry

> [!example] ทำไมสำคัญสำหรับไทย?
> Thai conglomerates หลายแห่งมี treasury cash ขนาดใหญ่ → ถ้าไม่ลบจะ **understate ROIC**

---

## 3. WACC Methodology

### สูตรหลัก

$$
\text{WACC} = \frac{E}{D+E} K_e + \frac{D}{D+E} K_d (1-T)
$$

### Cost of Equity (Ke)

$$
K_e = R_f + \beta \times \text{ERP} + \text{Size/Liquidity Premium}
$$

#### Risk-Free Rate (Rf)

| แหล่งข้อมูล | รายละเอียด |
|------------|------------|
| ThaiBMA | 10Y Government Bond Yield |
| Convention | Annual average หรือ year-end |

**แหล่ง:** https://www.thaibma.or.th/EN/Market/YieldCurve/Government.aspx

#### Beta (β)

> [!tip] Best Practice สำหรับ SET
> **Compute your own beta:**
> - Weekly returns, 3-5 years
> - vs SET Index (prefer Total Return Index)
>
> **ถ้า thin trading:**
> - ใช้ **bottom-up beta** from sector peers
> - Unlever/relever formula

#### Equity Risk Premium (ERP)

**แหล่ง:**
1. Damodaran Country Risk Premium: https://pages.stern.nyu.edu/~adamodar/
2. Implied ERP from Thai market

### Cost of Debt (Kd)

**Priority Order:**

| Priority | Method |
|----------|--------|
| 1 | YTM from listed bonds |
| 2 | $\frac{\text{Interest Expense}}{\text{Avg Interest-Bearing Debt}}$ (3Y normalized) |
| 3 | Thai corporate credit spreads by rating |

### Capital Structure Weights

> [!important] แนวทาง
> - **Equity:** Market value (preferred)
> - **Debt:** Book value (practical compromise)
> - **Unstable leverage:** ใช้ 3-year average weights

---

## 4. Edge Cases

### 4.1 Negative Earnings / Negative NOPAT

| สถานการณ์ | แนวทาง |
|-----------|--------|
| Single year negative | ใช้ **multi-year median** ROIC |
| Trend analysis | ดู recovery trajectory |
| Decision | หลีกเลี่ยง one-year ROIC-WACC verdicts |

### 4.2 Financial Companies (Banks, Insurance)

> [!warning] ห้ามใช้ ROIC-WACC กับ Financials
> - **Debt = Raw material** ไม่ใช่ funding
> - Regulatory capital requirements ต่างออกไป

**Alternative Framework:**
- Banks: ROE vs Cost of Equity
- Insurance: Excess Return on Regulatory Capital

### 4.3 Holding Companies

| ปัญหา | แนวทาง |
|-------|--------|
| Consolidated ROIC ผิดเพี้ยน | Value มาจาก stakes in subsidiaries |

**Solution: Sum-of-Parts**
1. Look-through NAV
2. Weighted subsidiary ROIC vs Holdco cost of capital
3. Apply holding-company discount separately

---

## 5. Implementation Workflow

### Step-by-Step Process

```
1. Pull Data
   ├── Annual statements (2016-2025)
   ├── Prices, shares outstanding
   └── Debt, interest, tax, lease, goodwill, cash

2. Standardize
   ├── Item mapping
   └── Currency/units

3. Classify
   └── Tag sector/edge-case category

4. Calculate NOPAT
   ├── Adjusted EBIT
   ├── Operating tax
   └── NOPAT

5. Calculate Invested Capital
   ├── Goodwill policy (incl/ex)
   ├── Lease policy
   └── Excess cash removal

6. Calculate ROIC
   └── Both versions (incl/ex goodwill)

7. Calculate WACC
   ├── Rf, Beta, ERP → Ke
   ├── Kd
   └── Weights

8. Calculate Spread
   ├── ROIC - WACC
   └── 3-year average spread

9. QA Checks
   ├── Outliers
   ├── Sign errors
   ├── Denominator near zero
   └── Accounting-break years

10. Output
    ├── Point-year data
    └── Through-cycle summaries
```

---

## 6. Thai Data Sources

### ข้อมูลงบการเงิน

| แหล่ง | URL | ข้อมูล |
|------|-----|--------|
| SEC iDISC | https://market.sec.or.th/public/idisc | Form 56-1 One Report |
| SET Data | https://www.set.or.th/app/online-data/fundamental-data | Fundamental data |
| SETSMART | https://www.set.or.th/en/services/connectivity-and-data/data | Premium data service |

### ข้อมูลตลาด

| แหล่ง | URL | ข้อมูล |
|------|-----|--------|
| ThaiBMA | https://www.thaibma.or.th | Government bond yields |
| BOT | https://www.bot.or.th | Macro/market statistics |
| Damodaran | https://pages.stern.nyu.edu/~adamodar/ | Country risk premium |

---

## 7. Output Template

### Data Structure

| Field | Type | Description |
|-------|------|-------------|
| ticker | string | Stock symbol |
| fiscal_year | int | FY2016-FY2025 |
| sector | string | Industry classification |
| nopat | float | Adjusted NOPAT (THB M) |
| invested_cap | float | Invested Capital (THB M) |
| roic | float | ROIC (%) |
| roic_ex_gw | float | ROIC ex-goodwill (%) |
| rf | float | Risk-free rate (%) |
| beta | float | Levered beta |
| erp | float | Equity risk premium (%) |
| ke | float | Cost of equity (%) |
| kd | float | Cost of debt (%) |
| wacc | float | WACC (%) |
| spread | float | ROIC - WACC (%) |
| spread_3y_avg | float | 3-year average spread (%) |

---

## 8. Quality Checks

### Pre-Analysis Checks

- [ ] ข้อมูลครบ 10 ปีสำหรับบริษัทที่ศึกษา
- [ ] NOPAT adjustments consistent
- [ ] Invested Capital treatment consistent
- [ ] WACC parameters reasonable
- [ ] Edge cases handled appropriately

### Red Flags

| Red Flag | สิ่งที่ต้องตรวจสอบ |
|----------|-------------------|
| ROIC > 50% | Excess cash removal? One-off gains? |
| ROIC < -20% | Negative NOPAT from restructuring? |
| WACC > 20% | Beta สูงผิดปกติ? Distressed? |
| Spread > 30% | Check all inputs |
| Large YoY change | Accounting change? M&A? |

---

## 🔗 Related Notes

- [[A1-EVA-Literature-Review]]
- [[ROIC-WACC Research Design]]
- [[ROIC-WACC Research Plan]]
- [[Quality Swing Investor]]
- [[Investing MOC]]

---

*Research: Codex | Synthesis: Synapse-O*
*Created: 2026-04-01*
