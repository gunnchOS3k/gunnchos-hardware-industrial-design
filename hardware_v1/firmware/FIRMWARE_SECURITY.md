# FIRMWARE SECURITY

**Generated:** 2026-09-18T16:02:19Z  
**Campaign:** `HARDWARE_1_0_MASTER_CAMPAIGN`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release.

## Mainline
- Vendor UEFI Secure Boot chain on COM-HPC module
- Zephyr EC with signed DFU for rings/EC
- TPM 2.0 on desk SKUs (Infineon SLB9672 class)

## Experimental
- coreboot (EXP-COREBOOT)
- RAUC A/B (EXP-RAUC)

## Secrets
No private keys, certs, or supplier credentials in-repo.
