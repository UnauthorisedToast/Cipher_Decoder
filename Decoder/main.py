#List of cyphers that can be decoded using this are:
#   reverse
#   atbash
#   caeser

import d_coder

string = input ("What is your cypher?     ")
dcode_m = input ("What is your cypher's type?     ")


if dcode_m == "reverse":
    decoded = d_coder.reversing_string (string)
    print (decoded)

if dcode_m == "atbash":
    decoded = d_coder.atbash_dcoder (string)
    print (decoded)

if dcode_m == "caeser":
    direction = input ("What direction does the decoder need to shift ('R' or 'L')?     ")
    shift_target = int(input ("How many shifts does the decoder need to perform?     "))
    decoded = d_coder.caeser_cypher_dcoder (string, shift_target, direction)
    print (decoded)