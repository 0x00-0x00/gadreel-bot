#!/usr/bin/env python3.6
from caesar import *


def main():
    data = "ANDRE"
    c = CaesarCipher(data)

    for i in range(0, 26):
        print(c.shift(i))
    return 0

if __name__ == "__main__":
    main()
