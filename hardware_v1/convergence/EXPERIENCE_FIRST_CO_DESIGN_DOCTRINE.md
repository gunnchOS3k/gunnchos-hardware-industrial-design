# Experience-first hardware/software co-design doctrine

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Core rule

> **Software must earn additional hardware.**

## Required flow

`USER OUTCOME`
→ Experience Contract
→ latency / quality / reliability / accessibility / offline / privacy target
→ software architecture
→ algorithm / data-flow efficiency
→ runtime / scheduler / memory optimization
→ hardware acceleration where justified
→ custom board / silicon optimization where justified

## Explicit anti-pattern

`faster hardware masking uncharacterized software inefficiency`

No hardware requirement may be treated as justified solely because a stronger SKU fixes a performance problem.

## Hardware-selection evidence (required before promotion)

| Evidence class | Question |
|---|---|
| workload | Which user-visible task fails or degrades? |
| latency | p50 / p95 / p99 interaction or frame latency |
| memory | Peak / sustained RSS and bandwidth |
| energy/task | Joules per completed user task |
| thermal/power | Sustained envelope vs skin/comfort limits |
| network | Bytes and RTT sensitivity |
| storage | IOPS / sequential impact on experience |
| accelerator utilization | CPU/GPU/NPU/FPGA useful occupancy |
| user-visible improvement | Measured delta vs Experience Contract targets |
| graceful-degradation | Behavior when accel / link / thermal is unavailable |

## Track application

- `PRODUCT_MAINLINE` (AMD): product Experience Contracts for education/work/create/game
- `OPEN_ENGINEERING_MAINLINE` (NXP): engineering learning contracts; methodology, not product parity
- `GREENFIELD_EXPERIMENT` (GXE): greenfield Experience Contracts (executed outside this repo)
- `REFERENCE_CONTROL`: control measurements only
