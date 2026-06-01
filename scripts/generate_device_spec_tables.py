#!/usr/bin/env python3
from pathlib import Path

def main():
    e2e = Path("results/e2e")
    e2e.mkdir(parents=True, exist_ok=True)
    lines = ["# Device spec summary", ""]
    for d in sorted(Path("devices").glob("*")):
        if d.is_dir():
            lines.append(f"- **{d.name}**: see devices/{d.name}/README.md")
    (e2e / "device_spec_summary.md").write_text("\n".join(lines) + "\n")
    print("Wrote device_spec_summary.md")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
