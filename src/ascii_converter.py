#!/usr/bin/env python3.6
import re


def ascii_to_text_regex(message):
    regex = "^\/asciid\s+(?P<data>[0-9\s]+)"
    m = re.match(regex, message)
    if not m:
        return -1
    else:
        print(m.groupdict()["data"])
        return m.groupdict()["data"]


def text_to_ascii_regex(message):
    regex = "^\/asciie\s+(?P<data>[a-zA-Z\s]+)"
    m = re.match(regex, message)
    if not m:
        return -1
    else:
        print(m.groupdict()["data"])
        return m.groupdict()["data"]


class AsciiConverter(object):
    """
    ASCII Converter written by zc00l on 20/04/2017
    Arguments: (Data, Mode)

    Modes:
        0 for To-Text;
        1 for To-Numbers;
    """
    def __init__(self, data, mode):
        if type(data) is bytes:
            data = data.decode()
        self.data = data
        if mode == 0:
            self.data = list(filter(lambda x: not "", [x for x in self.data]))
            self.converted = self._convert_to_text()
        elif mode == 1:
            self.converted = self._convert_to_number()

    def _convert_to_text(self):
        """
        Receives a list with ascii numbers and convert it back to ascii char-
        acters.
        Returns: String, List
        """
        out = str()
        for element in self.data:
            out += chr(int(element))
        return (out)

    def _convert_to_number(self):
        """
        Receives a string and convert it to a list of numbers.
        Returns: String, List
        """
        out = list()
        for char in self.data:
            out.append(ord(char))
        return (out)