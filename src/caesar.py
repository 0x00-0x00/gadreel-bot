import re


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_SHIFT = len(LETTERS)


def caesar_cipher_regex(message):
    regex = "^\/caesare\s+(?P<data>[a-zA-Z]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()["data"]

def caesar_cipher_decipher_regex(message):
    regex = "^\/caesard\s+(?P<data>[a-zA-Z]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()["data"]


class CaesarCipher(object):
    def __init__(self, data):
        if type(data) is bytes:
            data = data.decode()
        self.data = data.upper()

    def shift(self, shift_num):
        out = str()
        for char in self.data:
            print(char)
            index = LETTERS.index(char)
            print(index)
            index += shift_num
            out += LETTERS[index % MAX_SHIFT: (index % MAX_SHIFT)+1]
        return out
