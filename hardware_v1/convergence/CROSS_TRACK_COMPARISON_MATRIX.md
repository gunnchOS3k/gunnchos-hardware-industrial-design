# Cross-track comparison matrix

**Generated:** 2026-09-18T17:46:17Z  
**Campaign:** `HARDWARE_1_0D_FOUR_TRACK_CONVERGENCE_MERGE_READINESS`  
**Claim boundary:** architecture / control-plane baseline only — not physical pass, not certification, not fab release, not purchased, not GXE execution.


## Rule

Never create one simplistic overall winner score. Compare **per workload**.

| Dimension | PRODUCT_MAINLINE AMD | OPEN_ENGINEERING NXP | GREENFIELD GXE | REFERENCE_CONTROL COM-HPC/COTS |
|---|---|---|---|---|
| Primary question | Product experience + x86 compat | Board ownership / fab learning | Experience-first greenfield | Fault isolation / baseline |
| task success | required | engineering tasks | experimental | control |
| latency p50/p95/p99 | product SLOs | learning SLOs | experimental | control |
| energy/task | product | efficiency learning | experimental | control |
| memory | product | learning | experimental | control |
| CPU/GPU/NPU/FPGA util | product | AP/NPU learning | research | control |
| network bytes | product | as needed | experimental | control |
| storage I/O | product | as needed | experimental | control |
| thermal/power | product comfort | bring-up | experimental | control |
| user interactions | product | limited UI | core | control |
| accessibility completion | product | if UI present | experimental | control |
| recovery behavior | product | brick-avoidance | experimental | control |
| compatibility | Windows/Linux/games | Linux embedded | custom | x86 modular control |
| manufacturing complexity | high (owned MB) | high (owned MB) | variable | lower modular |
| serviceability | product intent | learning | experimental | modular swap |

Schema: `CROSS_TRACK_BENCHMARK_SCHEMA.json`
