program test;
begin
  x := 1;
  y := 2;
  z := 5;
  proc;
  read(x,y,z);
  write(x,y,x+y);
  read(y);
  if x = y then
    write(x);
end.
