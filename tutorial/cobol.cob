*> Bytes
program-id.e.data division.local-storage section.
1 n pic 99 value 0.
1 i pic 9999.
1 a pic X(99).
procedure division.
display"Hello, World!"
perform 10 times
display n(2- function log10(n):)
add 1 to n
end-perform.
accept i from argument-number
perform i times
accept a from argument-value
display a
end-perform.
*> --
*> Chars
*> (same as bytes)
