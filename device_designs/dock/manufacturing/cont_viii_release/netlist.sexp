(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/dock/kicad/dock.kicad_sch")
		(date "2026-08-09T14:46:55")
		(tool "Eeschema 10.0.5")
		(textvar
			(name "EDMUND_ACTION_REQUIRED") "install_kicad_cli")
		(textvar
			(name "KICAD_CLI") "ABSENT")
		(textvar
			(name "PACKAGE") "DOCK_PCB_DIGITAL_BEYOND_SKELETON")
		(sheet
			(number "1")
			(name "/")
			(tstamps "/")
			(title_block
				(title "Dock Main PCB — USB4/TB4 Cont VIII")
				(company "gunnchOS3k / CONTINUATION VIII")
				(rev "0.5.0-cont-viii")
				(date "2026-08-09")
				(source "dock.kicad_sch")
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
					(value "Compute MPN: JHL8440")
				)
				(comment
					(number "4")
					(value "Engineerability: ROLE_PUBLIC_PACKAGE_NDA")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
			(ref "JUSB2")
			(value "TYPE-C-31-M-12")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "HRO TYPE-C-31-M-12")
				(field
					(name "Role") "USB_C_DN")
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
				(value "USB_C_DN")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "b3e5e0e9-b53d-a63e-95d6-4880dc23466a")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
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
			(value "BQ25792RQMR")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "BQ25792RQMR")
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
				(value "BQ25792RQMR")
			)
			(property
				(name "Role")
				(value "CHARGER")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "8d1f40de-a956-7e58-8a7a-44d6430216b0")
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
			(ref "UETH1")
			(value "RTL8156")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "RTL8156")
				(field
					(name "Role") "ETHERNET")
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
				(part "RTL8156")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "RTL8156")
			)
			(property
				(name "Role")
				(value "ETHERNET")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "dfc08ffb-139e-7cc5-ae25-dfb503b7ef0e")
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
		(comp
			(ref "UHUB1")
			(value "VL817")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "VL817")
				(field
					(name "Role") "USB_HUB")
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
				(part "VL817")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "VL817")
			)
			(property
				(name "Role")
				(value "USB_HUB")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "05af4d55-c80f-105b-c788-a11fb0e8ae8b")
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
			(value "TPS65994ADFBRQ1")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "TPS65994ADFBRQ1")
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
				(value "TPS65994ADFBRQ1")
			)
			(property
				(name "Role")
				(value "PD")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "8a5a19bd-73ca-490f-abaa-1595d58c26a9")
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
		(comp
			(ref "UUSB4")
			(value "JHL8440")
			(footprint "gunnchos_functional:Block_SMD_safe")
			(fields
				(field
					(name "ContVIII") "FUNCTIONAL")
				(field
					(name "MPN") "JHL8440")
				(field
					(name "Role") "USB4_CTRL")
				(field
					(name "Evidence") "ROLE_PUBLIC")
				(field
					(name "NDA") "PACKAGE_BALL_MAP")
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
				(part "JHL8440_ROLE")
				(description "")
			)
			(property
				(name "ContVIII")
				(value "FUNCTIONAL")
			)
			(property
				(name "MPN")
				(value "JHL8440")
			)
			(property
				(name "Role")
				(value "USB4_CTRL")
			)
			(property
				(name "Evidence")
				(value "ROLE_PUBLIC")
			)
			(property
				(name "NDA")
				(value "PACKAGE_BALL_MAP")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "100ac6f0-6a4d-7487-ad2a-639b09883665")
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
							(num "9")
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
			(part "JHL8440_ROLE")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "JHL8440_ROLE")
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
					(name "USB4_UP_RX")
					(type "passive")
				)
				(pin
					(num "4")
					(name "USB4_UP_TX")
					(type "passive")
				)
				(pin
					(num "5")
					(name "DP_OUT")
					(type "passive")
				)
				(pin
					(num "6")
					(name "PCIE_DN")
					(type "passive")
				)
				(pin
					(num "7")
					(name "I2C_SCL")
					(type "passive")
				)
				(pin
					(num "8")
					(name "I2C_SDA")
					(type "passive")
				)
				(pin
					(num "9")
					(name "NOTE_NDA")
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
			(part "RTL8156")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "RTL8156")
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
					(name "VDD33")
					(type "passive")
				)
				(pin
					(num "2")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "3")
					(name "USB_D+")
					(type "passive")
				)
				(pin
					(num "4")
					(name "USB_D-")
					(type "passive")
				)
				(pin
					(num "5")
					(name "TD+")
					(type "passive")
				)
				(pin
					(num "6")
					(name "TD-")
					(type "passive")
				)
				(pin
					(num "7")
					(name "RD+")
					(type "passive")
				)
				(pin
					(num "8")
					(name "RD-")
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
		(libpart
			(lib "")
			(part "VL817")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "VL817")
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
					(name "UP_DP")
					(type "passive")
				)
				(pin
					(num "4")
					(name "UP_DM")
					(type "passive")
				)
				(pin
					(num "5")
					(name "DN1_DP")
					(type "passive")
				)
				(pin
					(num "6")
					(name "DN1_DM")
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
			(name "ETH_TD_N")
			(class "Default")
			(node
				(ref "UETH1")
				(pin "4")
				(pinfunction "USB_D-_4")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "ETH_TD_P")
			(class "Default")
			(node
				(ref "UETH1")
				(pin "3")
				(pinfunction "USB_D+_3")
				(pintype "passive")
			)
		)
		(net
			(code "4")
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
				(ref "JUSB1")
				(pin "A7")
				(pinfunction "DM_A7")
				(pintype "passive")
			)
			(node
				(ref "JUSB2")
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
				(ref "UETH1")
				(pin "8")
				(pinfunction "RD-_8")
				(pintype "passive")
			)
			(node
				(ref "UHUB1")
				(pin "6")
				(pinfunction "DN1_DM_6")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
			(node
				(ref "UUSB4")
				(pin "8")
				(pinfunction "I2C_SDA_8")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "HUB_DN1_DM")
			(class "Default")
			(node
				(ref "JUSB2")
				(pin "A1")
				(pinfunction "GND_A1")
				(pintype "passive")
			)
			(node
				(ref "UHUB1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "HUB_DN1_DP")
			(class "Default")
			(node
				(ref "JUSB2")
				(pin "A6")
				(pinfunction "DP_A6")
				(pintype "passive")
			)
			(node
				(ref "UHUB1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "I2C_SCL")
			(class "Default")
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
				(ref "UPD1")
				(pin "3")
				(pinfunction "CC2_3")
				(pintype "passive")
			)
			(node
				(ref "UUSB4")
				(pin "3")
				(pinfunction "USB4_UP_RX_3")
				(pintype "passive")
			)
		)
		(net
			(code "8")
			(name "I2C_SDA")
			(class "Default")
			(node
				(ref "UCHG1")
				(pin "2")
				(pinfunction "SYS_2")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "4")
				(pinfunction "GND_4")
				(pintype "passive")
			)
			(node
				(ref "UUSB4")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
		)
		(net
			(code "9")
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
			(code "10")
			(name "USB4_UP")
			(class "Default")
			(node
				(ref "UUSB4")
				(pin "6")
				(pinfunction "PCIE_DN_6")
				(pintype "passive")
			)
			(node
				(ref "UUSB4")
				(pin "7")
				(pinfunction "I2C_SCL_7")
				(pintype "passive")
			)
		)
		(net
			(code "11")
			(name "USB_DM")
			(class "Default")
			(node
				(ref "UETH1")
				(pin "6")
				(pinfunction "TD-_6")
				(pintype "passive")
			)
			(node
				(ref "UHUB1")
				(pin "4")
				(pinfunction "UP_DM_4")
				(pintype "passive")
			)
		)
		(net
			(code "12")
			(name "USB_DP")
			(class "Default")
			(node
				(ref "UETH1")
				(pin "5")
				(pinfunction "TD+_5")
				(pintype "passive")
			)
			(node
				(ref "UHUB1")
				(pin "3")
				(pinfunction "UP_DP_3")
				(pintype "passive")
			)
		)
		(net
			(code "13")
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
			(code "14")
			(name "VBUS")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "B5")
				(pinfunction "CC2_B5")
				(pintype "passive")
			)
			(node
				(ref "JUSB2")
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
			(code "15")
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
				(ref "UETH1")
				(pin "7")
				(pinfunction "RD+_7")
				(pintype "passive")
			)
			(node
				(ref "UHUB1")
				(pin "5")
				(pinfunction "DN1_DP_5")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "2")
				(pinfunction "CC1_2")
				(pintype "passive")
			)
			(node
				(ref "UUSB4")
				(pin "9")
				(pinfunction "NOTE_NDA_9")
				(pintype "passive")
			)
		)
		(net
			(code "16")
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
			(code "17")
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
			(code "18")
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
			(code "19")
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
			(code "20")
			(name "unconnected-(JUSB2-CC1-PadA5)")
			(class "Default")
			(node
				(ref "JUSB2")
				(pin "A5")
				(pinfunction "CC1_A5")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "21")
			(name "unconnected-(JUSB2-VBUS-PadA4)")
			(class "Default")
			(node
				(ref "JUSB2")
				(pin "A4")
				(pinfunction "VBUS_A4")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "22")
			(name "unconnected-(UETH1-GND-Pad2)")
			(class "Default")
			(node
				(ref "UETH1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "23")
			(name "unconnected-(UETH1-VDD33-Pad1)")
			(class "Default")
			(node
				(ref "UETH1")
				(pin "1")
				(pinfunction "VDD33_1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "24")
			(name "unconnected-(UPD1-SCL-Pad5)")
			(class "Default")
			(node
				(ref "UPD1")
				(pin "5")
				(pinfunction "SCL_5")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "25")
			(name "unconnected-(UUSB4-DP_OUT-Pad5)")
			(class "Default")
			(node
				(ref "UUSB4")
				(pin "5")
				(pinfunction "DP_OUT_5")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "26")
			(name "unconnected-(UUSB4-USB4_UP_TX-Pad4)")
			(class "Default")
			(node
				(ref "UUSB4")
				(pin "4")
				(pinfunction "USB4_UP_TX_4")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "27")
			(name "unconnected-(UUSB4-VDD-Pad1)")
			(class "Default")
			(node
				(ref "UUSB4")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive+no_connect")
			)
		)
	)
)
