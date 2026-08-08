# ADR-HW-001 — COM / SoM + carrier strategy (exact MPNs; no fake proprietary CPU BGA)

- Status: **ACCEPTED (amended — exact orderable MPNs)**
- Date: 2026-08-08T19:40:00Z
- Relates: field-kit ADR-FP-001 / ADR-FP-002 / ADR-FP-003; supersedes vague COM-class strings from family-depth pass

## Context
Full-product electrical design must not invent proprietary Intel/AMD/Rockchip **CPU BGA fanout** without vendor PDK/NDA package files. Vague BOM lines such as `COM-HPC-Mini-Ultra7-155H-32GB` are not orderable MPNs.

## Decision
1. **Student 14.5 & DS-XL Coder — exact COM MPN:**
   - **Primary:** ADLINK **`COM-HPC-mMTL-155H-32G`** (COM-HPC Mini, Intel Core Ultra 7 **155H**, 32GB LPDDR5x).
   - **Approved alternate:** ADLINK **`COM-HPC-mMTL-155H-64G`** (64GB).
   - Public docs: ADLINK COM-HPC Mini / iPi wiki COM-HPC-mMTL ModuleIntroduction / COM-HPC-mMTL spec PDF.
   - gunnchOS designs the **carrier PCB only** (PD, EC, WWAN/Wi-Fi M.2, audio, sensors, display connectors, battery charger, I/O, dock USB-C).
2. **Handheld Hybrid — exact SoM MPN:**
   - **Primary:** Radxa NX5 **`RM121-D8E32`** (RK3588S, 8GB LPDDR4X, 32GB eMMC, 260-pin SODIMM).
   - **Approved alternates:** `RM121-D8E16`, `RM121-D8E8`, `RM121-D8E0` (official brief table).
   - Public docs: Radxa NX5 product brief Rev 1.1; Radxa Docs NX5. Lifecycle note: availability stated until ≥ Sep 2033.
   - gunnchOS designs the **game carrier** only.
3. Reject any schematic that places a bare `Core Ultra 7 155H` or bare `RK3588S` BGA with invented ball map.
4. Do **not** freeze Congatec Panther Lake `conga-HPC/mPTL-*` as primary (different CPU generation vs ADR-FP-001 155H target).

## Consequences
- BOMs / KiCad values / ICDs use the exact MPNs above.
- Procurement / lifecycle documented in `docs/full_product_family/PROCUREMENT_LIFECYCLE.md`.
- Purchase remains **PHYSICAL_EXECUTION_FREEZE**.

## Non-claims
No statement that ADLINK or Radxa is under contract. AVL quote required before any future purchase.
