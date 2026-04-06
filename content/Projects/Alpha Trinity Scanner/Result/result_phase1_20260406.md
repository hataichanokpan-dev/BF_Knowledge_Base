# 🚨 CITICAL AUDIT REPORT: Look-Ahead Bias ใน Alpha Trinity Backtest

**วันที่:** 6 เมษายน 2026  
**ผู้ตรวจสอบ:** Damodaran + Codex + Gemini  
**ความรุนแรง:** 🔴 CRITICAL  
**สถานะ:** ผล backtest 2022-2025 **ไร้ความน่าเชื่อถือ**

---

## 📋 สารบัญผู้บริหาร

### สรุปฉบับย่อ

**การทดสอบ Walk-Forward Validation (2022-2025) ที่ผ่านมามีข้อผิดพลาดรุนแรง:**

> **ใช้ราคาหุ้นปัจจุบัน (2026) ไปคำนวณ Expectation Gap ย้อนหลังในปี 2022-2025**

**สรุป:**
- ระบบส่ง `as_of_date` (เช่น 2022-03-31) ไปที่ `GapScorer`
- แต่ `GapScorer` **ไม่ได้ใช้** `as_of_date` ต่อ
- `ImpliedExpectations` ไม่รับพารามิเตอร์วันที่เลย
- `ReverseDCFEngine` ดึง `currentPrice` จาก Yahoo Finance (ราคาวันนี้)
- **ผล:** ใช้ราคาปี 2026 ไปคำนวณ Gap Score ในปี 2022 = **LOOK-AHEAD BIAS**

**หมายเหตุ:** ผล backtest ที่รายงามก่อนหน้านี้ **ไม่สามารถเชื่อถือได้**

---

## 🔍 รายละเอียดการตรวจสอบ

### 1. Data Flow Trace

```
Walk-Forward Validation (2022-03-31 rebalance)
↓
scorer.calculate_gap_score("PTT", as_of_date=date(2022, 3, 31))
↓ [gap_scorer.py:166]
as_of_date parameter ถูกรับ แต่ไม่ถูกใช้!
↓ [gap_scorer.py:188]
self.expectations.decompose_expectations("PTT")  # ไม่ส่ง as_of_date!
↓ [implied_expectations.py:31]
decompose_expectations(symbol)  # ไม่รับวันที่!
↓ [implied_expectations.py:45]
self.engine.get_symbol_inputs("PTT")
↓ [reverse_dcf_engine.py:463]
info = self.dm.get_stock_data("PTT", ".BK", force_refresh=False)
↓ [data_manager.py:247]
ticker = yf.Ticker("PTT.BK")
↓
currentPrice = 35.25 บาท  ← ราคาปัจจุบัน 2026-04-06!
```

### 2. โค้ดที่มีปัญหา

| ไฟล์ | บรรทัด | ปัญหา |
|------|-------|--------|
| `gap_scorer.py` | 166, 188 | รับ `as_of_date` แต่ไม่ส่งต่อ |
| `implied_expectations.py` | 31, 45 | ไม่รับพารามิเตอร์วันที่ |
| `reverse_dcf_engine.py` | 463, 471 | ใช้ `currentPrice` (วันนี้) |
| `data_manager.py` | 247 | Fetch จาก Yahoo Finance (วันนี้) |
| `stock_snapshot_fetcher.py` | 5 | เขียนชัดเจน "NOT point-in-time" |

### 3. หลักฐานความผิดพลาด

```
┌────────────────────────────────────────────────────────┐
│                  ความเป็นจริง VS ที่ใช้ใน backtest          │
├────────────────────────────────────────────────────────┤
│                                                        │
│  Rebalance Date: 2022-03-31                           │
│  ┌──────────────────────────────────────────────────┐  │
│  │ ควรจะใช้:                                        │  │
│  │  - PTT ราคาณ วันที่ 31 มี.ค. 2022 = 38.00 บาท     │  │
│  │  - งบการเงิน Q4/2021 (ประกาศ 15 ก.พ. 2022)       │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
│  ที่ใช้จริง:                                         │
│  ┌──────────────────────────────────────────────────┐  │
│  │  - PTT ราคาณ วันที่ 6 เม.ย. 2026 = 35.25 บาท ← ใช้ตัวนี้! │  │
│  │  - งบการเงิน Q4/2025 (ล่าสุด) ← ใช้ตัวนี้!     │  │
│  └──────────────────────────────────────────────────┘  │
│                                                        │
└────────────────────────────────────────────────────────┘
```

