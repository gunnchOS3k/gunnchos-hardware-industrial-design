# ADR-HW-002 — Dock freezes as USB4/TB4 @ 40G; correct JHL9040 role; reject TB5

- Status: **ACCEPTED**
- Date: 2026-08-08T20:15:00Z
- Relates: field-kit ADR-FP-006, ADR-FP-001; amends hardware EXACT_MPN_MATRIX dock row from PR #47

## Context
PR #47 froze dock USB4 silicon as Intel **JHL9040** “Maple Ridge class controller.” Independent Continuation V verification against Intel public product pages shows:
- **JHL9040R** = Thunderbolt **4 Retimer** (Hayden Bridge), 40 Gbps — not Maple Ridge, not a dock controller.
- Maple Ridge host controller = **JHL8540**; typical dock/peripheral controller = **JHL8440** (Goshen Ridge).
- Thunderbolt **5** controllers = **JHL9480** / **JHL9580** (Barlow Ridge).

Normative product ADRs already require USB4 **40 Gbps** docking and forbid silent 80G claims.

## Decision
1. Freeze dock architecture as **USB4 / Thunderbolt 4 @ 40 Gbps**.
2. Primary Student/DS-XL dock controller MPN: **JHL8440**.
3. Retimer MPN when SI requires: **JHL9040R** (do not call it the controller).
4. **Reject** JHL9480/JHL9580 for this product generation (TB5 out of scope).
5. Retain VL108 cost-down SKU for Handheld-first (USB3+DP Alt only).

## Consequences
- BOM / KiCad Values / netlists / ICDs updated in Continuation V.
- Field-kit ADR-FP-006 text still says “JHL9040 / Maple Ridge class” — recommend companion amend in field-kit (separate PR); hardware ADR-HW-002 is authoritative for this repo.
- No purchase / fab.

## Non-claims
No Thunderbolt certification, no TB5 compatibility claim, no invented Intel package pinouts (controller pinout remains NDA/Intel design kit).
