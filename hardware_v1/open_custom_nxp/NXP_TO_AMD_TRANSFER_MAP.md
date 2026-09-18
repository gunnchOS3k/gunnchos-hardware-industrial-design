# NXP → AMD transfer map (updated NXP-1)

**Generated:** 2026-09-18T19:19:08Z

| Topic | Transfers to AMD custom | Does NOT transfer | Revalidation needed |
|---|---|---|---|
| Schematic sheet organization | Yes — hierarchical SoC/PMIC/DDR/HS/debug | Vendor net names | Yes |
| PMIC sequencing discipline | Yes — BBSM-first mindset | PF09 OTP map | Yes on AMD rails |
| DDR workflow | Yes — freeze topology before lengths | LPDDR5 rules | Yes (DDR5/LPDDR AMD) |
| Ballmap→symbol generator pattern | Yes | i.MX balls | Yes |
| BGA escape / stackup thinking | Yes | Exact stackup | Yes with AMD SI |
| SI/PI honesty gates | Yes | NXP IBIS | Yes |
| EC / DFT / bring-up scripts | Highly transferable | — | Light |
| Manufacturing outputs discipline | Yes | Gerbers themselves | Yes |

Do not copy vendor-specific nets/rules into AMD product mainline.
