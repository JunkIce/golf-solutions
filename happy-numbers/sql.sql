-- Bytes
WITH s(n,r)AS(SELECT'','¢¨«®´¸½ÀÁÍÒåçðó÷üÿĂąĈĎĢģĦĬňőŝşšŢ'UNION SELECT substr(r,1,1),substr(r,2)FROM s WHERE r>'')SELECT unicode(n)-161 FROM s;
-- --
-- Chars
-- (same as bytes)
