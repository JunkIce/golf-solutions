# Bytes
from decimal import*
getcontext().prec=1005
a=p=Decimal(1)
b=(a/2).sqrt()
t=a/4
exec('x=(a+b)/2;b=(a*b).sqrt();t-=p*(a-x)**2;a=x;p*=2;'*9)
print(str((a+b)**2/(4*t))[:-4])
# --
# Chars
exec(bytes('牦浯搠捥浩污椠灭牯⩴朊瑥潣瑮硥⡴⸩牰捥ㄽ〰ਵ㵡㵰敄楣慭⡬⤱戊⠽⽡⤲献牱⡴਩㵴⽡਴潦⁲ 湩せ⩝㨹㵸愨戫⼩㬲㵢愨截⸩煳瑲⤨琻㴭⩰愨砭⨩㈪愻砽瀻㴪ਲ牰湩⡴瑳⡲愨戫⨩㈪⠯⨴⥴嬩ⴺ崴㬩','u16')[2:])
