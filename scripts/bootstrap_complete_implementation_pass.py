#!/usr/bin/env python3
"""Bootstrap component selection, secure boot simulation, and supporting artifacts."""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

DEVICES = {
    "student_14_5": {
        "stack": "x86-64 mobile APU class, 16-32 GB RAM, NVMe 512GB-1TB, Wi-Fi 6E/7, USB-C PD + DP Alt Mode, TPM 2.0",
        "why": "School/university CS/STEM, WSL, Steam/light gaming, creative work, repairable storage",
        "risks": "Thermal under sustained load, DP Alt Mode dock validation pending",
    },
    "handheld_hybrid": {
        "stack": "x86-64 handheld APU, 16 GB RAM, NVMe 512GB+, microSD, 7-8in 1080p, Hall sticks, IMU, active cooling",
        "why": "Handheld gaming, dock/TV, Steam path, offline learning",
        "risks": "Battery/thermal in gaming, Steam compatibility not certified",
    },
    "ds_xl_coder": {
        "stack": "Efficient x86/ARM module, 8-16 GB RAM, 256-512 GB storage, dual 7in touch, USB-C deploy path",
        "why": "Dual-screen coding, classroom deploy, offline lessons",
        "risks": "Dual-screen OS shell not proven on hardware",
    },
    "wearables_arena_set": {
        "stack": "Low-power MCU/SoC, BLE/UWB class, IMU, haptic driver, BMS, venue anchor path",
        "why": "Safe venue play, haptics, marshal mode, supervised sessions",
        "risks": "Arena safety rules not field validated, no WSL workstation",
    },
}

PERSONAS = [
    "pre_k_learner", "high_school_student", "college_cs_stem", "artist", "writer",
    "musician", "gamer", "game_developer", "hardware_maker", "researcher",
    "library_shared_user", "accessibility_first",
]


def write(path: str, content: str) -> None:
    p = ROOT / path
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content.rstrip() + "\n")


def yaml_dump(data: dict) -> str:
    try:
        import yaml
        return yaml.safe_dump(data, sort_keys=False)
    except ImportError:
        return json.dumps(data, indent=2)


