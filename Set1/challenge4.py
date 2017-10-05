#!/usr/bin/env python

import challenge3
from euclid_dict import EuclidDict
import sys

ciphertext = "4.txt"


def main():

    euclid_dictionary_list = [EuclidDict()] * 0x100
    with open(ciphertext) as f:
        for line in f:
            for x in xrange(0x100):
                key = challenge3.get_hex(x) * (len(line) / 2)
                result = challenge3.xor_strings(key, line)
                euclid_dictionary_list[x].add_phrase(result)
    best_euclid_dict = EuclidDict()
    regex = '^[\w\s!-/:-@[-`]*$'
    for euclid_dict in euclid_dictionary_list:
        for phrase in euclid_dict.get_top_phrases(10, regex):
            best_euclid_dict.add_phrase(phrase)
    for i, phrase in enumerate(best_euclid_dict.get_top_phrases(5, regex)):
        print "Number " + str(i + 1) + ": " + phrase


if __name__ == "__main__":
    main()
