---
title: Master Plan v2 - Dual-AI 3-Round Execution Model
note_type: master-plan
status: active
created: 2026-04-02
updated: 2026-04-02
tags:
  - note/plan
  - investing
  - strategy
  - thai-market
  - dual-ai
  - collaborative
---

# Master Plan v2: Dual-AI 3-Round Execution Model

> **Proven Model:** Validated with Deep Value (965 lines, 91/100 final score)
> **Workflow:** R1 Codex Draft (400+ lines) → R1 Gemini Score → R2 Codex Fix (600+ lines) → R2 Gemini Verify → R3 Claude Final QC

---

## Validated Results: Deep Value

| Metric | Result |
|--------|--------|
| Final Lines | 965 lines |
| Final Score | 91/100 |
| R1 Score | 78/100 |
| R2 Score | 85/100 |
| Total Time | ~4 hours |

---

## Proven Execution Workflow (3 Rounds)

### Core Principle

```
OLD: Codex ทำบางอัน, Gemini ทำบางอัน (แยกกัน)
NEW: ทุกเอกสารผ่าน Codex + Gemini ร่วมกัน (3-Round)
```

### Final Workflow (Proven)

```
ROUND 1: DRAFT
Time: 60-90 min (Codex) + 30 min (Gemini)

Step 1: Codex (Drafter)
- Research strategy principles
- Create initial draft (400+ lines)
- Include: Definition, Metrics, Basic Checklist
- Output: [Strategy]_draft_v1.md
    |
    v
Step 2: Gemini (Scorer - Damodaran Persona)
- Read draft_v1.md
- SCORE out of 100:
  - Research Quality (30 pts)
  - Valuation Rigor (30 pts)
  - Communication (20 pts)
  - Risk Assessment (20 pts)
- Output: Score + Issues List

QUALITY GATE: Score >= 70 -> Proceed to R2
               Score < 70 -> Rework R1

================================================================================

ROUND 2: EXPAND & VERIFY
Time: 60 min (Codex) + 20 min (Gemini)

Step 3: Codex (Expander)
- Read Gemini's feedback
- Fix ALL issues identified
- Expand to 600+ lines
- Add Thai examples (5+ stocks)
- Add cross-links
- Output: [Strategy]_draft_v2.md
    |
    v
Step 4: Gemini (Verifier)
- Read draft_v2.md
- RE-SCORE out of 100
- Thai Market Check:
  - Governance risks covered?
  - RPT checks?
  - Thai stock examples (5+)?
  - Liquidity warnings?
- Output: Final Score + Remaining Issues

QUALITY GATE: Score >= 85 -> Proceed to R3
               Score < 85 -> Additional R2 round needed

================================================================================

ROUND 3: FINAL QC
Time: 15 min (Claude)

Step 5: Claude (Final QC)
- Verify 600+ lines
- Verify checklist complete (4 phases)
- Verify Thai examples present (5+ stocks)
- Verify cross-links (3+ concepts)
- Final formatting check
- Commit to BF-Vault + Record to Synapse-O
```

---

## Per-Document Timeline

| Phase | Task | Time | Owner |
|-------|------|------|-------|
| R1 | Codex Draft (400+ lines) | 60-90 min | Codex |
| R1 | Gemini Score | 30 min | Gemini |
| R2 | Codex Fix (600+ lines) | 60 min | Codex |
| R2 | Gemini Verify | 20 min | Gemini |
| R3 | Claude Final QC | 15 min | Claude |
| **Total** | **Per Document** | **~3-4 hours** | |

---

## Quality Gates Summary

| Gate | Threshold | Action if Fail |
|------|-----------|----------------|
| R1 Score | >= 70 | Rework R1 draft |
| R2 Score | >= 85 | Additional R2 round |
| Final Lines | >= 600 | Expand content |
| Thai Examples | >= 5 stocks | Add more examples |
| Cross-links | >= 3 concepts | Add related links |

---

## Quality Rubric (100 points)

| Category | Points | Criteria |
|----------|--------|----------|
| **Research Quality** | 30 | Primary sources (56-1, SET), Thai context, footnotes read |
| **Valuation Rigor** | 30 | Explicit assumptions, sensitivity analysis, cross-check |
| **Communication** | 20 | Beginner-friendly, structured, visual aids |
| **Risk Assessment** | 20 | Downside scenarios, governance, market risks |

