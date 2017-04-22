#!/usr/bin/env python3.6

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
            self.converted = self._convert_to_text()
        elif mode == 1:
            self.converted = self._convert_to_number()

    def _convert_to_text(self):
        """
        Receives a list with ascii numbers and convert it back to ascii char-
        acters.
        Returns: String, List
        """
        if type(self.data) is not list:
            return -1
        out = str()
        for element in self.data:
            out += chr(int(element))
        return (out)

    def _convert_to_number(self):
        """
        Receives a string and convert it to a list of numbers.
        Returns: String, List
        """
        if type(self.data) is not str:
            return -1
        out = list()
        for char in self.data:
            out.append(ord(char))
        return (out)



