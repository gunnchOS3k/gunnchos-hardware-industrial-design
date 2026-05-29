module gunnch_badge() {
  linear_extrude(badge_h) translate([0,0,0]) square([badge_w, badge_w/3], center=true);
}