---

## Document Status (19 Files)

### Phase 1: Upgrade Existing (8 Files Remaining)

| Priority | Document | Status | Score | Lines | Notes |
|----------|----------|--------|-------|-------|-------|
| - | Deep Value | COMPLETE | 91/100 | 965 | Template for others |
| 1 | Dividend Play | Pending | - | - | Short, needs expansion |
| 2 | Quality GARP | Pending | - | - | Popular strategy |
| 3 | Quality Swing Investor | Pending | - | - | Trading focus |
| 4 | Value Swing | Pending | - | - | Trading focus |
| 5 | Alpha Trinity Scanner | Pending | - | - | Tool document |
| 6 | Property Sector | Pending | - | - | Sector complete |
| 7 | Low-Rise Property | Pending | - | - | Sector |
| 8 | Mid-Market Property | Pending | - | - | Sector |

### Phase 2: Create New (10 Files)

| Priority | Strategy | Thai Fit | Status | Notes |
|----------|----------|----------|--------|-------|
| 1 | Quality Compounder | 5/5 | Pending | High priority - buy and hold |
| 2 | Banking Sector | 5/5 | Pending | High priority - 30% of SET |
| 3 | Growth at Fair Price | 4/5 | Pending | GARP variant |
| 4 | Small Cap Explorer | 4/5 | Pending | Alpha potential |
| 5 | Sector Rotation | 4/5 | Pending | Cyclical approach |
| 6 | Momentum + Quality | 3/5 | Pending | Trading strategy |
| 7 | Tourism Recovery | 4/5 | Pending | Thailand-specific |
| 8 | Special Situations | 3/5 | Pending | Event-driven |
| 9 | Turnaround | 2/5 | Pending | Distressed |
| 10 | Contrarian | 2/5 | Pending | Against the crowd |

---

## Timeline: 6 Weeks

**Total Effort:** 63 hours across 18 documents

### Week 1-2: High Priority New Documents

```
Week 1:
- Quality Compounder (Days 1-4)
  - R1: Codex Draft + Gemini Score
  - R2: Codex Expand + Gemini Verify
  - R3: Claude Final QC
- Banking Sector (Days 5-7)
  - Start R1

Week 2:
- Banking Sector (Days 1-3)
  - Complete R2 + R3
- Growth at Fair Price (Days 4-7)
  - Full 3-Round cycle
```

### Week 3-4: Continue New Documents

```
Week 3:
- Small Cap Explorer (Days 1-3)
- Sector Rotation (Days 4-7)

Week 4:
- Momentum + Quality (Days 1-3)
- Tourism Recovery (Days 4-7)
```

### Week 5: Upgrade Existing Documents

```
Week 5:
- Dividend Play (Days 1-2) - Short document
- Quality GARP (Days 3-4)
- Quality Swing Investor (Days 5-7)
```

### Week 6: Complete Remaining

```
Week 6:
- Value Swing + Alpha Trinity (Days 1-3)
- Property Sector + Low-Rise + Mid-Market (Days 4-5)
- Special Situations + Turnaround (Days 6)
- Contrarian + Final Integration (Day 7)
```

---

## Resource Allocation

### Total Effort Summary

| AI | Per Doc | 18 Docs | Role |
|----|---------|---------|------|
| Codex | 2 hours | 36 hours | Drafter + Expander |
| Gemini | 1 hour | 18 hours | Scorer + Verifier |
| Claude | 0.5 hour | 9 hours | Final QC + Commit |
| **Total** | **3.5 hours** | **63 hours** | |

### Weekly Commitment

| Week | Docs | Codex | Gemini | Claude | Total |
|------|------|-------|--------|--------|-------|
| 1-2 | 3 | 6h | 3h | 1.5h | 10.5h |
| 3-4 | 4 | 8h | 4h | 2h | 14h |
| 5 | 3 | 6h | 3h | 1.5h | 10.5h |
| 6 | 8 | 16h | 8h | 4h | 28h |
| **Total** | **18** | **36h** | **18h** | **9h** | **63h** |

---

## Thai Market Red Flags (Mandatory Checks)

### Gate 0: Knockout Criteria

| Criterion | Must Have | Why |
|-----------|-----------|-----|
| SET ESG Rating | 2025 rating | Corporate governance baseline |
| Free Float | >= 20% | Liquidity risk |
| Trading Signs | No caution/suspension | Regulatory issues |
| Audit Opinion | Unqualified only | Financial integrity |

