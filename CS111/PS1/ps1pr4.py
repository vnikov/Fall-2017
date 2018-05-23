# 
# ps1pr4.py - Problem Set 1, Problem 4
#
# Functions on strings and lists, part I
#
# name: Phumin Walaipatchara
# email: phuminw@bu.edu
#

def front3(s):
    """ return 3 copies of the front. If the string length is less than 3, return 3 copies of whatever is there. """
    return 3 * s[0:3]

def first_and_last(values):
    """ return the first and last value of the original list """
    # This function does not handle an empty string
    return [values[0]] + [values[-1]]

def longer_len(s1, s2):
    """ returns the length of the longer string """
    if len(s1) >= len(s2):
        return len(s1)
    else:
        return len(s2)

def move_to_end(s, n):
    """ returns the a new string in which the first n characters of s have been moved to the end of the string """
    if len(s) <= n:
        return s
    else:
        return s[n:] + s[0:n]

def test():
    """ Function to test front3(s) """
    print(front3('sa'))
    print(front3('asdfg'))
    print(front3(''))
    print(front3('-2'))
    print(first_and_last([1, 2, 3, 4]))
    print(first_and_last([0]))
    print(longer_len('computer', 'comput'))
    print(longer_len('hi', 'hello'))
    print(longer_len('Whooooo', 'Whooooo'))
    print(move_to_end('computer', 3))
    print(move_to_end('computer', 5))
    print(move_to_end('hi', 5))
    
