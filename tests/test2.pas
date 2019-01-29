(* fib.pas -  Compute fibonacci numbers *)

program fibonacci;
var n : int;                                  { Variable declaration }

(* A function declaration *)

procedure fib;
begin
        if n < 1 then                                  (* Conditionals *)
                fib := 1;
        fib := fib + fib
end;
begin
n := 10;
        while n < LAST do                       { Looping (while) }
        begin
                write(fibonacci);    { Printing }
                n := n + 1                              { Assignment }
        end
end.
