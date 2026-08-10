# Handheld Storage Policy (WP-002 / Outcome A)

**Status:** digital policy (E4) · **PHYSICAL_EXECUTION_FREEZE ACTIVE**  
**Defect:** `NPI_DEFECT-HANDHELD-STORAGE-HEADROOM-001`  
**Decision:** **A** — 32 GB on-module eMMC is system/recovery-focused; MLP user content requires supported expansion (microSD; USB optional tertiary).

Do not invent larger Radxa eMMC/UFS SKUs. Carrier NVMe remux is Class E only.

---

## Hardware truth (accepted)

| Tier | Device | Role |
|------|--------|------|
| Onboard | RM121-D8E32 on-module **32 GB eMMC** | Slot A/B, recovery, boot/firmware, core OS apps, AI Nano core, update/emergency reserves |
| Expansion (required for MLP) | **microSD** via SoM↔SDMMC ICD | Games, patches, shader caches, Flatpak runtimes, AI Fast/Pro + full vision/speech/embeddings, WAIKE, Archive, user docs/captures/saves, browser/messaging caches |
| Tertiary (optional) | USB-attached storage | Import/export, Archive overflow |
| Not in freeze | Carrier NVMe / larger eMMC MPN | Rejected for silent implementation |

Sources: `EXACT_MPN_MATRIX.md`, NX5 brief verify, `som_carrier_icd.md`, carrier netlist `STORAGE_SDMMC`.

---

## Placement rules

### Must stay on eMMC

- Slot A, Slot B, Recovery, boot/firmware
- Update staging / rollback reserve
- Emergency save reserve
- Core gunnchOS system apps (not full Flatpak cache)
- AI **Nano** core weights required for offline assistant boot
- Active logs / crash-dump budget
- Tiny user micro-workspace (settings, credentials metadata)

### Must live on expansion (microSD) when MLP content is present

- Four first-party game installs + patches + shader caches
- Flatpak/runtime overhead beyond core OS
- AI Fast/Pro tiers; full vision/speech/embedding/reranker sets
- AI model update overlap buffers
- Project indexes
- WAIKE offline pack
- Archive playable data
- User documents, screenshots/captures, save data
- Browser and messaging/media caches

### Immutable / never silently deleted

- Slot A/B payload integrity
- Recovery image
- User save data and documents (may **block** writes; may not silently drop)
- Update rollback slot contents while an update is in flight

---

## Reserves and warnings (onboard usable ≈ 29.76 GiB)

| Parameter | Value | Behavior |
|-----------|-------|----------|
| Minimum free reserve | `max(2.0 GiB, 10% usable)` ≈ **2.976 GiB** | Hard floor |
| Update / rollback reserve | **2.0 GiB** | Not available for games/models/caches |
| Emergency save reserve | **0.5 GiB** | Reserved for save-game / document / AI memory commits under pressure |
| Low-space warning | free &lt; **3.5 GiB** or &lt; **15%** | UI warning; prefer reclamation |
| Force reclamation | free ≤ minimum free reserve | Evict reclaimable caches before any nonessential write |
| Reject rule | `required_bytes < nominal_bytes` is **not** sufficient | Compare against **usable** bytes after format/FS/wear |

`required_bytes` for any install/update must leave all reserves intact on the target volume.

---

## Reclamation and eviction

Order (safe → aggressive):

1. Browser / messaging / shader / package download caches on expansion
2. AI model **update overlap** temp files (never the active pinned model)
3. Oldest unused game patches superseded by newer patches
4. Optional Flatpak runtimes not referenced by installed apps
5. **Prompt user** before removing a game install or AI Fast/Pro tier
6. **Never** auto-evict Slot A/B, recovery, saves, documents, or the active Nano core

If reclamation cannot free enough space: **fail closed** (deny install/update/download) with an actionable error. No silent truncate of user data.

---

## Offline-pack (WAIKE) policy

- WAIKE offline packs install only to **expansion** (or tertiary USB if explicitly selected).
- If microSD is absent/unmounted: deny pack download/install; keep Nano core and already-synced lesson stubs on eMMC if present.
- Pack updates must preflight `size + update_overlap + reserves` on the expansion volume.

---

## Update path

1. Preflight: Slot B / recovery healthy; onboard free ≥ update reserve + package size accounting.
2. Stage into update temp within reserve budget.
3. Apply to inactive slot; keep rollback slot intact.
4. On failure: roll back; do not consume emergency save reserve for package blobs.
5. Near-full eMMC: reclaim caches first; if still insufficient, **block update** rather than delete user data.

---

## Save / document / AI memory under pressure

When free &lt; warning threshold:

- Prefer writing saves/docs/AI project memory to expansion if mounted.
- If only eMMC remains and free &gt; emergency save reserve: allow one emergency commit from that reserve, then force reclamation UI.
- If free ≤ 0 after reserves: **deny write** with explicit error (no silent data loss).

---

## Expansion absent / unmounted

| Action | Result |
|--------|--------|
| Boot OS / recovery / Nano core | Allowed on eMMC |
| Install games / Fast-Pro models / WAIKE / Archive | **Denied** |
| Update OS | Allowed if eMMC reserves satisfied |
| Save game / document | Allowed on eMMC only within emergency/micro-workspace budgets; warn to insert media |

---

## Class E boundary (not implemented here)

Expanding carrier storage to NVMe/SATA via PCIe remux (vs WWAN/USB3) remains a **deferred architecture spike** requiring CR + ADR + Edmund approval. This policy closes the defect under Outcome A without that change.

---

## Cross-repo handoff

- Hardware capacity/growth artifacts: this package
- Device-OS enforcement / profile mirror: `gunnchos-device-os` handheld storage profile + Phase XV files_storage Outcome A recalculation
- Field-kit aggregation: may mirror decision; do not invent SKUs

## Claim boundary

Digital policy and simulation only. Physical endurance, microSD qualification, and field wear remain PHYSICAL_PENDING / E5.
