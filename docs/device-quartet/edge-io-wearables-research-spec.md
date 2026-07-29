# Edge IO Wearables Research Specification

## Research role
Embodied compute — sensing, haptic feedback, HUD overlay, and body-area safety benchmark.

## Primary workload
IMU sensing, haptic actuation, BLE/UWB positioning, environmental monitoring, safety alerts; continuous operation for 15–60 minute sessions.

## Network requirements
Ultra-low-latency body-area network; BLE/UWB to hub device; local edge for processing; minimal WAN dependence.

## Compute requirements
Low-power MCU/SoC; offload heavy processing to paired device or local edge; minimal local storage.

## Energy constraints
Coin-cell or small LiPo; extreme energy efficiency required; hours of continuous sensing; thermal limits critical for body-worn.

## Latency/reliability targets
- Event-to-feedback (haptics): <10ms
- Safety alerts: <20ms
- Reliability for safety: >99.9%
- Sensing sample rate: application-dependent (50–1000 Hz)

## Security/privacy concerns
Body-area data (motion, biometric-like signals); consent required for wearable sensing; data minimization mandatory; local processing preferred.

## Simulation substitute if hardware is incomplete
- Sensor trace replay from synthetic or recorded data
- Haptic latency emulation via software timing
- QEMU firmware simulation profile
- MCU emulation with artificial timing constraints

## Prototype workload plan
Capture representative sensor streams; model haptic feedback loops; measure end-to-end event-to-feedback latency; evaluate energy per sensing cycle.

## Failure/degraded-mode behavior
Local safety alerts operate without network; reduced haptic fidelity; store-and-forward telemetry; graceful degradation of non-safety features.

## What data is collected
Sensor event rates, haptic round-trip latency, energy per sensing cycle, BLE/UWB link quality, dropped event rate, thermal state.

## Whether ethics review is needed
**Yes** for any body-worn data involving human participants. Technical bench tests on non-human targets may not require review — confirm with institution.

## Current completion status
**Concept-complete** — QEMU profile, component selection (low-power MCU, BLE/UWB, IMU, haptic driver), OS validation doc, and mechanical specs exist.

## Remaining work
- Formalize sensing workload specification
- Define haptic latency budget breakdown
- Document body-area network model
- Create reproducible sensing simulation
- Define energy model per sensing mode

## Definition of done
Sensing/haptic workload specification with latency budgets, energy model, simulation plan, and reproducible experiment commands documented.
