import re
import base64


def b64decode_regex(message):
    regex = ""
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return True

def b64encode_regex(message):
    regex = ""
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return True

def b64d(message):
    string_to_decode = message.split(" ")[:-1]
    return base64.b64decode(string_to_decode)

def b64e(message):
    string_to_encode = message.split(" ")[:-1]
    return base64.b64encode(string_to_encode)
