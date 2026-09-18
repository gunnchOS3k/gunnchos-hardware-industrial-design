# NXP-0 Final Report A–V

**Generated:** 2026-09-18T18:55:43Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.

## A. Accepted-main baseline

- `origin/main` tip at preflight: `4a8aefb5fd6203842267f5adbd72b8ed324e1fac`
- HW1D architecture merge PR **#68** SHA: `e5f15d1f1b6ddefa73c0a6127bced8d784aae425`
- HW1D.1 evidence PR **#80** MERGED at 2026-09-18T18:25:04Z; merge SHA `4a8aefb5fd6203842267f5adbd72b8ed324e1fac`; evidence commit `46707749398b8a32fa24d277672fafbcbe391dbf`
- Experiments **#69–#79**: OPEN + draft + unmerged (verified via `gh pr list`)
- Software RC1 identity `v1.0.0-rc.1` untouched (`SOFTWARE_RC1_INTERFACE_IMPACT_REGISTER.json`)
- Existing `hardware_v1/open_custom_nxp/` architecture package present and extended
- Starting state: `NXP0_STARTING_STATE.json`

## B. NXP collateral inventory

- `PUBLIC_COLLATERAL_INDEX.md` / `.json` rebuilt for NXP-0 with datasheets (IMX95IEC/CEC/XEC/AEC), IMX95RM, UG10210 (account), EVK GS + QSG, MCUX board docs, errata, BSDL/IBIS, EdgeLock index, BSP portal
- `NXP_PUBLIC_COLLATERAL_INDEX_COMPLETE=true` (category coverage complete; gated files not all downloaded)
- Gaps: `PUBLIC_COLLATERAL_GAP_REGISTER.md`
- No NDA-required items identified; no restricted binaries committed

## C. Exact SoC/package

- **Selected: MIMX9596AVZXN** (19×19 mm VZ FCBGA, 0.7 mm) — see `CPB0_OPEN_SOC_SELECTION.md`
- Evidence: MCUXpresso IMX95LPD5EVK-19 docs list this PartNumber; package class from IMX95IEC

## D. Public pinmap status

- Interface ownership defined in `CPB0_OPEN_INTERFACE_MAP.md`
- Machine-readable `CPB0_OPEN_PINMUX_MAP.csv` exists with **all rows unresolved** at ball level
- **`NXP_PUBLIC_PINMAP_UNDERSTOOD=false`**

## E. Power architecture

- `CPB0_OPEN_POWER_TREE.md`, `CPB0_OPEN_POWER_BUDGET.csv`, `CPB0_OPEN_SEQUENCE.md`
- Rail names + BBSM-first sequencing from public IMX95IEC
- Currents not fabricated; PMIC OPN pending
- **`NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD=true`**

## F. Memory topology

- High-level LPDDR5 x32 decision aligned to LPD5 EVK-19 / IMX95IEC
- Detailed skew/impedance blocked on UG10210 / EVK layout
- **`NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false`**

## G. PCIe/USB/network

- Documented in `CPB0_OPEN_PCIE_USB_NETWORK_ARCHITECTURE.md`
- PCIe0→NVMe, PCIe1→Wi-Fi, USB-C (no USB4), 2×GbE + optional 10GbE, optional 5G DNP

## H. Display/camera/audio

- `CPB0_OPEN_MEDIA_ARCHITECTURE.md` — MIPI DSI + CSI + SAI/codec paths with debug connectors

## I. Security/boot

- `CPB0_OPEN_SECURITY_BOOT_ARCHITECTURE.md` — ROM / U-Boot control / EdgeLock / recovery
- No secure-boot pass claim

## J. EC

- Separate Zephyr EC preferred — `CPB0_OPEN_EC_ARCHITECTURE.md`

## K. Schematic plan

- 18-sheet hierarchy in `CPB0_OPEN_SCHEMATIC_SHEET_PLAN.md`

## L. Actual EDA status

