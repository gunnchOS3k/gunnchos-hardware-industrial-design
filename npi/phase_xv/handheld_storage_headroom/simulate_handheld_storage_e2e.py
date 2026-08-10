#!/usr/bin/env python3
"""WP-002 E2E digital simulation: Handheld storage Outcome A.

Simulates fill / update / save / cleanup without silent data loss.
No physical media. Evidence class E4.
"""
from __future__ import annotations

import json
from dataclasses import dataclass, field, asdict
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[3]
PKG = Path(__file__).resolve().parent
OUT = PKG / "HANDHELD_STORAGE_E2E_SIM_RESULT.json"

ONBOARD_USABLE_GB = 29.76
EXPANSION_USABLE_GB = 59.52  # representative 64GB microSD @ 93%

MIN_FREE_GB = max(2.0, 0.10 * ONBOARD_USABLE_GB)  # 2.976
UPDATE_RESERVE_GB = 2.0
EMERGENCY_SAVE_GB = 0.5
WARNING_FREE_GB = 3.5

# Protected categories — never silently deleted
PROTECTED = {
    "slot_a",
    "slot_b",
    "recovery",
    "boot_firmware",
    "save_data",
    "user_documents",
    "ai_nano_core",
    "update_rollback_slot",
}


@dataclass
class Volume:
    name: str
    usable_gb: float
    used: dict[str, float] = field(default_factory=dict)
    mounted: bool = True
    events: list[dict[str, Any]] = field(default_factory=list)

    @property
    def used_gb(self) -> float:
        return round(sum(self.used.values()), 6)

    @property
    def free_gb(self) -> float:
        return round(self.usable_gb - self.used_gb, 6)

    def reserve_floor(self) -> float:
        if self.name == "onboard":
            return MIN_FREE_GB + UPDATE_RESERVE_GB + EMERGENCY_SAVE_GB
        return 4.0  # expansion large-install floor from growth policy

    def available_for(self, kind: str) -> float:
        """Bytes available for a write of the given kind after reserves."""
        floor = self.reserve_floor()
        if kind in {"save_data", "user_documents", "ai_memory"} and self.name == "onboard":
            # May dip into emergency save only (still keep min free + update reserve)
            floor = MIN_FREE_GB + UPDATE_RESERVE_GB
        if kind == "os_update" and self.name == "onboard":
            # Update may consume update reserve; keep min free + emergency
            floor = MIN_FREE_GB + EMERGENCY_SAVE_GB
        return round(self.free_gb - floor, 6)


@dataclass
class SimResult:
    ok: bool = True
    silent_data_loss: bool = False
    steps: list[dict[str, Any]] = field(default_factory=list)
    failures: list[dict[str, Any]] = field(default_factory=list)

    def record(self, step: str, **kwargs: Any) -> None:
        self.steps.append({"step": step, **kwargs})


def allocate(vol: Volume, key: str, gb: float, *, protect: bool = False) -> None:
    vol.used[key] = vol.used.get(key, 0.0) + gb
    if protect:
        assert key in PROTECTED or key.startswith("protected_")


def try_write(
    result: SimResult,
    vol: Volume,
    key: str,
    gb: float,
    kind: str,
    *,
    allow_reclaim: bool = True,
) -> bool:
    if not vol.mounted:
        err = {
            "ok": False,
            "error": "volume_unmounted",
            "volume": vol.name,
            "key": key,
            "kind": kind,
            "gb": gb,
        }
        result.failures.append(err)
        result.record("write_denied", **err)
        return False

    need = gb
    avail = vol.available_for(kind)
    if avail < need and allow_reclaim:
        reclaimed = reclaim_caches(vol)
        result.record("reclaim", volume=vol.name, reclaimed_gb=reclaimed)
        avail = vol.available_for(kind)

    if avail < need:
        err = {
            "ok": False,
            "error": "insufficient_space",
            "volume": vol.name,
            "key": key,
            "kind": kind,
            "gb": gb,
            "available_gb": avail,
            "free_gb": vol.free_gb,
        }
        result.failures.append(err)
        result.record("write_denied", **err)
        return False

    allocate(vol, key, gb)
    result.record(
        "write_ok",
        volume=vol.name,
        key=key,
        kind=kind,
        gb=gb,
        free_gb=vol.free_gb,
    )
    return True


