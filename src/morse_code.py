import re

CODE = {'A': '.-',     'B': '-...',   'C': '-.-.',
        'D': '-..',    'E': '.',      'F': '..-.',
        'G': '--.',    'H': '....',   'I': '..',
        'J': '.---',   'K': '-.-',    'L': '.-..',
        'M': '--',     'N': '-.',     'O': '---',
        'P': '.--.',   'Q': '--.-',   'R': '.-.',
        'S': '...',    'T': '-',      'U': '..-',
        'V': '...-',   'W': '.--',    'X': '-..-',
        'Y': '-.--',   'Z': '--..',

        '0': '-----',  '1': '.----',  '2': '..---',
        '3': '...--',  '4': '....-',  '5': '.....',
        '6': '-....',  '7': '--...',  '8': '---..',
        '9': '----.'
        }

CODE_REVERSED = {value:key for key,value in CODE.items()}

def morse_encode(text):
    out = str()
    for char in text.upper():
        if char == " ":
            continue
        out += CODE[char] + " "
    return out

def morse_decode(code):
    out = str()
    signs = code.split(" ")
    for element in signs[:-1]:
        out += CODE_REVERSED[element]
    return out


def morse_encode_regex(text):
    regex = "^\/morsee\s+(?P<data>[a-zA-Z0-9]+)"
    m = re.match(regex, text)
    if not m:
        return None
    else:
        return m.groupdict()

def morse_decode_regex(text):
    regex = "^\/morsed\s+(?P<data>[\.\-]+)"
    m = re.match(regex, text)
    if not m:
        return None
    else:
        return m.groupdict()
