# Bytes
import sys
for x in sys.argv[1:]:
	a,n=map(int,x.split());j=1
	while a:
		while a%2<1:a/=2;j*=[1,-1][n%8in[3,5]]
		a,n=n,a;j*=[1,-1][a%4>2and n%4>2];a%=n
	print(j*(n<2))
# --
# Chars
exec(bytes('浩潰瑲猠獹昊牯砠椠⁮祳⹳牡癧ㅛ崺਺愉測洽灡椨瑮砬献汰瑩⤨㬩㵪਱眉楨敬愠਺उ桷汩⁥╡㰲㨱⽡㈽樻㴪ㅛ⴬崱湛㠥湩㍛㔬嵝ऊ愉測渽愬樻㴪ㅛ⴬崱慛㐥㈾湡⁤╮㸴崲愻㴥੮瀉楲瑮樨⠪㱮⤲㬩','u16')[2:])
