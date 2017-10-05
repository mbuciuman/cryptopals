#!/usr/bin/env python

import challenge2


message = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"


def create_rep_key(key, message):
    return (key * (len(message) / len(key) + 1))[:len(message)]


def main():
    hex_message = message.encode('hex')
    hex_key = key.encode('hex')
    repeating_key = create_rep_key(hex_key, hex_message)
    ciphertext = challenge2.xor(repeating_key, hex_message)
    print ciphertext

if __name__ == "__main__":
    main()
