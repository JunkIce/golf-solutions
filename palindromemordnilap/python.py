# Bytes
import sys
for s in sys.argv[1:]:print([s+s[:i][::-1]for i in range(len(s))if s[i:]==s[i:][::-1]][0])
# --
# Chars
exec(bytes('浩潰瑲猠獹昊牯猠椠⁮祳⹳牡癧ㅛ崺瀺楲瑮嬨⭳孳椺孝㨺ㄭ晝牯椠椠⁮慲杮⡥敬⡮⥳椩⁦孳㩩㵝猽楛崺㩛ⴺ崱孝崰㬩','u16')[2:])
