// Stream E dock enclosure concept
module dock_shell() {
  difference() {
    cube([180, 80, 28], center=true);
    translate([0,0,2]) cube([172, 72, 28], center=true);
    for (x=[-60,60]) translate([x, -40, 0]) cube([12, 20, 10], center=true); // USB-C
    translate([0, -40, 0]) cube([16, 20, 12], center=true); // RJ45
  }
}
dock_shell();
