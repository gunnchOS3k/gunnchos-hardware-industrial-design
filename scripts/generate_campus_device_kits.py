#!/usr/bin/env python3
import csv, json, sys
from pathlib import Path
import yaml
cfg = Path(__file__).resolve().parents[1] / "configs" / "campus_device_kits"
out = Path("results/campus_device_kits")
out.mkdir(parents=True, exist_ok=True)
for p in sorted(cfg.glob("*.yaml")):
    data = yaml.safe_load(p.read_text(encoding="utf-8"))
    sid = data["site_id"]
    (out / f"{sid}_device_kit.md").write_text(f"# Kit — {sid}\n\n{data['kit_name']}\n", encoding="utf-8")
    with (out / f"{sid}_bom_targets.csv").open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["device", "tier"])
        for d in data["device_mix"]:
            w.writerow([d, data["community_baseline_tier"]])
    (out / f"{sid}_adoption_risks.md").write_text(
        "# Risks\n\n" + "\n".join(f"- {r}" for r in data["logistics_risks"]) + "\n\nNot manufacturing ready.\n",
        encoding="utf-8",
    )
print("Wrote campus device kits")
