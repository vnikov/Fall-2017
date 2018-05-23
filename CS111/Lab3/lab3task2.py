#
# Name: Phumin W.
#
# lab3task2.py
#

def num_consonants(s):
    """ returns the number of consonants in s
        parameter: s is a string of lower-case letters
    """
    if s == '':
        return 0
    else:
        num_in_rest = num_consonants(s[1:])
        if s[0] not in 'aeiou':
            return num_in_rest
        else:
            return num_in_rest + 1
