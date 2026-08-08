# ICD — DS-XL second display

Updated: 2026-08-08T01:15:00Z  
ADR: ADR-FP-003

## Panels
| ID | Role | Interface | Resolution class | Touch | Evidence |
|---|---|---|---|---|---|
| DISP_UPPER | Primary IDE/canvas | eDP0 from COM | 2560×1600 @13–14" | USB-HID / I2C | MODELED |
| DISP_LOWER | Secondary tools | eDP1 from COM or eDP bridge | 1920×1200 @13–14" | USB-HID / I2C | MODELED |

## Electrical
| Net / link | From | To | Notes |
|---|---|---|---|
| eDP0_TX[3:0]+CLK | COM | Upper panel FPC | Main panel |
| eDP1_TX[3:0]+CLK | COM or PS8625/LT8711-class bridge | Lower panel FPC | If COM exposes only one eDP, bridge from DP/USB4 |
| BL_EN / PWM | EC | each panel | Independent backlight
| TOUCH_USB / I2C | panels | COM/EC hub | Separate HID devices |
| HINGE_FLEX | upper carrier | lower lid PCB | Strain relief; ZIF dual |

## Software contract (must be real layouts)
Host compositor exposes two DRM connectors; gunnchOS layouts:
1. code / terminal
2. preview / profiler
3. lesson / lab
4. topology / packet analysis
5. 3D scene / properties
6. Archive world / scientific journal

## Non-claims
No measured hinge cycle life. No panel AVL PO. No CLI ERC/DRC.


Continuation VI: status token `DSXL_BLOCKED_NDA` — Option 3 public-engineerability gate.
