#!/usr/bin/python

str_1="1c0111001f010100061a024b53535009181c"
str_2="686974207468652062756c6c277320657965"

def xor(strA, strB):
    return "".join((str(hex(ord(charA) ^ ord(charB)))[2:] for charA,charB in zip(strA,strB)))

print xor(str_1, str_2)
