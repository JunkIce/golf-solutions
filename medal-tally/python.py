# Bytes
import sys
for l in sys.argv[1:]:
	l=l.split();d=g=p=0;m=[0]*3
	for x in l:
		if g!=x:p+=m[p]
		if p>2:break
		d|=l.index(x)<1and l.count(x)<2
		m[p]+=1;g=x
	print(f"{'1💎 '*d}{m[0]}🥇{f' {m[1]}🥈'if m[1]else''}{f' {m[2]}🥉'if m[2]else''}")
# --
# Chars
exec(bytes('浩潰瑲猠獹昊牯氠椠⁮祳⹳牡癧ㅛ崺਺氉氽献汰瑩⤨搻朽瀽〽活嬽崰㌪ऊ潦⁲⁸湩氠਺उ晩朠㴡㩸⭰洽灛੝उ晩瀠㈾戺敲歡ऊ搉㵼⹬湩敤⡸⥸ㄼ湡⁤⹬潣湵⡴⥸㈼ऊ洉灛⭝ㄽ朻砽ऊ牰湩⡴≦❻銟₎⨧絤浻せ絝鿰螥晻‧浻ㅛ絝鿰袥椧⁦孭崱汥敳✧筽❦笠孭崲ꖟ➉晩洠㉛敝獬❥紧⤢','u16')[2:])
