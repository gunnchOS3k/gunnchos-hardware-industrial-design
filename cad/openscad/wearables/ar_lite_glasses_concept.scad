// EVT-0 AR-lite frame
scale([1.2,1,1]) difference() {
  union() {
    translate([-50,0,0]) cube([100,5,5]);
    translate([-55,-25,0]) cylinder(h=5,d=8);
    translate([45,-25,0]) cylinder(h=5,d=8);
  }
  translate([0,0,-1]) cube([80,30,10], center=true);
}
