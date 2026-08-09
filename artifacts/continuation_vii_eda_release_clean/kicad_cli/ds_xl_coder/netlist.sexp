(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_sch")
		(date "2026-08-09T12:16:24")
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
				(title "DS-XL Coder Carrier — Cont VII")
				(company "gunnchOS3k / CONTINUATION VII")
				(rev "0.4.0-cont-vii")
				(date "2026-08-09")
				(source "ds_xl_coder.kicad_sch")
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
			(ref "J_EDP0")
			(value "UPPER_eDP_2560x1600")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DISPLAY_UPPER")
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
				(value "DISPLAY_UPPER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "e2e14d2a-44ff-b8ca-57cb-4fbf2d3032e1")
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
			(ref "J_EDP1")
			(value "LOWER_eDP_1920x1200")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "DISPLAY_LOWER")
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
				(value "DISPLAY_LOWER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "9c2b70a1-1d20-4339-03d8-708af1bdbdc2")
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
			(ref "J_HINGE")
			(value "HINGE_FLEX")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "HINGE_B2B")
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
				(value "HINGE_B2B")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "bba2dc81-69d3-40ca-4513-587a54bf7c01")
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
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
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
			(ref "U_BRG")
			(value "LT8711_or_PS8625")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "EDP_BRIDGE_OPTIONAL")
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
				(value "EDP_BRIDGE_OPTIONAL")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
			)
			(property
				(name "dnp")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "2dfca221-7961-90c4-d5a2-052524ba0403")
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
			(value "BQ25792")
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
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
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
			(value "EC_NPCX_or_ITE")
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
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
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
			(ref "U_PD")
			(value "TPS65994")
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
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
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
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
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
				(value "ds_xl_coder")
			)
			(property
				(name "Sheetfile")
				(value "ds_xl_coder.kicad_sch")
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
			(name "BL_PWM_L")
			(class "Default")
			(node
				(ref "U_PD")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "BL_PWM_U")
			(class "Default")
			(node
				(ref "U_BRG")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "VSYS")
			(class "Default")
			(node
				(ref "J_EDP1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "4")
			(name "eDP0")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "eDP1")
			(class "Default")
			(node
				(ref "J_EDP0")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "unconnected-(J_EDP0-Pad1)")
			(class "Default")
			(node
				(ref "J_EDP0")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "7")
			(name "unconnected-(J_EDP1-Pad1)")
			(class "Default")
			(node
				(ref "J_EDP1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "8")
			(name "unconnected-(J_HINGE-Pad1)")
			(class "Default")
			(node
				(ref "J_HINGE")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "9")
			(name "unconnected-(J_HINGE-Pad2)")
			(class "Default")
			(node
				(ref "J_HINGE")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "10")
			(name "unconnected-(UCOM1-Pad1)")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "11")
			(name "unconnected-(U_BRG-Pad1)")
			(class "Default")
			(node
				(ref "U_BRG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "12")
			(name "unconnected-(U_CHG-Pad1)")
			(class "Default")
			(node
				(ref "U_CHG")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "13")
			(name "unconnected-(U_CHG-Pad2)")
			(class "Default")
			(node
				(ref "U_CHG")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "14")
			(name "unconnected-(U_EC-Pad1)")
			(class "Default")
			(node
				(ref "U_EC")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "15")
			(name "unconnected-(U_EC-Pad2)")
			(class "Default")
			(node
				(ref "U_EC")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "16")
			(name "unconnected-(U_PD-Pad1)")
			(class "Default")
			(node
				(ref "U_PD")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "17")
			(name "unconnected-(U_WIFI-Pad1)")
			(class "Default")
			(node
				(ref "U_WIFI")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "18")
			(name "unconnected-(U_WIFI-Pad2)")
			(class "Default")
			(node
				(ref "U_WIFI")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "19")
			(name "unconnected-(U_WWAN-Pad1)")
			(class "Default")
			(node
				(ref "U_WWAN")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "20")
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
