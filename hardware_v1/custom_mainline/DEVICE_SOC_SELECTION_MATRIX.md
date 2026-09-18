# Device SoC selection matrix

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


Selections are **mainline candidates**, subject to exact AMD embedded design-collateral confirmation.
Public OPNs below are from public product briefs — not proof of pin compatibility. Pin compatibility across SKUs is **not assumed**.

| Device | Main candidate | Public OPN (reference) | Package | Nominal / config TDP (public brief class) | Notes |
|---|---|---|---|---|---|
| Student 14.5 | Ryzen Embedded 8840U | `100-000001317E` | FP7r2 BGA | ~28 W; 15–30 W class | Balanced education/work/gaming; commonality with Handheld |
| Handheld Hybrid | Ryzen Embedded 8840U | `100-000001317E` | FP7r2 BGA | lower sustained within supported envelope | Compact custom MB; COM-HPC mule = REFERENCE_CONTROL only |
| DS-XL Coder | Ryzen Embedded 8845HS | `100-000001316E` | FP7r2 BGA | ~45 W; 35–54 W class | Higher sustained for creation/build/deploy |
| CPB0 learning board | Ryzen Embedded 8845HS preferred | `100-000001316E` | FP7r2 BGA | debug-friendly envelope | Fallback to 8840U only if vendor-access requires |

## Commonality intent

- Maximum reuse of Platform Core schematic blocks across Student / Handheld / DS-XL
- Do **not** force identical PCB dimensions
- Do **not** treat 8840U and 8845HS as drop-in pin-compatible without AMD confirmation

## Experimental higher-AI / higher-perf alternatives

| Experiment | Candidate class | vs mainline |
|---|---|---|
| EXP-DSXL-X100-001 | Ryzen AI Embedded X100 / X168i-class | DS-XL 8845HS |
| EXP-P100-AI-001 | Ryzen AI Embedded P132 / P132i-class | Student 8840U |
