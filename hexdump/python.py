# Bytes
import sys
for s in sys.argv[1:]:[print(f"{i:08x}: {' '.join([''.join([f"{ord(c):02x}"for c in s[i:i+16]][j:j+2])for j in range(0,16,2)]).ljust(39)}  {''.join(['.'if c=='\n'else c if 31<ord(c)<127else'.'for c in s[i:i+16]])}")for i in range(0,len(s),16)];print()
# --
# Chars
exec(bytes('浩潰瑲猠獹昊牯猠椠⁮祳⹳牡癧ㅛ崺嬺牰湩⡴≦楻〺砸㩽笠‧⸧潪湩嬨✧樮楯⡮晛笢牯⡤⥣〺砲≽潦⁲⁣湩猠楛椺ㄫ崶孝㩪⭪崲昩牯樠椠⁮慲杮⡥ⰰ㘱㈬崩⸩橬獵⡴㤳紩†❻⸧潪湩嬨⸧椧⁦㵣挽牨ㄨ⤰汥敳挠椠⁦ㄳ漼摲挨㰩㈱攷獬❥✮潦⁲⁣湩猠楛椺ㄫ崶⥝≽昩牯椠椠⁮慲杮⡥ⰰ敬⡮⥳ㄬ⤶㭝牰湩⡴㬩','u16')[2:])
