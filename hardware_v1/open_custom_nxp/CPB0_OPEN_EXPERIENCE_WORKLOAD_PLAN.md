# CPB0-O experience-first workload plan

**Generated:** 2026-09-18T18:54:56Z  
**Campaign:** `NXP0_OPEN_CUSTOM_IMX95_IMPLEMENTATION_FOUNDATION`  
**Claim boundary:** architecture / public-collateral implementation foundation only — not physical pass, not certification, not fab release, not purchased, not NDA, not GXE execution, not software RC1 change.



Aligned to `hardware_v1/convergence/HARDWARE_EXPERIENCE_CONTRACT_*` and GXE integration contract (GXE not executed here).

| Workload | Instrumentation hooks (digital) | Physical measurement |
|---|---|---|
| boot-to-usable | UART timestamps; EC PG timeline; boot stage GPIO | PENDING_PHYSICAL |
| local lesson | storage mount latency hook; display ready GPIO | PENDING_PHYSICAL |
| local AI small-model | NPU/CPU utilization hook; thermal sensor log | PENDING_PHYSICAL |
| edit/build/run | storage + memory pressure hooks | PENDING_PHYSICAL |
| native game baseline | frame-time hook placeholder (not product claim) | PENDING_PHYSICAL |
| recovery | EC recovery strap event log; boot-mode sense | PENDING_PHYSICAL |

No physical measurements in NXP-0. Hooks only.
