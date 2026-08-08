# COM-HPC / NX5 feasibility — pinout & power evidence classes

Updated: 2026-08-08T20:15:00Z  
Rule: **no invented nets**. Every ICD net must carry an evidence class.

## Evidence classes

| Class | Meaning | Allowed use |
|---|---|---|
| `PUBLIC_DOCS` | Published vendor wiki/PDF/XLSX | Freeze power rails, high-level I/O groups, mechanical |
| `PUBLIC_PINOUT` | Vendor pinout table with pin numbers | Carrier schematic nets for those pins |
| `NARROW_NDA` | PICMG / ADLINK carrier design guide / Intel USB4 PDK | Full COM-HPC Mini connector pin map; controller package fanout |
| `MODELED` | Engineering assumption pending PUBLIC_PINOUT or NDA | Power budgets, keep-outs, placeholder hierarchical sheets |
| `FORBIDDEN` | Invented ball maps / guessed differential pairs | Never commit as truth |

## ADLINK COM-HPC-mMTL (Student / DS-XL)

| Topic | Class | Notes |
|---|---|---|
| Module MPN / CPU / memory SKU | PUBLIC_DOCS | iPi ModuleIntroduction ordering table |
| Vin 8–20V / AT 12V±5% | PUBLIC_DOCS | Power section |
| USB4 / eDP / PCIe / I226 feature groups | PUBLIC_DOCS | Counts + mux notes only |
| Mechanical 95×70 + heatspreader HTS-mMTL-B | PUBLIC_DOCS | |
| **Full 400-pin COM-HPC Mini net-by-net** | **NARROW_NDA** | PICMG COM-HPC + ADLINK carrier design kit — **not** in public wiki |
| Exact mating connector MPN | NARROW_NDA or AVL quote | Pending ADLINK channel |

**Feasibility:** Carrier architecture is feasible on PUBLIC_DOCS feature groups + MODELED power tree. **Fabrication of a production carrier requires NARROW_NDA pinout** — do not invent pin numbers.

ICD: `device_designs/student_14_5/docs/com_carrier_icd.md` (evidence column must stay honest).

## Radxa NX5 RM121-D8E32 (Handheld)

| Topic | Class | Notes |
|---|---|---|
| SKU RM121-D8E32 | PUBLIC_DOCS | Product brief Rev 1.1 |
| 5V input, SODIMM-260, I/O feature groups | PUBLIC_DOCS | Brief §3 |
| **Pin-by-pin SODIMM map** | **PUBLIC_PINOUT** | `radxa_nx5_260_pinout_v1100.xlsx` / `radxa_nx5_pinout_v1.1.xlsx` at https://dl.radxa.com/nx5/ |
| Module schematic | PUBLIC_DOCS | `radxa_nx5_schematic_v1100.pdf` |
| 3D STEP | PUBLIC_DOCS (binary) | `radxa_nx5_v1.1_3d_stp.zip` — import into CAD; do not re-draw as invented |
| Bare RK3588S BGA fanout | FORBIDDEN | SoM only |

**Feasibility:** Handheld game carrier can proceed to real schematic nets from **public pinout** without NDA. Mux notes (USB3/PCIe/SATA) must follow Radxa pinout rows — no invented remux.

ICD: `device_designs/handheld_hybrid/docs/som_carrier_icd.md`.

## Token
`COM_HPC_NX5_FEASIBILITY_PINOUT_CLASSIFIED`
