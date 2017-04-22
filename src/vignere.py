import re

LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX_SHIFT = len(LETTERS)

def vigneree_regex(message):
    regex = "^\/vigneree\s+(?P<data>[a-zA-Z\s]+)\s?|`(?P<key>[a-zA-Z]+)`$"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()

def vignered_regex(message):
    regex = "^\/vignered\s+(?P<data>[a-zA-Z\s]+)\s?|`(?P<key>[a-zA-Z]+)`$"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()


class VignereCipher(object):
    def __init__(self, message, key):
        if type(message) is bytes:
            message = message.decode()

        if type(key) is bytes:
            key = key.decode()

        self.message = message.upper()
        self.msg_length = len(self.message)
        self.key = key.upper()
        self.key_length = len(self.key)
        self.exp_key = self._expand_key()

    def _expand_key(self):
        """
        Method to expand the key to the message length
        """
        if self.msg_length > self.key_length:
            n = self.msg_length / self.key_length + 1
        expanded_key = self.key * int(n)
        expanded_key = expanded_key[:self.msg_length]
        return expanded_key

    def _encrypt(self):
        """
        Encrypt a message using the vignere cipher
        """
        i = 0
        out = str()
        for char in self.message:
            k_value = self._index(self.exp_key[i])
            m_value = self._index(char)
            index = (k_value + m_value) % 26
            cipher = LETTERS[index%MAX_SHIFT: (index%MAX_SHIFT)+1]
            out += cipher
            i += 1
        return out

    def _decrypt(self):
        """
        Decrypt a message using the vignere cipher
        """
        i = 0
        out = str()
        for char in self.message:
            k_value = self._index(self.exp_key[i])
            m_value = self._index(char)
            index = (m_value - k_value) % 26
            plaintext = LETTERS[index%MAX_SHIFT: (index%MAX_SHIFT)+1]
            out += plaintext
            i+=1
        return out

    @staticmethod
    def _index(char):
        if char in LETTERS:
            return LETTERS.index(char)
        else:
            return None
