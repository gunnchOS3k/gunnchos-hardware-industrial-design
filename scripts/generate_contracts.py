#!/usr/bin/env python3
import json
from pathlib import Path

DEVICES = ["student_14_5", "handheld_hybrid", "ds_xl_coder", "wearables_arena_set"]
ROOT = Path(__file__).resolve().parents[1]


def profile(device: str) -> dict:
    return {
        "device_id": device,
        "readiness_level": "H2",
        "thermal_limits": {"skin_c_max": 45},
        "battery_limits": {"max_charge_w": 65},
        "display_capabilities": {"touch": device != "wearables_arena_set"},
        "input_capabilities": {"keyboard": device == "student_14_5"},
        "wireless_capabilities": {"wifi": "6e_minimum"},
        "security_capabilities": {"tpm_target": True, "secure_boot_target": True},
        "factory_test_points": ["TP1", "TP2"],
        "repairability_flags": {"battery_service": "evaluated"},
    }


def main() -> None:
    out = ROOT / "results/contracts"
    out.mkdir(parents=True, exist_ok=True)
    for d in DEVICES:
        p = out / f"{d}_hardware_profile.json"
        p.write_text(json.dumps(profile(d), indent=2) + "\n", encoding="utf-8")
    print("Generated hardware contracts")


if __name__ == "__main__":
    main()
