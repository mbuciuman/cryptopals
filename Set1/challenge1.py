#!/usr/bin/python
import sys

def to_base_64(hex_string):
    base_64_string = ""
    base_64_list = []
    for i in xrange(0,len(hex_string),6):
        hex_chars = hex_string[i:i+6] if (i + 6) < len(hex_string) else hex_string[i:]
        base_64_chars = hex_chars_to_base64(hex_chars)
        base_64_list.append(base_64_chars)
    return "".join(base_64_list)

def hex_chars_to_base64(hex_chars):
    if len(hex_chars) > 6: 
        sys.stderr.write('Too many hex chars! Exiting...') 
        exit(1)
    if len(hex_chars) % 2 == 1:
        hex_chars += '0'
    binary_string = ""
    for char in hex_chars:
        binary_char = str(bin(int(char,16)))[2:]
        binary_char = '0'*(4-len(binary_char)) + binary_char
        binary_string += binary_char
        #print 'Char: ' + char + ' ; Binary char: ' + binary_char
    base_64_list = []
    for i in xrange(0, len(binary_string), 6):
        binary_base64_char = binary_string[i:i+6] if (i + 6) < len(binary_string) else binary_string[i:]+'0'*(6-(len(binary_string)-i))
        base_64_list.append(binary_char_to_base64(binary_base64_char))
    if(len(hex_chars) == 4):
        base_64_list.append('=')
    if(len(hex_chars) == 2):
        base_64_list.append('==')
    return "".join(base_64_list)

def binary_char_to_base64(binary_base64_char):
    int_from_binary = int(binary_base64_char,2)
    base_64_char = ''
    if(int_from_binary >= 0 and int_from_binary <= 25):
        base_64_char = chr(ord('A') + int_from_binary)   
    elif(int_from_binary >= 26 and int_from_binary <= 51):
        base_64_char = chr(ord('a') + (int_from_binary - 26))   
    elif(int_from_binary >= 52 and int_from_binary <= 61):
        base_64_char = chr(ord('0') + (int_from_binary - 52))   
    elif(int_from_binary == 62):
        base_64_char = '+'
    elif(int_from_binary == 63):
        base_64_char = '/'
    #print 'Int given: ' + str(int_from_binary) + ' Converted character: ' + str(base_64_char)
    if(base_64_char == ''):
        sys.stderr.write('Invalid binary number given! Input: ' + str(binary_base64_char) + ' Value: ' + str(int_from_binary) + ' Exiting...') 
        exit(1)
    return base_64_char

hex_string="49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d12"
        
print to_base_64(hex_string)
print 'Verification: ' + hex_string.decode('hex').encode('base64')
