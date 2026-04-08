# ROIC - WACC: จากทฤษฎีสู่การลงทุนจริง

> **Research Question:** ช่องว่าง ROIC - WACC ช่วยให้วิเคราะห์ ประเมิน และเลือกหุ้นได้ดีขึ้นจริงหรือไม่?

---

## 🎯 สาระสำคัญที่ต้องพิสูจน์

### 1. Thesis Statement
> "บริษัทที่มี ROIC > WACC อย่างต่อเนื่อง จะสร้างผลตอบแทนที่ดีกว่าตลาดในระยะยาว"

**แต่... คำถามท้าทาย:**
- ตลาดรู้เรื่องนี้แล้วหรือยัง? (priced in?)
- Gap ต้องกว่าเท่าไหร่ถึง matter?
- เป็น leading หรือ lagging indicator?

---

## 📊 Research Framework

### Phase 1: ทบทวนทฤษฎี (Literature Review)

| หัวข้อ | คำถามหลัก | แหล่งข้อมูล |
|--------|-----------|-------------|
| EVA Origins | Stewart (1991) กล่าวอ้างอะไร | EVA literature |
| Academic Evidence | หลักฐานเชิงวิชาการสนับสนุนไหม | Journal articles |
| Practitioner Use | Fund managers ใช้จริงไหม | Interviews, Reports |

### Phase 2: สร้าง Dataset

**ตัวแปรที่ต้องเก็บ:**

| Variable | Definition | Source |
|----------|------------|--------|
| ROIC | NOPAT / Invested Capital | งบการเงิน |
| WACC | Cost of Equity × Weight + Cost of Debt × Weight | คำนวณ |
| Spread | ROIC - WACC | Derived |
| Excess Return | Stock Return - Market Return | Price data |
| Valuation Multiple | P/E, P/BV, EV/EBITDA | Market data |

**ช่วงเวลา:** 10 ปี (2016-2025)

**กลุ่มตัวอย่าง:**
- SET 100 หรือ SET 50
- แบ่งเป็น deciles ตาม ROIC-WACC spread

### Phase 3: การทดสอบสมมติฐาน

#### H1: Predictive Power
```
H0: ROIC-WACC spread ไม่สามารถทำนาย excess returns
H1: ROIC-WACC spread สามารถทำนาย excess returns
```

**Method:** Regression analysis
```
Excess Return = α + β₁(ROIC-WACC) + β₂(Size) + β₃(BTM) + ε
```

#### H2: Persistence
```
H0: High spread บริษัทไม่ maintain สถานะ
H1: High spread บริษัท maintain สถานะ (moat exists)
```

**Method:** Transition matrix (Year N → Year N+1, N+3, N+5)

#### H3: Priced In?
```
H0: ตลาดได้ priced in ช่องว่าง ROIC-WACC แล้ว
H1: ตลาดยังไม่ได้ priced in อย่างสมบูรณ์
```

**Method:** Compare high spread stocks' valuations vs returns

---

## 🔬 Research Design: 3 แนวทาง

### แนวทาง A: Quantitative Portfolio Test

**ขั้นตอน:**
1. จัดกลุ่มหุ้นเป็น 5 quintiles ตาม ROIC-WACC spread
2. สร้าง equal-weighted portfolio แต่ละกลุ่ม
3. Rebalance ทุกปี
4. วัด: Return, Volatility, Sharpe Ratio, Max Drawdown

**สิ่งที่ต้องดู:**
- Top quintile ชนะ bottom quintile ไหม?
- Alpha หลัง adjust risk แล้วเหลือไหม?
- Transaction costs กินกำไรไปไหม?

### แนวทาง B: Case Study Analysis

**เลือก 10 บริษัทศึกษาลึก:**
- 5 บริษัทที่ spread สูงต่อเนื่อง
- 5 บริษัทที่ spread ติดลบต่อเนื่อง

**วิเคราะห์:**
- อะไรขับเคลื่อน ROIC สูง? (moat, pricing power, efficiency)
- ทำไม spread ติดลบ? (commoditized, high capex, poor allocation)
- ตลาดประเมินถูก/ผิดตอนไหน?

### แนวทาง C: Valuation Integration Test

**คำถาม:** ใช้ ROIC-WACC เพื่อประเมินมูลค่าได้ไหม?

**วิธีทดสอบ:**
1. DCF แบบใช้ ROIC assumption ใน terminal value
2. เทียบ intrinsic value กับ market price
3. วัด accuracy ของการทำนาย price correction

---

## 📋 หัวข้อวิจัยย่อย (Sub-Research Questions)

### SR1: Sector Sensitivity
> "ROIC-WACC spread ใช้ได้ผลกับทุก sector หรือไม่?"

**สมมติฐาน:** ใช้ได้ดีกับ capital-intensive sectors แต่อาจมี noise ใน sectors ที่ asset-light

### SR2: Size Effect
> "ขนาดบริษัทมีผลต่อประสิทธิภาพของ metric นี้ไหม?"

**สมมติฐาน:** Large caps มี ROIC ซับซ้อนกว่า small caps

### SR3: Mean Reversion
> "ROIC-WACC spread mean-revert ไวแค่ไหน?"

**สมมติฐาน:** High ROIC attracts competition → reverts to cost of capital

### SR4: Quality vs Value
> "ROIC-WACC เป็น quality factor, value factor, หรือผสม?"

**ทดสอบ:** Factor analysis vs Fama-French factors

---

## 🎓 Damodaran's Critical Questions

> *"Don't just accept the metric. Understand when it works and when it fails."*

### คำถามท้าทายที่ต้องตอบ:

1. **Accounting Issues:** NOPAT และ Invested Capital คำนวณยังไง? Adjustments ที่จำเป็น?
2. **Negative WACC:** ทำไงเมื่อ cost of debt > cost of equity (distressed)?
3. **Cyclical Businesses:** ROIC ผันผวนตาม cycle จะตีความยังไง?
4. **Growth Phase:** Startups ที่ ROIC < WACC แต่กำลัง grow จะประเมินยังไง?
5. **Time Horizon:** Spread ต้องดู 1 ปี, 3 ปี, หรือ 5 ปี?

---

## 📦 Deliverables

| # | ผลงาน | Format |
|---|-------|--------|
| 1 | Literature Review Summary | Note |
| 2 | Dataset (SET stocks, 10Y) | CSV/Database |
| 3 | Quantitative Analysis Report | Note + Charts |
| 4 | Case Studies (10 companies) | Notes |
| 5 | Practical Framework | Checklist/Template |
| 6 | Final Thesis Document | Full paper |

---

## 🚀 Next Steps

- [ ] รวบรวม literature ที่เกี่ยวข้อง
- [ ] กำหนด scope (SET 50 หรือ SET 100)
- [ ] สร้าง data collection template
- [ ] เลือก case study companies

---

*Created: 2026-04-01*
*Persona: Professor Aswath Damodaran*
