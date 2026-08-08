# Open-documentation alternative audit — Student / DS-XL compute

Updated: 2026-08-08T20:58:59Z  
Branch: `cursor/full-product-continuation-vi-eda-closure`  
Rule: alternatives must be orderable MPNs with **public** pinout sufficient for carrier nets.

| Candidate | Public pinout? | Matches ADR Ultra 7 155H? | Form factor | Verdict |
|---|---|---|---|---|
| ADLINK **COM-HPC-mMTL-155H-32G** (current) | Feature groups PUBLIC; **full 400-pin NARROW_NDA** | YES | COM-HPC Mini 95×70 | **KEEP** under Option 3 |
| ADLINK COM-HPC-mMTL-155H-64G | Same NDA class | YES (mem SKU) | Same | Approved alternate only |
| Congatec conga-HPC/mPTL-* | Vendor portal / NDA typical | **NO** (Panther Lake ≠ 155H) | COM-HPC Mini | Rejected as primary (wrong gen) |
| congatec / SECO / AAEON Meteor Lake COM-HPC | Carrier guides usually NDA | Possible SKU match | COM-HPC Mini | Same NDA class — no public win |
| LattePanda Mu / other N100 NUC boards | Partial public | **NO** (wrong CPU class) | Not COM-HPC | Rejected — breaks family ADR |
| Up Board / AAEON UP Xtreme | Partial | **NO** | Not COM-HPC | Rejected |
| Radxa NX5 RM121-D8E32 | **YES PUBLIC_PINOUT** | **NO** (RK3588S) | SODIMM-260 | Used for **Handheld only** — not Student/DS-XL substitute |
| Firefly Core-3588SJD4 | Partial public | **NO** | SODIMM | Handheld AVL fail path only |

## Conclusion
No audited alternate unlocks Student/DS-XL pin-accurate public engineerability without either:
1. accepting NARROW_NDA COM-HPC pinout intake, or
2. amending product ADRs to a different CPU/module class.

Therefore Option 3 stands. Handheld proceeds independently on Radxa public pinout.

## Token
`OPEN_DOCUMENTATION_ALTERNATIVE_AUDIT_COMPLETE`
