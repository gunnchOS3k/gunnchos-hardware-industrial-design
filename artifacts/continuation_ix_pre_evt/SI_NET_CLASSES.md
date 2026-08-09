# SI net classes / rules — Cont IX (design intent; no SI simulation)

| Class | Zdiff target | Width/gap intent | Boards |
|---|---|---|---|
| USB2 | 90 Ω | 0.20 / 0.20 mm | all |
| USB3 / USB4 / TB4 | 85–90 Ω | 0.15 / 0.15 mm | handheld, dock, student, ds_xl |
| PCIe | 85 Ω | 0.15 / 0.15 mm | student, ds_xl, handheld |
| eDP | 100 Ω | 0.10 / 0.10 mm | student, ds_xl |
| Ethernet | 100 Ω | 0.20 / 0.20 mm | dock, student, ds_xl |
| MIPI | 100 Ω | 0.10 / 0.10 mm | handheld |

Encoded on PCB Dwgs.User + manufacturing/impedance_note.md + stackup.yaml.
**No SI simulation claimed.**
