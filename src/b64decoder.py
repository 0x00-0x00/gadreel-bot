import re
import base64


def b64decode_regex(message):
    regex = "^\/b64[d]\s(?P<data>[a-zA-Z0-9\=]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return True

def b64encode_regex(message):
    regex = "^\/b64[e]\s(?P<data>[a-zA-Z0-9\=]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return True

def b64d(message):
    regex = "^\/b64[de]\s(?P<data>[a-zA-Z0-9\=]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        decoded_string = base64.b64decode(m["data"])
        return base64.b64decode(decoded_string)

def b64e(message):
    regex = "^\/b64[de]\s(?P<data>[a-zA-Z0-9\=]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        encoded_string = base64.b64encode(m["data"])
        return base64.b64decode(encoded_string)
