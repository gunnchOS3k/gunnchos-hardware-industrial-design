// EVT-1 common modules — dimensions/tolerances are placeholders, not final mechanical drawings
include <common/dimensions.scad>
include <common/ports.scad>
include <common/branding.scad>
include <common/labels.scad>

module screw_boss(r=2.5, h=6) { cylinder(r=r, h=h, $fn=24); }
module service_panel(w=40, h=20, t=2) { cube([w, h, t]); }
module cooling_vent(w=60, slots=5) {
  for (i=[0:slots-1]) translate([i*12-w/2, 0, 0]) cube([8, 2, 4], center=true);
}
module battery_compartment(w=80, d=60, h=8) { cube([w, d, h], center=true); }
module label_zone(w=30, h=10) { translate([0,0,0.1]) cube([w, h, 0.2]); }
