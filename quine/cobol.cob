*> Bytes
       program-id. q.
       data division.
       working-storage section.
       01 p pic x value '.'.
       01 s pic x(7).
       01 n pic 99.
       01 source-code.
       05 value "05 value                                      ".
       05 value "program-id. q.                                ".
       05 value "data division.                                ".
       05 value "working-storage section.                      ".
       05 value "01 p pic x value '.'.                         ".
       05 value "01 s pic x(7).                                ".
       05 value "01 n pic 99.                                  ".
       05 value "01 source-code.                               ".
       05 value "01 elements redefines source-code.            ".
       05 value "05 element pic x(46) occurs 22 times.         ".
       05 value "procedure division.                           ".
       05 value "perform varying n from 2 by 1 until n > 8     ".
       05 value "  display s function trim(element(n) trailing)".
       05 value "end-perform                                   ".
       05 value "perform varying n from 1 by 1 until n > 22    ".
       05 value "  display s function trim(element(1))         ".
       05 value "          space quote element(n) quote p      ".
       05 value "end-perform                                   ".
       05 value "perform varying n from 9 by 1 until n > 22    ".
       05 value "  display s function trim(element(n) trailing)".
       05 value "end-perform                                   ".
       05 value "goback.                                       ".
       01 elements redefines source-code.
       05 element pic x(46) occurs 22 times.
       procedure division.
       perform varying n from 2 by 1 until n > 8
         display s function trim(element(n) trailing)
       end-perform
       perform varying n from 1 by 1 until n > 22
         display s function trim(element(1))
                 space quote element(n) quote p
       end-perform
       perform varying n from 9 by 1 until n > 22
         display s function trim(element(n) trailing)
       end-perform
       goback.

*> --
*> Chars
*> (same as bytes)