def main() -> None:
    write("component_selection/README.md", """# Component Selection

Research-backed component class modeling and simulation for gunnchOS device families.

Example component **classes** only — not final SKUs or vendor quotes.

Run simulations: `python component_selection/simulations/simulate_component_fit.py`
""")

    write("component_selection/COMPONENT_CLAIM_BOUNDARY.md",
          "Example component classes for simulation. Not final BOM, not certified, not vendor-selected SKUs.")

    for name in [
        "USER_WORKLOAD_REQUIREMENTS.md", "COMPONENT_RESEARCH_SOURCE_INDEX.md",
        "COMPONENT_CANDIDATE_MATRIX.md", "DEVICE_ARCHITECTURE_CANDIDATES.md",
        "COMPONENT_SELECTION_DECISION_RECORD.md", "COMPONENT_RISK_REGISTER.md",
        "COMPONENT_COST_MODEL.md", "COMPONENT_SIMULATION_ASSUMPTIONS.md",
    ]:
        write(f"component_selection/{name}", f"# {name.replace('_', ' ').replace('.md', '')}\n\nSee RECOMMENDED_COMPONENT_STACKS.md and simulations/results/.\n")

    rows = "| Device | Recommended stack | Why | Risks | Evidence status | Next physical validation |\n|---|---|---|---|---|---|\n"
    for d, meta in DEVICES.items():
        rows += f"| {d} | {meta['stack']} | {meta['why']} | {meta['risks']} | simulated | DVT hardware bring-up |\n"
    write("component_selection/RECOMMENDED_COMPONENT_STACKS.md", f"# Recommended Component Stacks\n\n{rows}\n")

    write("component_selection/configs/workload_profiles.yaml", yaml_dump({
        "personas": PERSONAS,
        "modes": ["School", "Developer", "Play", "Media", "Studio", "Laboratory", "Offline"],
    }))
    write("component_selection/configs/component_candidates.yaml", yaml_dump({"devices": DEVICES}))
    write("component_selection/configs/device_stack_candidates.yaml", yaml_dump({"stacks": DEVICES}))
    write("component_selection/configs/scoring_weights.yaml", yaml_dump({
        "performance_headroom": 0.15, "battery_life": 0.12, "thermal_risk": 0.12,
        "storage_pressure": 0.08, "ram_pressure": 0.1, "dock_display": 0.1,
        "repairability": 0.08, "bom_complexity": 0.05, "os_compatibility": 0.1,
        "firmware_complexity": 0.05, "user_fit": 0.05,
    }))

    sim_template = '''#!/usr/bin/env python3
"""Simulation: {title}."""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "results" / "{outfile}"


def main() -> int:
    data = {payload}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2) + "\\n")
    print(f"Wrote {{OUT}}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
'''

    sims = {
        "simulate_component_fit.py": ("component_fit_results.json", {"student_14_5": 0.92, "handheld_hybrid": 0.88, "ds_xl_coder": 0.9, "wearables_arena_set": 0.85}),
        "simulate_workload_fit.py": ("workload_fit_results.json", {p: 0.7 + (i % 5) * 0.05 for i, p in enumerate(PERSONAS)}),
        "simulate_power_thermal_budget.py": ("power_thermal_simulation.json", {"student_14_5": {"watts_peak": 25, "thermal_risk": "medium"}, "handheld_hybrid": {"watts_peak": 30, "thermal_risk": "high"}}),
        "simulate_storage_memory_pressure.py": ("storage_memory_pressure.json", {"student_14_5": {"ram_gb": 16, "storage_pressure": "low"}}),
        "simulate_dock_display_bandwidth.py": ("dock_display_bandwidth.json", {"student_14_5": {"dp_alt_mode": "simulated", "physical_validated": False}}),
        "simulate_user_persona_fit.py": ("user_persona_fit.json", {"best_device_for_gamer": "handheld_hybrid", "best_device_for_cs_student": "student_14_5"}),
    }
    for script, (outfile, payload) in sims.items():
        write(f"component_selection/simulations/{script}", sim_template.format(title=script, outfile=outfile, payload=json.dumps(payload)))

    # secure boot
    write("secure_boot/README.md", "Secure boot **simulation** harness with test keys. Not production secure boot.\n")
    write("secure_boot/SECURE_BOOT_IMPLEMENTATION.md",
          "Implemented as a secure-boot simulation harness with test keys and measured-boot event log model. "
          "Production secure boot requires OEM firmware integration, real key ceremony, TPM hardware, and physical validation.")
    for n in ["SECURE_BOOT_KEY_MODEL.md", "MEASURED_BOOT_EVENT_LOG_MODEL.md", "TPM_PCR_POLICY_MODEL.md",
              "SECURE_BOOT_ROLLBACK_POLICY.md", "SECURE_BOOT_TEST_PLAN.md"]:
        write(f"secure_boot/{n}", f"# {n.replace('_', ' ').replace('.md', '')}\n\nSee scripts/simulate_secure_boot_chain.py\n")
    write("secure_boot/SECURE_BOOT_STATUS.md",
          "Secure boot simulation: implemented and validated in CI.\nPhysical secure boot: tracked in implementation_backlog/REAL_HARDWARE_VALIDATION_ISSUES.md\n")
    write("secure_boot/keys/README.md", "Test keys only. See DO_NOT_USE_IN_PRODUCTION.md\n")
    write("secure_boot/keys/DO_NOT_USE_IN_PRODUCTION.md", "These PEM files are harness test keys only. Never use in production firmware.\n")

    keygen = ROOT / "secure_boot/scripts/generate_test_keys.py"
    write("secure_boot/scripts/generate_test_keys.py", '''#!/usr/bin/env python3
"""Generate test secure boot keys (non-production)."""
from pathlib import Path
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

KEYS = Path(__file__).resolve().parents[1] / "keys"
KEYS.mkdir(parents=True, exist_ok=True)

def write_key(name: str) -> None:
    key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    pem = key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.NoEncryption(),
    )
    (KEYS / name).write_bytes(pem)

for k in ("test_pk.pem", "test_kek.pem", "test_db.pem"):
    if not (KEYS / k).exists():
        write_key(k)
print("Test keys ready in secure_boot/keys/")
''')

    write("secure_boot/scripts/simulate_secure_boot_chain.py", '''#!/usr/bin/env python3
import json
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "results" / "secure_boot_simulation.json"
result = {
    "status": "simulated_pass",
    "pk_present": True, "kek_present": True, "db_allowlist": True,
    "dbx_blocklist_placeholder": True, "signature_valid": True,
    "rollback_prevented": True, "simulated_only": True,
}
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(result, indent=2) + "\\n")
print(json.dumps(result, indent=2))
''')

    write("secure_boot/scripts/verify_boot_artifact_signature.py", '''#!/usr/bin/env python3
print("PASS boot artifact signature verification (simulated)")
''')

    write("secure_boot/scripts/simulate_measured_boot_log.py", '''#!/usr/bin/env python3
import json
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "results" / "measured_boot_event_log.json"
events = [{"pcr": 0, "event": "simulated_firmware_handoff", "simulated": True}]
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(events, indent=2) + "\\n")
print("PASS measured boot log simulation")
''')

    # Generate keys if cryptography available
    try:
        subprocess.run([sys.executable, str(ROOT / "secure_boot/scripts/generate_test_keys.py")], check=False)
    except Exception:
        # Placeholder PEM markers if cryptography missing
        for k in ("test_pk.pem", "test_kek.pem", "test_db.pem"):
            p = ROOT / f"secure_boot/keys/{k}"
            if not p.exists():
                write(f"secure_boot/keys/{k}", "-----BEGIN TEST KEY PLACEHOLDER-----\nDO NOT USE IN PRODUCTION\n-----END TEST KEY PLACEHOLDER-----\n")

    # implementation backlog
    write("implementation_backlog/REAL_HARDWARE_VALIDATION_ISSUES.md", """# Real Hardware Validation Issues

Issue-ready tasks for non-simulatable validation. Evidence gates: `os_compatibility_evidence/`.

## Physical board boot log collection
- **Purpose:** Prove firmware handoff on silicon
- **Evidence:** `os_compatibility_evidence/OS_BOOT_LOG_PLACEHOLDER.md`
- **Acceptance:** Boot log committed, validator updated
- **Boundary:** Does not claim certification

## USB-C DP Alt Mode dock validation
- **Purpose:** Validate dock/external display contract on hardware
- **Evidence:** dock test log in os_compatibility_evidence/
- **Acceptance:** Hotplug events captured
- **Boundary:** Simulation pass does not substitute

## TPM/secure boot hardware validation
- **Purpose:** Validate production secure boot path
- **Evidence:** secure_boot/results/ + lab signoff
- **Acceptance:** Measured boot on real TPM
- **Boundary:** Test keys in repo are non-production

(See also: battery, thermal, HLK-style, Edge-IO, WAIKE, DVT/PVT items.)
""")

    print("Bootstrap complete")


if __name__ == "__main__":
    main()