def reclaim_caches(vol: Volume) -> float:
    """Reclaim only non-protected caches. Never touch saves/docs/slots."""
    reclaimable = [
        "browser_cache",
        "messaging_media_cache",
        "shader_caches",
        "download_cache",
        "ai_model_update_overlap",
        "flatpak_unused_runtime",
    ]
    total = 0.0
    for key in reclaimable:
        if key in vol.used and key not in PROTECTED:
            total += vol.used.pop(key)
    return round(total, 6)


def fresh_install(onboard: Volume) -> None:
    allocate(onboard, "slot_a", 5.0, protect=True)
    allocate(onboard, "slot_b", 5.0, protect=True)
    allocate(onboard, "recovery", 2.0, protect=True)
    allocate(onboard, "boot_firmware", 0.25, protect=True)
    allocate(onboard, "gunnchos_apps_core", 2.0)
    allocate(onboard, "ai_nano_core", 2.0, protect=True)
    allocate(onboard, "vision_speech_stub", 0.25)
    allocate(onboard, "embeddings_stub", 0.25)
    allocate(onboard, "logs", 0.5)
    allocate(onboard, "crash_dumps", 0.25)
    allocate(onboard, "user_micro_workspace", 0.5)
    # Reserves are free space accounting, not allocated blobs.