---

## 💥 ผลกระทบ

### 1. ผล backtest ที่รายงามไปก่อนหน้า

```
┌────────────────────────────────────────────────────────┐
│  ผลที่รายงามมา (ผิดพลาด)                          │
├────────────────────────────────────────────────────────┤
│  Total Return:       -23.17%                          │
│  Excess Return:      +2.19%                           │
│  Max Drawdown:       -42.79%                          │
│  Sharpe Ratio:       -0.33                            │
│                                                        │
│  ❌ ผลเหล่านี้ "ไร้ความหมาย" เพราะ:                   │
│     - ใช้ราคาปี 2026 ไปคำนวณ Gap Score ปี 2022      │
│     - ใช้งบการเงินปี 2025 ไปคำนวณ Gap Score ปี 2022 │
│     - ราคาและ fundamentals ณ วันนั้น "บอกเหตุ"      │
│       เรื่อง 2022 ไม่มีทราบ                               │
└────────────────────────────────────────────────────────┘
```

### 2. เปรียบเทียบ: ถ้าทำถูกต้อง

```
ถ้าใช้ Point-in-Time Data อย่างถูกต้อง:

Rebalance 2022-03-31:
├─ ราคา PTT ณ วันที่ 31 มี.ค. 2022 = 38.00 บาท
├─ Implied Growth = ถอย้อนจากราคา 38 บาท
└─ Gap Score = (Implied - Realistic) / Realistic

vs

ที่ผิดพลาดที่ทำ:
Rebalance 2022-03-31:
├─ ราคา PTT ณ วันที่ 6 เม.ย. 2026 = 35.25 บาท
├─ Implied Growth = ถอย้อนจากราคา 35.25 บาท ← ไม่ใช่ราคาปี 2022!
└─ Gap Score = (Implied - Realistic) / Realistic ← ผิด!
```

### 3. ตัวอย่างที่เห็นได้ชัด

```
สถานการณ์: วันที่ 31 มี.ค. 2022

PTT ในปี 2022:
├─ ราคาจริง: 38.00 บาท (ณ วันที่ 31 มี.ค. 2022)
├─ Implied Growth (จากราคา 38): 8%
└─ Realistic Cap: 10%
    → Gap = (8-10)/10 = -20% → ACCEPTABLE ✅

PTT วันนี้ (2026):
├─ ราคาจริง: 35.25 บาท
├─ Implied Growth (จากราคา 35.25): 6%
└─ Realistic Cap: 10%
    → Gap = (6-10)/10 = -40% → ACCEPTABLE ✅

ปัญหา:
- Gap Score ที่ได้ มาจากราคา 35.25 (2026) ไม่ใช่ราคา 38 (2022)
- แต่เราถือว่าเป็น Gap Score ของวันที่ 31 มี.ค. 2022
- นี่คือการ "โกง" อย่างรุนแรง!
```

---

## 🛠️ วิธีแก้ไข (แนวทางการแก้)

### Phase 0: Critical Fix (ต้องทำก่อนใช้จริง)

