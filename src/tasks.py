import re

def task_regex(message):
    """
    Regex to match the task creation request
    """
    regex = "^(criar?|nova?|new?|registrar?|register)\s?|nova?|(tarefa?|task)[^>](?P<task>[a-zA-Z0-9\s]+)"
    m = re.match(regex, message)
    if not m:
        return None
    else:
        return m.groupdict()
