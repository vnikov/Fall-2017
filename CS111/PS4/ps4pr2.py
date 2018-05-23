# 
# ps4pr2.py - Problem Set 4, Problem 2
#
# Using your conversion functions
#

from ps4pr1 import *

def mul_bin(b1, b2):
    ''' multiply the numbers and return the result in the form of
    a string that represents a binary number '''
    return dec_to_bin(bin_to_dec(b1) * bin_to_dec(b2))

def add_bytes(b1, b2):
    ''' compute the sum of the two bytes and return that sum in the
    form of a string that represents an 8-bit binary number. '''
    sum_bytes = dec_to_bin(bin_to_dec(b1) + bin_to_dec(b2))
    if len(sum_bytes) > 8:
        sum_bytes = sum_bytes[-8:]
    elif len(sum_bytes) < 8:
        sum_bytes = ('0' * (8 - len(sum_bytes))) + sum_bytes
    return sum_bytes

def test():
    ''' function to test functions '''
    print("mul_bin('11', '10') returns", mul_bin('11', '10'))
    print("mul_bin('1001', '101') returns", mul_bin('1001', '101'))
    print("add_bytes('00000011', '00000001') returns", add_bytes('00000011', '00000001'))
    print("add_bytes('00011100', '00011110') returns", add_bytes('00011100', '00011110'))
    print("add_bytes('10000011', '11000001')  returns", add_bytes('10000011', '11000001') )
    
