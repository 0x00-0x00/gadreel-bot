#/usr/bin/env python3.6
from vignere import *

def main():
    m = "COMMONSENSEISNOTSOCOMMON"
    n = "RWLLOCADMSTQRMOIANBOBUNM"
    k = "PIZZA"
    v1 = VignereCipher(m, k)
    v1._encrypt()

    v2 = VignereCipher(n, k)
    v2._decrypt()
    return 0

if __name__ == "__main__":
    main()
