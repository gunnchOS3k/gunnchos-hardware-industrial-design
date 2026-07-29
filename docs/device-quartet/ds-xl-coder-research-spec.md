# DS-XL Coder Research Specification

## Research role
Creation compute — local build, test, deploy workflows and peer collaboration benchmark.

## Primary workload
Code compilation, container builds, local AI inference, peer code sharing, deploy-to-edge operations; sessions of 60–240 minutes.

## Network requirements
Local edge / LAN for peer transfer; intermittent WAN for package fetch and sync; high local storage I/O.

## Compute requirements
Higher local compute than other devices; GPU/NPU for local inference; large storage for containers and models.

## Energy constraints
Plugged-in primary use; 4+ hour portable battery for field creation; higher thermal budget allows burst compute.

## Latency/reliability targets
- Local edge response: <20ms
- Sync/deploy operations: <500ms
- Build feedback: <5s
- Peer transfer: LAN-speed
- Reliability: >99% for local operations

## Security/privacy concerns
Code IP protection, credentials, local inference models, peer trust for device-to-device transfers.

## Simulation substitute if hardware is incomplete
- Build-deploy workload replay on standard dev machine
- Emulated edge and peer network (Docker compose + tc)
- Resource-constrained VM matching spec compute budget
- QEMU profile exists in this repository

## Prototype workload plan
Model build-test-deploy cycles; measure local vs. edge vs. cloud placement tradeoffs; evaluate peer transfer under varying connectivity.

## Failure/degraded-mode behavior
Full local operation continues if network unavailable; sync queued for later; peer discovery via local mesh; no work lost.

## What data is collected
Build times, sync delays, peer transfer throughput, energy per operation, edge offload ratio, local vs. remote compute fraction.

## Whether ethics review is needed
Not for technical telemetry. Yes if student code or project data is analyzed for research purposes.

## Current completion status
**Concept-complete** — Deploy contract, device profile, OS export, and firmware manifest exist.

## Remaining work
- Formalize creation workload traces
- Define peer transfer protocol benchmarks
- Document edge placement experiment plan
- Create reproducible build-deploy simulation

## Definition of done
Creation/deployment workload specification with local-edge metrics, peer transfer plan, and reproducible experiment commands documented.
