# Bytes
p=[i:=1]+[0]*99
for _ in p:
	for j in range(i,100):p[j]+=p[j-i]
	i+=1
*map(print,p),
# --
# Chars
exec(bytes('㵰楛㴺崱嬫崰㤪ਹ潦⁲ 湩瀠਺昉牯樠椠⁮慲杮⡥Ⱪ〱⤰瀺橛⭝瀽橛椭੝椉㴫਱洪灡瀨楲瑮瀬Ⱙ','u16')[2:])
