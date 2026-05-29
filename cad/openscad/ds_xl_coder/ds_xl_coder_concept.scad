include <../common/dimensions.scad>
include <../common/ports.scad>

clamshell_l=160; clamshell_w=90; thickness=12;

module half(label_z) {
  difference() {
    translate([0,0,label_z]) minkowski() {
      cube([clamshell_l-2*corner_r, clamshell_w-2*corner_r, thickness], center=true);
      cylinder(r=corner_r, h=0.01, $fn=32);
    }
    // screen recess
    translate([0,5,label_z+thickness/2-1]) cube([clamshell_l-20, 2, clamshell_w-25], center=true);
  }
}

// hinge
translate([0,-clamshell_w/2+8,0]) rotate([0,90,0]) cylinder(h=clamshell_w-16, r=5, $fn=48);

difference() {
  union() {
    translate([0,0,thickness/2+2]) half(thickness/2+2);   // lower code screen
    translate([0,0,thickness*1.5+8]) half(thickness*1.5+8); // upper preview
  }
  translate([clamshell_l/2-4, -clamshell_w/2+10, thickness/2]) rotate([90,0,0]) usb_c_cutout();
  // pogo keyboard connector
  translate([0,-clamshell_w/2+4, thickness/2]) cube([50,2,2], center=true);
}
