# Bytes
t=[[' 'for _ in[0]*32]for _ in[0]*16]
def f(x,y,s):
	if s<2:t[y][x]='▲'
	else:n=s//2;f(x,y,n);f(x-n,y+n,n);f(x+n,y+n,n)
f(15,0,16)
for r in t:print(''.join(r))
# --
# Chars
exec(bytes('㵴孛‧昧牯张椠孮崰㌪崲潦⁲ 湩せ⩝㘱੝敤⁦⡦ⱸⱹ⥳਺椉⁦㱳㨲孴嵹硛㵝늖ਧ攉獬㩥㵮⽳㈯昻砨礬測㬩⡦⵸Ɱ⭹Ɱ⥮昻砨渫礬渫測਩⡦㔱〬ㄬ⤶昊牯爠椠⁮㩴牰湩⡴✧樮楯⡮⥲㬩','u16')[2:])
