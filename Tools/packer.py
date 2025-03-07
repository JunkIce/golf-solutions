# Compresses python code for chars scoring

# Chose 1:2 or 1:3 compression. 1:3 has significantly more overhead but is good for really long scripts
mode=3

#Put code here
CODE="""from string import*;
r=0;
for c in"t1d0)n}ky/,/Z}:YHIjmRRVQz(ZPgiwAhn(p&$ro+yPYo0dXZ2(ziJ`>G+E_SZWl~jabR@5:|Ea1tb4uC]yX_s}'xn[4r(I]]}=9tRMu%uT9}-w$6w0)ei3xn&+ZD?&v5g6<JFw+@[$DhbN<x*BcP>PgB9I!7rmAq6t,VrSQqC{ CF'JRS0^!+QdTA?mmcqK5LG$Wk;Q-(LPRL2&kpNG3!z_bmqC0{F^q7/_1<Q|'}3PV/wpF@Hlj>2RFFR@i3_{{Ln8n)b*6t$lK%[ :whlre I4,KY))PJL]W1H=NLk>~hM;[P#/X[Rcp,%G^weX[A>jM_pF`0qHb #p!/YU59WfP/}<L?dkk`_[{sr?H:W?hn9~b7 ;#+Ch>,90H7n%z!DdEDTiUOMkaYa'3GC-|`93Q/B0NthI+{&Dn$E_0i=bo?~iV9Ebfb[J#F=~Tv2YR.1s%lF#Od@8{?[b%mIma7x6X=#wnP09oJ+&ga!!Hz4cBq{2`IU*Ss>;CLHU!X":r=r*93+{c:i for i,c in enumerate(digits+ascii_uppercase+ascii_lowercase+"!#$%&'()*+-.:;<=>?@[]^_{|}~`,/ ")}[c]
print(f"0.{r}")"""
print()

#1:2 compressor
if mode==2:
    if len(CODE)%2!=0:
        CODE+=';'# Code needs to be an even number of chars, so just appends a ; if needed
    print(f'exec(bytes(\'{CODE.encode().decode("u16")}\',\'u16\')[2:])')

#1:3 compressor
elif mode==3:
    def crt(a, n):
        s, p = 0, 1
        for x in n:
            p *= x
        for x, y in zip(a, n):
            q = p // y
            s += q * x * pow(q, -1, y)
        return s % p

    # Compression
    code = CODE.replace('\n', chr(127))  # Replace newline with a placeholder character (ord=127)
    compressed = ''
    for i in range(0, len(code), 3):
        a = [ord(c) - 32 for c in code[i:i+3]]
        compressed += chr(crt(a, [101, 102, 103]))

    print(f"Compressed: {compressed}")

    # Decompression
    print(f'exec(\'\'.join(chr(ord(c)%i+32)for c in\'{compressed}\'for i in b\'efg\').replace(\'\\x7f\',\'\\n\'))')
print()

