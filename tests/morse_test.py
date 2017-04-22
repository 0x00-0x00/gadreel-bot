#!/usr/bin/env python3.6
from morse_code import *


def main():
    unencoded = "Tell the warriors to come"
    encoded = morse_encode(unencoded)
    print(encoded)

    decoded = morse_decode(encoded)
    print(decoded)
    return 0

if __name__ == "__main__":
    main()