```python
# 1. gap_scorer.py - ส่ง as_of_date ต่อ
def calculate_gap_score(
    self,
    symbol: str,
    as_of_date: Optional[date] = None,  # ← รับแล้ว
) -> Dict:
    try:
        # STEP: ส่ง as_of_date ต่อให้ expectations
        implied = self.expectations.decompose_expectations(
            symbol, 
            as_of_date=as_of_date  # ← เพิ่มพารามิเตอร์นี้
        )
        
        # ... rest of code

# 2. implied_expectations.py - รับ as_of_date
def decompose_expectations(
    self,
    symbol: str,
    as_of_date: Optional[date] = None,  # ← เพิ่ม
) -> Dict:
    try:
        # STEP: ส่ง as_of_date ต่อให้ engine
        inputs = self.engine.get_symbol_inputs(
            symbol,
            as_of_date=as_of_date  # ← เพิ่มพารามิเตอร์นี้
        )

# 3. reverse_dcf_engine.py - รับ as_of_date
def get_symbol_inputs(
    self,
    symbol: str,
    as_of_date: Optional[date] = None,  # ← เพิ่ม
    market_price: Optional[float] = None,
) -> Dict[str, float]:
    """
    Get symbol inputs ณ วันที่ระบุ (Point-in-Time)
    
    Args:
        symbol: Stock symbol
        as_of_date: วันที่ที่ต้องการ (สำหรับ PIT)
        market_price: ราคาที่ override (optional)
    """
    # STEP: ถ้าระบุ as_of_date → ใช้ราคาจากชุดข้อมูลย้อนหลัง
    if as_of_date is not None:
        # ดึงราคาจาก historical prices
        hist_price = self.get_historical_price(symbol, as_of_date)
        if hist_price is not None:
            px = hist_price
        else:
            raise ValueError(f"No historical price for {symbol} as of {as_of_date}")
    
    # STEP: ถ้าไม่ระบุ market_price → ดึง current price (แต่ควรระวัง!)
    if market_price is None:
        # ถ้าเป็น backtest mode → ห้ามใช้ current price!
        if as_of_date is not None and as_of_date < date.today():
            raise ValueError(
                f"Cannot use current price for backtest "
                f"(as_of_date={as_of_date}, today={date.today()})"
            )
        info = self.dm.get_stock_data(symbol, self.suffix, force_refresh=False)
        px = float(info.get("currentPrice") or 0.0)
    else:
        px = market_price
    
    # ... rest of code

# 4. เพิ่ม method สำหรับดึงราคาย้อนหลัง
def get_historical_price(
    self,
    symbol: str,
    as_of_date: date,
) -> Optional[float]:
    """
    ดึงราคาย้อนหลัง ณ วันที่ที่ระบุ
    
    Args:
        symbol: Stock symbol (เช่น PTT)
        as_of_date: วันที่ที่ต้องการ
    
    Returns:
        ราคาปิด (close) ณ วันที่ as_of_date หรือก่อนหน้า
    """
    # ใช้ returns_df ที่มีอยู่แล้ว (จาก Yahoo Finance)
    # หรือจาก historical data cache
    
    # ถ้ามี as_of_date ใน returns_df → ใช้ราคานั้น
    # ถ้าไม่ → ใช้ราคาล่าสุดก่อนหน้า
    
    # TODO: Implement this properly!
```

### Phase 1: ใช้ข้อมูลที่มีอยู่แล้ว

```python
# ใน walk_forward_validator.py แก้ไขการคัดหุ้น

def _rebalance(self, signal_date: date) -> List[str]:
    """
    Rebalance ณ วันที่ signal_date
    """
    # STEP 1: Get all gap scores
    gap_results = []
    for symbol in self.universe:
        # เปลี่ยนแนวทาง: ใช้ closes จาก returns_df
        # แทนที่จะใช้ GapScorer (ที่ใช้ current price)
        
        # วิธีที่ถูกต้อง:
        # 1. ดึงราคาณ วันที่ signal_date จาก returns_df
        if symbol in self.returns_df.columns:
            if signal_date in self.returns_df.index:
                price = self.returns_df.loc[signal_date, symbol]
            else:
                # ถ้าไม่ม → ใช้ราคาล่าสุดก่อนหน้า
                prior_dates = self.returns_df.index[self.returns_df.index <= signal_date]
                if len(prior_dates) > 0:
                    price = self.returns_df.loc[prior_dates[-1], symbol]
                else:
                    continue  # Skip symbol
        else:
            continue
        
        # 2. คำนวณ gap score จาก fundamentals ที่มีใน cache
        # แต่ต้องมั่นใจว่า fundamentals ที่ใช้เป็น PIT
        snapshot = self.pit_cache.get_snapshot(symbol, signal_date)
        if snapshot is None:
            continue
        
        # 3. คำนวณ implied expectations จาก fundamentals + price
        implied_growth = self._calculate_implied_growth(snapshot, price)
        realistic_growth = self.realistic_calculator.calculate_growth_cap(symbol, implied_growth)
        
        gap = (implied_growth - realistic_growth) / realistic_growth
        gap_results.append((symbol, gap))
    
    # STEP 2: Select top_n
    gap_results.sort(key=lambda x: x[1])  # น้อยสุด = ดีสุด
    selected = [s for s, _ in gap_results[:self.top_n]]
    
    return selected
```

---

## 📊 สถานะปัจจุบัน

### Data ที่มีอยู่ vs ที่ต้องการ

