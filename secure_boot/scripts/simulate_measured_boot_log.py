#!/usr/bin/env python3
import json
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "results" / "measured_boot_event_log.json"
events = [{"pcr": 0, "event": "simulated_firmware_handoff", "simulated": True}]
OUT.parent.mkdir(parents=True, exist_ok=True)
OUT.write_text(json.dumps(events, indent=2) + "\n")
print("PASS measured boot log simulation")
