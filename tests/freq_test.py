#!/usr/bin/env python3.6

from frequency_analysis import *

#ciphers = [
#        "CLQLPWJ",
#        "OXCXBIV",
#        "PYDYCJW",
#        "QZEZDKX",
#        "FOTOSZM",
#        "MVAVZGT",
#        "TCHCGNA",
#        "RAFAELY",
#        ]


ciphers = [
        "FQHQBUBUFYFUTE",
        "ALCLWPWPATAPOZ",
        "EPGPATATEXETSD",
        "VGXGRKRKVOVKJU",
        "UFWFQJQJUNUJIT",
        "TEVEPIPITMTIHS",
        "SDUDOHOHSLSHGR",
        "RCTCNGNGRKRGFQ",
        "QBSBMFMFQJQFEP",
        "PARALELEPIPEDO",
        ]


def main():
    delta_freq = {}
    for cipher in ciphers:
        f = Frequency(PORTUGUESE_FREQ, cipher)
        delta_freq[f.distance] = f.cipher

    chosen = min(delta_freq.keys())
    print("Right one: {0}".format(delta_freq[chosen]))

    return 0


if __name__ == "__main__":
    main()
