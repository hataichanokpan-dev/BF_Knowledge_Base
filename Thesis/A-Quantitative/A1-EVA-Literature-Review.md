# EVA และ ROIC-WACC Spread: การทบทวนวรรณกรรม

> **Research Question:** EVA และช่องว่าง ROIC-WACC ช่วยให้เลือกหุ้นได้ดีขึ้นจริงหรือไม่?
> **Source:** Gemini Literature Review
> **Date:** 2026-04-01

---

## 1. ที่มาของ EVA (Stewart, 1991)

### แนวคิดหลัก

**Economic Value Added (EVA)** ถูกนำเสนอโดย **Joel Stern** และ **G. Bennett Stewart III** แห่ง **Stern Stewart & Co.** ในหนังสือ *"The Quest for Value"* (1991)

> [!info] ทำไมต้อง EVA?
> มาตรวัดดั้งเดิม (Net Income, EPS) ไม่คำนึงถึง **ต้นทุนของส่วนของผู้ถือหุ้น** ทำให้เข้าใจผิดว่าบริษัททำกำไร แต่จริงๆ แล้วอาจทำลายมูลค่า

### สูตรการคำนวณ

$$
\text{EVA} = \text{NOPAT} - (\text{Invested Capital} \times \text{WACC})
$$

หรือเขียนในรูป spread:

$$
\text{EVA} = \text{Invested Capital} \times (\text{ROIC} - \text{WACC})
$$

| ตัวแปร | ความหมาย |
|--------|-----------|
| NOPAT | Net Operating Profit After Tax |
| ROIC | NOPAT / Invested Capital |
| WACC | Weighted Average Cost of Capital |

> [!tip] สาระสำคัญ
> **ROIC > WACC = สร้างมูลค่า**
> **ROIC < WACC = ทำลายมูลค่า**

---

## 2. หลักฐานเชิงวิชาการที่สนับสนุน

### งานวิจัยหลัก

| Author | Year | สรุป |
|--------|------|------|
| Stewart | 1991 | EVA ดีกว่ามาตรวัดบัญชีเพราะคำนึงต้นทุนเงินทุนทั้งหมด |
| Grant | 1996 | EVA เป็นตัวขับเคลื่อนมูลค่าองค์กร |
| O'Byrne | 1996 | บริษัท EVA บวกต่อเนื่อง → ผลตอบแทนดีกว่าตลาด |
| Ehrbar | 1998 | ยืนยันความสัมพันธ์ EVA กับ Market Value |
| Fernandez | 2002 | EVA สอดคล้องกับมูลค่าเพิ่มที่แท้จริง |
| Chen & Dodd | 2001 | ROIC > WACC ต่อเนื่อง → หุ้นให้ผลตอบแทนดีระยะยาว |

### กลไกการสร้างมูลค่า

```
ROIC > WACC ต่อเนื่อง
      ↓
แสดงถึง Competitive Advantage (Moat)
      ↓
ตลาดยังไม่ priced in ทั้งหมด
      ↓
ผลตอบแทนส่วนเกิน (Alpha) ในระยะยาว
```

---

## 3. หลักฐานที่โต้แย้ง

> [!warning] คำถามท้าทาย
> EVA อาจไม่ได้เหนือกว่ามาตรวัดบัญชีดั้งเดิมอย่างมีนัยสำคัญ

### งานวิจัยที่โต้แย้ง

| Author | Year | ข้อโต้แย้ง |
|--------|------|-----------|
| Biddle, Bowen & Wallace | 1997 | EVA ไม่มีข้อมูลเพิ่มเติมเหนือกว่า Net Income หรือ Operating Cash Flow |
| Dodd & Chen | 1997 | การปรับปรุงงบการเงินต่างกัน → ผลลัพธ์แปรปรวน |
| Stern & Shiely | 2001 | การใช้ไม่ถูกต้องหรือปรับปรุงไม่เหมาะสม → ข้อสรุปผิดพลาด |

### ปัญหาหลัก

1. **ความซับซ้อน:** การปรับปรุงงบการเงินหลายรายการอาจมีความเป็นอัตวิสัย
2. **ความไม่สอดคล้อง:** นักวิเคราะห์คนต่างๆ อาจคำนวณ EVA ต่างกัน
3. **ตลาดอาจรู้แล้ว:** ข้อมูลอาจถูก priced in แล้ว

---

## 4. ข้อจำกัดของ Metric

### ข้อจำกัดสำคัญ

