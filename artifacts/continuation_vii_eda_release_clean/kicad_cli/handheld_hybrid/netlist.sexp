(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/handheld_hybrid/kicad/handheld_hybrid.kicad_sch")
		(date "2026-08-09T12:16:27")
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
				(title "Handheld Hybrid SoM Carrier — Cont VII PUBLIC_PINOUT")
				(company "gunnchOS3k / CONTINUATION VII")
				(rev "0.4.0-cont-vii")
				(date "2026-08-09")
				(source "handheld_hybrid.kicad_sch")
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
			(ref "BT1")
			(value "6000mAh_pack")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "BATTERY")
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
				(value "BATTERY")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "4ee50c34-c2bf-4c98-9900-9626da98808d")
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
			(ref "JS1")
			(value "RKJXV122400D")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "ANALOG_STICK_L")
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
				(value "ANALOG_STICK_L")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "51b1b893-f6eb-a55c-8c85-c6c086152d04")
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
			(ref "JS2")
			(value "RKJXV122400D")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "ANALOG_STICK_R")
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
				(value "ANALOG_STICK_R")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "d5ef19ec-7276-17ce-8d98-4a1d821419d6")
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
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "SOM_SOCKET")
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
				(value "SOM_SOCKET")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "7392fc3d-1502-f19e-78e8-e341d0fe7cfb")
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
			(ref "J_AUDIO")
			(value "I2S_HP_codec")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "AUDIO")
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
				(value "AUDIO")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "e7e78658-2809-e768-408e-6301c5da8c95")
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
			(ref "J_DBG")
			(value "UART2_3pin")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DEBUG")
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
				(value "DEBUG")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "8c5383bc-efae-90a4-a3c3-3935922b7177")
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
			(ref "J_DISP")
			(value "7in_1080p_120Hz_IPS")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DISPLAY")
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
				(value "DISPLAY")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "26460ddf-9759-8a9a-cb5f-9f7b51887c2b")
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
			(ref "J_USBC")
			(value "USB_C_receptacle")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DOCK_PORT")
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
				(value "DOCK_PORT")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "5c5e9706-1f1f-b8d7-54b5-446d2255033e")
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
			(ref "J_USD")
			(value "microSD_socket")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "STORAGE")
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
				(value "STORAGE")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "b8a240e7-9d80-69b3-7836-8da9dd0e10f7")
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
			(ref "SW_ABXY")
			(value "tactile_ABXY_LR_DPAD")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "CONTROLS")
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
				(value "CONTROLS")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "e9d06f23-dae9-880e-391c-07ada9f4a8e6")
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
			(ref "USOM1")
			(value "RM121-D8E32")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "SOM_MODULE")
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
				(value "SOM_MODULE")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "d66aedc7-bbcc-e192-4f01-83ecd2c7b96a")
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
			(ref "U_CHG")
			(value "BQ25895RTWR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "CHARGER")
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
				(value "CHARGER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "c267a83e-2d72-edf1-69fe-5677978f615b")
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
			(ref "U_FG")
			(value "BQ27Z561YPHR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "FUEL_GAUGE")
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
				(value "FUEL_GAUGE")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "e3509ed0-2992-dd7c-97db-43d12c31e8b9")
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
			(ref "U_HID")
			(value "STM32F103C8T6")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "GAMEPAD_MCU")
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
				(value "GAMEPAD_MCU")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "dd0597aa-86d1-3411-ac86-39e5a538a948")
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
			(ref "U_PD")
			(value "TPS65987DDHRSHR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "PD")
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
				(value "PD")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "5a2c79c5-a2b9-29f7-010e-d070b8fce683")
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
			(ref "U_SE")
			(value "SE050C1HQ1")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "SECURE_ELEMENT")
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
				(value "SECURE_ELEMENT")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "9c46d75d-5348-ef67-5ead-0d2b0421628f")
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
			(ref "U_WIFI")
			(value "AP6275P")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "WIFI6E_BT")
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
				(value "WIFI6E_BT")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
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
			(tstamps "1a648bc6-324e-e3d2-5c0b-c08d19038077")
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
			(ref "U_WWAN")
			(value "RM520N-GL")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "WWAN_OPTIONAL")
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
				(value "WWAN_OPTIONAL")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "handheld_hybrid")
			)
			(property
				(name "Sheetfile")
				(value "handheld_hybrid.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "c7b886e5-d6ec-7d73-669d-81e9a2754586")
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
				(ref "SW_ABXY")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "CC2")
			(class "Default")
			(node
				(ref "JS1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "GND")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "4")
			(name "HDMI0_TX")
			(class "Default")
			(node
				(ref "J_DISP")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "I2C0_HID")
			(class "Default")
			(node
				(ref "U_SE")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "I2S0")
			(class "Default")
			(node
				(ref "J_USD")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "LCD_BL_PWM")
			(class "Default")
			(node
				(ref "U_WWAN")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "8")
			(name "LCD_RESET_L")
			(class "Default")
			(node
				(ref "U_HID")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "9")
			(name "MIPI_DPHY_TX")
			(class "Default")
			(node
				(ref "U_WIFI")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "10")
			(name "PCIE20_WWAN")
			(class "Default")
			(node
				(ref "J_AUDIO")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "11")
			(name "SDMMC")
			(class "Default")
			(node
				(ref "U_FG")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "12")
			(name "UART2_DBG")
			(class "Default")
			(node
				(ref "J_USBC")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "13")
			(name "USB20_HOST0_DM")
			(class "Default")
			(node
				(ref "U_PD")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "14")
			(name "USB30_SS")
			(class "Default")
			(node
				(ref "U_CHG")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "15")
			(name "VBAT")
			(class "Default")
			(node
				(ref "BT1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "16")
			(name "VBUS_PD")
			(class "Default")
			(node
				(ref "J_DBG")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "17")
			(name "VCC_SYSIN")
			(class "Default")
			(node
				(ref "USOM1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "18")
			(name "unconnected-(BT1-Pad1)")
			(class "Default")
			(node
				(ref "BT1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "19")
			(name "unconnected-(JS1-Pad1)")
			(class "Default")
			(node
				(ref "JS1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "20")
			(name "unconnected-(JS2-Pad1)")
			(class "Default")
			(node
				(ref "JS2")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "21")
			(name "unconnected-(JS2-Pad2)")
			(class "Default")
			(node
				(ref "JS2")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "22")
			(name "unconnected-(JSOM1-Pad1)")
			(class "Default")
			(node
				(ref "JSOM1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "23")
			(name "unconnected-(J_AUDIO-Pad1)")
			(class "Default")
			(node
				(ref "J_AUDIO")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "24")
			(name "unconnected-(J_DBG-Pad1)")
			(class "Default")
			(node
				(ref "J_DBG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "25")
			(name "unconnected-(J_DISP-Pad1)")
			(class "Default")
			(node
				(ref "J_DISP")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "26")
			(name "unconnected-(J_USBC-Pad1)")
			(class "Default")
			(node
				(ref "J_USBC")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "27")
			(name "unconnected-(J_USD-Pad1)")
			(class "Default")
			(node
				(ref "J_USD")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "28")
			(name "unconnected-(SW_ABXY-Pad1)")
			(class "Default")
			(node
				(ref "SW_ABXY")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "29")
			(name "unconnected-(USOM1-Pad1)")
			(class "Default")
			(node
				(ref "USOM1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "30")
			(name "unconnected-(U_CHG-Pad1)")
			(class "Default")
			(node
				(ref "U_CHG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "31")
			(name "unconnected-(U_FG-Pad1)")
			(class "Default")
			(node
				(ref "U_FG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "32")
			(name "unconnected-(U_HID-Pad1)")
			(class "Default")
			(node
				(ref "U_HID")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "33")
			(name "unconnected-(U_PD-Pad1)")
			(class "Default")
			(node
				(ref "U_PD")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "34")
			(name "unconnected-(U_SE-Pad1)")
			(class "Default")
			(node
				(ref "U_SE")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "35")
			(name "unconnected-(U_WIFI-Pad1)")
			(class "Default")
			(node
				(ref "U_WIFI")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "36")
			(name "unconnected-(U_WWAN-Pad1)")
			(class "Default")
			(node
				(ref "U_WWAN")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
	)
)
