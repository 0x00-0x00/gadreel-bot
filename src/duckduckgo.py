import re
import duckduckgo

def duckduck_regex(message):
    regex = "^\/duckduck\s+(?P<data>[a-zA-Z0-9\s]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()["data"]

def ddg(query):
    """
    DuckDuckGo search
    """
    return duckduckgo.get_zci(query)
