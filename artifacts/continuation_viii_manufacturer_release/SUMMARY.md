# Continuation VIII — Manufacturer release packages

Updated: 2026-08-09T19:46:44Z  
Branch: `continuation-viii/manufacturer-release-packages`  
Base: `c5b6afd6a792d367593867fc7533f413a5146db4`

## Architecture decision
**OPTION_B_KEEP_ADLINK_ACCEPT_NARROW_EXTERNAL_BLOCK** (Option B)

## ERC/DRC
| Product | ERC errors | DRC errors | Gerbers | STEP bytes |
|---|---:|---:|---:|---:|
| handheld_hybrid | 0 | 0 | 19 | 14828 |
| edge_io_rings | 0 | 0 | 19 | 14776 |
| dock | 0 | 0 | 19 | 14806 |
| student_14_5 | 0 | 0 | 19 | 14822 |
| ds_xl_coder | 0 | 0 | 19 | 14820 |

## Readiness tokens (honest)
- `handheld_hybrid`: manufacturer_ready=conditional, adopter_ready=limited, reproducible_ready=limited, EDA_CLEAN=True
- `edge_io_rings`: manufacturer_ready=conditional, adopter_ready=limited, reproducible_ready=limited, EDA_CLEAN=True
- `dock`: manufacturer_ready=conditional, adopter_ready=limited, reproducible_ready=limited, EDA_CLEAN=True
- `student_14_5`: manufacturer_ready=conditional, adopter_ready=limited, reproducible_ready=limited, EDA_CLEAN=True
- `ds_xl_coder`: manufacturer_ready=conditional, adopter_ready=limited, reproducible_ready=limited, EDA_CLEAN=True
