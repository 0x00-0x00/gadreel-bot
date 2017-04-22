
LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_SHIFT = len(LETTERS)

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
