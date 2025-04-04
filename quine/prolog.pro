% Bytes
:- initialization(main).
before(Lines) :- Lines = [
  ":- initialization(main).",
  "before(Lines) :- Lines = ["
].

after(Lines) :- Lines = [
  "].",
  "",
  "maskCode(34, 64).",
  "maskCode(92, 47).",
  "maskCode(10, 35).",
  "maskCode(X, X).",
  "",
  "encode(D, S) :- ",
  "  string_codes(D, DC),",
  "  maplist(maskCode, DC, SC),",
  "  string_codes(S, SC).",
  "",
  "decode(S, D) :- ",
  "  string_codes(S, SC),",
  "  maplist(maskCode, DC, SC),",
  "  string_codes(D, DC).",
  "",
  "mkStringList([],@@).",
  "mkStringList([Single],Out) :-",
  "  atomics_to_string([@  /@@, Single, @/@@], Out).",
  "",
  "mkStringList([H|T], Res) :-",
  "  mkStringList(T, TailRes),",
  "  atomics_to_string([@  /@@, H, @/@,/n@, TailRes], Res).",
  "",
  "quine(Q) :- ",
  "  before(BeforeEncoded),",
  "  after(AfterEncoded),",
  "  maplist(decode, BeforeEncoded, BeforeDecoded),",
  "  maplist(decode,  AfterEncoded, AfterDecoded),",
  "  atomic_list_concat(BeforeDecoded, @/n@, B),",
  "  atomic_list_concat(AfterDecoded, @/n@, A),",
  "  mkStringList(BeforeEncoded, BeforeData),",
  "  mkStringList(AfterEncoded, AfterData),",
  "  Center = @/n]./n/nafter(Lines) :- Lines = [/n@,",
  "  atomic_list_concat([",
  "     B, @/n@, BeforeData, ",
  "     Center, ",
  "     AfterData, @/n@, A, @/n@",
  "  ], Q).",
  "",
  "main :- (quine(Q), write(Q);true),halt."
].

maskCode(34, 64).
maskCode(92, 47).
maskCode(10, 35).
maskCode(X, X).

encode(D, S) :- 
  string_codes(D, DC),
  maplist(maskCode, DC, SC),
  string_codes(S, SC).

decode(S, D) :- 
  string_codes(S, SC),
  maplist(maskCode, DC, SC),
  string_codes(D, DC).

mkStringList([],"").
mkStringList([Single],Out) :-
  atomics_to_string(["  \"", Single, "\""], Out).

mkStringList([H|T], Res) :-
  mkStringList(T, TailRes),
  atomics_to_string(["  \"", H, "\",\n", TailRes], Res).

quine(Q) :- 
  before(BeforeEncoded),
  after(AfterEncoded),
  maplist(decode, BeforeEncoded, BeforeDecoded),
  maplist(decode,  AfterEncoded, AfterDecoded),
  atomic_list_concat(BeforeDecoded, "\n", B),
  atomic_list_concat(AfterDecoded, "\n", A),
  mkStringList(BeforeEncoded, BeforeData),
  mkStringList(AfterEncoded, AfterData),
  Center = "\n].\n\nafter(Lines) :- Lines = [\n",
  atomic_list_concat([
     B, "\n", BeforeData, 
     Center, 
     AfterData, "\n", A, "\n"
  ], Q).

main :- (quine(Q), write(Q);true),halt.

% --
% Chars
% (same as bytes)
