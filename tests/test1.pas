program test;
begin
  x := 1;
  y := 2;
  z := 5;
  proc;
  read(x,y,z);
  write(x,y,x+y);
  read(y);
  if -x <> y*1 then
    write(x)
  else
    write(y);
  read(z);
  if not "holi" = (y and 1 = 2) then
  begin
    write("hola");
    write("chao")
  end
  else
  begin
    read(z);
    y := x + 1
  end;
  read(x)
end.
