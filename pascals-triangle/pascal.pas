{ Bytes
program PascalsTriangle;const R=19;var
T:array[0..R,0..R]of longint;i,j:integer;
begin
for i:=0 to R do
begin
T[i,0]:=1;T[i,i]:=1;for j:=1 to i-1 do
T[i,j]:=T[i-1,j-1]+T[i-1,j];end;for i:=0 to R do
begin
for j:=0 to i do
write(T[i,j],' ');writeln;end;end.
{ --
{ Chars
{ (same as bytes)