**Gate 0 FAIL = Skip stock, no further analysis needed**

### RPT Risk Levels (Required in Every Document)

| Level | RPT % of Revenue | Action |
|-------|------------------|--------|
| Green | < 10% | Proceed with normal DD |
| Yellow | 10-20% | Investigate deeply |
| Red | > 20% | Avoid |

### Thai-Specific Risks to Cover

| Risk | What to Check | Red Flag |
|------|---------------|----------|
| Governance | Board independence | CEO = Chairman |
| RPT | Related party % | > 10% of revenue |
| Liquidity | Daily volume | < 10M THB |
| Concentration | Major holders | > 70% |

---

## Execution Commands

### Round 1: Codex Draft

```bash
codex exec "
Project: C:\Users\bfipa\Documents\BF-Vault
Task: Create [Strategy Name] strategy document - Draft v1

Requirements:
1. 400+ lines minimum
2. Follow template in MASTER-PLAN-v2-Collaborative.md
3. Include: Definition, Philosophy, 4+ Metrics, Phase 1-2 Checklist
4. Use Thai stock examples where possible
5. Include Gate 0 knockout criteria

Output: Concepts/[Strategy Name]_draft_v1.md
" --skip-git-repo-check
```

### Round 1: Gemini Score

```bash
gemini -p "
Project: C:\Users\bfipa\Documents\BF-Vault
Role: Professor Damodaran (Reviewer)

Task: Score Concepts/[Strategy Name]_draft_v1.md

Score out of 100:
- Research Quality (30 pts): Primary sources, Thai context
- Valuation Rigor (30 pts): Explicit assumptions, sensitivity
- Communication (20 pts): Beginner-friendly, structured
- Risk Assessment (20 pts): Downside, governance, market risks

Also identify:
1. Clarity issues
2. Missing sections
3. Example gaps
4. Jargon problems

Output: Score + Issues List
"
```

### Round 2: Codex Expand

```bash
codex exec "
Project: C:\Users\bfipa\Documents\BF-Vault
Task: Expand [Strategy Name] based on Gemini review

Input:
- Draft: Concepts/[Strategy Name]_draft_v1.md
- Gemini Score + Issues

Actions:
1. Address ALL issues identified
2. Expand to 600+ lines
3. Add 5+ Thai stock examples
4. Add 3+ cross-links to related concepts
5. Complete all 4 checklist phases
6. Include Thai-specific risks (RPT, governance, liquidity)

Output: Concepts/[Strategy Name]_draft_v2.md
" --skip-git-repo-check
```

### Round 2: Gemini Verify

```bash
gemini -p "
Project: C:\Users\bfipa\Documents\BF-Vault
Role: Professor Damodaran (Verifier)

Task: Re-score Concepts/[Strategy Name]_draft_v2.md

Score out of 100:
- Research Quality (30 pts)
- Valuation Rigor (30 pts)
- Communication (20 pts)
- Risk Assessment (20 pts)

Thai Market Check:
- Governance risks covered?
- RPT checks included?
- 5+ Thai stock examples?
- Liquidity warnings present?

Output: Final Score + Pass/Fail Recommendation
"
```

---

## Per-Document Checklist

| Gate | Criteria | Required |
|------|----------|----------|
| **Length** | 600+ lines | Required |
| **Checklist** | 4 phases complete | Required |
| **Examples** | 5+ Thai stocks | Required |
| **Risks** | 3+ risk types | Required |
| **Case Studies** | 1 success + 1 failure | Required |
| **Thai Checks** | Governance + RPT + Liquidity | Required |
| **Cross-links** | 3+ related concepts | Required |
| **Format** | Follow template | Required |

---

## Ready to Execute

**Status:** Plan Active
**Next Step:** Execute Priority 1 - Dividend Play (upgrade existing)

**Command to Start:**
```
codex exec "Project: C:\Users\bfipa\Documents\BF-Vault
Task: Create Dividend Play strategy document - Draft v1
Requirements: 400+ lines, follow MASTER-PLAN template, Thai examples
Output: Concepts/Dividend Play_draft_v1.md" --skip-git-repo-check
```

---

*Created: 2026-04-02 | Updated: 2026-04-02*
*Version: 2.1 - Final Execution Model (Proven with Deep Value)*