- Real KiCad 10 project under `eda/cpb0_open/` (cover + hierarchical placeholders + PCB stub)
- **`CPB0_OPEN_SCHEMATIC_STARTED=true`**
- **`CPB0_OPEN_SCHEMATIC_ERC_PASS=false`**
- No authoritative i.MX95 symbol/footprint yet

## M. PCB/stackup

- Architecture + draft 12-layer stackup docs
- PCB file is non-routed stub only
- **`CPB0_OPEN_PCB_STARTED=false`**, **`CPB0_OPEN_PCB_DRC_PASS=false`**

## N. SI/PI plan

- `CPB0_OPEN_SI_PI_PLAN.md` — plan only; no pass claims; IBIS account-gated

## O. BOM/AVL

- `CPB0_OPEN_BOM.csv`, `CPB0_OPEN_AVL.csv`, `CPB0_OPEN_BOM_RISK.md`
- Critical SoC MPN set; PMIC/DRAM still PENDING; stock/price = VERIFY_AT_PURCHASE

## P. No-NDA blocker register

- `NXP_PUBLIC_BLOCKER_REGISTER.md` — account-login / tooling / EDA / physical classes; no NDA stop

## Q. Transfer map

- `NXP_TO_AMD_TRANSFER_MAP.md` — EC highly transferable; silicon paths require revalidation

## R. Experience workload plan

- `CPB0_OPEN_EXPERIENCE_WORKLOAD_PLAN.md` — hooks only; no physical measurements

## S. Validators

- `make nxp-open-audit`
- `make nxp-open-validate`
- `make nxp-open-gates`
- Scripts: `scripts/audit_nxp_open.py`, `scripts/validate_nxp_open.py`

## T. Gate tokens

See printed block below / `NXP0_GATES.json`.

## U. Exact remaining digital blockers

1. Extract ball-accurate pinmux from IMX95IEC package assignments + IMX95RM
2. Owner ordinary-account fetch of UG10210 (+ hash); close DDR constraint rows
3. EVK BOM → freeze PMIC + LPDDR5 MPNs
4. Authoring KiCad SoC symbol/footprint from public package data (license-safe)
5. Fill schematic sheets; run ERC to zero errors
6. Start real PCB layout; stackup with fab notes; DRC
7. Local SHA-256 archive of public PDFs (no illegal redistribution)
8. Ingest errata IMX95_P21N (account)

## V. Next owner / Cursor action

- **Cursor / hardware:** `NEXT_HARDWARE_ACTION=CONTINUE_CPB0_OPEN_EDA`
- **Owner:** `NEXT_OWNER_ACTION=LOGIN_FETCH_UG10210_AND_HASH_PUBLIC_PDFS`
- Do **not** purchase, RFQ, or fab.
- Do **not** merge #69–#79.
- Do **not** modify software RC1 baselines.
- Fab-ready owner action remains future-only: `QUOTE_CPB0_OPEN_FAB` (not unlocked).

---

## Printed token block

```
NXP_OPEN_CUSTOM_TRACK_IMPLEMENTATION_STARTED=true
NXP_PUBLIC_COLLATERAL_INDEX_COMPLETE=true
NXP_PUBLIC_PINMAP_UNDERSTOOD=false
NXP_PUBLIC_POWER_ARCHITECTURE_UNDERSTOOD=true
NXP_PUBLIC_MEMORY_TOPOLOGY_UNDERSTOOD=false
CPB0_OPEN_SCHEMATIC_STARTED=true
CPB0_OPEN_SCHEMATIC_ERC_PASS=false
CPB0_OPEN_PCB_STARTED=false
CPB0_OPEN_PCB_DRC_PASS=false
CPB0_OPEN_READY_FOR_FAB=false
EVT_PENDING=true
DVT_PENDING=true
PVT_PENDING=true
PHYSICAL_HARDWARE_VALIDATED=false
NEXT_HARDWARE_ACTION=CONTINUE_CPB0_OPEN_EDA
```
