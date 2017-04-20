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


class MorseHandler(object):
    def __init__(self, message, sender):
        if type(message) is bytes:
            message = message.decode()

        self.message = message
        self.sender = sender
        self._parse_regex()

    def _parse_regex(self):
        decoded = self._decode()
        encoded = self._encoded()
        if not decoded and not encoded:
            return -1

        if encoded:
            data = encoded["data"]
            await self.sender.sendMessage(morse_encode(data))

        if decoded:
            data = decoded["data"]
            await self.sender.sendMessage(morse_decode(data))


    def _encode(self):
        regex = "^\/morsee\s+(?P<data>[a-zA-Z0-9]+)"
        m = re.match(regex, self.message)
        if not m:
            return None
        else:
            return m.groupdict()

    def _decode(self):
        regex = "^/morsed\s+(?P<data>[a-zA-Z0-9]+)"
        m = re.match(regex, self.message)
        if not m:
            return None
        else:
            return m.groupdict()
