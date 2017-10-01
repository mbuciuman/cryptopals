#!/usr/bin/python

import challenge1
import challenge2
import sys

hex_encoded_string="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def xor_char(int_char):
    padded_hex_char = chr(int_char).encode('hex').zfill(2)
    key=padded_hex_char*(len(hex_encoded_string)/2)
    return (challenge2.xor(key, hex_encoded_string)).decode('hex')

def main():
    if len(sys.argv) == 2:
        print "Character Specified in args: " + sys.argv[1] + " Result: " + xor_char(ord(sys.argv[1]))
    else:
        print "Trying all ASCII chars."
        for i in xrange(0x100):
            print "Character used for XOR: " + chr(i) + " Result: " + xor_char(i)

if __name__ == "__main__":
    main()
