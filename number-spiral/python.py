# Bytes
x=y=e=0
t=[[-1]*10for _ in[0]*10]
d=[(0,1),(1,0),(0,-1),(-1,0)]
for i in range(100):
	t[x][y]=i;a,b=d[e];w,z=x+a,y+b
	if not(0<=w<10>z>=0>t[w][z]):a,b=d[e:=(e+1)%4];w,z=x+a,y+b
	x,y=w,z
for r in t:print(*[f"{n:2}"for n in r])
# --
# Chars
exec(bytes('㵸㵹㵥ਰ㵴孛ㄭ⩝〱潦⁲ 湩せ⩝〱੝㵤⡛ⰰ⤱⠬ⰱ⤰⠬ⰰㄭⰩ⴨ⰱ⤰੝潦⁲⁩湩爠湡敧ㄨ〰㨩ऊ孴嵸祛㵝㭩ⱡ㵢孤嵥眻稬砽愫礬戫ऊ晩渠瑯〨㴼㱷〱稾㴾㸰孴嵷穛⥝愺戬搽敛㴺攨ㄫ┩崴眻稬砽愫礬戫ऊⱸ㵹ⱷ੺潦⁲⁲湩琠瀺楲瑮⨨晛笢㩮紲昢牯渠椠⁮嵲㬩','u16')[2:])
