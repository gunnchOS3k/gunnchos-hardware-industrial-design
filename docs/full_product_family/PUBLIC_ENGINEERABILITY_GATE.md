# Public-engineerability gate — Student 14.5 / DS-XL Coder

Updated: 2026-08-08T20:58:59Z  
Branch: `cursor/full-product-continuation-vi-eda-closure`  
Base: `origin/main` @ `38b37221074446730709af5682a06cb4cefd39fc` (#48)

PHYSICAL_EXECUTION_FREEZE ACTIVE — decision is digital/process only.

## Question
Can Student / DS-XL carriers be fully public-engineered (pin-accurate schematic nets) without
PICMG / ADLINK / Intel NDA material?

## Options evaluated

### Option 1 — Public docs only
Use only ADLINK iPi ModuleIntroduction + PICMG public overviews.
- Feasible for: module MPN freeze, mechanical 95×70, Vin 8–20V / AT 12V±5%, I/O **feature groups**.
- **Not feasible** for: COM-HPC Mini **400-pin net-by-net** map, mating connector exact MPN,
  USB4 controller package fanout, differential pair pin assignment.
- Verdict: keeps architecture FROZEN_DIGITAL; **blocks** pin-accurate carrier COMPLETE.

### Option 2 — Alternate public module
Swap ADLINK COM-HPC-mMTL for a fully public-documented compute module.
Candidates audited in `OPEN_DOCUMENTATION_ALTERNATIVE_AUDIT.md`.
- Would require ADR-HW-001 / ADR-FP-001 amendment (Ultra 7 155H Meteor Lake COM-HPC Mini is normative).
- No audited alternate currently matches **public pinout + Ultra 7 155H + COM-HPC Mini** simultaneously.
- Verdict: **deferred** — do not silent-swap under freeze.

### Option 3 — Keep ADLINK; NDA nets external only (**SELECTED**)
Keep **COM-HPC-mMTL-155H-32G** as frozen compute MPN.
- In-repo carrier artifacts: hierarchical architecture, power tree, I/O groups, BOM, CAD envelope —
  all tagged `PUBLIC_DOCS` / `MODELED`.
- Full pin-by-pin COM-HPC Mini nets: **out of tree**, held under NARROW_NDA intake when available.
- **No invented pin numbers** in KiCad / netlists / ICDs.
- Student / DS-XL status tokens: `STUDENT_BLOCKED_NDA`, `DSXL_BLOCKED_NDA`.

## Decision
**Option 3 selected.**

## Explicit non-claims
- No fake COM-HPC pinout.
- No `FULL_HARDWARE_DESIGN_RELEASE_COMPLETE` for Student or DS-XL while NDA pinout absent.
- Handheld / Dock / Rings are **not** blocked by this COM-HPC NDA gate.

## Token
`PUBLIC_ENGINEERABILITY_GATE_OPTION3_ADLINK_NDA_EXTERNAL`
