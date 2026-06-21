#!/usr/bin/env python3
"""Validate component selection package and simulation outputs."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "component_selection/README.md",
    "component_selection/RECOMMENDED_COMPONENT_STACKS.md",
    "component_selection/configs/component_candidates.yaml",
    "component_selection/simulations/simulate_component_fit.py",
    "component_selection/results/component_fit_results.json",
]


def main() -> int:
    missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        # auto-run simulations
        sim = ROOT / "component_selection/simulations/simulate_component_fit.py"
        if sim.exists():
            import subprocess
            for s in (ROOT / "component_selection/simulations").glob("simulate_*.py"):
                subprocess.run([sys.executable, str(s)], cwd=ROOT, check=False)
        missing = [f for f in REQUIRED if not (ROOT / f).exists()]
    if missing:
        print("FAIL missing component selection files:", missing)
        return 1
    print("PASS component selection validation")
    return 0


if __name__ == "__main__":
    sys.exit(main())
