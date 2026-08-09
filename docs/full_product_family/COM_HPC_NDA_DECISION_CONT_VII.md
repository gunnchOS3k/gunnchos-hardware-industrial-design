# Student + DS-XL COM-HPC NDA decision — Continuation VII §14

Updated: 2026-08-09T17:16:18Z  
Branch: `cursor/full-product-continuation-vii-eda-release-clean`

## Decision
**`KEEP_ADLINK_AND_ACCEPT_NARROW_EXTERNAL_BLOCK`**

Reaffirms Cont VI Option 3. Cont VII re-checked public-engineerability alternatives;
no migration performed.

## Why not migrate
- Product ADRs freeze **COM-HPC-mMTL-155H-32G** (Ultra 7 155H, COM-HPC Mini).
- Public alternatives either lack pinout, lack 155H, or are wrong form-factor.
- Inventing pin numbers is forbidden.

## Tokens
- `PUBLIC_ENGINEERABILITY_GATE_OPTION3_ADLINK_NDA_EXTERNAL`
- `STUDENT_BLOCKED_NDA`
- `DSXL_BLOCKED_NDA`

## Explicit
Handheld / Ring / Dock are **not** blocked by this NDA gate.
Pin-accurate Student/DS-XL carrier nets remain **EXTERNAL_NDA_BLOCKED** until
narrow NDA intake — architecture/BOM/CAD remain in-repo as public/modeled.
