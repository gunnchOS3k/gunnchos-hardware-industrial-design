# gunnchos Hardware Industrial Design

Conceptual **EVT-0 industrial design** for gunnchOS modular console ecosystem.

> **DISCLAIMER:** These CAD files are conceptual EVT-0 industrial design artifacts. They are **not** certified mechanical drawings, **not** safety-certified consumer products, and **not** ready for manufacturing. Not FCC/CE/manufacturing-ready claims.

## Devices

- Student 14.5"
- Handheld Hybrid
- DS-XL Coder
- Wearables/Arena Set

## CAD

OpenSCAD parametric models under `cad/openscad/`. Export with `scripts/render_openscad.sh`.

---

## What is this?

**Document affordable, repairable device families from concept CAD toward manufacturable EVT—not certified hardware yet.**

| | |
|---|---|
| **Status** | Hardware EVT planning repo |
| **Evidence today** | Level 1 smoke test — see [Evidence status](#evidence-status-smoke-test-vs-real-validation) |
| **Start** | [docs/START_HERE.md](docs/START_HERE.md) |

## What problem does this solve?

**Human:** Learners need accessible devices for edge AI and 6G labs without enterprise-only hardware.

**Technical:** EVT-0 concepts must mature to manufacturable CAD, electrical design, BOM, and compliance plans.

**Who is harmed if unsolved:** Schools and labs if hardware is unsafe, unaffordable, or non-repairable.

**Gary / 7GC / digital equality:** This repo supports equitable connectivity research for under-connected communities; Gary is the flagship urban anchor where applicable.

## Beginner mental model

The **blueprint workshop** for tools students would hold in their hands.

## How this repo addresses the problem

Device spec packages, diagrams, BOM validation Makefile, affordability/repairability docs.

**Main output:** Validated spec artifacts (`make e2e` smoke)—no mass-produced units yet.

**Output does NOT prove:** FCC/CE certification or DVT/PVT manufacturing sign-off.

## How this fits gunnchOS3k MLV

Physical endpoint for device OS, Edge-IO, and WAIKE lab kits.

Deep dive: [docs/HOW_THIS_FITS_GUNNCHOS.md](docs/HOW_THIS_FITS_GUNNCHOS.md) · [docs/CROSS_REPO_DEPENDENCY_MAP.md](docs/CROSS_REPO_DEPENDENCY_MAP.md) (where present)

## How this fits 6G PhD research

Relevant themes: **Edge AI platforms · testbed hardware · digital equality access devices**

Oulu/CWC-style alignment (research direction, not affiliation claim): [docs/HOW_THIS_FITS_6G_PHD_RESEARCH.md](docs/HOW_THIS_FITS_6G_PHD_RESEARCH.md)

## What exists today

- devices/* specs
- docs 00–17
- Makefile validate
- Diagrams

Details: [docs/WHAT_IS_REAL_TODAY.md](docs/WHAT_IS_REAL_TODAY.md)

## Evidence status: smoke test vs real validation

- `make smoke` / `make e2e` = **CI smoke test** — proves code runs, **not** that research claims are field-validated.
- See [docs/NO_MORE_TOY_DEMOS.md](docs/NO_MORE_TOY_DEMOS.md) · [docs/EVIDENCE_STANDARD.md](docs/EVIDENCE_STANDARD.md) · [quality/CLAIMS_TO_EVIDENCE_MATRIX.md](quality/CLAIMS_TO_EVIDENCE_MATRIX.md)

**Next real evidence needed:**

- EVT-1 CAD
- Schematics
- BOM quotes
- Thermal/battery plan
- Compliance plan
- Prototype build

## Run or inspect this repo

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
make e2e
```

| | |
|---|---|
| **Output** | `validation logs under results/` |
| **Means** | Reproducible smoke artifacts for CI and reviewers |
| **Does not mean** | Conference, adoption, or manufacturing readiness |

Video: [docs/video_walkthrough_script.md](docs/video_walkthrough_script.md)

## Visual map

```mermaid
flowchart LR
  HW[gunnchos-hardware] --> DeviceOS[gunnchos-device-os]
  HW --> EdgeIO[edge-io-measurement-node]
```

More diagrams: [docs/diagrams/README.md](docs/diagrams/README.md) (if present) · [docs/uml/README.md](docs/uml/README.md) (spectrumx)

## Start here based on who you are

| Reader | Start here | You will learn |
|--------|------------|----------------|
| Beginner | [docs/PLAIN_ENGLISH_EXPLANATION.md](docs/PLAIN_ENGLISH_EXPLANATION.md) | Idea without jargon |
| Student / WAIKE | [docs/AUDIENCE_GUIDE.md](docs/AUDIENCE_GUIDE.md) | Learning path |
| Researcher / professor | [docs/HOW_THIS_FITS_6G_PHD_RESEARCH.md](docs/HOW_THIS_FITS_6G_PHD_RESEARCH.md) | Research fit |
| Contributor | [CONTRIBUTING.md](CONTRIBUTING.md) or Issues | How to help |
| City / school partner | [docs/PROBLEM_SOLUTION_MAP.md](docs/PROBLEM_SOLUTION_MAP.md) | Why it matters locally |

## What would make this final?

**Not satisfied yet** for final / conference / adoption / manufacturing gates—see audit:

- [docs/WHAT_WOULD_MAKE_THIS_FINAL.md](docs/WHAT_WOULD_MAKE_THIS_FINAL.md)
- [quality/FINAL_READINESS_CONFIRMATION.md](quality/FINAL_READINESS_CONFIRMATION.md)

## Roadmap from current state to final readiness

| Gate | Status |
|------|--------|
| Concept | Met |
| Smoke test | Met (`make smoke`) |
| Real evidence pipeline | Open |
| Benchmark / field data | Open |
| Internal validation | Open |
| External reproduction | Open |
| Candidate release | Open |
| Final | Not claimed |

Full table: [quality/READINESS_GATE_TABLE.md](quality/READINESS_GATE_TABLE.md)

## Related repos in the 7GC research spine


| Repo | Role |
|------|------|
| [7gc-digital-twin](https://github.com/gunnchOS3k/7gc-digital-twin) | Community digital twin spine |
| [spectrumx-ai-ran-gary](https://github.com/gunnchOS3k/spectrumx-ai-ran-gary) | AI-RAN + SpectrumX competition path |
| [readygary-6g-beam-selection](https://github.com/gunnchOS3k/readygary-6g-beam-selection) | Beam selection / PHY-facing evidence |
| [edge-io-measurement-node](https://github.com/gunnchOS3k/edge-io-measurement-node) | Privacy-first edge measurement |
| [ntn-resilience-sim](https://github.com/gunnchOS3k/ntn-resilience-sim) | NTN + terrestrial resilience |
| [waike-research-ops](https://github.com/gunnchOS3k/waike-research-ops) | Education & workforce pipeline |
| [gunnchos-hardware-industrial-design](https://github.com/gunnchOS3k/gunnchos-hardware-industrial-design) | Device hardware EVT planning |
| [gunnchos-device-os](https://github.com/gunnchOS3k/gunnchos-device-os) | School/research device OS prototype |
| [gunnchAI3k](https://github.com/gunnchOS3k/gunnchAI3k) | Learning assistant (where relevant) |


## Claims and non-claims

**Supports today:** Runnable scaffold, documented methods, smoke-test artifacts, honest limitations.

**Does not prove yet:** FCC/CE certification or DVT/PVT manufacturing sign-off.

**Requires evidence issues:** See GitHub `[Evidence TODO]` issues and `quality/CLAIMS_TO_EVIDENCE_MATRIX.md`.

---

## Industry / research-grade tooling alignment

| Tool / ecosystem | Why it matters | Adapter | Runs now? | Access? |
|------------------|----------------|---------|-----------|---------|
| See matrix | Evidence upgrade path | `industry_research_stack/` | Stub exports | Optional |

**Commands:** `make e2e` (includes tool export stubs) · `python3 scripts/run_all_tool_exports.py`

**Notice:** Aligned with public research ecosystems — [non-affiliation](industry_research_stack/NON_AFFILIATION_NOTICE.md). Smoke stubs only unless documented otherwise.

## Wireless engineering alignment

See [docs/WIRELESS_ENGINEERING_ALIGNMENT.md](docs/WIRELESS_ENGINEERING_ALIGNMENT.md).


---

## EVT-1 hardware package (this pass)

**Status:** manufacturing-track architecture package — **not** final manufacturing release.

```bash
python3 scripts/validate_bom.py
pytest -q tests/test_bom_schema.py tests/test_required_files.py
```

PRD: [product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md](product/PRD_GUNNCHOS_MODULAR_CONSOLE_ECOSYSTEM.md) (full §1–12)

Supporting: [PERFORMANCE_TARGETS](product/PERFORMANCE_TARGETS.md) · [USER_PERSONAS](product/USER_PERSONAS.md) · [SOFTWARE_ECOSYSTEM](product/SOFTWARE_ECOSYSTEM.md) · [MVP_SCOPE](product/MVP_SCOPE.md) · [CLAIM_BOUNDARY](product/CLAIM_BOUNDARY.md)

OS contract: [docs/OS_HARDWARE_CONTRACT.md](docs/OS_HARDWARE_CONTRACT.md)
