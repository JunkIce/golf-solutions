# Bytes
l=[1]
for i in range(20):print(*l);l+=0,;l=[l[j-1]+l[j]for j in range(i+2)]
# --
# Chars
exec(bytes('㵬ㅛ੝潦⁲⁩湩爠湡敧㈨⤰瀺楲瑮⨨⥬氻㴫ⰰ氻嬽孬⵪崱氫橛晝牯樠椠⁮慲杮⡥⭩⤲㭝','u16')[2:])
