// Edge I/O Ring PCB 3D (digital)
od=22.0; id=16.0; t=0.8;
difference(){
  cylinder(h=t,r=od/2,$fn=128);
  translate([0,0,-0.1]) cylinder(h=t+0.2,r=id/2,$fn=128);
}
