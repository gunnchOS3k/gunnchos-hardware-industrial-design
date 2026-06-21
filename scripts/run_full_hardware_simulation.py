#!/usr/bin/env python3
"""Run full hardware simulation pipeline."""
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STEPS = [
    ["component_selection/simulations/simulate_component_fit.py"],
    ["component_selection/simulations/simulate_workload_fit.py"],
    ["component_selection/simulations/simulate_power_thermal_budget.py"],
    ["component_selection/simulations/simulate_storage_memory_pressure.py"],
    ["component_selection/simulations/simulate_dock_display_bandwidth.py"],
    ["component_selection/simulations/simulate_user_persona_fit.py"],
    ["secure_boot/scripts/simulate_secure_boot_chain.py"],
    ["secure_boot/scripts/simulate_measured_boot_log.py"],
    ["scripts/run_firmware_compat_smoke.py"],
]


def main() -> int:
    for step in STEPS:
        r = subprocess.run([sys.executable, *step], cwd=ROOT)
        if r.returncode != 0:
            print(f"FAIL full simulation step: {' '.join(step)}")
            return 1
    print("PASS full hardware simulation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
