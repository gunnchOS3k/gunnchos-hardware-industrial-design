# CPB0-O power / reset sequence

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Authoritative public sequence (IMX95IEC)

1. **NVCC_BBSM_1P8** reaches operating range first.
2. SoC asserts **PMIC_ON_REQ** after `tPMIC_ON_REQ` (datasheet timing table — use datasheet numbers; do not invent).
3. PMIC brings up digital/analog/DDR/I/O rails in datasheet step order (`tstep_*` family).
4. **POR_B** released only after rails valid (external PU to NVCC_BBSM; no internal PU).
5. Cold reset via **WDOG_ANY** → PMIC recycle per datasheet notes.
6. Power-down: reverse order; BBSM last.

## Board-level additions (architecture)

- EC holds/observes enables and reports PG to debug LEDs.
- M.2 / USB VBUS enables sequenced after SoC rails PG.
- Display/camera rails after MIPI PHY rails stable.

## Non-claims

- No measured rise times.
- No claim that a specific third-party PMIC is validated without EVK/UG citation.
