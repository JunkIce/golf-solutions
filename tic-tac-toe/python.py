# Bytes
import sys
for g in sys.argv[1:]:print(next((p for p,M in zip('XO',[[[c==t for c in r]for r in g.split()]for t in'XO'])if any(map(all,M+[*zip(*M),[M[i][i]for i in(0,1,2)],[M[i][2-i]for i in(0,1,2)]]))),'-'))
# --
# Chars
exec(bytes('浩潰瑲猠獹昊牯朠椠⁮祳⹳牡癧ㅛ崺瀺楲瑮渨硥⡴瀨映牯瀠䴬椠⁮楺⡰堧❏嬬孛㵣琽映牯挠椠⁮嵲潦⁲⁲湩朠献汰瑩⤨晝牯琠椠❮佘崧椩⁦湡⡹慭⡰污ⱬ⭍⩛楺⡰䴪Ⱙ䵛楛孝嵩潦⁲⁩湩〨ㄬ㈬崩嬬孍嵩㉛椭晝牯椠椠⡮ⰰⰱ⤲嵝⤩Ⱙⴧ⤧㬩','u16')[2:])
