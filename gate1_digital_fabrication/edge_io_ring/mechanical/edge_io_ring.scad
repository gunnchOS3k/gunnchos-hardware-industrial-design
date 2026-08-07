// Edge I/O Ring enclosure — digital prototype geometry
// Sizes US 7..10 parameterized
inner_d = 18.2; // US ~8 baseline
wall = 1.2;
band_h = 8.5;
pcb_od = 22.0;
pcb_id = 16.0;
battery_cavity_w = 12; battery_cavity_h = 4; battery_cavity_d = 22;
antenna_keepout_deg = 60;
module band() {
  difference() {
    cylinder(h=band_h, r=inner_d/2 + wall + 2.5, $fn=128);
    translate([0,0,-0.1]) cylinder(h=band_h+0.2, r=inner_d/2, $fn=128);
    // electronics cavity
    translate([0,0,1.2]) cylinder(h=2.0, r=pcb_od/2+0.15, $fn=128);
    // battery cavity
    translate([-battery_cavity_d/2, inner_d/2+0.2, 2]) cube([battery_cavity_d, battery_cavity_w, battery_cavity_h]);
    // charge pogo access
    translate([0, -(inner_d/2+1.0), 3]) rotate([90,0,0]) cylinder(h=3, r=0.6, $fn=32);
    translate([2, -(inner_d/2+1.0), 3]) rotate([90,0,0]) cylinder(h=3, r=0.6, $fn=32);
  }
}
band();