| ข้อจำกัด | คำอธิบาย | ผลกระทบ |
|----------|-----------|----------|
| **ความซับซ้อน** | ต้องปรับปรุงงบหลายรายการ | อัตวิสัย, เปรียบเทียบยาก |
| **การประมาณ WACC** | Beta, Market Risk Premium ไม่แม่นยำ | ผลลัพธ์ผันผวน |
| **ข้อมูลย้อนหลัง** | เป็น backward-looking | อาจไม่ทำนายอนาคตได้ |
| **ความผันผวนระยะสั้น** | การลงทุนใหญ่ทำ EVA ติดลบชั่วคราว | ตีความผิดได้ |
| **ละเลยคุณภาพ** | เชิงปริมาณเท่านั้น | ไม่เห็น Management Quality, ESG |

### คำถามจาก Professor Damodaran

> [!quote] Damodaran's Critical Questions
> 1. NOPAT และ Invested Capital คำนวณยังไง? Adjustments ที่จำเป็น?
> 2. ทำไงเมื่อ cost of debt > cost of equity (distressed)?
> 3. Cyclical businesses: ROIC ผันผวนตาม cycle จะตีความยังไง?
> 4. Startups ที่ ROIC < WACC แต่กำลัง grow จะประเมินยังไง?
> 5. Time Horizon: Spread ต้องดู 1 ปี, 3 ปี, หรือ 5 ปี?

---

## 5. การประยุกต์ใช้ใน Emerging Markets (ตลาดไทย)

### โอกาส

- เน้น **การสร้างมูลค่า** แทนกำไรทางบัญชี
- คัดกรอง **หุ้นคุณภาพ** ที่มี moat ชัดเจน
- ใช้เป็น **internal performance metric** กระตุ้นการตัดสินใจเชิงมูลค่า

### ความท้าทายในตลาดไทย

| ปัจจัย | ความท้าทาย |
|--------|------------|
| **คุณภาพข้อมูล** | มาตรฐานบัญชีอาจต่างจาก US GAAP |
| **WACC ผันผวน** | อัตราดอกเบี้ย, ความเสี่ยงการเมือง |
| **สภาพคล่อง** ต่ำ | ราคาหุ้นผันผวน, spread กว้าง |
| **ปัจจัยเฉพาะประเทศ** | นโยบายรัฐ, การเมือง, ภัยธรรมชาติ |

### คำแนะนำสำหรับตลาดไทย

> [!tip] Best Practices
> 1. ใช้ **multi-year median** แทนค่าปีเดียว
> 2. ปรับ WACC ตาม **Thailand Country Risk Premium**
> 3. ใช้ร่วมกับ **การวิเคราะห์เชิงคุณภาพ**
> 4. เปรียบเทียบ **ภายใน sector เดียวกัน**

---

## 6. สรุป: EVA ใช้ได้ไหม?

### คำตอบสั้น: **ใช้ได้ แต่ต้องระวัง**

| กรณีที่ใช้ได้ดี | กรณีที่ต้องระวัง |
|-----------------|-------------------|
| บริษัท stable, mature | Startups, high-growth |
| Capital-intensive sectors | Asset-light sectors |
| ดูระยะยาว (3-5 ปี) | ดูระยะสั้น (1 ปี) |
| เปรียบเทียบใน sector เดียวกัน | เปรียบเทียบข้าม sectors |

### Key Takeaways

1. **EVA เป็นเครื่องมือ ไม่ใช่คำตอบ** - ต้องใช้ร่วมกับการวิเคราะห์อื่น
2. **Persistent spread สำคัญกว่า point-in-time** - ดูแนวโน้ม 3-5 ปี
3. **ตลาดอาจรู้แล้วบางส่วน** - ต้องหาจังหวะที่ตลาดยังไม่ priced in
4. **Emerging markets มีความท้าทายเพิ่ม** - ต้องปรับ methodology ให้เหมาะสม

---

## 7. Key Citations

```bibtex
@book{stewart1991quest,
  title={The Quest for Value: The EVA Management Guide},
  author={Stewart, G. Bennett},
  year={1991},
  publisher={HarperBusiness}
}

@article{biddle1997eva,
  title={Economic Value Added: Some empirical evidence},
  author={Biddle, Gary C and Bowen, Robert M and Wallace, James S},
  journal={Journal of Applied Corporate Finance},
  volume={9},
  number={3},
  pages={73--82},
  year={1997}
}

@article{chen2001eva,
  title={Economic Value Added (EVA): An empirical examination},
  author={Chen, Shimin and Dodd, James L},
  journal={Journal of Managerial Issues},
  pages={317--333},
  year={2001}
}
```

---

## 🔗 Related Notes

- [[ROIC-WACC Research Design]]
- [[ROIC-WACC Research Plan]]
- [[A2-Data-Methodology]]
- [[Quality Swing Investor]]
- [[Investing MOC]]

---

*Research: Gemini | Synthesis: Synapse-O*
*Created: 2026-04-01*
