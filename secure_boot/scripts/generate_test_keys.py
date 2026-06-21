#!/usr/bin/env python3
"""Generate test secure boot keys (non-production) — openssl or placeholder fallback."""
import subprocess
from pathlib import Path

KEYS = Path(__file__).resolve().parents[1] / "keys"
KEYS.mkdir(parents=True, exist_ok=True)


def gen(name: str) -> None:
    path = KEYS / name
    if path.exists():
        return
    if subprocess.run(["openssl", "genrsa", "-out", str(path), "2048"], capture_output=True).returncode == 0:
        print(f"Generated {name} via openssl")
        return
    path.write_text(
        "-----BEGIN TEST KEY PLACEHOLDER-----\n"
        "DO NOT USE IN PRODUCTION — harness simulation only\n"
        "-----END TEST KEY PLACEHOLDER-----\n"
    )
    print(f"Wrote placeholder {name}")


for k in ("test_pk.pem", "test_kek.pem", "test_db.pem"):
    gen(k)
print("Test keys ready in secure_boot/keys/")
