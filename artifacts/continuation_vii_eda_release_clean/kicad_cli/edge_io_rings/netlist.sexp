(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch")
		(date "2026-08-09T12:16:29")
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
				(title "Edge I/O Ring EVT1 — Cont VII")
				(company "gunnchOS3k / CONTINUATION VII")
				(rev "0.4.0-cont-vii")
				(date "2026-08-09")
				(source "edge_io_rings.kicad_sch")
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
			(ref "ANT1")
			(value "2450AT18A100")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "BLE_ANTENNA")
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
				(value "BLE_ANTENNA")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "edce38f3-4950-7927-fb01-5dfb194d52d5")
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
			(ref "BT1")
			(value "LiPo_80to250mAh")
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
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
			(ref "U1")
			(value "nRF52840-QIAA-R")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "MCU_BLE")
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
				(value "MCU_BLE")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
			(ref "U2")
			(value "BMI270")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "IMU_6AXIS")
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
				(value "IMU_6AXIS")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
			(value "IQS7222A")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "CAPACITIVE_REQUIRED")
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
				(value "CAPACITIVE_REQUIRED")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
			(value "DWM3001C")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "UWB_FOOTPRINT")
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
				(value "UWB_FOOTPRINT")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
			)
			(property
				(name "dnp")
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
			(value "BHI360")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "SENSOR_HUB_OPTIONAL")
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
				(value "SENSOR_HUB_OPTIONAL")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
			)
			(property
				(name "dnp")
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
			(value "BMM350")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "MAG_OPTIONAL")
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
				(value "MAG_OPTIONAL")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
			)
			(property
				(name "dnp")
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
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
			(value "DRV2605LDGSR")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "HAPTIC_DRIVER")
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
				(value "HAPTIC_DRIVER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
			(value "npm1300-CAAA-R")
			(footprint "gunnchos_structural:Block_SMD_10x10")
			(fields
				(field
					(name "Role") "PMIC_CHARGER")
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
				(value "PMIC_CHARGER")
			)
			(property
				(name "ContVII")
				(value "FUNC_BLOCK_NO_VENDOR_PINOUT")
			)
			(property
				(name "Sheetname")
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
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
		(comp
			(ref "U10")
			(value "TLV75533PDBVR")
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
				(value "edge_io_rings")
			)
			(property
				(name "Sheetfile")
				(value "edge_io_rings.kicad_sch")
			)
			(sheetpath
				(names "/")
				(tstamps "/")
			)
			(tstamps "a16b9492-a68f-e7be-ae51-e43e5a841e07")
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
			(name "CAP_RDY")
			(class "Default")
			(node
				(ref "U10")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "CHG_STATUS")
			(class "Default")
			(node
				(ref "U8")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "HAPTIC_TRIG")
			(class "Default")
			(node
				(ref "U9")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "4")
			(name "I2C_SCL")
			(class "Default")
			(node
				(ref "U3")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "I2C_SDA")
			(class "Default")
			(node
				(ref "U2")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "IMU_INT")
			(class "Default")
			(node
				(ref "U5")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "SE_I2C_SCL")
			(class "Default")
			(node
				(ref "U7")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "8")
			(name "SE_I2C_SDA")
			(class "Default")
			(node
				(ref "U6")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "9")
			(name "SPI_UWB")
			(class "Default")
			(node
				(ref "U4")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "10")
			(name "VDD_3V3")
			(class "Default")
			(node
				(ref "U1")
				(pin "2")
				(pintype "passive")
			)
		)
		(net
			(code "11")
			(name "unconnected-(ANT1-Pad1)")
			(class "Default")
			(node
				(ref "ANT1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "12")
			(name "unconnected-(ANT1-Pad2)")
			(class "Default")
			(node
				(ref "ANT1")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "13")
			(name "unconnected-(BT1-Pad1)")
			(class "Default")
			(node
				(ref "BT1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "14")
			(name "unconnected-(BT1-Pad2)")
			(class "Default")
			(node
				(ref "BT1")
				(pin "2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "15")
			(name "unconnected-(U1-Pad1)")
			(class "Default")
			(node
				(ref "U1")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "16")
			(name "unconnected-(U2-Pad1)")
			(class "Default")
			(node
				(ref "U2")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "17")
			(name "unconnected-(U3-Pad1)")
			(class "Default")
			(node
				(ref "U3")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "18")
			(name "unconnected-(U4-Pad1)")
			(class "Default")
			(node
				(ref "U4")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "19")
			(name "unconnected-(U5-Pad1)")
			(class "Default")
			(node
				(ref "U5")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "20")
			(name "unconnected-(U6-Pad1)")
			(class "Default")
			(node
				(ref "U6")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "21")
			(name "unconnected-(U7-Pad1)")
			(class "Default")
			(node
				(ref "U7")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "22")
			(name "unconnected-(U8-Pad1)")
			(class "Default")
			(node
				(ref "U8")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "23")
			(name "unconnected-(U9-Pad1)")
			(class "Default")
			(node
				(ref "U9")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "24")
			(name "unconnected-(U10-Pad1)")
			(class "Default")
			(node
				(ref "U10")
				(pin "1")
				(pintype "passive+no_connect")
			)
		)
	)
)
