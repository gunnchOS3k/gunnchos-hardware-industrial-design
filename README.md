# gunnchos-hardware-industrial-design

Industrial and electrical design source of truth for the **gunnchOS3k** first-party device family (Student 14.5, Handheld Hybrid, DS-XL Coder, Edge I/O Rings, First-party Dock).

> **Current release/state:** `PHYSICAL_PENDING` — design/BOM/RFQ *packets* exist; no fab, no certification, no RFQ send from Cursor.

Ecosystem portal: [gunnchos-research-portal](https://github.com/gunnchOS3k/gunnchos-research-portal) · Product charter: [gunnchOS3k_PRODUCT_CHARTER.md](https://github.com/gunnchOS3k/gunnchos-7gc-ai-ran-field-kit/blob/main/program/charter/gunnchOS3k_PRODUCT_CHARTER.md)

## What is this?

CAD, BOM, device-class specs, firmware/OS compatibility handoff packages, and manufacturer-facing design artifacts for first-party hardware.

## Why does it exist?

So OS, Lab, manufacturing, and education work share one honest hardware truth before physical EVT.

## Where does it fit?

Product Charter **layer 1**. Consumed by `gunnchos-device-os`. Linked from the Ecosystem Portal.

## What is real today?

- Device-family design packages and BOM/validation scripts (`make validate`, `make e2e` smoke)
- OS/firmware compatibility export packages for Device Lab / OS
- RFQ *packet* preparation artifacts (packets ≠ sent RFQs)

## What is simulated / modelled?

- QEMU/host firmware dry-runs and capsule *simulation*
- Conceptual/legacy EVT-0 CAD framing (see `docs/history/`)

## What is physical / external pending?

- Physical EVT/HIL, battery/thermal/RF bring-up
- Fab, purchase, RFQ **send**, FCC/CE/USB-IF and related marks (`EXTERNAL_PENDING`)
- Shipping mechanical drawings certified for manufacturing

## Try / inspect in 5 minutes

```bash
pip install -r requirements.txt
make validate
make e2e   # smoke — not manufacturing readiness
```
Start: [docs/START_HERE.md](docs/START_HERE.md) when present.

## Architecture

Device packages under `device_designs/` / `devices/` + `cad/`, `bom/`, `firmware/`, `os_compatibility/`, certification *planning* docs (not certificates).

## Repo map

| Path | Role |
|---|---|
| `device_designs/` / `devices/` | Per-SKU design SoT |
| `bom/` | BOM truth |
| `firmware/` | Firmware manifests / host dry-run |
| `os_compatibility/` | Handoff to device-os |
| `docs/history/` | HISTORICAL README eras |

## Interfaces

Exports consumed by `gunnchos-device-os` hardware/firmware compatibility layers. No live manufacturer API.

## Tests

```bash
make test
make validate-bom validate-cad
```

## Evidence

Smoke/e2e records and design packages in-repo. Physical EVT evidence is **not** claimed here.

## Known gaps

Physical silicon freeze for EVT, SI bring-up, certification marks, human preference (E6), carrier (E7).

## Beginner path

This is the **blueprint shop** for the five first-party devices — drawings and parts lists, not finished gadgets in a store.

## Intern path

Run `make e2e`, open one device package, and list which claims are digital vs PHYSICAL_PENDING.

## Expert path

Trace BOM → OS profile → RFQ packet readiness; keep `no_RFQ_send` / no fab claims intact.

## Contribution path

Fix design honesty, validators, and handoff packages. Do **not** send RFQs or claim certification from this repo alone.

## Current release / state

**PHYSICAL_PENDING** + **EXTERNAL_PENDING**. Not production-ready hardware. Not certified.

## Claim boundary

No commercial 6G · no certification · no RFQ send · no fab/purchase authorization · Cursor opens **DRAFT** PRs only.

---

## Retained detail (post–Cycle 3A front door)

Practical OS/firmware handoff docs remain below and under `os_compatibility/`, `firmware/`. Prior EVT-0-heavy front door: [docs/history/README_PRE_WP012_EVT0_FRONT.md](docs/history/README_PRE_WP012_EVT0_FRONT.md).

### Quick links

- [os_compatibility/README.md](os_compatibility/README.md)
- [firmware/README.md](firmware/README.md)
- OpenSCAD under `cad/openscad/`
