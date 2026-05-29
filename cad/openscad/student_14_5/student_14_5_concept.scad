include <../common/dimensions.scad>
include <../common/ports.scad>
include <../common/branding.scad>

base_l=320; base_w=220; base_h=18;
screen_l=300; screen_w=200; screen_t=6;

module student_base() {
  difference() {
    hull() {
      translate([0,0,base_h/2]) minkowski() {
        cube([base_l-2*corner_r, base_w-2*corner_r, base_h], center=true);
        cylinder(r=corner_r, h=0.01, $fn=32);
      }
      // keyboard deck
      translate([0,-20,base_h]) cube([base_l-40, base_w-60, 3], center=true);
      // trackpad
      translate([0,55,base_h+1]) cube([70,45,1.5], center=true);
    }
    // vent slots
    for (i=[-4:4]) translate([-80+i*20, -base_w/2+8, base_h/2]) cube([14, 2, base_h+2], center=true);
    // ports left
    translate([-base_l/2+2, 30, base_h/2]) usb_c_cutout();
    translate([-base_l/2+2, 10, base_h/2]) usb_c_cutout();
    translate([-base_l/2+2, -10, base_h/2]) usb_a_cutout();
    translate([-base_l/2+2, -30, base_h/2]) usb_a_cutout();
    translate([base_l/2-2, 0, base_h/2]) rotate([0,90,0]) audio_3_5_cutout();
  }
}

module student_screen() {
  difference() {
    translate([0,-base_w/2+screen_w/2+10, base_h+screen_t/2+40]) cube([screen_l, screen_t, screen_w], center=true);
    translate([0,-base_w/2+screen_w/2+10, base_h+screen_t/2+40]) cube([screen_l-10, screen_t+2, screen_w-10], center=true);
  }
  // hinge
  translate([0,-base_w/2+15, base_h+20]) rotate([90,0,0]) cylinder(h=screen_w-20, r=4, $fn=48);
}

union() {
  student_base();
  student_screen();
  translate([0,70,base_h+2]) gunnch_badge();
}
