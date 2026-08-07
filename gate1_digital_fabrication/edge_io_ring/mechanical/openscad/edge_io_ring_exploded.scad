// Edge I/O Ring EVT0 digital mechanical package — 2026-08-07T22:20:56Z
$fn = 128;
inner_d = 19.8; band_width = 8.0; wall = 1.6; outer_d = inner_d + 2*wall;
pcb_len = 28.0; pcb_w = 10.0; pcb_t = 0.8;
module ring_band() {
  difference() {
    cylinder(h=band_width, d=outer_d, center=true);
    cylinder(h=band_width+0.2, d=inner_d, center=true);
    translate([inner_d/2 + wall/2, 0, 0]) rotate([90,0,0]) cube([pcb_t+0.2, pcb_w+0.3, pcb_len+0.4], center=true);
    translate([outer_d/2 - 0.4, 0, 0]) sphere(d=4.2);
    translate([0, outer_d/2 - 0.2, 0]) rotate([90,0,0]) cylinder(h=2, d=2.2, center=true);
    translate([0, -outer_d/2 + 0.2, 0]) rotate([90,0,0]) cylinder(h=2, d=3.5, center=true);
  }
}
module exploded() {
  exploded();
  translate([0,0,12]) color("green") translate([inner_d/2 + wall/2,0,0]) rotate([90,0,0]) cube([pcb_t,pcb_w,pcb_len], center=true);
  translate([0,0,-12]) color("silver") translate([-inner_d/2 - wall/2,0,0]) cube([1.2,6.0,14.0], center=true);
  translate([18,0,0]) color("gray") cylinder(h=2.0, d=10.0, center=true);
}
exploded();
