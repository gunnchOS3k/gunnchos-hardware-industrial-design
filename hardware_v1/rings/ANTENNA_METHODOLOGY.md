# Antenna methodology

**Generated:** 2026-09-18T18:37:46Z
**Campaign:** `STREAM_E_DIGITAL_HARDWARE_ENGINEERING_EXHAUSTION`
**Claim boundary:** digital engineering exhaustion under public collateral + local EDA only — not physical pass, not certification, not fab release, not purchased, not GXE execution, no invented NDA pin maps.


1. Start from Nordic PCA10156 DK RF reference (hashed zip in package strategy).
2. Place chip antenna (`Johanson 2450AT18A100` class) with vendor keep-outs.
3. Matching network = placeholder pi (R/C positions on schematic) until VNA tune.
4. Do **not** claim conducted/radiated pass from digital work alone.

Pending physical: antenna tuning, hand-effect, enclosure dielectric, battery life.
