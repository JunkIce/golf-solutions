# Bytes
for n in range(9986):
	r,k,l,f=2,str(n),'',0
	while n>1:
		while n%r<1:l+=str(r);f+=1;n//=r
		r+=1
	if(f>1and sum(map(int,l))==sum(map(int,k))):print(k)
# --
# Chars
exec(bytes('潦⁲⁮湩爠湡敧㤨㠹⤶਺爉欬氬昬㈽猬牴渨Ⱙ✧〬ऊ桷汩⁥㹮㨱ऊ眉楨敬渠爥ㄼ氺㴫瑳⡲⥲昻㴫㬱⽮㴯ੲउ⭲ㄽऊ晩昨ㄾ湡⁤畳⡭慭⡰湩ⱴ⥬㴩猽浵洨灡椨瑮欬⤩㨩牰湩⡴⥫','u16')[2:])
