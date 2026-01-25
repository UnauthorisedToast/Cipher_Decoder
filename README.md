There are 2 main portions:-

main.py
which folder contains the code that takes the input and output. This calls the functions in order to decode various ciphers as well.

d_coder.py
which has all the functions and acts as a self-made library for various ciphers. The functions here are then called in main.py. The library makes use of unicode values of each alphabet and then manipulates them accordingly in order to calculate a new value. The value is then converted back to an alphabet. Doing this for every character, it re-assembles the string afterwards to get a decoded cipher.
