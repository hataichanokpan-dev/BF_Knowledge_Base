---
tags: [deployment, vercel, sync, quartz]
project: bf-knowledge-base
type: guide
language: thai
created: 2026-04-05
updated: 2026-04-05
---

# วิธี Sync เนื้อหาไป BF-Knowledge-Base (Vercel)

## ภาพรวม

```
BF-Vault (Obsidian) → sync-from-vault.ps1 → BF-Vault-Web/content → GitHub → Vercel
     ↑                                                   ↓
   User edits                                    https://bf-knowledge-base.vercel.app/
```

**คำอธิบาย**:
1. **BF-Vault** = Obsidian vault ที่คุณแก้ไขเอกสาร (Source)
2. **BF-Vault-Web** = Quartz project ที่ deploy บน Vercel (Website)
3. **sync-from-vault.ps1** = Script คัดลอกไฟล์จาก Vault → Web

---

## วิธี Sync (คำสั่งเดียวเสร็จ)

### PowerShell Command

```powershell
cd "C:\Users\bfipa\Documents\BF-Vault-Web"
.\sync-from-vault.ps1 -Push
```

### ที่คำสั่งนี้ทำ:

1. **คัดลอกไฟล์** - Copy เฉพาะไฟล์ที่เปลี่ยนแปลงจาก BF-Vault → BF-Vault-Web/content
2. **Commit** - Commit การเปลี่ยนแปลงพร้อม timestamp
3. **Push** - Push ไปยัง GitHub
4. **Auto Deploy** - Vercel จะ rebuild อัตโนมัติ (ใช้เวลา 1-2 นาที)

### ผลลัพธ์:

หลังจาก 1-2 นาที เนื้อหาจะปรากฏที่:
```
https://bf-knowledge-base.vercel.app/
```

---

## คำสั่งอื่นๆ

### Sync แต่ไม่ Push (ทดสอบก่อน)

```powershell
cd "C:\Users\bfipa\Documents\BF-Vault-Web"
.\sync-from-vault.ps1
```

### Force Sync ทั้งหมด (รวมไฟล์ที่ไม่เปลี่ยน)

```powershell
cd "C:\Users\bfipa\Documents\BF-Vault-Web"
.\sync-from-vault.ps1 -Push -Force
```

### เช็คไฟล์ที่จะถูก sync

```powershell
cd "C:\Users\bfipa\Documents\BF-Vault-Web"
.\sync-from-vault.ps1 -WhatIf
```

---

## Paths สำคัญ

| Location | Path |
|----------|------|
| Source (Obsidian) | `C:\Users\bfipa\Documents\BF-Vault` |
| Deploy Repo (Quartz) | `C:\Users\bfipa\Documents\BF-Vault-Web` |
| Sync Script | `C:\Users\bfipa\Documents\BF-Vault-Web\sync-from-vault.ps1` |
| Website | https://bf-knowledge-base.vercel.app/ |

---

## ไฟล์ที่ถูก Sync

### รูปแบบ

Script จะ sync เฉพาะไฟล์ที่มี **frontmatter** (YAML metadata):

```
---
tags: [...]
project: ...
type: ...
---

# Content here
```

### โฟลเดอร์ที่ถูก Sync

| จาก BF-Vault | ไปยัง BF-Vault-Web |
|---------------|---------------------|
| `Knowledge/` | `content/Knowledge/` |
| `Concepts/` | `content/Concepts/` |
| `Projects/Alpha Trinity Scanner/` | `content/Projects/Alpha Trinity Scanner/` |
| `MOCs/` | `content/MOCs/` |
| `Processes/` | `content/Processes/` |

### ไฟล์ที่ไม่ถูก Sync

- ไฟล์ที่ไม่มี frontmatter
- ไฟล์ใน `.obsidian/`
- ไฟล์ใน `Templates/`
- ไฟล์ที่ซ่อน (ขึ้นต้นด้วย `.`)

---

## ปัญหาที่พบบ่อย

### 1. YAML Frontmatter Error

```
ERROR: bad indentation of a mapping entry
```

**สาเหตุ**: Value มี special characters แต่ไม่ได้ quote

**วิธีแก้**:
```yaml
# ❌ ผิด
set_esg: - (NOT RATED)
title: Investment: Strategies for 2024

# ✅ ถูก
set_esg: '"- (NOT RATED)"'
title: 'Investment: Strategies for 2024'
```

### 2. ไฟล์ไม่ปรากฏบนเว็บ

**ตรวจสอบ**:
1. ไฟล์มี frontmatter หรือยัง?
2. รอ 1-2 นาทีสำหรับ Vercel rebuild
3. เช็ค Vercel dashboard: https://vercel.com/dashboard

### 3. Vercel Deploy ล้มเหลว

**ตรวจสอบ**:
1. ไปที่ Vercel Dashboard
2. เลือก project → Deployments
3. ดู log ว่า error อะไร

---

## Alpha Trinity Scanner Files

### ไฟล์ที่เพิ่งสร้าง (พร้อม sync)

```
Projects/Alpha Trinity Scanner/
├── MOC.md
├── 00 - Project Summary.md
├── 01 - Technical Documentation.md
├── 02 - Risk Framework & Stress Testing.md
├── 03 - LITERATURE REVIEW.md
├── 04 - METHODOLOGY DEEP DIVE.md
├── 05 - API REFERENCE.md
├── สรุปโปรเจกต์.md                    ← ไฟล์นี้ (ภาษาไทย)
└── Sector Analysis/
    ├── Energy Sector Analysis.md
    ├── Technology Sector Analysis.md
    └── Healthcare Sector Analysis.md
```

### หลังจาก Sync

เข้าถึงได้ที่:
```
https://bf-knowledge-base.vercel.app/Projects/Alpha%20Trinity%20Scanner
```

---

## Troubleshooting

### Sync script ทำงานไม่ได้

```powershell
# เช็คว่าอยู่ที่ path ที่ถูกต้อง
Get-Location

# ต้องอยู่ที่
# C:\Users\bfipa\Documents\BF-Vault-Web
```

### Git push ล้มเหลว

```powershell
# เช็ค git status
git status

# Commit ก่อนแล้วค่อย push
git add .
git commit -m "Update from vault"
git push
```

### แก้ไข frontmatter แต่ sync ไม่อัปเดต

```powershell
# ลบ cache แล้ว sync ใหม่
.\sync-from-vault.ps1 -Push -Force
```

---

## Quick Reference

| การกระทำ | คำสั่ง |
|-----------|---------|
| Sync + Push | `.\sync-from-vault.ps1 -Push` |
| Sync อย่างเดียว | `.\sync-from-vault.ps1` |
| Force Sync | `.\sync-from-vault.ps1 -Push -Force` |
| Test Sync | `.\sync-from-vault.ps1 -WhatIf` |

---

**Last Updated**: 2026-04-05
**Website**: https://bf-knowledge-base.vercel.app/
