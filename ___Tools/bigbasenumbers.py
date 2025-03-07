# for puting numbers in big bases to reduce overall chars. Does not increase bytes size since stays in the ascii space. defaults to base-93 but can be changed as needed


number = 7945071927794792762403624156360456462985771009886069672658867371538147750246050153642329497318744922597650432133122381456242259141637544281388404986296014813250203200299775312204572205786844363481735193274370846097481321962085743588705637176441430215883431232498028486565855956743384725624863858171054907549352606638123461677335696682530707000099883441742261731533357981951614296137553874112128143917426025578358420171332328623170643408853930209585391082992162641473274851857016962909430762951612473755099961034929659942390562074624420161149786912908149773069197347642142910110070447310029702020886203513513301428993859530304436363949158738485277572004039916265592850315038741018282301383603610543128861005697949361221157894935364642623267878361142863458459305686296999605471470454134204345400779937112765597628388594645053060225949457341559196110640516125405727365862266669090528048652395018976865244173698258171772168511287021894518616053970806736858386548128961613011460662776100636983139773876954

import string

#either dec or hex
MODE='dec'

# Define the base-9x character set
BASE92_CHARS = string.digits + string.ascii_uppercase + string.ascii_lowercase + "!#$%&'()*+-.:;<=>?@[]^_{|}~`,/ "
BASE92_MAP = {char: index for index, char in enumerate(BASE92_CHARS)}
BASE = len(BASE92_CHARS)

def decimal_to_base92(n):
    """Converts a decimal number to a base-92 encoded string."""
    if n == 0:
        return BASE92_CHARS[0]
    
    result = []
    while n > 0:
        n, remainder = divmod(n, BASE)
        result.append(BASE92_CHARS[remainder])
    
    return ''.join(result[::-1])

def base92_to_decimal(s):
    """Converts a base-92 encoded string back to a decimal number."""
    result = 0
    for char in s:
        result = result * BASE + BASE92_MAP[char]
    
    return result

def hex_to_b92(n):
    return decimal_to_base92(int(n,16))

def base92_to_hex(s):
    return hex(base92_to_decimal(s))[2:]


if MODE=='dec':
    encoded = decimal_to_base92(number)
    decoded = base92_to_decimal(encoded)
    print(f"Base-92: {encoded}")
    print(f'Decoded matches encoded: {number==decoded}')

    print(f'Use in script:')
    print(f'from string import*\nr=0\nfor c in"{encoded}":r=r*{BASE}+{"{"}c:i for i,c in enumerate(digits+ascii_uppercase+ascii_lowercase+"!#$%&\'()*+-.:;<=>?@[]^_{"{"}|{"}"}~`,/ "){"}"}[c]\nprint(f"0.{"{"}r{"}"}")')
    print()
    print(f'from string import*\nprint(sum((digits+ascii_uppercase+ascii_lowercase+"!#$%&\'()*+-.:;<=>?@[]^_{"{"}|{"}"}~`,/ ").index(c)*{BASE}**i for i,c in enumerate("{encoded}")))')

elif MODE=='hex':
    encoded=hex_to_b92(number)
    decoded=hex_to_b92(number)
    print(f'bigbase: {encoded}')
    print(f'decoded matches encoded: {number==encoded}')

    print(f'use in script:')
    print(f'from string import*\nr=0\nfor c in"{encoded}":r=r*{BASE}+{"{"}c:i for i,c in enumerate(digits+ascii_uppercase+ascii_lowercase+"!#$%&\'()*+-.:;<=>?@[]^_{"{"}|{"}"}~`,/ "){"}"}[c]\nprint(hex(r)[2:])')
    print()
    