# Bytes
import sys
m={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
for r in sys.argv[1:]:
	n=0
	for i in range(len(r)):n+=m[r[i]]*(1if i==len(r)-1or m[r[i]]>=m[r[i+1]]else-1)
	print(n)
# --
# Chars
exec(bytes('浩潰瑲猠獹洊笽䤧㨧ⰱ嘧㨧ⰵ堧㨧〱✬❌㔺ⰰ䌧㨧〱ⰰ䐧㨧〵ⰰ䴧㨧〱〰੽潦⁲⁲湩猠獹愮杲孶㨱㩝ऊ㵮ਰ昉牯椠椠⁮慲杮⡥敬⡮⥲㨩⭮洽牛楛嵝⠪椱⁦㵩氽湥爨⴩漱⁲孭孲嵩㹝洽牛楛ㄫ嵝汥敳ㄭ਩瀉楲瑮渨㬩','u16')[2:])
