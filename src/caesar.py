import re


LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_SHIFT = len(LETTERS)


def caesar_cipher_regex(message):
    regex = "^\/caesar\s+(?P<data>[a-zA-Z]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()["data"]


class CaesarCipher(object):
    def __init__(self, data):
        if type(data) is bytes:
            data = data.decode()
        self.data = data

    def shift(self, shift_num):
        out = str()
        for char in self.data:
            index = LETTERS.index(char)
            index += shift_num
            out += LETTERS[index % MAX_SHIFT: (index % MAX_SHIFT)+1]
        return out
