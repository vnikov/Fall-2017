# 
# ps4pr1.py - Problem Set 4, Problem 1
#
# From binary to decimal and back!
#

def dec_to_bin(n):
    ''' return a string version of the binary representation of
    the decimal number '''
    if n == 0:
        return '0'
    elif n == 1:
        return '1'
    else:
        if n % 2 == 0:
            return dec_to_bin(n // 2) + '0'
        else:
            return dec_to_bin(n // 2) + '1'

def bin_to_dec(s):
    ''' return the binary form of the integer '''
    if s[-1] == '1' and len(s) == 1:
        return 1
    elif s[-1] == '0' and len(s) == 1:
        return 0
    else:
        if s[-1] == '1':
            return (2 * bin_to_dec(s[:-1])) + 1
        else:
            return 2 * bin_to_dec(s[:-1])

def test():
    ''' function to test functions '''
    print("dec_to_bin(0) returns", dec_to_bin(0))
    print("dec_to_bin(1) returns", dec_to_bin(1))
    print("dec_to_bin(4) returns", dec_to_bin(4))
    print("dec_to_bin(7) returns", dec_to_bin(7))
    print("dec_to_bin(10) returns", dec_to_bin(10))
    print("dec_to_bin(111) returns", dec_to_bin(111))
    print("bin_to_dec('101') returns", bin_to_dec('101'))
    print("bin_to_dec('1100') returns", bin_to_dec('1100'))
    print("bin_to_dec('0') returns", bin_to_dec('0'))
    print("bin_to_dec('1') returns", bin_to_dec('1'))
    print("bin_to_dec('100') returns", bin_to_dec('100'))
    print("bin_to_dec('111') returns", bin_to_dec('111'))
    print("bin_to_dec('1110') returns", bin_to_dec('1110'))
    print("bin_to_dec('00011010') returns", bin_to_dec('00011010'))
    print("bin_to_dec('1111111') returns", bin_to_dec('1111111'))
    
    
