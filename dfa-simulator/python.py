# Bytes
import sys
for n in sys.argv[1:]:
	n=n.split('\n');S=n[0].split();G=n[1:-1];I=n[-1][1:-1];g={};A=p=''
	for w in G:
		g[R:=w[2]]=w[4:].split()
		if w[0]=='>':p=R
		if w[1]=='F':A+=R
	for i in I:p=g[p][S.index(i)]
	print(p,['Reject','Accept'][p in A])
# --
# Chars
exec(bytes('浩潰瑲猠獹昊牯渠椠⁮祳⹳牡癧ㅛ崺਺渉渽献汰瑩✨湜⤧医渽せ⹝灳楬⡴㬩㵇孮㨱ㄭ㭝㵉孮ㄭ孝㨱ㄭ㭝㵧絻䄻瀽✽ਧ昉牯眠椠⁮㩇ऊ有剛㴺孷崲㵝孷㨴⹝灳楬⡴਩उ晩眠せ㵝✽✾瀺刽ऊ椉⁦孷崱㴽䘧㨧⭁刽ऊ潦⁲⁩湩䤠瀺朽灛孝⹓湩敤⡸⥩੝瀉楲瑮瀨嬬刧橥捥❴✬捁散瑰崧灛椠⁮嵁㬩','u16')[2:])
