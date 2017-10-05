#!/usr/bin/env python

import challenge2
import challenge3
from euclid_dict import EuclidDict

test_string_one = "this is a test"
test_string_two = "wokka wokka!!!"
filename = "6.txt"


def edit_distance(hex_string_one, hex_string_two):
    xor_of_strings = challenge2.xor(hex_string_one, hex_string_two)
    bit_count = bin(int(xor_of_strings, 16)).count("1")
    return bit_count


def test_portion():
    hex_string_one = test_string_one.encode('hex')
    hex_string_two = test_string_two.encode('hex')
    test_edit_distance = edit_distance(hex_string_one, hex_string_two)
    print "Edit distance of '" + test_string_one + "' and '" + test_string_two + "' is: " + str(test_edit_distance)


def get_keysize_edit_dists(ciphertext):
    key_edit_dist_dict = {}
    for x in range(2, 41):
        first_string = ciphertext[:x]
        second_string = ciphertext[x:2 * x]
        edit_dist = edit_distance(first_string, second_string)
        normalized_edit_dist = edit_dist / float(x)
        key_edit_dist_dict[x] = normalized_edit_dist
    return key_edit_dist_dict


def get_best_keysizes(keysize_edit_dists, num):
    keysizes = keysize_edit_dists.keys()
    best_sorted_keysizes = sorted(
        keysizes, key=keysize_edit_dists.__getitem__)[:num]
    best_keysizes_dict = {key: keysize_edit_dists[
        key] for key in best_sorted_keysizes}
    return best_keysizes_dict


def break_ciphertext_into_blocks(ciphertext, blocksize):
    blocked_ciphertext = []
    total_blocks = len(ciphertext) / blocksize
    for i in xrange(total_blocks):
        blocked_ciphertext.append(
            ciphertext[blocksize * i:blocksize * (i + 1)])
    return blocked_ciphertext


def transpose_blocks(blocked_ciphertext):
    transposed_ciphertext = [""] * len(blocked_ciphertext[0])
    for i in xrange(len(blocked_ciphertext[0])):
        for block in blocked_ciphertext:
            if len(block) > i:
                transposed_ciphertext[i] += block[i]
    return transposed_ciphertext


def untranspose_blocks(transposed_ciphertext):
    blocked_ciphertext = [""] * len(transposed_ciphertext[0])
    for i in xrange(len(transposed_ciphertext[0])):
        for j in xrange(len(transposed_ciphertext)):
            if len(transposed_ciphertext[j]) > i:
                blocked_ciphertext[i] += transposed_ciphertext[j][i]
    return blocked_ciphertext


def main():
    test_portion()
    print
    base64_text = ""
    with open(filename) as f:
        for line in f:
            base64_text += line[:-1]  # remove newline
    ciphertext = base64_text.decode('base64').encode('hex')
    keysize_edit_dists = get_keysize_edit_dists(ciphertext)
    best_keysizes = get_best_keysizes(keysize_edit_dists, 5)
    sorted_best_keysizes = sorted(
        best_keysizes.keys(), key=best_keysizes.__getitem__)
    for i, keysize in enumerate(sorted_best_keysizes):
        print "Best Keysize #" + str(i + 1) + ": " + str(keysize) + " with Normalized Edit Distance: " + str(best_keysizes[keysize])
    print
    print "Ciphertext:\n" + ciphertext + "\n"
    print "Blocked Ciphertext:\n"
    blocked_ciphertext = break_ciphertext_into_blocks(
        ciphertext, sorted_best_keysizes[0])
    for line in blocked_ciphertext:
        print str(line)
    print "Transposed Ciphertext:\n"
    transposed_ciphertext = transpose_blocks(blocked_ciphertext)
    for line in transposed_ciphertext:
        print str(line)
    print "Untransposed Ciphertext:\n"
    untransposed_ciphertext = untranspose_blocks(transposed_ciphertext)
    for line in untransposed_ciphertext:
        print str(line)
    euclid_dict = [EuclidDict()] * len(transposed_ciphertext)
    best_key = ""
    for i, line in enumerate(transposed_ciphertext):
        for j in xrange(0x100):
            key = challenge3.get_hex(j) * (len(line) / 2)
            result = challenge3.xor_strings(key, line)
            euclid_dict[i].add_phrase(result)


if __name__ == "__main__":
    main()
