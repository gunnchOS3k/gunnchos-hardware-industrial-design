#!/usr/bin/env python3
from pathlib import Path
out = Path("results/tool_exports/validation_toolchain_matrix.md")
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("| Tool | Role | Required? |\n|------|------|-----------|\n| Open source smoke | CI | Yes |\n| R&S/Keysight | Lab RF | No |\n", encoding="utf-8")
