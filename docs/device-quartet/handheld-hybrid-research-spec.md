# Handheld Hybrid Research Specification

## Research role
Mobile/docked compute — portable learning, communication, and docked expansion benchmark.

## Primary workload
Mobile lessons, messaging, AR/camera demos, docked display for presentation/gaming; frequent mobility with handover events.

## Network requirements
Cellular/Wi-Fi with frequent handover; must handle mobility and intermittent coverage; dock mode uses stable Wi-Fi.

## Compute requirements
Mobile SoC for real-time interaction; dock mode enables larger display and peripherals; moderate GPU for AR/gaming.

## Energy constraints
6+ hour mobile battery; dock mode uses external power; thermal management for sustained gaming/AR.

## Latency/reliability targets
- Real-time interaction (gaming/AR): <50ms
- Mobile learning content: <150ms
- Handover interruption: <200ms target
- Reliability: >99% for interactive sessions

## Security/privacy concerns
Location data in mobile mode; camera/microphone privacy; device loss/theft risk; dock-mode access control.

## Simulation substitute if hardware is incomplete
- Mobile workload traces on emulated device
- ns-3 or similar for mobility/handover simulation
- Network emulation with handover event injection
- QEMU profile exists in this repository

## Prototype workload plan
Model mobile session patterns; simulate handover events; measure session continuity during mobility; evaluate docked vs. mobile performance.

## Failure/degraded-mode behavior
Seamless handover to local edge; offline mode with local content; dock-failover to cached state; session persistence across mode transitions.

## What data is collected
Handover events, mobility traces (simulated), jitter, session interruption duration, energy per mode, throughput variation.

## Whether ethics review is needed
Not for technical telemetry. Yes if location tracking or camera use involves human participants.

## Current completion status
**Concept-complete** — OS behavior doc, device profile YAML, firmware manifest, and mechanical specs exist.

## Remaining work
- Formalize mobility workload with handover scenarios
- Define docked-mode transition metrics
- Document handover benchmark experiment plan
- Create reproducible mobility simulation

## Definition of done
Mobility and handover workload specification with quantified metrics, simulation plan, and reproducible experiment commands documented.
