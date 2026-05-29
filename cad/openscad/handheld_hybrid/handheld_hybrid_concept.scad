include <../common/dimensions.scad>
include <../common/ports.scad>

body_l=180; body_w=80; body_h=22;

module handheld_body() {
  difference() {
    minkowski() {
      cube([body_l-2*corner_r, body_w-2*corner_r, body_h], center=true);
      cylinder(r=corner_r, h=0.01, $fn=32);
    }
  }
}

module screen_cutout() {
  translate([0,8,body_h/2-1]) cube([body_l-30, 2, body_w-20], center=true);
}

module controls() {
  // sticks
  translate([-35,-15,body_h/2]) cylinder(h=8, d=12, $fn=32);
  translate([35,-15,body_h/2]) cylinder(h=8, d=12, $fn=32);
  // d-pad
  translate([-35,15,body_h/2]) cube([16,16,3], center=true);
  // ABXY
  for (a=[0:3]) rotate([0,0,a*90]) translate([35,15,body_h/2]) cylinder(h=3, d=8, $fn=24);
  // shoulders
  translate([-body_l/2+10, -body_w/2+5, body_h/2+2]) cube([30,6,4], center=true);
  translate([body_l/2-10, -body_w/2+5, body_h/2+2]) cube([30,6,4], center=true);
}

difference() {
  union() { handheld_body(); controls(); }
  screen_cutout();
  // USB-C bottom
  translate([0,-body_w/2+2, -5]) rotate([90,0,0]) usb_c_cutout();
  // speaker grills
  for (i=[-2:2]) translate([i*15, body_w/2-3, 0]) cube([8,2,body_h+2], center=true);
  // dock groove
  translate([0,-body_w/2+6, -body_h/2]) cube([60,4,3], center=true);
}
