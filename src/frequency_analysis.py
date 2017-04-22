#!/usr/bin/env python3.6

PORTUGUESE_FREQ = {
        "A": 0.14634,
        "B": 0.01043,
        "C": 0.03882,
        "D": 0.04992,
        "E": 0.12570,
        "F": 0.01023,
        "G": 0.01303,
        "H": 0.00781,
        "I": 0.06186,
        "J": 0.00397,
        "K": 0.00015,
        "L": 0.02779,
        "M": 0.04738,
        "N": 0.04446,
        "O": 0.09735,
        "P": 0.02523,
        "Q": 0.01204,
        "R": 0.06530,
        "S": 0.06805,
        "T": 0.04336,
        "U": 0.03639,
        "V": 0.01575,
        "W": 0.00037,
        "X": 0.00253,
        "Y": 0.00006,
        "Z": 0.00470,
        }


ENGLISH_FREQ = {
        "A": 0.08167,
        "B": 0.01492,
        "C": 0.02782,
        "D": 0.04253,
        "E": 0.12702,
        "F": 0.02228,
        "G": 0.02015,
        "H": 0.06094,
        "I": 0.06966,
        "J": 0.00153,
        "K": 0.00772,
        "L": 0.04025,
        "M": 0.02406,
        "N": 0.06749,
        "O": 0.07507,
        "P": 0.01929,
        "Q": 0.00095,
        "R": 0.05987,
        "S": 0.06327,
        "T": 0.09056,
        "U": 0.02758,
        "V": 0.00978,
        "W": 0.02360,
        "X": 0.00150,
        "Y": 0.01974,
        "Z": 0.00074,
        }


class Frequency(object):
    def __init__(self, freq, cipher):
        if type(cipher) is bytes:
            cipher = cipher.decode()
        self.cipher = cipher
        self.model_frequency = freq
        self.cipher_frequency = dict()
        self.cipher_len = len(self.cipher)
        self.distance = 0
        self._analyze_frequency()
        self._measure_distance()

    def _analyze_frequency(self):
        cipher_letters = set(self.cipher)
        for char in cipher_letters:
            self.cipher_frequency[char] = (self.cipher.count(char) / float(self.cipher_len))
        #print(self.cipher_frequency)
        return 0

    def _measure_distance(self):
        for element in self.cipher_frequency:
            model_frequency = self.model_frequency[element]
            cipher_frequency = self.cipher_frequency[element]
            self.distance = self.distance + (cipher_frequency - model_frequency)

            #print("Model Frequency for '{0}': {1}".format(element, model_frequency))
            #print("Cipher frequency for '{0}: {1}'".format(element, cipher_frequency))
        #print("Distance between the models: {0}".format(self.distance))


        return 0



