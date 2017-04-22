#!/usr/bin/env python3.6
# -----------------------------------------
# Encoder / Decoder for GaleguinhoCipher
# -----------------------------------------
import re

SUBST = {
        "7":"L", "p":"D", "d":"P", "@":"A",
        "W":"M", "3":"E", "0":"O", "!":"I",
        "_|_":"T", "n": "U",
        }

def galegoe_regex(message):
    if type(message) is bytes:
        message = message.decode()
    regex = "^\/galegoe\s+(?P<data>[a-zA-Z0-9\s]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()["data"]

def galegod_regex(message):
    if type(message) is bytes:
        message = message.decode()
    regex = "^\/galegod\s+(?P<data>[a-zA-Z0-9@!_|\s]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()["data"]

def decryption(cipher):
    for element in SUBST:
        cipher = cipher.replace(element, SUBST[element])
    return cipher[::-1]

def encryption(message):
    REV = {value:key for key,value in SUBST.items()}
    for element in REV:
        message = message.replace(element, REV[element])
    return message[::-1]
