#!/usr/bin/python

str_1="1c0111001f010100061a024b53535009181c"
str_2="686974207468652062756c6c277320657965"

def xor(strA, strB):

    returned_string = ""
    for charA,charB in zip(strA,strB):
        xor_int = int(charA,16) ^ int(charB,16)
        xor_hex = hex(xor_int)
        xor_string = str(xor_hex)[2:]
        returned_string += str(xor_string)

    return returned_string

def main():

    print xor(str_1, str_2)

if __name__ == "__main__":
    main()
