path='C:/Users/clayt/Downloads/code-golf-export(3).json'

import os
import json
import __data

#with open(path,'r',encoding="UTF-16-BE") as file:
    #print(chardet.detect(raw))
#    data=json.load(file)

with open('./AA_Tools/langmap.json','r') as file:
    langmap=json.load(file)
    extension=langmap['Extensions']
    comment=langmap['Comments']

#print(data['solutions'][0]['scoring'])
# Parse through each solution
#print(os.listdir('./12-days-of-christmas'))

data=__data.data

for solution in data['solutions']:
    hole = solution['hole']
    lang = solution['lang']
    scoring = solution['scoring']
    code = solution['code']
    #print(lang)

    if hole not in os.listdir(): # For newly solved holes
        os.mkdir(hole)
    
    if lang not in extension: # fallback incase new language
        extension[lang]=lang
    if lang not in comment:
        comment[lang]=''

    if not f"{lang}.{extension[lang]}" in os.listdir(f'./{hole}/'):
        file=open(f'./{hole}/{lang}.{extension[lang]}','w',encoding='utf-16')
        file.write(f'{comment[lang]} Bytes\n{comment[lang]} --\n{comment[lang]} Chars')
        file.close()
    
    file=open(f'./{hole}/{lang}.{extension[lang]}','r',encoding='utf-16')
    lines=file.read().splitlines()
    div=lines.index(f'{comment[lang]} --')

    bytes_lines=lines[1:div]
    chars_lines=lines[div+2:]
    _bytes='\n'.join(bytes_lines)
    _chars='\n'.join(chars_lines)

    file.close()

    if hole!='quine':
        _bytes=_bytes.strip()
        _chars=_chars.strip()

    if scoring=='bytes':
        if _bytes!=code:
            _bytes=code

    if scoring=='chars':
        if _chars!=code:
            _chars=code

    file=open(f'./{hole}/{lang}.{extension[lang]}','w',encoding='utf-16')
    file.write(
f'''{comment[lang]} Bytes
{_bytes}
{comment[lang]} --
{comment[lang]} Chars
{_chars}
''')
    file.close()
