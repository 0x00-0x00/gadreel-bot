def vpn_r(message):
    regex = "^\/vpn$"
    m = re.match(regex, message)
    if not m:
        return None
    else:
	return True
