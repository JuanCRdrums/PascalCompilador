program test;
var x,y,z : integer;
c : char;
procedure holi;
begin
  write("holi")
end;
procedure chau;
begin
  write("chau")
end;
begin
  x := -1*2 + (3 - 5);
  y := 2 div 3 div 5*3 - (3*5 + 2) div 2;
  z := 5;
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
