import re
import requests


BASE_URL = "https://md5.gromweb.com/?md5="

def parse_response(response):
    if type(response) is bytes:
        response = response.decode()
    regex = "The MD5 hash:\s+(?P<hash>[a-f0-9]+)\s+was succesfully reversed into the string:\s+(?P<plaintext>[^\s]+)"
    m = re.match(regex, response)
    if not m:
        return None
    else:
        return m.groupdict()

def request_reverse(hash):
    if type(hash) is bytes:
        hash = hash.decode()

    return requests.get(BASE_URL + str(hash)).content
