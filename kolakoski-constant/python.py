# Bytes
from decimal import*
s=[0,1,1]
[s.extend([0if s[-1]>0else 1]*(s[i]+1))for i in range(2,2500)]
getcontext().prec=999
print(f'{Decimal(int(b:=''.join(map(str,s[1:])),2))/2**len(b)}4')
# --
# Chars
exec(bytes('牦浯搠捥浩污椠灭牯⩴猊嬽ⰰⰱ崱嬊⹳硥整摮嬨椰⁦孳ㄭ㹝攰獬⁥崱⠪孳嵩ㄫ⤩潦⁲⁩湩爠湡敧㈨㈬〵⤰੝敧捴湯整瑸⤨瀮敲㵣㤹ਹ牰湩⡴❦䑻捥浩污椨瑮戨㴺✧樮楯⡮慭⡰瑳Ⱳ孳㨱⥝Ⱙ⤲⼩⨲氪湥戨紩✴㬩','u16')[2:])
