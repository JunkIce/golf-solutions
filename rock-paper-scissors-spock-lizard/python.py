# Bytes
import sys;S,P,D,L,H='✂📄💎🦎🖖'
r={S+P:"cuts",P+D:"covers",D+L:"crushes",L+H:"poisons",H+S:"smashes",S+L:"decapitates",L+P:"eats",P+H:"disproves",H+D:"vaporizes",D+S:"crushes"}
for a in sys.argv[1:]:print("Tie"if a[0]==a[1]else f"{a[0]} {r[a]} {a[1]}"if a in r else f"{a[1]} {r[a[::-1]]} {a[0]}")
# --
# Chars
exec(bytes('浩潰瑲猠獹医倬䐬䰬䠬✽鳢鎟銟ꚟ隟➖爊笽⭓㩐挢瑵≳倬䐫∺潣敶獲Ⱒ⭄㩌挢畲桳獥Ⱒ⭌㩈瀢楯潳獮Ⱒ⭈㩓猢慭桳獥Ⱒ⭓㩌搢捥灡瑩瑡獥Ⱒ⭌㩐攢瑡≳倬䠫∺楤灳潲敶≳䠬䐫∺慶潰楲敺≳䐬匫∺牣獵敨≳੽潦⁲⁡湩猠獹愮杲孶㨱㩝牰湩⡴吢敩椢⁦孡崰㴽孡崱汥敳映笢孡崰⁽牻慛絝笠孡崱≽晩愠椠⁮⁲汥敳映笢孡崱⁽牻慛㩛ⴺ崱絝笠孡崰≽㬩','u16')[2:])
