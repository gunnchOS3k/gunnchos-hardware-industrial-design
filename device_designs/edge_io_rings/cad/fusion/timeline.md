# Fusion timeline recipe — Edge I/O Ring

Updated: 2026-08-08T19:40:00Z

1. New Design → units mm
2. Create parameters from `parameters.yaml`
3. Revolve band profile (ellipse/rounded rect) for each size configuration (Design Configuration / Derive)
4. Shell to `band_thickness_mm`
5. Extrude-cut PCB pocket on inner dorsal face
6. Cut pogo contact wells (Mill-Max class)
7. Split faces for antenna keep-out painting
8. Derive PCB outline STEP from KiCad (when CLI export available)
9. Interference check PCB vs pocket
10. Export STEP/STL per `export_manifest.yaml`

Binary `.f3d` not authored in this environment — see `EDMUND_ACTION_REQUIRED.md`.