| ประเภทที่ต้องการ | สถานะ | Source |
|---------------------|---------|--------|
| **ราคาย้อนหลัง (2022-2025)** | ✅ มีแล้ว | `data/historical/returns_2022_2025.csv` |
| **ราคาปัจจุบัน (2026)** | ✅ มีแต่ใช้ผิด | Yahoo Finance API |
| **Fundamentals 2022-2025** | ✅ มีใน cache | `HistoricalDataCache` |
| **Fundamentals PIT** | ⚠️ มีแต่ต้อง validate | `RegulatoryDeadlineProxy` |

### สิ่งที่ต้องแก้ไข

```
รายการลำดับความสำคัญ:

1. CRITICAL - แก้ Look-ahead Bias (ต้องทำก่อนใช้)
   ✅ gap_scorer.py → ส่ง as_of_date ต่อ
   ✅ implied_expectations.py → รับ as_of_date
   ✅ reverse_dcf_engine.py → ใช้ historical price
   ✅ walk_forward_validator.py → ใช้ closes จาก returns_df

2. HIGH - Validate Fundamentals PIT
   ✅ ตรวจสอบงบการเงินที่ใช้ประกาศหลัง as_of_date
   ✅ ใช้ RegulatoryDeadlineProxy อย่างถูกต้อง

3. MEDIUM - Re-run Validation
   ✅ รัน backtest ใหม่ look-ahead bias
   ✅ เปรียบผล Before vs After

4. LOW - Documentation
   ✅ บันทึกขั้นตอนการแก้ไข
```

---

## 🎯 คำแนะนำสุดท้าย

### สำหรับการใช้งานตอนนี้

```
1. หยุดรัน backtest ในรูปแบที่ผ่านมา
   → ผลลัพธ์ไม่สามารถเชื่อถือได้

2. รอให้แก้ไข look-ahead bias ให้เสร็จ
   → ตาม Phase 0 ด้านบน

3. Re-run backtest ใหม่ข้อมูลที่ถูกต้อง
   → คาดว่าผลจะเปลี่ยนแค่ไหน

4. ถ้าผลดีขึ้น → พิจารณาใช้งานจริง
   → ถ้าผลแย่ลง → ควรตัดสินใจที่จะทำต่อ
```

### สำหรับการพัฒนาระบบ

```
Option A: แก้ไขให้ถูกต้องทั้งหมด
├─ Pros: Backtest มีความน่าเชื่อถือ
├─ Cons: ใช้เวลานานมาก
└─ Timeline: 1-2 สัปดาห์

Option B: ใช้เป็น Screening Tool เท่านั้น
├─ Pros: ไม่ต้อง backtest, ใช้ได้เลย
├─ Cons: ไม่มีหลักฐานว่า strategy ทำงาน
└─ Timeline: ใช้ได้ทันที

Option C: เริ่มใหม่ข้อมูลที่ถูกต้อง
├─ Pros: ใช้เวลาเร็ว
├─ Cons: อาจต้องเปลี่ยน architecture ใหม่
└─ Timeline: 2-3 วัน
```

---

## 📝 บันทึกความทรงจำ

```
**สิ่งที่ค้นพบ:**
- WalkForwardValidator ส่ง as_of_date แต่ไม่ถูกใช้
- ImpliedExpectations ไม่รับพารามิเตอร์วันที่
- ReverseDCFEngine ใช้ currentPrice จาก Yahoo Finance
- ระบบทั้งหมดใช้ราคา/งบการเงิน "วันนี้"
- ไปคำนวณ Gap Score ย้อนหลัง

**ความรุนแรง:**
- SEVERITY: CRITICAL
- IMPACT: INVALIDATES ALL BACKTEST RESULTS
- ACTION REQUIRED: แก้ไขก่อนใช้จริงอีกครั้ง
```

---

**End of Critical Audit Report**

---
*Prepared by:* Damodaran (Financial Analyst) + Codex (Code Auditor) + Gemini (Strategy Auditor)  
*Date:* 6 April 2026  
*Version:* 1.0 - CRITICAL

**⚠️ คำเตือน:** อย่าใช้ผลการทดสอบ walk-forward 2022-2025 ที่รายงามไปก่อหน้า  
อย่าใช้ Gap Score จากคำนวณ Reverse DCF ปัจจุบันสำหรับตัดสินใจลงทุน
จนกว่าจะมีการแก้ไข look-ahead bias ให้เสร็จ
