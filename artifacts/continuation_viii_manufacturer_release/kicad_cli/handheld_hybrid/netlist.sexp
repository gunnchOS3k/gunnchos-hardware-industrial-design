(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch")
		(date "2026-08-09T14:46:48")
		(tool "Eeschema 10.0.5")
		(textvar
			(name "EDMUND_ACTION_REQUIRED") "install_kicad_cli")
		(textvar
			(name "KICAD_CLI") "ABSENT")
		(sheet
			(number "1")
			(name "/")
			(tstamps "/")
			(title_block
				(title "Handheld Hybrid SoM Carrier — Cont VIII PUBLIC_PINOUT")
				(company "gunnchOS3k / CONTINUATION VIII")
				(rev "0.5.0-cont-viii")
				(date "2026-08-09")
				(source "handheld_hybrid.kicad_sch")
				(comment
					(number "1")
					(value "Functional multi-pin circuits with exact MPN properties")
				)
				(comment
					(number "2")
					(value "PHYSICAL_EXECUTION_FREEZE ACTIVE — DRAFT PR only")
				)
				(comment
					(number "3")
					(value "Compute MPN: RM121-D8E32")
				)
				(comment
					(number "4")
					(value "Engineerability: PUBLIC_PINOUT")
				)
				(comment
					(number "5")
					(value "")
				)
				(comment
					(number "6")
					(value "")
				)
				(comment
					(number "7")
					(value "")
				)
				(comment
					(number "8")
					(value "")
				)
				(comment
					(number "9")
					(value "")
				)
			)
		)
	)
	(components
		(comp
			(ref "C1")
			(value "CL05A104KA5NNNC")
			(footprint "gunnchos_functional:C_0402")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "CL05A104KA5NNNC")
				(field
					(name "Role") "DECAP")
				(field
					(name "Footprint") "gunnchos_functional:C_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "C")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "CL05A104KA5NNNC")
			)
			(property
				(name "Role")
				(value "DECAP")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "996ad7db-d38d-3fc0-244e-b26602ef4f7e")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "2")
						)
					)
				)
			)
		)
		(comp
			(ref "C2")
			(value "GRM188R60J106ME47D")
			(footprint "gunnchos_functional:C_0402")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "GRM188R60J106ME47D")
				(field
					(name "Role") "BULK")
				(field
					(name "Footprint") "gunnchos_functional:C_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "C")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "GRM188R60J106ME47D")
			)
			(property
				(name "Role")
				(value "BULK")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "a551f86f-b51e-89c0-faef-811984ed8fd2")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "2")
						)
					)
				)
			)
		)
		(comp
			(ref "D1")
			(value "APTD1608LCGCK")
			(footprint "gunnchos_functional:LED_0603")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "APTD1608LCGCK")
				(field
					(name "Role") "STATUS_LED")
				(field
					(name "Footprint") "gunnchos_functional:LED_0603")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "LED")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "APTD1608LCGCK")
			)
			(property
				(name "Role")
				(value "STATUS_LED")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "cfb3aa38-22a6-3e43-ee36-16d4c3364c93")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "2")
						)
					)
				)
			)
		)
		(comp
			(ref "DESD1")
			(value "PESD5V0S1UL")
			(footprint "gunnchos_functional:R_0402")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "PESD5V0S1UL")
				(field
					(name "Role") "ESD")
				(field
					(name "Footprint") "gunnchos_functional:R_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "C")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "PESD5V0S1UL")
			)
			(property
				(name "Role")
				(value "ESD")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "27314f45-8f2b-a5a3-2f63-7e969109ec75")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "2")
						)
					)
				)
			)
		)
		(comp
			(ref "JSOM1")
			(value "SODIMM-260")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "SODIMM-260")
				(field
					(name "Role") "SOM_SOCKET")
				(field
					(name "Evidence") "PUBLIC_PINOUT")
				(field
					(name "Footprint") "gunnchos_functional:Block_SMD_safe")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "SODIMM260")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "SODIMM-260")
			)
			(property
				(name "Role")
				(value "SOM_SOCKET")
			)
			(property
				(name "Evidence")
				(value "PUBLIC_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "d6da0211-a331-e7e8-39c1-a705a1d1577c")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "251")
						)
						(pin
							(num "1")
						)
						(pin
							(num "111")
						)
						(pin
							(num "238")
						)
						(pin
							(num "187")
						)
						(pin
							(num "126")
						)
						(pin
							(num "65")
						)
						(pin
							(num "227")
						)
						(pin
							(num "252")
						)
						(pin
							(num "109")
						)
						(pin
							(num "236")
						)
						(pin
							(num "185")
						)
						(pin
							(num "220")
						)
						(pin
							(num "63")
						)
						(pin
							(num "219")
						)
						(pin
							(num "229")
						)
					)
				)
			)
		)
		(comp
			(ref "JUSB1")
			(value "TYPE-C-31-M-12")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "HRO TYPE-C-31-M-12")
				(field
					(name "Role") "USB_C")
				(field
					(name "Footprint") "gunnchos_functional:Block_SMD_safe")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "USB_C")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "HRO TYPE-C-31-M-12")
			)
			(property
				(name "Role")
				(value "USB_C")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "bda24c56-421a-31cb-edb6-39b3cc0298aa")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "A1")
						)
						(pin
							(num "A5")
						)
						(pin
							(num "A7")
						)
						(pin
							(num "A4")
						)
						(pin
							(num "A6")
						)
						(pin
							(num "B5")
						)
					)
				)
			)
		)
		(comp
			(ref "R1")
			(value "RC0402FR-0710KL")
			(footprint "gunnchos_functional:R_0402")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "RC0402FR-0710KL")
				(field
					(name "Role") "PULLUP")
				(field
					(name "Footprint") "gunnchos_functional:R_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "R")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "RC0402FR-0710KL")
			)
			(property
				(name "Role")
				(value "PULLUP")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "c132b0c9-7f1a-1e0b-2368-0b50ae80e76f")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "2")
						)
					)
				)
			)
		)
		(comp
			(ref "R2")
			(value "RC0402FR-071K0L")
			(footprint "gunnchos_functional:R_0402")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "RC0402FR-071K0L")
				(field
					(name "Role") "LED_R")
				(field
					(name "Footprint") "gunnchos_functional:R_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "R")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "RC0402FR-071K0L")
			)
			(property
				(name "Role")
				(value "LED_R")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "86a63b4d-220b-e913-3001-4852e7fc290f")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "2")
						)
					)
				)
			)
		)
		(comp
			(ref "U3V3")
			(value "TPS62864")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "TPS62864")
				(field
					(name "Role") "BUCK_3V3")
				(field
					(name "Footprint") "gunnchos_functional:Block_SMD_safe")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "BUCK")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "TPS62864")
			)
			(property
				(name "Role")
				(value "BUCK_3V3")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "0962ce93-d041-0653-da95-a1ea4ed4c7d5")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "3")
						)
						(pin
							(num "2")
						)
						(pin
							(num "4")
						)
					)
				)
			)
		)
		(comp
			(ref "UCHG1")
			(value "BQ25895RTWR")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "BQ25895RTWR")
				(field
					(name "Role") "CHARGER")
				(field
					(name "Footprint") "gunnchos_functional:Block_SMD_safe")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "CHARGER")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "BQ25895RTWR")
			)
			(property
				(name "Role")
				(value "CHARGER")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "9b99baba-b507-f709-8fdf-6524a957ae9d")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "3")
						)
						(pin
							(num "5")
						)
						(pin
							(num "2")
						)
						(pin
							(num "4")
						)
						(pin
							(num "6")
						)
					)
				)
			)
		)
		(comp
			(ref "UHID1")
			(value "STM32F103C8T6")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "STM32F103C8T6")
				(field
					(name "Role") "HID_MCU")
				(field
					(name "Footprint") "gunnchos_functional:Block_SMD_safe")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "HID_MCU")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "STM32F103C8T6")
			)
			(property
				(name "Role")
				(value "HID_MCU")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "b7a5d672-98de-ef16-181e-55d9bde5fefb")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "3")
						)
						(pin
							(num "5")
						)
						(pin
							(num "2")
						)
						(pin
							(num "4")
						)
						(pin
							(num "6")
						)
					)
				)
			)
		)
		(comp
			(ref "UPD1")
			(value "TPS65987DDHRSHR")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "TPS65987DDHRSHR")
				(field
					(name "Role") "PD")
				(field
					(name "Footprint") "gunnchos_functional:Block_SMD_safe")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "PD_CTRL")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "TPS65987DDHRSHR")
			)
			(property
				(name "Role")
				(value "PD")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "81860b31-2ebb-570b-c87e-4e00b6bff405")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "1")
						)
						(pin
							(num "3")
						)
						(pin
							(num "5")
						)
						(pin
							(num "7")
						)
						(pin
							(num "2")
						)
						(pin
							(num "4")
						)
						(pin
							(num "6")
						)
						(pin
							(num "8")
						)
					)
				)
			)
		)
	)
	(groups)
	(variants)
	(libparts
		(libpart
			(lib "")
			(part "BUCK")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "BUCK")
				(field
					(name "Footprint")
				)
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "VIN")
					(type "passive")
				)
				(pin
					(num "2")
					(name "EN")
					(type "passive")
				)
				(pin
					(num "3")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "4")
					(name "VOUT")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "C")
			(fields
				(field
					(name "Reference") "C")
				(field
					(name "Value") "C")
				(field
					(name "Footprint") "gunnchos_functional:C_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "")
					(type "passive")
				)
				(pin
					(num "2")
					(name "")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "CHARGER")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "CHARGER")
				(field
					(name "Footprint")
				)
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "VBUS")
					(type "passive")
				)
				(pin
					(num "2")
					(name "SYS")
					(type "passive")
				)
				(pin
					(num "3")
					(name "BAT")
					(type "passive")
				)
				(pin
					(num "4")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "5")
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "6")
					(name "SDA")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "HID_MCU")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "HID_MCU")
				(field
					(name "Footprint")
				)
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "VDD")
					(type "passive")
				)
				(pin
					(num "2")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "3")
					(name "USB_DP")
					(type "passive")
				)
				(pin
					(num "4")
					(name "USB_DM")
					(type "passive")
				)
				(pin
					(num "5")
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "6")
					(name "SDA")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "LED")
			(fields
				(field
					(name "Reference") "D")
				(field
					(name "Value") "LED")
				(field
					(name "Footprint") "gunnchos_functional:LED_0603")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "K")
					(type "passive")
				)
				(pin
					(num "2")
					(name "A")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "PD_CTRL")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "PD_CTRL")
				(field
					(name "Footprint")
				)
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "VBUS")
					(type "passive")
				)
				(pin
					(num "2")
					(name "CC1")
					(type "passive")
				)
				(pin
					(num "3")
					(name "CC2")
					(type "passive")
				)
				(pin
					(num "4")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "5")
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "6")
					(name "SDA")
					(type "passive")
				)
				(pin
					(num "7")
					(name "VSYS")
					(type "passive")
				)
				(pin
					(num "8")
					(name "3V3")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "R")
			(fields
				(field
					(name "Reference") "R")
				(field
					(name "Value") "R")
				(field
					(name "Footprint") "gunnchos_functional:R_0402")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "")
					(type "passive")
				)
				(pin
					(num "2")
					(name "")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "SODIMM260")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "SODIMM260")
				(field
					(name "Footprint")
				)
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "1")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "63")
					(name "HDMI0_TX2N")
					(type "passive")
				)
				(pin
					(num "65")
					(name "HDMI0_TX2P")
					(type "passive")
				)
				(pin
					(num "109")
					(name "USB20_HOST0_DM")
					(type "passive")
				)
				(pin
					(num "111")
					(name "USB20_HOST0_DP")
					(type "passive")
				)
				(pin
					(num "126")
					(name "LCD_RESET_L")
					(type "passive")
				)
				(pin
					(num "185")
					(name "I2C0_SCL")
					(type "passive")
				)
				(pin
					(num "187")
					(name "I2C0_SDA")
					(type "passive")
				)
				(pin
					(num "219")
					(name "SDMMC_D0")
					(type "passive")
				)
				(pin
					(num "220")
					(name "LCD_BL_PWM")
					(type "passive")
				)
				(pin
					(num "227")
					(name "SDMMC_CMD")
					(type "passive")
				)
				(pin
					(num "229")
					(name "SDMMC_CLK")
					(type "passive")
				)
				(pin
					(num "236")
					(name "UART2_TX")
					(type "passive")
				)
				(pin
					(num "238")
					(name "UART2_RX")
					(type "passive")
				)
				(pin
					(num "251")
					(name "VCC_SYSIN")
					(type "passive")
				)
				(pin
					(num "252")
					(name "VCC_SYSIN2")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "USB_C")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "USB_C")
				(field
					(name "Footprint")
				)
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(pins
				(pin
					(num "A1")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "A4")
					(name "VBUS")
					(type "passive")
				)
				(pin
					(num "A5")
					(name "CC1")
					(type "passive")
				)
				(pin
					(num "A6")
					(name "DP")
					(type "passive")
				)
				(pin
					(num "A7")
					(name "DM")
					(type "passive")
				)
				(pin
					(num "B5")
					(name "CC2")
					(type "passive")
				)
			)
		)
	)
	(libraries)
	(nets
		(net
			(code "1")
			(name "CC1")
			(class "Default")
			(node
				(ref "DESD1")
				(pin "1")
				(pintype "passive")
			)
			(node
				(ref "JUSB1")
				(pin "A5")
				(pinfunction "CC1_A5")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "8")
				(pinfunction "3V3_8")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "GND")
			(class "Default")
			(node
				(ref "C1")
				(pin "2")
				(pintype "passive")
			)
			(node
				(ref "C2")
				(pin "2")
				(pintype "passive")
			)
			(node
				(ref "D1")
				(pin "1")
				(pinfunction "K_1")
				(pintype "passive")
			)
			(node
				(ref "DESD1")
				(pin "2")
				(pintype "passive")
			)
			(node
				(ref "JSOM1")
				(pin "65")
				(pinfunction "HDMI0_TX2P_65")
				(pintype "passive")
			)
			(node
				(ref "JUSB1")
				(pin "A7")
				(pinfunction "DM_A7")
				(pintype "passive")
			)
			(node
				(ref "U3V3")
				(pin "1")
				(pinfunction "VIN_1")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "4")
				(pinfunction "GND_4")
				(pintype "passive")
			)
			(node
				(ref "UHID1")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "I2C_SCL")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "220")
				(pinfunction "LCD_BL_PWM_220")
				(pintype "passive")
			)
			(node
				(ref "R1")
				(pin "2")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "1")
				(pinfunction "VBUS_1")
				(pintype "passive")
			)
			(node
				(ref "UHID1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "3")
				(pinfunction "CC2_3")
				(pintype "passive")
			)
		)
		(net
			(code "4")
			(name "I2C_SDA")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "238")
				(pinfunction "UART2_RX_238")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "2")
				(pinfunction "SYS_2")
				(pintype "passive")
			)
			(node
				(ref "UHID1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "4")
				(pinfunction "GND_4")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "LCD_BL_PWM")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "185")
				(pinfunction "I2C0_SCL_185")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "LED_A")
			(class "Default")
			(node
				(ref "D1")
				(pin "2")
				(pinfunction "A_2")
				(pintype "passive")
			)
			(node
				(ref "R2")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "SOM_VIN")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "227")
				(pinfunction "SDMMC_CMD_227")
				(pintype "passive")
			)
		)
		(net
			(code "8")
			(name "UART_RX")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "187")
				(pinfunction "I2C0_SDA_187")
				(pintype "passive")
			)
		)
		(net
			(code "9")
			(name "UART_TX")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "63")
				(pinfunction "HDMI0_TX2N_63")
				(pintype "passive")
			)
		)
		(net
			(code "10")
			(name "USB_DM")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "219")
				(pinfunction "SDMMC_D0_219")
				(pintype "passive")
			)
			(node
				(ref "UHID1")
				(pin "4")
				(pinfunction "USB_DM_4")
				(pintype "passive")
			)
		)
		(net
			(code "11")
			(name "USB_DP")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "126")
				(pinfunction "LCD_RESET_L_126")
				(pintype "passive")
			)
			(node
				(ref "UHID1")
				(pin "3")
				(pinfunction "USB_DP_3")
				(pintype "passive")
			)
		)
		(net
			(code "12")
			(name "VBAT")
			(class "Default")
			(node
				(ref "UCHG1")
				(pin "3")
				(pinfunction "BAT_3")
				(pintype "passive")
			)
		)
		(net
			(code "13")
			(name "VBUS")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "B5")
				(pinfunction "CC2_B5")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "5")
				(pinfunction "SCL_5")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "7")
				(pinfunction "VSYS_7")
				(pintype "passive")
			)
		)
		(net
			(code "14")
			(name "VDD_3V3")
			(class "Default")
			(node
				(ref "C1")
				(pin "1")
				(pintype "passive")
			)
			(node
				(ref "R1")
				(pin "1")
				(pintype "passive")
			)
			(node
				(ref "R2")
				(pin "1")
				(pintype "passive")
			)
			(node
				(ref "U3V3")
				(pin "2")
				(pinfunction "EN_2")
				(pintype "passive")
			)
			(node
				(ref "U3V3")
				(pin "4")
				(pinfunction "VOUT_4")
				(pintype "passive")
			)
			(node
				(ref "UHID1")
				(pin "5")
				(pinfunction "SCL_5")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "2")
				(pinfunction "CC1_2")
				(pintype "passive")
			)
		)
		(net
			(code "15")
			(name "VSYS")
			(class "Default")
			(node
				(ref "C2")
				(pin "1")
				(pintype "passive")
			)
			(node
				(ref "U3V3")
				(pin "3")
				(pinfunction "GND_3")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "1")
				(pinfunction "VBUS_1")
				(pintype "passive")
			)
		)
		(net
			(code "16")
			(name "unconnected-(JSOM1-GND-Pad1)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "1")
				(pinfunction "GND_1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "17")
			(name "unconnected-(JSOM1-SDMMC_CLK-Pad229)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "229")
				(pinfunction "SDMMC_CLK_229")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "18")
			(name "unconnected-(JSOM1-UART2_TX-Pad236)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "236")
				(pinfunction "UART2_TX_236")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "19")
			(name "unconnected-(JSOM1-USB20_HOST0_DM-Pad109)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "109")
				(pinfunction "USB20_HOST0_DM_109")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "20")
			(name "unconnected-(JSOM1-USB20_HOST0_DP-Pad111)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "111")
				(pinfunction "USB20_HOST0_DP_111")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "21")
			(name "unconnected-(JSOM1-VCC_SYSIN-Pad251)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "251")
				(pinfunction "VCC_SYSIN_251")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "22")
			(name "unconnected-(JSOM1-VCC_SYSIN2-Pad252)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "252")
				(pinfunction "VCC_SYSIN2_252")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "23")
			(name "unconnected-(JUSB1-DP-PadA6)")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "A6")
				(pinfunction "DP_A6")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "24")
			(name "unconnected-(JUSB1-GND-PadA1)")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "A1")
				(pinfunction "GND_A1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "25")
			(name "unconnected-(JUSB1-VBUS-PadA4)")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "A4")
				(pinfunction "VBUS_A4")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "26")
			(name "unconnected-(UPD1-SCL-Pad5)")
			(class "Default")
			(node
				(ref "UPD1")
				(pin "5")
				(pinfunction "SCL_5")
				(pintype "passive+no_connect")
			)
		)
	)
)
