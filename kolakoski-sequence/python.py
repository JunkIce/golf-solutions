# Bytes
s=[1,2,2]
[s.extend([1if s[-1]>1else 2]*s[i])for i in range(2,1000)]
print(*s[:1000])
# --
# Chars
exec(bytes('㵳ㅛ㈬㈬੝獛攮瑸湥⡤ㅛ晩猠ⵛ崱ㄾ汥敳㈠⩝孳嵩昩牯椠椠⁮慲杮⡥ⰲ〱〰崩瀊楲瑮⨨孳ㄺ〰崰㬩','u16')[2:])
