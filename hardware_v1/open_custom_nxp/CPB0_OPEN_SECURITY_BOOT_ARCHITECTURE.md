# CPB0-O security / boot / recovery

**Generated:** 2026-09-18T18:53:20Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



## Boundaries

| Layer | Role |
|---|---|
| Immutable ROM | NXP ROM boot — not modified |
| Boot media | SPI NOR (FlexSPI) + eMMC (uSDHC); SD optional |
| Control bootloader | NXP U-Boot / BSP reference as bring-up control |
| Product target | gunnchOS boot path later — **not** software RC1 change in this campaign |
| Secure enclave | EdgeLock Secure Enclave (Advanced Profile) per public description |
| Keys / fuses | lifecycle TBD; **no secure-boot pass claim without hardware** |
| Rollback | A/B strategy TBD; RAUC experiment remains unmerged (#76) |
| Recovery | EC-forced boot strap + serial console + USB SDP/serial download per NXP tools |
| Board-ID | GPIO straps + EC EEPROM |
| Debug lifecycle | JTAG open on EVT; production policy = disable after fuse (future) |

## Honesty

`SECURE_BOOT_PASS` is **not** asserted. Physical validation pending.
