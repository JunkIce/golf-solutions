# Compresses python code for chars scoring

# Chose 1:2 or 1:3 compression. 1:3 has significantly more overhead but is good for really long scripts
mode=3

#Put code here
CODE="""//Your//Code//Here"""
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

