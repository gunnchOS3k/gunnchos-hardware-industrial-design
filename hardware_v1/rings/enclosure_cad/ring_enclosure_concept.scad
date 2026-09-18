// Stream E — ring enclosure concept (digital). Ergonomics PENDING physical.
$fn = 64;
inner_r = 9.5;
outer_r = 12.0;
height = 6.5;
difference() {
  cylinder(h=height, r=outer_r);
  translate([0,0,-1]) cylinder(h=height+2, r=inner_r);
  translate([0, outer_r-1.2, height/2]) cube([8, 2.5, 3], center=true); // antenna window placeholder
}
