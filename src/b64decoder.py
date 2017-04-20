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
        to_decode = m["data"]

        # Bug Fix #1
        # Python3.6 requires that a bytes object is used for base64 operations
        # This way it could be used both on python2.7 and python3.6
        try:
            decoded_string = base64.b64decode(to_decode)
        except TypeError:
            decoded_string = base64.b64decode(to_decode.encode())
        return base64.b64decode(decoded_string)

def b64e(message):
    regex = "^\/b64[de]\s(?P<data>[a-zA-Z0-9\=]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        to_encode = m["data"]
        try:
            encoded_string = base64.b64encode(to_encode)
        except TypeError:
            encoded_string = base64.b64encode(to_encode.encode())
        return base64.b64decode(encoded_string)
