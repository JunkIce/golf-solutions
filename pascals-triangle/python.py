# Bytes
for n in range(20):
	r,s=1,[]
	for k in range(1,n+2):s+=[r];r=(r*(n-k+1)//k)
	print(*s)
# --
# Chars
exec(bytes('潦⁲⁮湩爠湡敧㈨⤰਺爉猬ㄽ嬬੝昉牯欠椠⁮慲杮⡥ⰱ⭮⤲猺㴫牛㭝㵲爨⠪⵮⭫⤱⼯⥫ऊ牰湩⡴猪㬩','u16')[2:])
