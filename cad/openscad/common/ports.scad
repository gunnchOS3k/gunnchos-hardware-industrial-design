module usb_c_cutout() {
  translate([0,0,-1]) cube([9, 3.5, wall+2], center=true);
}
module usb_a_cutout() {
  translate([0,0,-1]) cube([12, 5, wall+2], center=true);
}
module audio_3_5_cutout() {
  translate([0,0,-1]) cylinder(h=wall+2, d=6, $fn=32);
}
