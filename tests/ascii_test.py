#!/usr/bin/env python3.6
from ascii_converter import *


def main():
    list_data = [0x41, 0x41, 0x41, 0x41]
    string_data = "ANDRE"

    ascii_obj1 = AsciiConverter(list_data, 0)
    ascii_obj2 = AsciiConverter(string_data, 1)

    print(ascii_obj1.converted)
    print(ascii_obj2.converted)
    return 0

if __name__ == "__main__":
    main()
