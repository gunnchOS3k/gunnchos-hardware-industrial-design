(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/student_14_5/kicad/student_14_5.kicad_sch")
		(date "2026-08-09T12:16:21")
		(tool "Eeschema 10.0.5")
		(textvar
			(name "EDMUND_ACTION_REQUIRED") "install_kicad_cli")
		(textvar
			(name "FAMILY_DEPTH") "1")
		(textvar
			(name "KICAD_CLI") "ABSENT")
		(sheet
			(number "1")
			(name "/")
			(tstamps "/")
			(title_block
				(title "Student 14.5 Carrier — Cont VII")
				(company "gunnchOS3k / CONTINUATION VII")
				(rev "0.4.0-cont-vii")
				(date "2026-08-09")
				(source "student_14_5.kicad_sch")
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
			(value "4S1P_60Wh")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "BATTERY_PACK")
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
				(value "BATTERY_PACK")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
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
			(ref "JCOM1")
			(value "COM-HPC-Mini-Connector")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "COM_CONNECTOR")
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
				(value "COM_CONNECTOR")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "8ffd9c61-79ff-27ad-80f2-4bb5a935cb5e")
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
			(ref "J_EDP")
			(value "eDP_14_5_panel")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DISPLAY_EDP")
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
				(value "DISPLAY_EDP")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "c964e90f-f489-a8d7-f794-b2c45c0f8798")
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
			(ref "J_USB4")
			(value "USB4_TypeC_x2")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "USB4_DOCK")
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
				(value "USB4_DOCK")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "15c79e77-c9d8-da1f-247d-c0fcc2aa6084")
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
			(ref "SSD1")
			(value "NVMe_512GB")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "STORAGE_NVME")
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
				(value "STORAGE_NVME")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "48d6e47c-4322-440c-b5e9-ca7c8d0c65f7")
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
			(ref "UCOM1")
			(value "COM-HPC-mMTL-155H-32G")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "COM_MODULE")
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
				(value "COM_MODULE")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "8b75a06a-7cf0-e9f6-c56e-fbbe287dd7b1")
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
			(ref "U_3V3")
			(value "TPS62864YCPR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "BUCK_3V3")
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
				(value "BUCK_3V3")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "e80b528b-9663-bd96-4a3f-4fc9bca1bc89")
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
			(ref "U_5V")
			(value "TPS51396AJYYR")
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
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "92dcc04b-10c4-cffe-abed-02e3501c0d65")
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
			(ref "U_AUD")
			(value "ALC256")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "AUDIO_CODEC")
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
				(value "AUDIO_CODEC")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "80346a1e-f0e7-4af6-38b4-6b0ed0a44a45")
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
			(value "BQ25792RQMR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "BATTERY_CHARGER")
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
				(value "BATTERY_CHARGER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
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
			(ref "U_EC")
			(value "ITE5570-or-NPCX9")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "EMBEDDED_CONTROLLER")
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
				(value "EMBEDDED_CONTROLLER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "b290df5a-f089-12c4-af83-cf656b217589")
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
			(value "BQ40Z50-R2")
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
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
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
			(ref "U_PD")
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
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
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
			(ref "U_TPM")
			(value "SLB9672XQ2.0")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "TPM2")
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
				(value "TPM2")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "687acd5b-3df4-7f24-71a6-5b370db6537b")
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
			(value "BE200")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "WIFI7_BT_M2")
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
				(value "WIFI7_BT_M2")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
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
					(name "Role") "WWAN_5G_M2")
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
				(value "WWAN_5G_M2")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "student_14_5")
			)
			(property
				(name "Sheetfile")
				(value "student_14_5.kicad_sch")
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
			(name "COM_VIN")
			(class "Default")
			(node
				(ref "JCOM1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "I2C_EC")
			(class "Default")
			(node
				(ref "U_FG")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "VBUS_PD")
			(class "Default")
			(node
				(ref "U_PD")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "4")
			(name "VDD_3V3")
			(class "Default")
			(node
				(ref "U_EC")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "VSYS")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "eDP0")
			(class "Default")
			(node
				(ref "U_CHG")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "unconnected-(BT1-Pad1)")
			(class "Default")
			(node
				(ref "BT1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "8")
			(name "unconnected-(BT1-Pad2)")
			(class "Default")
			(node
				(ref "BT1")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "9")
			(name "unconnected-(JCOM1-Pad1)")
			(class "Default")
			(node
				(ref "JCOM1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "10")
			(name "unconnected-(J_EDP-Pad1)")
			(class "Default")
			(node
				(ref "J_EDP")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "11")
			(name "unconnected-(J_EDP-Pad2)")
			(class "Default")
			(node
				(ref "J_EDP")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "12")
			(name "unconnected-(J_USB4-Pad1)")
			(class "Default")
			(node
				(ref "J_USB4")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "13")
			(name "unconnected-(J_USB4-Pad2)")
			(class "Default")
			(node
				(ref "J_USB4")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "14")
			(name "unconnected-(SSD1-Pad1)")
			(class "Default")
			(node
				(ref "SSD1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "15")
			(name "unconnected-(SSD1-Pad2)")
			(class "Default")
			(node
				(ref "SSD1")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "16")
			(name "unconnected-(UCOM1-Pad1)")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "17")
			(name "unconnected-(U_3V3-Pad1)")
			(class "Default")
			(node
				(ref "U_3V3")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "18")
			(name "unconnected-(U_3V3-Pad2)")
			(class "Default")
			(node
				(ref "U_3V3")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "19")
			(name "unconnected-(U_5V-Pad1)")
			(class "Default")
			(node
				(ref "U_5V")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "20")
			(name "unconnected-(U_5V-Pad2)")
			(class "Default")
			(node
				(ref "U_5V")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "21")
			(name "unconnected-(U_AUD-Pad1)")
			(class "Default")
			(node
				(ref "U_AUD")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "22")
			(name "unconnected-(U_AUD-Pad2)")
			(class "Default")
			(node
				(ref "U_AUD")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "23")
			(name "unconnected-(U_CHG-Pad1)")
			(class "Default")
			(node
				(ref "U_CHG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "24")
			(name "unconnected-(U_EC-Pad1)")
			(class "Default")
			(node
				(ref "U_EC")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "25")
			(name "unconnected-(U_FG-Pad1)")
			(class "Default")
			(node
				(ref "U_FG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "26")
			(name "unconnected-(U_PD-Pad1)")
			(class "Default")
			(node
				(ref "U_PD")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "27")
			(name "unconnected-(U_TPM-Pad1)")
			(class "Default")
			(node
				(ref "U_TPM")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "28")
			(name "unconnected-(U_TPM-Pad2)")
			(class "Default")
			(node
				(ref "U_TPM")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "29")
			(name "unconnected-(U_WIFI-Pad1)")
			(class "Default")
			(node
				(ref "U_WIFI")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "30")
			(name "unconnected-(U_WIFI-Pad2)")
			(class "Default")
			(node
				(ref "U_WIFI")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "31")
			(name "unconnected-(U_WWAN-Pad1)")
			(class "Default")
			(node
				(ref "U_WWAN")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "32")
			(name "unconnected-(U_WWAN-Pad2)")
			(class "Default")
			(node
				(ref "U_WWAN")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
	)
)
