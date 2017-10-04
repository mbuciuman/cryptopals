#!/usr/bin/python

import challenge1
import challenge2
from euclid_dict import EuclidDict
import sys

hex_encoded_string="1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

def get_hex(int_char):

	return chr(int_char).encode('hex').zfill(2)


def xor_strings(hex_string_one, hex_string_two):

	return (challenge2.xor(hex_string_one, hex_string_two)).decode('hex')


def main():

	if len(sys.argv) == 2:
		print "Character Specified in args: " + sys.argv[1] + " Result: " + xor_char(ord(sys.argv[1]))
	else:
		print "Trying all ASCII chars."
		euclid_dict = EuclidDict()
		for i in xrange(0x100):
			key = get_hex(i)*(len(hex_encoded_string)/2)
			result = xor_strings(key, hex_encoded_string)
			euclid_dict.add_phrase(result)
		regex = '^[\w\s!-/:-@[-`]*$'
		for i, phrase in enumerate(euclid_dict.get_top_phrases(5, regex)):
			print "Number " + str(i+1) + ": " + phrase

if __name__ == "__main__":
	main()
