# Decision ledger

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## DEC-DOCTRINE-001 — Architecture doctrine
- **state:** `ADOPTED_MAINLINE`
- **mainline:** MAINLINE_CUSTOM owns board around silicon; COTS/modular = REFERENCE_CONTROL; experiments need measured evidence to promote
- **rationale:** Owner-directed HW1C custom-first pivot

## DEC-COMPUTE-001 — Student 14.5 / DS-XL compute (custom mainline)
- **state:** `ADOPTED_MAINLINE`
- **mainline:** gunnchOS Platform Core v1 — AMD Ryzen Embedded 8000 FP7r2 BGA custom motherboard (Student 8840U OPN ref 100-000001317E; DS-XL 8845HS OPN ref 100-000001316E). Pin compatibility NOT assumed.
- **rationale:** HW1C custom-first doctrine: own the board around the silicon. COM-HPC Mini reclassified REFERENCE_CONTROL_MODULAR_X86.

## DEC-COMPUTE-002 — Handheld Hybrid compute
- **state:** `ADOPTED_MAINLINE`
- **mainline:** Custom Handheld-MB-v1 with Ryzen Embedded 8840U (same family target as Student). COM-HPC Handheld mule = REFERENCE_CONTROL only.
- **rationale:** Custom-first ownership; lower sustained power within supported envelope; compact topology pending vendor docs.

## DEC-COMPUTE-003 — Handheld production board geometry
- **state:** `PENDING_PHYSICAL_MEASUREMENT`
- **mainline:** Handheld-MB-v1 geometry PENDING_PHYSICAL_MEASUREMENT after CPB0/EVT data
- **rationale:** Cannot freeze production board without measured thermal/power/fit

## DEC-CPB0-001 — Custom Platform Board 0
- **state:** `ADOPTED_MAINLINE`
- **mainline:** CPB0 debug-friendly learning board on 8845HS preferred; READY_FOR_FAB=false without collateral+EDA
- **rationale:** Primary learning path for custom motherboard ownership

## DEC-COMHPC-001 — COM-HPC role
- **state:** `EXPERIMENTAL_COMPARE`
- **mainline:** ADLINK COM-HPC Mini mMTL + Mini Base classified REFERENCE_CONTROL_MODULAR_X86 (not product mainline)
- **rationale:** Preserve RP0-A COTS packet for software/bring-up isolation; optional owner order

## DEC-MEMORY-001 — DDR topology
- **state:** `PENDING_VENDOR_CONFIRMATION`
- **mainline:** UNFROZEN — prefer debug-friendly on CPB0, serviceability on Student, capacity on DS-XL, compactness on Handheld if vendor allows
- **rationale:** Must not freeze without AMD topology rules

## DEC-FW-001 — Host firmware stack
- **state:** `ADOPTED_MAINLINE`
- **mainline:** Vendor UEFI on COM-HPC module + Zephyr EC on companion MCU
- **rationale:** Ship path with vendor support; open alternatives experimental

## DEC-DISPLAY-001 — Student / DS-XL display technology
- **state:** `ADOPTED_MAINLINE`
- **mainline:** IPS LCD panels on custom Platform Core boards (Student: single eDP; DS-XL: one native eDP + DDI/DP). Not dual native eDP unless authoritative SoC docs prove it.
- **rationale:** Preserve HW1B architecture correction; apply to custom AMD boards. OLED remains experiment.

## DEC-STORAGE-001 — Storage / Wi-Fi
- **state:** `ADOPTED_MAINLINE`
- **mainline:** M.2 NVMe + M.2 Key E Wi-Fi on custom Platform Core boards (field replaceable where packaging permits)
- **rationale:** Custom motherboard ownership of PCIe/NVMe/Wi-Fi integration

## DEC-CELLULAR-001 — Optional cellular
- **state:** `ADOPTED_MAINLINE`
- **mainline:** Optional Telit FN990B40 M.2 5G Sub-6 module exact MPN FN990B40W01T010300; Quectel RM520N-GL approved alternate
- **rationale:** HW1B closed AVL identity with exact MPN + live distributor/manufacturer evidence. PRODUCT_CELLULAR_ANTENNA_DESIGN_PENDING=true (dev antennas ≠ production).

## DEC-DOCK-001 — Dock Gen-1 link rate
- **state:** `ADOPTED_MAINLINE`
- **mainline:** USB4 40 Gbps (Intel JHL8440 + JHL9040R retimer) + USB-C PD EPR-class controller
- **rationale:** Reconciles DOCK_ARCHITECTURE_FREEZE_USB4_TB4; no USB4 80 in main BOM

## DEC-RINGS-001 — Rings MCU
- **state:** `ADOPTED_MAINLINE`
- **mainline:** Nordic nRF54L15 (BLE + LE Audio). RING_EVT_ELECTRICAL_PLATFORM=QFN48/DK reference (PCA10156); RING_FORM_FACTOR_CANDIDATE=CSP47
- **rationale:** HW1B closed RP0-A footprint uncertainty via Nordic public DK/QFN48 files. CSP47 wearable geometry remains a separate HDI/assembly gate; DK ≠ wearable validation.

## DEC-RINGS-002 — Rings sensing + charge EVT
- **state:** `ADOPTED_MAINLINE`
- **mainline:** IMU + capacitive/touch + magnetic cradle charge contacts for EVT
- **rationale:** Measurable EVT path; inductive and sEMG isolated as experiments

## DEC-BATT-001 — Battery chemistry
- **state:** `ADOPTED_MAINLINE`
- **mainline:** Qualified Li-ion / LiPo only; no experimental chemistries in mainline
- **rationale:** UN38.3 / transport path; experimental chemistries deferred Gen2

## DEC-QA-001 — PCB assembly quality class
- **state:** `ADOPTED_MAINLINE`
- **mainline:** IPC Class 2 baseline with selective tighter controls on BGA/COM connector / RF keepouts (not blanket Class 3)
- **rationale:** Cost/yield vs reliability; Class 3 reserved for selective high-risk zones

## DEC-RP0-001 — Reference Platform 0 scope
- **state:** `ADOPTED_MAINLINE`
- **mainline:** Two-stage RP0: RP0-A COTS Integration Bench (ADLINK Mini Base + mMTL + nRF54L15 DK + COTS USB4 dock) then RP0-B custom gunnchOS carrier/dock/ring EVT electronics
- **rationale:** Do not order custom PCB that is not fabrication-ready. COTS unlocks physical bring-up while vendor-gated pin maps remain RP0-B blockers.
