# CPB0 debug plan

**Generated:** 2026-09-18T16:48:54Z  
**Campaign:** `HARDWARE_1_0C_CUSTOM_FIRST_MAINLINE_PIVOT`  
**Claim boundary:** digital architecture / EVT preparation only — not physical pass, not certification, not fab release, not purchased.


## Required debug affordances

- UART console, JTAG/SWD where applicable
- POST/debug LEDs, board-revision straps
- recovery switch + firmware recovery header
- rail test points + current sensing
- external bench power + battery emulator input
- thermistor headers

`CUSTOM_DEBUG_ARCHITECTURE_UNDERSTOOD=false` until vendor debug tool requirements are acquired.
