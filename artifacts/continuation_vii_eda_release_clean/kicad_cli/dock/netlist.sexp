(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/dock/kicad/dock.kicad_sch")
		(date "2026-08-09T12:16:32")
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
				(title "Dock Main PCB — USB4/TB4 Cont VII")
				(company "gunnchOS3k / CONTINUATION VII")
				(rev "0.4.0-cont-vii")
				(date "2026-08-09")
				(source "dock.kicad_sch")
				(comment
					(number "1")
					(value "Functional nets wired to FuncBlock pins — no invented vendor pin numbers")
				)
				(comment
					(number "2")
					(value "KICAD_CLI_EXECUTION_PASS != EDA_RELEASE_CLEAN_PASS")
				)
				(comment
					(number "3")
					(value "PHYSICAL_EXECUTION_FREEZE ACTIVE")
				)
				(comment
					(number "4")
					(value "Structural Device-geometry blocks until vendor libs")
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
			(ref "FORBID1")
			(value "JHL9480")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "REJECTED_TB5")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "REJECTED_TB5")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "473845e9-7d51-fce5-20b1-39905879853c")
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
			(ref "FORBID2")
			(value "JHL9580")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "REJECTED_TB5")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "REJECTED_TB5")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "d3da9590-4672-fb97-1a10-d4d22aae98e5")
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
			(ref "J1")
			(value "USB4085")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "HOST_PORT")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "HOST_PORT")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "caba1435-39ea-21bb-3719-88e17bb5457e")
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
			(ref "J2A")
			(value "USB4085")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DOWNSTREAM_C1")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "DOWNSTREAM_C1")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "003f7080-5876-d1e1-3f21-e3a6a8fa9767")
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
			(ref "J2B")
			(value "USB4085")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DOWNSTREAM_C2")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "DOWNSTREAM_C2")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "76ceec93-e048-3c6b-5001-497be59a93c8")
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
			(ref "J3A")
			(value "USB3_A")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DOWNSTREAM_A1")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "DOWNSTREAM_A1")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "acab54a5-25eb-1f46-f87e-cbf19a6fae6d")
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
			(ref "J3B")
			(value "USB3_A")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DOWNSTREAM_A2")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "DOWNSTREAM_A2")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "85e165a1-c7c2-8512-f885-9f648eacc20b")
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
			(ref "J4")
			(value "HDMI_TypeA")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "VIDEO_EGRESS")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "VIDEO_EGRESS")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "14c7bb2c-d3a6-7c6c-dfd3-055101777a5c")
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
			(ref "J5")
			(value "JK0-0136NL")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "ETHERNET")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "ETHERNET")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "8ddf641a-7134-add3-ee13-c5eb10150aad")
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
			(ref "J6")
			(value "Mill-Max_pogo")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "RING_CHARGE")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "RING_CHARGE")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "6da460a7-aad2-111c-e0c7-629f57aabef5")
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
			(ref "U1")
			(value "JHL8440")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "USB4_TB4_DOCK_CONTROLLER")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "USB4_TB4_DOCK_CONTROLLER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "27dce889-98eb-028c-0025-c07a655cff3f")
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
			(ref "U1A")
			(value "VL108")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "USB3DP_COSTDOWN_SKU")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "USB3DP_COSTDOWN_SKU")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "2e22bb21-82d8-fe86-675e-c8c9a6e261ec")
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
			(ref "U1R")
			(value "JHL9040R")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "TB4_RETIMER")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "TB4_RETIMER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "19f956aa-480c-177b-6c2f-fd1861902ea6")
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
			(ref "U2")
			(value "TPS65994ADFBRQ1")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "PD_CONTROLLER")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "PD_CONTROLLER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "cd83e76f-8e6c-8e84-1032-b2db1a787879")
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
			(ref "U3")
			(value "RTL8156")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "ETHERNET_2G5")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "ETHERNET_2G5")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "d583e422-ff84-c3ac-4e78-3a83265b00ea")
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
			(ref "U4")
			(value "VL817")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "USB_HUB")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "USB_HUB")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "ccaf909b-8bc9-c190-828b-f44727b1a0c8")
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
			(ref "U5")
			(value "TPS55288RPMR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "VBUS_BUCKBOOST")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "VBUS_BUCKBOOST")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "b01c369b-c9a5-3ac3-6d18-47019af7cc4f")
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
			(ref "U6")
			(value "TPS62864")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "BUCK_5V")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "BUCK_5V")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "e9d8b60a-75b5-66ed-fca1-846f8bef2e06")
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
			(ref "U7")
			(value "TLV75533PDRVR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "LDO_3V3")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "LDO_3V3")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "233530ee-5f0f-ea55-42f8-2e5109125436")
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
			(ref "U8")
			(value "DWM3001C")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "UWB_COMPANION")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "UWB_COMPANION")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "975a2b93-f506-03eb-cfe7-1a75a39df209")
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
			(ref "U9")
			(value "ALC4050")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "USB_AUDIO_OPT")
				(field
					(name "ContVII") "FUNC_BLOCK_NO_VENDOR_PINOUT")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "FuncBlock")
				(description "")
			)
			(property
				(name "Role")
				(value "USB_AUDIO_OPT")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "dock")
			)
			(property
				(name "Sheetfile")
				(value "dock.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "72e0757b-c84f-0dbc-c7d4-e30c0485ac65")
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
	)
	(groups)
	(variants)
	(libparts
		(libpart
			(lib "")
			(part "FuncBlock")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "FuncBlock")
				(field
					(name "Footprint") "gunnchos_structural:Block_SMD_10x10")
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
	)
	(libraries)
	(nets
		(net
			(code "1")
			(name "CC1")
			(class "Default")
			(node
				(ref "J3A")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "CC2")
			(class "Default")
			(node
				(ref "J3B")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "HDMI_TX")
			(class "Default")
			(node
				(ref "U1")
				(pin "1")
				(pintype "passive")
			)
		)
		(net
			(code "4")
			(name "I2C_PD")
			(class "Default")
			(node
				(ref "J4")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "I2C_RETIMER")
			(class "Default")
			(node
				(ref "J5")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "MDI")
			(class "Default")
			(node
				(ref "FORBID2")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "RING_CHARGE_5V")
			(class "Default")
			(node
				(ref "U1R")
				(pin "1")
				(pintype "passive")
			)
		)
		(net
			(code "8")
			(name "SPI_UWB")
			(class "Default")
			(node
				(ref "U1A")
				(pin "1")
				(pintype "passive")
			)
		)
		(net
			(code "9")
			(name "SS_RX_DS1")
			(class "Default")
			(node
				(ref "J1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "10")
			(name "SS_RX_DS2")
			(class "Default")
			(node
				(ref "J2B")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "11")
			(name "SS_RX_HOST")
			(class "Default")
			(node
				(ref "U6")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "12")
			(name "SS_RX_UP")
			(class "Default")
			(node
				(ref "U8")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "13")
			(name "SS_TX_DS1")
			(class "Default")
			(node
				(ref "U9")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "14")
			(name "SS_TX_DS2")
			(class "Default")
			(node
				(ref "J2A")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "15")
			(name "SS_TX_HOST")
			(class "Default")
			(node
				(ref "U5")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "16")
			(name "SS_TX_UP")
			(class "Default")
			(node
				(ref "U7")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "17")
			(name "USB_A1")
			(class "Default")
			(node
				(ref "J6")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "18")
			(name "USB_A2")
			(class "Default")
			(node
				(ref "FORBID1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "19")
			(name "VBUS_DS1")
			(class "Default")
			(node
				(ref "U1R")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "20")
			(name "VBUS_DS2")
			(class "Default")
			(node
				(ref "U1A")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "21")
			(name "VBUS_UPSTREAM")
			(class "Default")
			(node
				(ref "U1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "22")
			(name "VDD_1V8")
			(class "Default")
			(node
				(ref "U4")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "23")
			(name "VDD_3V3")
			(class "Default")
			(node
				(ref "U3")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "24")
			(name "VSYS_5V")
			(class "Default")
			(node
				(ref "U2")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "25")
			(name "unconnected-(FORBID1-Pad1)")
			(class "Default")
			(node
				(ref "FORBID1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "26")
			(name "unconnected-(FORBID2-Pad1)")
			(class "Default")
			(node
				(ref "FORBID2")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "27")
			(name "unconnected-(J1-Pad1)")
			(class "Default")
			(node
				(ref "J1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "28")
			(name "unconnected-(J2A-Pad1)")
			(class "Default")
			(node
				(ref "J2A")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "29")
			(name "unconnected-(J2B-Pad1)")
			(class "Default")
			(node
				(ref "J2B")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "30")
			(name "unconnected-(J3A-Pad1)")
			(class "Default")
			(node
				(ref "J3A")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "31")
			(name "unconnected-(J3B-Pad1)")
			(class "Default")
			(node
				(ref "J3B")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "32")
			(name "unconnected-(J4-Pad1)")
			(class "Default")
			(node
				(ref "J4")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "33")
			(name "unconnected-(J5-Pad1)")
			(class "Default")
			(node
				(ref "J5")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "34")
			(name "unconnected-(J6-Pad1)")
			(class "Default")
			(node
				(ref "J6")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "35")
			(name "unconnected-(U2-Pad1)")
			(class "Default")
			(node
				(ref "U2")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "36")
			(name "unconnected-(U3-Pad1)")
			(class "Default")
			(node
				(ref "U3")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "37")
			(name "unconnected-(U4-Pad1)")
			(class "Default")
			(node
				(ref "U4")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "38")
			(name "unconnected-(U5-Pad1)")
			(class "Default")
			(node
				(ref "U5")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "39")
			(name "unconnected-(U6-Pad1)")
			(class "Default")
			(node
				(ref "U6")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "40")
			(name "unconnected-(U7-Pad1)")
			(class "Default")
			(node
				(ref "U7")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "41")
			(name "unconnected-(U8-Pad1)")
			(class "Default")
			(node
				(ref "U8")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "42")
			(name "unconnected-(U9-Pad1)")
			(class "Default")
			(node
				(ref "U9")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
	)
)
