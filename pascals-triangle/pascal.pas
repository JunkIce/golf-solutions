{ Bytes
program PascalsTriangle;
const Rows=19;
var
	Triangle: array[0..Rows, 0..Rows] of longint;
	i, j: integer;
begin
  for i := 0 to Rows do
  begin
    Triangle[i, 0] := 1;
    Triangle[i, i] := 1;
    for j := 1 to i - 1 do
      Triangle[i, j] := Triangle[i - 1, j - 1] + Triangle[i - 1, j];
  end;
  for i := 0 to Rows do
  begin
    for j := 0 to i do
      write(Triangle[i, j], ' ');
    writeln;
  end;
end.
{ --
{ Chars
program PascalsTriangle;
const Rows=19;
var
	Triangle: array[0..Rows, 0..Rows] of longint;
	i, j: integer;
begin
  for i := 0 to Rows do
  begin
    Triangle[i, 0] := 1;
    Triangle[i, i] := 1;
    for j := 1 to i - 1 do
      Triangle[i, j] := Triangle[i - 1, j - 1] + Triangle[i - 1, j];
  end;
  for i := 0 to Rows do
  begin
    for j := 0 to i do
      write(Triangle[i, j], ' ');
    writeln;
  end;
end.

