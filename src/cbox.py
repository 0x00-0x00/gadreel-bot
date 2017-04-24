#!/usr/bin/env python3.6
from shemutils.logger import Logger
import re

# Static variables
logger = Logger("CaesarBoxCipher")


def caesarboxe_regex(message):
    message = decode_data(message)
    regex = '^\/caesarboxe\s"(?P<data>[a-zA-Z]+)"\s+"(?P<key>[a-zA-Z]+)"'
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()

def caesarboxd_regex(message):
    message = decode_data(message)
    regex = '^\/caesarboxd\s"(?P<data>[a-zA-Z]+)"\s+"(?P<key>[a-zA-Z]+)"'
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()

def decode_data(data):
    if type(data) is bytes:
        return data.decode()
    else:
        return data

def validate_key(key):
    if type(key) is not int and key < 1:
        return None
    else:
        return key



class CaesarBoxCipher(object):
    def __init__(self, data, keysize):
        self.data = decode_data(data)
        self.keysize = validate_key(keysize)
        self.message_length = len(self.data)
        self._format_data()
        self.rows = self._rows_count(keysize)
        self.boxes = self._transposition()

    def _rows_count(self, keysize):
        """
        Returns how many rows are going to be produced by the cipher
        """
        return int(self.message_length / keysize) + 1

    def _format_data(self):
        suffix = 0
        k = self.message_length
        if self.message_length % self.keysize == 0:
            return 0
        else:
            while k % self.keysize != 0:
                k += 1
                suffix += 1

        self.data += "_" * suffix
        return 0

    def _transposition(self):
        """
        Evaluates the data from object and convert it to a transpositioned
        string.
        """
        i = 0
        index = 0
        boxes = []
        while  i <= self.rows:
            if i > len(self.data):
                remainder = len(self.data) % self.keysize
                boxes.append(self.data[index:index+remainder])
            else:
                boxes.append(self.data[index:index+self.keysize])
            i += 1
            index += self.keysize
        return list(filter(lambda x: x is not u"" and x is not "" ,boxes))


    def _rne(self, n, lObj):
        """
        Returns the N elementh of every element from a set of sets.
        """
        out = list()
        for element in lObj:
            out.append(element[n:n+1])
        return out

    def encrypt(self):
        """
        Encrypt the message with column transposition (Box)
        """
        i = 0
        out = str()
        while i < self.keysize:
            for block in self.boxes:
                out += (block[i:i+1])
            i += 1
        return out

    def print_boxes(self):
        return [print(box) for box in self.boxes]

    def decrypt(self):
        t_rows = self.keysize
        t_keysize = self.rows - 1
        self.rows = t_rows
        self.keysize = t_keysize
        self.boxes = self._transposition()
        dec = list()
        for i in range(0, self.keysize):
            dec.append(self._rne(i, self.boxes))
        return ''.join([''.join(x) for x in dec])