def run_e2e(*, expansion_mounted: bool = True) -> dict[str, Any]:
    result = SimResult()
    onboard = Volume("onboard", ONBOARD_USABLE_GB)
    expansion = Volume("expansion", EXPANSION_USABLE_GB, mounted=expansion_mounted)

    # 1. Fresh install (system on eMMC)
    fresh_install(onboard)
    result.record(
        "fresh_install",
        onboard_used_gb=onboard.used_gb,
        onboard_free_gb=onboard.free_gb,
        meets_reserves=onboard.free_gb >= MIN_FREE_GB + UPDATE_RESERVE_GB + EMERGENCY_SAVE_GB,
    )

    # 2. Four games + patches + shaders on expansion
    for i in range(4):
        ok = try_write(result, expansion, f"game_{i}", 1.5, "game_install")
        if not ok and expansion_mounted:
            result.ok = False
    try_write(result, expansion, "game_patches", 1.5, "game_patch")
    try_write(result, expansion, "shader_caches", 1.0, "cache")

    # 3. Local AI models (Fast/Pro + full vision on expansion; Nano already onboard)
    try_write(result, expansion, "ai_fast_pro", 3.0, "ai_model")
    try_write(result, expansion, "vision_speech_full", 1.0, "ai_model")
    try_write(result, expansion, "embeddings_reranker", 0.75, "ai_model")
    try_write(result, expansion, "ai_model_update_overlap", 1.0, "cache")

    # 4. WAIKE + Archive + user files
    try_write(result, expansion, "waike_offline_pack", 1.5, "offline_pack")
    try_write(result, expansion, "archive_playable_data", 2.0, "archive")
    try_write(result, expansion, "user_documents", 2.0, "user_documents")
    try_write(result, expansion, "screenshots_captures", 1.0, "cache")
    try_write(result, expansion, "save_data", 0.5, "save_data")
    try_write(result, expansion, "browser_cache", 1.0, "cache")
    try_write(result, expansion, "messaging_media_cache", 1.0, "cache")
    try_write(result, expansion, "flatpak_runtime_overhead", 4.0, "runtime")
    try_write(result, expansion, "project_indexes", 0.5, "index")

    # 5. Fill toward threshold on expansion with download cache
    while expansion.mounted and expansion.available_for("cache") > 1.0:
        try_write(result, expansion, "download_cache", 1.0, "cache", allow_reclaim=False)
        if expansion.free_gb < 8.0:
            break

    # 6. OS update attempt on onboard
    update_ok = try_write(result, onboard, "update_temp", 1.0, "os_update")
    if update_ok:
        # Simulate commit to inactive slot then free temp
        onboard.used.pop("update_temp", None)
        result.record("update_commit_and_cleanup", onboard_free_gb=onboard.free_gb)
    else:
        # Must not destroy user data to force update
        for key in list(onboard.used):
            if key in PROTECTED:
                continue
        result.record("update_blocked_without_data_loss", onboard_free_gb=onboard.free_gb)

    # 7. Game save + document save + AI memory under pressure
    # Fill onboard logs to approach warning
    while onboard.available_for("cache") > 0.25:
        try_write(result, onboard, "logs", 0.25, "cache", allow_reclaim=False)
        if onboard.free_gb <= WARNING_FREE_GB:
            break

    save_target = expansion if expansion.mounted else onboard
    save_ok = try_write(result, save_target, "save_data", 0.05, "save_data")
    doc_ok = try_write(result, save_target, "user_documents", 0.05, "user_documents")
    mem_ok = try_write(result, save_target, "ai_memory", 0.05, "ai_memory")

    # 8. Cache cleanup must not touch protected
    before_protected = {k: onboard.used.get(k, 0.0) for k in PROTECTED}
    before_exp_protected = {k: expansion.used.get(k, 0.0) for k in PROTECTED}
    reclaim_caches(onboard)
    reclaim_caches(expansion)
    after_protected = {k: onboard.used.get(k, 0.0) for k in PROTECTED}
    after_exp_protected = {k: expansion.used.get(k, 0.0) for k in PROTECTED}
    if before_protected != after_protected or before_exp_protected != after_exp_protected:
        result.silent_data_loss = True
        result.ok = False
        result.failures.append({"error": "protected_data_mutated_by_reclaim"})

    result.record(
        "cleanup",
        protected_onboard_unchanged=before_protected == after_protected,
        protected_expansion_unchanged=before_exp_protected == after_exp_protected,
        onboard_free_gb=onboard.free_gb,
        expansion_free_gb=expansion.free_gb if expansion.mounted else None,
    )

    # 9. Rollback path: ensure slot_b/recovery still present after update attempt
    rollback_ok = onboard.used.get("slot_b", 0) >= 5.0 and onboard.used.get("recovery", 0) >= 2.0
    result.record("rollback_slots_intact", ok=rollback_ok)
    if not rollback_ok:
        result.ok = False
        result.silent_data_loss = True

    # Outcome checks
    if expansion_mounted:
        if not (save_ok and doc_ok and mem_ok):
            result.ok = False
        if onboard.free_gb < MIN_FREE_GB:
            # After cleanup should be able to stay above absolute min if possible
            result.record("warning_onboard_below_min_free", free_gb=onboard.free_gb)
    else:
        # Without expansion, game/AI/WAIKE installs must have been denied — not silently placed on eMMC
        illicit = [k for k in expansion.used if k.startswith("game_") or k in {
            "waike_offline_pack", "ai_fast_pro", "archive_playable_data"
        }]
        if illicit:
            result.ok = False
            result.failures.append({"error": "content_on_unmounted_volume", "keys": illicit})
        # Writes to expansion should have failed closed
        denied = [f for f in result.failures if f.get("error") == "volume_unmounted"]
        result.record("expansion_absent_fail_closed", denied_count=len(denied))
        if len(denied) < 4:
            result.ok = False

    if result.silent_data_loss:
        result.ok = False

    report = {
        "schema": "gunnchos.wp002.handheld_storage_e2e_sim.v1",
        "decision_outcome": "A",
        "expansion_mounted": expansion_mounted,
        "ok": result.ok,
        "silent_data_loss": result.silent_data_loss,
        "onboard": {
            "usable_gb": onboard.usable_gb,
            "used_gb": onboard.used_gb,
            "free_gb": onboard.free_gb,
            "used": dict(onboard.used),
        },
        "expansion": {
            "usable_gb": expansion.usable_gb,
            "mounted": expansion.mounted,
            "used_gb": expansion.used_gb if expansion.mounted else 0.0,
            "free_gb": expansion.free_gb if expansion.mounted else None,
            "used": dict(expansion.used),
        },
        "margins": {
            "min_free_gb": MIN_FREE_GB,
            "update_reserve_gb": UPDATE_RESERVE_GB,
            "emergency_save_gb": EMERGENCY_SAVE_GB,
            "warning_free_gb": WARNING_FREE_GB,
        },
        "steps": result.steps,
        "failures": result.failures,
        "claim_boundary": (
            "Digital E2E simulation only. No physical media endurance claim. "
            "Independent V1 verifier owns VP-002-RESULT.json."
        ),
    }
    return report


def main() -> int:
    mounted = run_e2e(expansion_mounted=True)
    absent = run_e2e(expansion_mounted=False)
    combined = {
        "schema": "gunnchos.wp002.handheld_storage_e2e_sim_bundle.v1",
        "decision_outcome": "A",
        "with_expansion": mounted,
        "without_expansion": absent,
        "ok": bool(mounted["ok"] and absent["ok"] and not mounted["silent_data_loss"] and not absent["silent_data_loss"]),
        "PHYSICAL_EXECUTION_FREEZE": "ACTIVE",
        "evidence_class": "E4_DIGITAL",
    }
    OUT.write_text(json.dumps(combined, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({"ok": combined["ok"], "out": str(OUT)}, indent=2))
    return 0 if combined["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
