#!/usr/bin/env python3
"""Log UART console to file. No hardware assumed present."""
from __future__ import annotations
import argparse
import sys
from pathlib import Path

def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--port")
    ap.add_argument("--out", default="logs/console.log")
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()
    Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    if args.dry_run or not args.port:
        Path(args.out).write_text("# dry-run: no serial opened\n", encoding="utf-8")
        print("dry-run ok")
        return 0
    try:
        import serial  # noqa: F401
    except ImportError:
        print("pyserial not installed; use --dry-run", file=sys.stderr)
        return 2
    print("physical serial path not executed in digital campaign")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
