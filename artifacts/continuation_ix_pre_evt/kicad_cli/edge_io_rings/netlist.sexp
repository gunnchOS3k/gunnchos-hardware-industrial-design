(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/edge_io_rings/kicad/edge_io_rings.kicad_sch")
		(date "2026-08-09T15:51:01")
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
				(title "Edge I/O Ring EVT1 — Cont IX Pre-EVT")
				(company "gunnchOS3k / CONTINUATION IX")
				(rev "0.6.0-cont-ix")
				(date "2026-08-09")
				(source "edge_io_rings.kicad_sch")
				(comment
					(number "1")
					(value "Production JEDEC/vendor footprints — Cont VIII proxies retired")
				)
				(comment
					(number "2")
					(value "PHYSICAL_EXECUTION_FREEZE ACTIVE — DRAFT PR only")
				)
				(comment
					(number "3")
					(value "Compute MPN: nRF52840-QIAA-R")
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
			(ref "ANT1")
			(value "2450AT18A100")
			(footprint "gunnchos_production:Antenna_Johanson_2450AT18A100")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "2450AT18A100")
				(field
					(name "Role") "BLE_ANT")
				(field
					(name "Footprint") "gunnchos_production:Antenna_Johanson_2450AT18A100")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "ANT")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "2450AT18A100")
			)
			(property
				(name "Role")
				(value "BLE_ANT")
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
			(tstamps "d41e67cb-a928-acc3-68f8-fd469be982bb")
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
					)
				)
			)
		)
		(comp
			(ref "C1")
			(value "CL05A104KA5NNNC")
			(footprint "gunnchos_production:C_0402")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "CL05A104KA5NNNC")
				(field
					(name "Role") "DECAP")
				(field
					(name "Footprint") "gunnchos_production:C_0402")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(footprint "gunnchos_production:C_0402")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "GRM188R60J106ME47D")
				(field
					(name "Role") "BULK")
				(field
					(name "Footprint") "gunnchos_production:C_0402")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(footprint "gunnchos_production:LED_0603")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "APTD1608LCGCK")
				(field
					(name "Role") "STATUS_LED")
				(field
					(name "Footprint") "gunnchos_production:LED_0603")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "PESD5V0S1UL")
				(field
					(name "Role") "ESD")
				(field
					(name "Footprint") "gunnchos_production:DFN1006-2")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "ESD")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
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
			(ref "JE1")
			(value "CAP_ELECTRODE")
			(footprint "gunnchos_production:TestPoint_Pad")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "ELECTRODE_GEO")
				(field
					(name "Role") "ELECTRODE")
				(field
					(name "Footprint") "gunnchos_production:TestPoint_Pad")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "ELEC")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "ELECTRODE_GEO")
			)
			(property
				(name "Role")
				(value "ELECTRODE")
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
			(tstamps "d70ec78d-acd0-c814-defd-35ef4f0d763d")
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
			(ref "JP1")
			(value "POGO_CHARGE")
			(footprint "gunnchos_production:TestPoint_Pad")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "Mill-Max-319")
				(field
					(name "Role") "CHARGE_CONTACT")
				(field
					(name "Footprint") "gunnchos_production:TestPoint_Pad")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "CHGPOGO")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "Mill-Max-319")
			)
			(property
				(name "Role")
				(value "CHARGE_CONTACT")
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
			(tstamps "9f0cbef2-4584-817c-c91b-d26f42e564a0")
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
			(footprint "gunnchos_production:USB_C_Receptacle_Production")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "HRO TYPE-C-31-M-12")
				(field
					(name "Role") "USB_C")
				(field
					(name "Footprint") "gunnchos_production:USB_C_Receptacle_Production")
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
				(name "ContIX")
				(value "PRODUCTION")
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
							(num "S1")
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
			(footprint "gunnchos_production:R_0402")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "RC0402FR-0710KL")
				(field
					(name "Role") "PULLUP")
				(field
					(name "Footprint") "gunnchos_production:R_0402")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(footprint "gunnchos_production:R_0402")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "RC0402FR-071K0L")
				(field
					(name "Role") "LED_R")
				(field
					(name "Footprint") "gunnchos_production:R_0402")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(ref "U1")
			(value "nRF52840-QIAA-R")
			(footprint "gunnchos_production:Nordic_AQFN-73-1EP_7x7mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "nRF52840-QIAA-R")
				(field
					(name "Role") "MCU")
				(field
					(name "Evidence") "PUBLIC_PINOUT")
				(field
					(name "Footprint") "gunnchos_production:Nordic_AQFN-73-1EP_7x7mm_P0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "NRF52840")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "nRF52840-QIAA-R")
			)
			(property
				(name "Role")
				(value "MCU")
			)
			(property
				(name "Evidence")
				(value "PUBLIC_PINOUT")
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
			(tstamps "a78665a3-e0b6-254a-ad36-156fd2e32c68")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "13")
						)
						(pin
							(num "15")
						)
						(pin
							(num "17")
						)
						(pin
							(num "43")
						)
						(pin
							(num "2")
						)
						(pin
							(num "33")
						)
						(pin
							(num "14")
						)
						(pin
							(num "16")
						)
						(pin
							(num "42")
						)
						(pin
							(num "1")
						)
						(pin
							(num "32")
						)
						(pin
							(num "49")
						)
					)
				)
			)
		)
		(comp
			(ref "U2")
			(value "npm1300-CAAA-R")
			(footprint "gunnchos_production:WLCSP-36_2.1x2.1mm_P0.4mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "npm1300-CAAA-R")
				(field
					(name "Role") "PMIC")
				(field
					(name "Footprint") "gunnchos_production:WLCSP-36_2.1x2.1mm_P0.4mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "NPM1300")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "npm1300-CAAA-R")
			)
			(property
				(name "Role")
				(value "PMIC")
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
			(tstamps "840f82be-ed55-7188-3597-735efdd28b74")
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
			(ref "U3")
			(value "IQS7222A")
			(footprint "gunnchos_production:QFN-20-1EP_3x3mm_P0.4mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "IQS7222A")
				(field
					(name "Role") "CAP_TOUCH")
				(field
					(name "Footprint") "gunnchos_production:QFN-20-1EP_3x3mm_P0.4mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "IQS7222A")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "IQS7222A")
			)
			(property
				(name "Role")
				(value "CAP_TOUCH")
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
			(tstamps "96f759d6-e3ec-699b-5620-20f8359ba925")
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
					)
				)
			)
		)
		(comp
			(ref "U3V3")
			(value "TPS62864")
			(footprint "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "TPS62864")
				(field
					(name "Role") "BUCK_3V3")
				(field
					(name "Footprint") "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(ref "U4")
			(value "BMI270")
			(footprint "gunnchos_production:Bosch_LGA-14_3x2.5mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "BMI270")
				(field
					(name "Role") "IMU")
				(field
					(name "Footprint") "gunnchos_production:Bosch_LGA-14_3x2.5mm_P0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "BMI270")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "BMI270")
			)
			(property
				(name "Role")
				(value "IMU")
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
			(tstamps "1f403d35-e36f-0de3-d0c0-ec2a23297918")
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
			(ref "U5")
			(value "SE050C1HQ1")
			(footprint "gunnchos_production:HXQFN-20-1EP_4x4mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "SE050C1HQ1")
				(field
					(name "Role") "SE")
				(field
					(name "Footprint") "gunnchos_production:HXQFN-20-1EP_4x4mm_P0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "SE050")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "SE050C1HQ1")
			)
			(property
				(name "Role")
				(value "SE")
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
			(tstamps "812a2dbf-c1f9-e09a-5969-f005a28c7258")
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
			(footprint "gunnchos_production:WQFN-29-1EP_4x4mm_P0.4mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "BQ25792RQMR")
				(field
					(name "Role") "CHARGER")
				(field
					(name "Footprint") "gunnchos_production:WQFN-29-1EP_4x4mm_P0.4mm")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(ref "UHAP1")
			(value "DRV2605LDGSR")
			(footprint "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "DRV2605LDGSR")
				(field
					(name "Role") "HAPTICS")
				(field
					(name "Footprint") "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "HAP")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "DRV2605LDGSR")
			)
			(property
				(name "Role")
				(value "HAPTICS")
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
			(tstamps "12c87fee-087a-a56a-75b4-c6b12c07e5f2")
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
			(ref "UPD1")
			(value "TPS65994ADFBRQ1")
			(footprint "gunnchos_production:VQFN-48-1EP_7x7mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "TPS65994ADFBRQ1")
				(field
					(name "Role") "PD")
				(field
					(name "Footprint") "gunnchos_production:VQFN-48-1EP_7x7mm_P0.5mm")
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
				(name "ContIX")
				(value "PRODUCTION")
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
			(ref "UWBDNP")
			(value "DWM3001C")
			(footprint "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "DWM3001C")
				(field
					(name "Role") "UWB_DNP")
				(field
					(name "DNP") "TRUE")
				(field
					(name "Footprint") "gunnchos_production:QFN-16-1EP_3x3mm_P0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "UWB")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "DWM3001C")
			)
			(property
				(name "Role")
				(value "UWB_DNP")
			)
			(property
				(name "DNP")
				(value "TRUE")
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
			(tstamps "1d316335-05f4-93e4-5068-3befd7a22184")
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
	)
	(groups)
	(variants)
	(libparts
		(libpart
			(lib "")
			(part "ANT")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "ANT")
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
					(name "FEED")
					(type "passive")
				)
				(pin
					(num "2")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "3")
					(name "NC")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "BMI270")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "BMI270")
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
					(name "VDDIO")
					(type "passive")
				)
				(pin
					(num "3")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "4")
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "5")
					(name "SDA")
					(type "passive")
				)
				(pin
					(num "6")
					(name "INT1")
					(type "passive")
				)
			)
		)
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
			(part "CHGPOGO")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "CHGPOGO")
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
					(name "GND")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "ELEC")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "ELEC")
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
					(name "RX")
					(type "passive")
				)
				(pin
					(num "2")
					(name "GND")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "ESD")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "ESD")
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
					(name "IO")
					(type "passive")
				)
				(pin
					(num "2")
					(name "GND")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "HAP")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "HAP")
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
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "4")
					(name "SDA")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "IQS7222A")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "IQS7222A")
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
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "4")
					(name "SDA")
					(type "passive")
				)
				(pin
					(num "5")
					(name "RX0")
					(type "passive")
				)
				(pin
					(num "6")
					(name "TX0")
					(type "passive")
				)
				(pin
					(num "7")
					(name "RDY")
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
			(part "NPM1300")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "NPM1300")
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
					(name "VBAT")
					(type "passive")
				)
				(pin
					(num "3")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "4")
					(name "VOUTLDO1")
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
			(part "NRF52840")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "NRF52840")
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
					(name "P0.00_XL1")
					(type "passive")
				)
				(pin
					(num "2")
					(name "P0.01_XL2")
					(type "passive")
				)
				(pin
					(num "13")
					(name "VDD")
					(type "passive")
				)
				(pin
					(num "14")
					(name "VDDH")
					(type "passive")
				)
				(pin
					(num "15")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "16")
					(name "DEC1")
					(type "passive")
				)
				(pin
					(num "17")
					(name "DEC2")
					(type "passive")
				)
				(pin
					(num "32")
					(name "P0.06_I2C_SCL")
					(type "passive")
				)
				(pin
					(num "33")
					(name "P0.08_I2C_SDA")
					(type "passive")
				)
				(pin
					(num "42")
					(name "SWDIO")
					(type "passive")
				)
				(pin
					(num "43")
					(name "SWDCLK")
					(type "passive")
				)
				(pin
					(num "49")
					(name "EPAD")
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
			(part "SE050")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "SE050")
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
					(name "SCL")
					(type "passive")
				)
				(pin
					(num "4")
					(name "SDA")
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
				(pin
					(num "S1")
					(name "SHIELD")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "UWB")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "UWB")
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
					(name "SPI_CS")
					(type "passive")
				)
				(pin
					(num "4")
					(name "SPI_CLK")
					(type "passive")
				)
			)
		)
	)
	(libraries)
	(nets
		(net
			(code "1")
			(name "CAP_RX0")
			(class "Default")
			(node
				(ref "JE1")
				(pin "1")
				(pinfunction "RX_1")
				(pintype "passive")
			)
			(node
				(ref "U3")
				(pin "3")
				(pinfunction "SCL_3")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "CAP_TX0")
			(class "Default")
			(node
				(ref "U3")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "CC1")
			(class "Default")
			(node
				(ref "DESD1")
				(pin "1")
				(pinfunction "IO_1")
				(pintype "passive")
			)
			(node
				(ref "JUSB1")
				(pin "A7")
				(pinfunction "DM_A7")
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
			(code "4")
			(name "CC2")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "A4")
				(pinfunction "VBUS_A4")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "5")
				(pinfunction "SCL_5")
				(pintype "passive")
			)
		)
		(net
			(code "5")
			(name "GND")
			(class "Default")
			(node
				(ref "ANT1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
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
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JE1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JP1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JUSB1")
				(pin "A1")
				(pinfunction "GND_A1")
				(pintype "passive")
			)
			(node
				(ref "JUSB1")
				(pin "S1")
				(pinfunction "SHIELD_S1")
				(pintype "passive")
			)
			(node
				(ref "U1")
				(pin "14")
				(pinfunction "VDDH_14")
				(pintype "passive")
			)
			(node
				(ref "U1")
				(pin "2")
				(pinfunction "P0.01_XL2_2")
				(pintype "passive")
			)
			(node
				(ref "U2")
				(pin "3")
				(pinfunction "GND_3")
				(pintype "passive")
			)
			(node
				(ref "U3")
				(pin "6")
				(pinfunction "TX0_6")
				(pintype "passive")
			)
			(node
				(ref "U3V3")
				(pin "1")
				(pinfunction "VIN_1")
				(pintype "passive")
			)
			(node
				(ref "U4")
				(pin "3")
				(pinfunction "GND_3")
				(pintype "passive")
			)
			(node
				(ref "U5")
				(pin "4")
				(pinfunction "SDA_4")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "4")
				(pinfunction "GND_4")
				(pintype "passive")
			)
			(node
				(ref "UHAP1")
				(pin "4")
				(pinfunction "SDA_4")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
			(node
				(ref "UWBDNP")
				(pin "4")
				(pinfunction "SPI_CLK_4")
				(pintype "passive")
			)
		)
		(net
			(code "6")
			(name "I2C_SCL")
			(class "Default")
			(node
				(ref "R1")
				(pin "2")
				(pintype "passive")
			)
			(node
				(ref "U1")
				(pin "16")
				(pinfunction "DEC1_16")
				(pintype "passive")
			)
			(node
				(ref "U2")
				(pin "1")
				(pinfunction "VBUS_1")
				(pintype "passive")
			)
			(node
				(ref "U3")
				(pin "5")
				(pinfunction "RX0_5")
				(pintype "passive")
			)
			(node
				(ref "U4")
				(pin "4")
				(pinfunction "SCL_4")
				(pintype "passive")
			)
			(node
				(ref "U5")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "1")
				(pinfunction "VBUS_1")
				(pintype "passive")
			)
			(node
				(ref "UHAP1")
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
			(code "7")
			(name "I2C_SDA")
			(class "Default")
			(node
				(ref "U1")
				(pin "13")
				(pinfunction "VDD_13")
				(pintype "passive")
			)
			(node
				(ref "U2")
				(pin "2")
				(pinfunction "VBAT_2")
				(pintype "passive")
			)
			(node
				(ref "U3")
				(pin "4")
				(pinfunction "SDA_4")
				(pintype "passive")
			)
			(node
				(ref "U4")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "U5")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "2")
				(pinfunction "SYS_2")
				(pintype "passive")
			)
			(node
				(ref "UHAP1")
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
			(code "8")
			(name "IMU_INT1")
			(class "Default")
			(node
				(ref "U4")
				(pin "2")
				(pinfunction "VDDIO_2")
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
			(name "RF_2G4")
			(class "Default")
			(node
				(ref "ANT1")
				(pin "3")
				(pinfunction "NC_3")
				(pintype "passive")
			)
		)
		(net
			(code "11")
			(name "SWDCLK")
			(class "Default")
			(node
				(ref "U1")
				(pin "17")
				(pinfunction "DEC2_17")
				(pintype "passive")
			)
		)
		(net
			(code "12")
			(name "SWDIO")
			(class "Default")
			(node
				(ref "U1")
				(pin "1")
				(pinfunction "P0.00_XL1_1")
				(pintype "passive")
			)
		)
		(net
			(code "13")
			(name "USB_DM")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "A5")
				(pinfunction "CC1_A5")
				(pintype "passive")
			)
		)
		(net
			(code "14")
			(name "USB_DP")
			(class "Default")
			(node
				(ref "JUSB1")
				(pin "A6")
				(pinfunction "DP_A6")
				(pintype "passive")
			)
		)
		(net
			(code "15")
			(name "VBAT")
			(class "Default")
			(node
				(ref "U2")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
			(node
				(ref "UCHG1")
				(pin "3")
				(pinfunction "BAT_3")
				(pintype "passive")
			)
		)
		(net
			(code "16")
			(name "VBUS")
			(class "Default")
			(node
				(ref "JP1")
				(pin "1")
				(pinfunction "VBUS_1")
				(pintype "passive")
			)
			(node
				(ref "JUSB1")
				(pin "B5")
				(pinfunction "CC2_B5")
				(pintype "passive")
			)
			(node
				(ref "U2")
				(pin "5")
				(pinfunction "SCL_5")
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
			(code "17")
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
				(ref "U1")
				(pin "33")
				(pinfunction "P0.08_I2C_SDA_33")
				(pintype "passive")
			)
			(node
				(ref "U2")
				(pin "4")
				(pinfunction "VOUTLDO1_4")
				(pintype "passive")
			)
			(node
				(ref "U3")
				(pin "7")
				(pinfunction "RDY_7")
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
				(ref "U4")
				(pin "5")
				(pinfunction "SDA_5")
				(pintype "passive")
			)
			(node
				(ref "U4")
				(pin "6")
				(pinfunction "INT1_6")
				(pintype "passive")
			)
			(node
				(ref "U5")
				(pin "3")
				(pinfunction "SCL_3")
				(pintype "passive")
			)
			(node
				(ref "UHAP1")
				(pin "3")
				(pinfunction "SCL_3")
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
			(code "18")
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
			(code "19")
			(name "unconnected-(ANT1-FEED-Pad1)")
			(class "Default")
			(node
				(ref "ANT1")
				(pin "1")
				(pinfunction "FEED_1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "20")
			(name "unconnected-(U1-EPAD-Pad49)")
			(class "Default")
			(node
				(ref "U1")
				(pin "49")
				(pinfunction "EPAD_49")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "21")
			(name "unconnected-(U1-GND-Pad15)")
			(class "Default")
			(node
				(ref "U1")
				(pin "15")
				(pinfunction "GND_15")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "22")
			(name "unconnected-(U1-P0.06_I2C_SCL-Pad32)")
			(class "Default")
			(node
				(ref "U1")
				(pin "32")
				(pinfunction "P0.06_I2C_SCL_32")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "23")
			(name "unconnected-(U1-SWDCLK-Pad43)")
			(class "Default")
			(node
				(ref "U1")
				(pin "43")
				(pinfunction "SWDCLK_43")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "24")
			(name "unconnected-(U1-SWDIO-Pad42)")
			(class "Default")
			(node
				(ref "U1")
				(pin "42")
				(pinfunction "SWDIO_42")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "25")
			(name "unconnected-(U3-VDD-Pad1)")
			(class "Default")
			(node
				(ref "U3")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "26")
			(name "unconnected-(UWBDNP-GND-Pad2)")
			(class "Default")
			(node
				(ref "UWBDNP")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "27")
			(name "unconnected-(UWBDNP-SPI_CS-Pad3)")
			(class "Default")
			(node
				(ref "UWBDNP")
				(pin "3")
				(pinfunction "SPI_CS_3")
				(pintype "passive+no_connect")
			)
		)
		(net
			(code "28")
			(name "unconnected-(UWBDNP-VDD-Pad1)")
			(class "Default")
			(node
				(ref "UWBDNP")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive+no_connect")
			)
		)
	)
)
