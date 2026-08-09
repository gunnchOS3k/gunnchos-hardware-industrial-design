(export
	(version "E")
	(design
		(source "/Users/gunnchos/Downloads/gunnchos-7gc-research-product-spine/repos/gunnchos-hardware-industrial-design/device_designs/ds_xl_coder/kicad/ds_xl_coder.kicad_sch")
		(date "2026-08-09T15:51:11")
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
				(title "DS-XL Coder Carrier — Cont IX Option B + dual display")
				(company "gunnchOS3k / CONTINUATION IX")
				(rev "0.6.0-cont-ix")
				(date "2026-08-09")
				(source "ds_xl_coder.kicad_sch")
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
					(value "Compute MPN: COM-HPC-mMTL-155H-32G")
				)
				(comment
					(number "4")
					(value "Engineerability: PUBLIC_DOCS_FEATURE_GROUPS")
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
			(ref "JAUD1")
			(value "AUDIO")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "AUDIO_CONN")
				(field
					(name "Role") "AUDIO")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "AUDIO_CONN")
			)
			(property
				(name "Role")
				(value "AUDIO")
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
			(tstamps "f8ad438b-b16a-85a3-efc7-4cf5dbdce8bb")
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
			(ref "JBAT1")
			(value "BATTERY_BMS")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "BATTERY_BMS_CONN")
				(field
					(name "Role") "BATTERY_BMS")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "BATTERY_BMS_CONN")
			)
			(property
				(name "Role")
				(value "BATTERY_BMS")
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
			(tstamps "3a3c78fc-3fc4-58e2-1014-b1d9d824d7e6")
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
			(ref "JCAM1")
			(value "CAMERA")
			(footprint "gunnchos_production:FFC_40P_0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "CAMERA_CONN")
				(field
					(name "Role") "CAMERA")
				(field
					(name "Footprint") "gunnchos_production:FFC_40P_0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "CAMERA_CONN")
			)
			(property
				(name "Role")
				(value "CAMERA")
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
			(tstamps "1de8a305-6454-21fc-8ef7-12d135ce1900")
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
			(ref "JDBG1")
			(value "DEBUG")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "DEBUG_CONN")
				(field
					(name "Role") "DEBUG")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "DEBUG_CONN")
			)
			(property
				(name "Role")
				(value "DEBUG")
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
			(tstamps "0d52d9b5-c2b6-33d5-3195-1da390e3a1b8")
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
			(ref "JDISP1")
			(value "eDP_primary_panel")
			(footprint "gunnchos_production:FFC_40P_0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "PANEL_AVL_PENDING")
				(field
					(name "Role") "DISPLAY")
				(field
					(name "Footprint") "gunnchos_production:FFC_40P_0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "PANEL_EDP")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "PANEL_AVL_PENDING")
			)
			(property
				(name "Role")
				(value "DISPLAY")
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
			(tstamps "44656068-d01a-9c6a-7b59-243ea1a6171c")
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
			(ref "JDISP2")
			(value "eDP_secondary_panel")
			(footprint "gunnchos_production:FFC_40P_0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "PANEL2_AVL_PENDING")
				(field
					(name "Role") "DISPLAY2")
				(field
					(name "Footprint") "gunnchos_production:FFC_40P_0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "PANEL_EDP2")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "PANEL2_AVL_PENDING")
			)
			(property
				(name "Role")
				(value "DISPLAY2")
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
			(tstamps "5a708bb0-eae8-c815-4a00-583431b90832")
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
			(ref "JEC1")
			(value "EC_FAN")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "EC_FAN_CONN")
				(field
					(name "Role") "EC_FAN")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "EC_FAN_CONN")
			)
			(property
				(name "Role")
				(value "EC_FAN")
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
			(tstamps "b846095b-9664-c69b-9d82-3122942113f2")
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
			(ref "JETH1")
			(value "ETHERNET")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "ETHERNET_CONN")
				(field
					(name "Role") "ETHERNET")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "ETHERNET_CONN")
			)
			(property
				(name "Role")
				(value "ETHERNET")
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
			(tstamps "90e942f2-a398-3702-3424-96c5ad34a17a")
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
			(ref "JKEY1")
			(value "KEYBOARD")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "KEYBOARD_CONN")
				(field
					(name "Role") "KEYBOARD")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "KEYBOARD_CONN")
			)
			(property
				(name "Role")
				(value "KEYBOARD")
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
			(tstamps "4457ab3e-0d4a-d98a-0272-7440146ae1bb")
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
			(ref "JNVME1")
			(value "NVME")
			(footprint "gunnchos_production:FFC_40P_0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "NVME_CONN")
				(field
					(name "Role") "NVME")
				(field
					(name "Footprint") "gunnchos_production:FFC_40P_0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "NVME_CONN")
			)
			(property
				(name "Role")
				(value "NVME")
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
			(tstamps "0807da59-ffeb-2272-f801-7fc83e0585d2")
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
			(ref "JSEC1")
			(value "SECURITY")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "SECURITY_CONN")
				(field
					(name "Role") "SECURITY")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "SECURITY_CONN")
			)
			(property
				(name "Role")
				(value "SECURITY")
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
			(tstamps "8272c96e-1af5-68c9-0106-3c2ccb6f9258")
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
			(ref "JSIM1")
			(value "SIM")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "SIM_CONN")
				(field
					(name "Role") "SIM")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "SIM_CONN")
			)
			(property
				(name "Role")
				(value "SIM")
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
			(tstamps "4de0165d-5c87-a028-68df-83595b2b3f67")
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
			(ref "JTRK1")
			(value "TRACKPAD")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "TRACKPAD_CONN")
				(field
					(name "Role") "TRACKPAD")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "TRACKPAD_CONN")
			)
			(property
				(name "Role")
				(value "TRACKPAD")
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
			(tstamps "3e2f6f5b-bcfe-b218-63d9-0f99ef8fff77")
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
			(ref "JWIFI1")
			(value "WIFI")
			(footprint "gunnchos_production:DFN1006-2")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "WIFI_CONN")
				(field
					(name "Role") "WIFI")
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
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "WIFI_CONN")
			)
			(property
				(name "Role")
				(value "WIFI")
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
			(tstamps "15e91a8a-f3c1-cb49-9851-1ec06ab010d4")
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
			(ref "JWWAN1")
			(value "WWAN")
			(footprint "gunnchos_production:FFC_40P_0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "WWAN_CONN")
				(field
					(name "Role") "WWAN")
				(field
					(name "Footprint") "gunnchos_production:FFC_40P_0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "PERIPH")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "WWAN_CONN")
			)
			(property
				(name "Role")
				(value "WWAN")
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
			(tstamps "c7ab4288-d587-1ea4-af2a-16712ec01fab")
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
			(ref "UCOM1")
			(value "COM-HPC-mMTL-155H-32G")
			(footprint "gunnchos_production:COMHPC_Mini_envelope")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "COM-HPC-mMTL-155H-32G")
				(field
					(name "Role") "COM_MODULE")
				(field
					(name "Evidence") "PUBLIC_DOCS")
				(field
					(name "NDA") "400PIN_EXTERNAL")
				(field
					(name "Footprint") "gunnchos_production:COMHPC_Mini_envelope")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "COMHPC_PUBLIC")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "COM-HPC-mMTL-155H-32G")
			)
			(property
				(name "Role")
				(value "COM_MODULE")
			)
			(property
				(name "Evidence")
				(value "PUBLIC_DOCS")
			)
			(property
				(name "NDA")
				(value "400PIN_EXTERNAL")
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
			(tstamps "9e957e23-e32b-34a1-16eb-1f3c9f8eb039")
			(units
				(unit
					(name "A")
					(pins
						(pin
							(num "VIN")
						)
						(pin
							(num "PWRBTN")
						)
						(pin
							(num "GND")
						)
						(pin
							(num "UART_TX")
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
			(ref "UTPM1")
			(value "SLB9672XQ2.0")
			(footprint "gunnchos_production:VQFN-32-1EP_5x5mm_P0.5mm")
			(fields
				(field
					(name "ContIX") "PRODUCTION")
				(field
					(name "MPN") "SLB9672XQ2.0")
				(field
					(name "Role") "TPM")
				(field
					(name "Footprint") "gunnchos_production:VQFN-32-1EP_5x5mm_P0.5mm")
				(field
					(name "Datasheet")
				)
				(field
					(name "Description")
				)
			)
			(libsource
				(lib "")
				(part "TPM")
				(description "")
			)
			(property
				(name "ContIX")
				(value "PRODUCTION")
			)
			(property
				(name "MPN")
				(value "SLB9672XQ2.0")
			)
			(property
				(name "Role")
				(value "TPM")
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
			(tstamps "c835f675-4b80-3add-c3f3-21fbf59f6139")
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
			(part "COMHPC_PUBLIC")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "COMHPC_PUBLIC")
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
					(num "GND")
					(name "GND")
					(type "passive")
				)
				(pin
					(num "PWRBTN")
					(name "PWRBTN")
					(type "passive")
				)
				(pin
					(num "UART_TX")
					(name "UART_TX")
					(type "passive")
				)
				(pin
					(num "VIN")
					(name "VIN_12V")
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
			(part "PANEL_EDP")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "PANEL_EDP")
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
					(name "EDP_TX0N")
					(type "passive")
				)
				(pin
					(num "4")
					(name "EDP_TX0P")
					(type "passive")
				)
				(pin
					(num "5")
					(name "BL_EN")
					(type "passive")
				)
				(pin
					(num "6")
					(name "BL_PWM")
					(type "passive")
				)
				(pin
					(num "7")
					(name "T_SCL")
					(type "passive")
				)
				(pin
					(num "8")
					(name "T_SDA")
					(type "passive")
				)
			)
		)
		(libpart
			(lib "")
			(part "PANEL_EDP2")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "PANEL_EDP2")
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
					(name "EDP_TX0N")
					(type "passive")
				)
				(pin
					(num "4")
					(name "EDP_TX0P")
					(type "passive")
				)
				(pin
					(num "5")
					(name "HINGE")
					(type "passive")
				)
				(pin
					(num "6")
					(name "BL_PWM")
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
			(part "PERIPH")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "PERIPH")
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
					(name "SIG")
					(type "passive")
				)
				(pin
					(num "4")
					(name "CTRL")
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
			(part "TPM")
			(fields
				(field
					(name "Reference") "U")
				(field
					(name "Value") "TPM")
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
				(pin
					(num "5")
					(name "SPI_MOSI")
					(type "passive")
				)
				(pin
					(num "6")
					(name "SPI_MISO")
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
	)
	(libraries)
	(nets
		(net
			(code "1")
			(name "BL_EN")
			(class "Default")
			(node
				(ref "JDISP1")
				(pin "3")
				(pinfunction "EDP_TX0N_3")
				(pintype "passive")
			)
		)
		(net
			(code "2")
			(name "BL_PWM")
			(class "Default")
			(node
				(ref "JDISP1")
				(pin "4")
				(pinfunction "EDP_TX0P_4")
				(pintype "passive")
			)
		)
		(net
			(code "3")
			(name "BL_PWM2")
			(class "Default")
			(node
				(ref "JDISP2")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
		)
		(net
			(code "4")
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
			(code "5")
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
			(code "6")
			(name "COM_VIN")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "PWRBTN")
				(pinfunction "PWRBTN_PWRBTN")
				(pintype "passive")
			)
		)
		(net
			(code "7")
			(name "EDP0_N")
			(class "Default")
			(node
				(ref "JDISP1")
				(pin "5")
				(pinfunction "BL_EN_5")
				(pintype "passive")
			)
		)
		(net
			(code "8")
			(name "EDP0_P")
			(class "Default")
			(node
				(ref "JDISP1")
				(pin "6")
				(pinfunction "BL_PWM_6")
				(pintype "passive")
			)
		)
		(net
			(code "9")
			(name "EDP1_N")
			(class "Default")
			(node
				(ref "JDISP2")
				(pin "3")
				(pinfunction "EDP_TX0N_3")
				(pintype "passive")
			)
		)
		(net
			(code "10")
			(name "EDP1_P")
			(class "Default")
			(node
				(ref "JDISP2")
				(pin "4")
				(pinfunction "EDP_TX0P_4")
				(pintype "passive")
			)
		)
		(net
			(code "11")
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
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JAUD1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JAUD1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JBAT1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JBAT1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JCAM1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JCAM1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JDBG1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JDBG1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JDISP1")
				(pin "8")
				(pinfunction "T_SDA_8")
				(pintype "passive")
			)
			(node
				(ref "JDISP2")
				(pin "6")
				(pinfunction "BL_PWM_6")
				(pintype "passive")
			)
			(node
				(ref "JEC1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JEC1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JETH1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JETH1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JKEY1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JKEY1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JNVME1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JNVME1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JSEC1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JSEC1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JSIM1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JSIM1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JTRK1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JTRK1")
				(pin "4")
				(pinfunction "CTRL_4")
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
				(ref "JWIFI1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JWIFI1")
				(pin "4")
				(pinfunction "CTRL_4")
				(pintype "passive")
			)
			(node
				(ref "JWWAN1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
			(node
				(ref "JWWAN1")
				(pin "4")
				(pinfunction "CTRL_4")
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
				(ref "UCOM1")
				(pin "UART_TX")
				(pinfunction "UART_TX_UART_TX")
				(pintype "passive")
			)
			(node
				(ref "UPD1")
				(pin "6")
				(pinfunction "SDA_6")
				(pintype "passive")
			)
			(node
				(ref "UTPM1")
				(pin "6")
				(pinfunction "SPI_MISO_6")
				(pintype "passive")
			)
		)
		(net
			(code "12")
			(name "HINGE_FLEX")
			(class "Default")
			(node
				(ref "JDISP2")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
		)
		(net
			(code "13")
			(name "I2C_SCL")
			(class "Default")
			(node
				(ref "JDISP1")
				(pin "1")
				(pinfunction "VDD_1")
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
				(ref "UPD1")
				(pin "3")
				(pinfunction "CC2_3")
				(pintype "passive")
			)
		)
		(net
			(code "14")
			(name "I2C_SDA")
			(class "Default")
			(node
				(ref "JDISP1")
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
				(ref "UPD1")
				(pin "4")
				(pinfunction "GND_4")
				(pintype "passive")
			)
		)
		(net
			(code "15")
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
			(code "16")
			(name "PWRBTN")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "VIN")
				(pinfunction "VIN_12V_VIN")
				(pintype "passive")
			)
		)
		(net
			(code "17")
			(name "SPI_CLK")
			(class "Default")
			(node
				(ref "UTPM1")
				(pin "4")
				(pinfunction "SPI_CLK_4")
				(pintype "passive")
			)
		)
		(net
			(code "18")
			(name "SPI_CS")
			(class "Default")
			(node
				(ref "UTPM1")
				(pin "3")
				(pinfunction "SPI_CS_3")
				(pintype "passive")
			)
		)
		(net
			(code "19")
			(name "SPI_MISO")
			(class "Default")
			(node
				(ref "UTPM1")
				(pin "2")
				(pinfunction "GND_2")
				(pintype "passive")
			)
		)
		(net
			(code "20")
			(name "SPI_MOSI")
			(class "Default")
			(node
				(ref "UTPM1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
		)
		(net
			(code "21")
			(name "UART_TX")
			(class "Default")
			(node
				(ref "UCOM1")
				(pin "GND")
				(pinfunction "GND_GND")
				(pintype "passive")
			)
		)
		(net
			(code "22")
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
			(code "23")
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
			(code "24")
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
			(code "25")
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
			(code "26")
			(name "VDD_3V3")
			(class "Default")
			(node
				(ref "C1")
				(pin "1")
				(pintype "passive")
			)
			(node
				(ref "JAUD1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JAUD1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JBAT1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JBAT1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JCAM1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JCAM1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JDBG1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JDBG1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JDISP1")
				(pin "7")
				(pinfunction "T_SCL_7")
				(pintype "passive")
			)
			(node
				(ref "JDISP2")
				(pin "5")
				(pinfunction "HINGE_5")
				(pintype "passive")
			)
			(node
				(ref "JEC1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JEC1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JETH1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JETH1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JKEY1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JKEY1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JNVME1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JNVME1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JSEC1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JSEC1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JSIM1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JSIM1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JTRK1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JTRK1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JWIFI1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JWIFI1")
				(pin "3")
				(pinfunction "SIG_3")
				(pintype "passive")
			)
			(node
				(ref "JWWAN1")
				(pin "1")
				(pinfunction "VDD_1")
				(pintype "passive")
			)
			(node
				(ref "JWWAN1")
				(pin "3")
				(pinfunction "SIG_3")
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
				(ref "UPD1")
				(pin "2")
				(pinfunction "CC1_2")
				(pintype "passive")
			)
			(node
				(ref "UTPM1")
				(pin "5")
				(pinfunction "SPI_MOSI_5")
				(pintype "passive")
			)
		)
		(net
			(code "27")
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
	)
)
