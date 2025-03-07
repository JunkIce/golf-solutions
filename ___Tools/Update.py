import os
import json
import __data 

with open('./___Tools/langmap.json','r') as file:
    langmap=json.load(file)
    extension=langmap['Extensions']
    comment=langmap['Comments']

data=__data.data # freaks the fuck out when trying to parse json with utf-16 chars, so I'm just going to change it to a package bc i'd like to stay sane

# Parse through each solution
for solution in data['solutions']:
    hole = solution['hole']
    lang = solution['lang']
    scoring = solution['scoring']
    code = solution['code']

    if hole not in os.listdir(): # Make directory for newly solved holes
        os.mkdir(hole)
    
    if lang not in extension: # In case lang not in language list
        extension[lang]=lang
    if lang not in comment:
        comment[lang]=''

    # Sets up lang solution file
    if not f"{lang}.{extension[lang]}" in os.listdir(f'./{hole}/'):
        file=open(f'./{hole}/{lang}.{extension[lang]}','w',encoding='utf-16')
        file.write(f'{comment[lang]} Bytes\n{comment[lang]} --\n{comment[lang]} Chars')
        file.close()
    
    # Yes I know there are better ways of parsing data but i fucking hate dealing with text encoding and this just works and i'm not gonna touch it
    file=open(f'./{hole}/{lang}.{extension[lang]}','r',encoding='utf-16')
    lines=file.read().splitlines()
    div=lines.index(f'{comment[lang]} --')
    bytes_lines=lines[1:div]
    chars_lines=lines[div+2:]
    _bytes='\n'.join(bytes_lines)
    _chars='\n'.join(chars_lines)
    file.close()

    # You usually need the trailing whitespace on quine
    if hole!='quine':
        _bytes=_bytes.strip()
        _chars=_chars.strip()

    #checks and replaces the data
    if scoring=='bytes':
        if _bytes!=code:
            _bytes=code

    if scoring=='chars':
        if _chars!=code:
            _chars=code

# Writes back to the file (yes i know this is redundant, sue me)
    file=open(f'./{hole}/{lang}.{extension[lang]}','w',encoding='utf-16')
    file.write(
f'''{comment[lang]} Bytes
{_bytes}
{comment[lang]} --
{comment[lang]} Chars
{_chars}
''')
    file.close()
