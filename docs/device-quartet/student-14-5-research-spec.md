# Student 14.5" Research Specification

## Research role
Desk compute — sustained learning, work, and full-session interaction benchmark.

## Primary workload
Video conferencing, document editing, coursework, LMS interaction, local IDE, sustained sessions (30–120 minutes).

## Network requirements
Stable broadband or Wi-Fi preferred; must tolerate degraded connectivity with graceful degradation to cached content.

## Compute requirements
Moderate local CPU/GPU for browser, IDE, video decode; edge offload capability for heavy tasks.

## Energy constraints
8+ hour battery target; sustained thermal envelope (~15W) for long sessions without throttling.

## Latency/reliability targets
- Interactive tasks: <100ms
- Buffered learning content: <200ms acceptable
- Reliability: >99% session continuity

## Security/privacy concerns
Student identity, coursework, credentials; guardian policies for minors; local credential storage.

## Simulation substitute if hardware is incomplete
- Workload trace replay on commodity laptop
- Resource-constrained VM (cgroups limiting CPU/memory to spec)
- Network emulation via tc/netem for connectivity degradation
- QEMU profile exists in this repository

## Prototype workload plan
Capture representative learning/work session traces; replay under varied connectivity conditions using the digital-twin scenario framework.

## Failure/degraded-mode behavior
Local cache serves recently accessed content; sync deferred; session state preserved to local storage; user notified of degraded state.

## What data is collected
Technical telemetry only: latency, throughput, energy, thermal state, connectivity transitions, cache hit rates.

## Whether ethics review is needed
Not for technical telemetry alone. Yes if learner identity, progress, or behavior is logged. Yes if minors use the device.

## Current completion status
**Concept-complete** — OS behavior doc, device profile YAML, firmware manifest, QEMU profile, and mechanical specs exist.

## Remaining work
- Formalize benchmark workload traces
- Define specific metric targets per scenario
- Document simulation experiment plan
- Create reproducible evaluation scripts

## Definition of done
Workload specification with quantified metrics, simulation plan, evaluation criteria, and reproducible experiment commands documented.
