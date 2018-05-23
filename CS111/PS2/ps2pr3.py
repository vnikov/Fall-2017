#
# Name: Phumin W.
# 
# ps2pr3.py - Problem Set 2, Problem 3
#

def copy(s, n):
    ''' return a string in which n copies of s have been concatenated together.
    If n is less than or equal to 0, the function return the empty string'''
    rep = 0
    if n <= 0 and rep == 0:
        return ''
    elif n == 0:
        return s
    else:
        rep += 1
        return s + copy(s, n-1)

def compare(list1, list2):
    ''' return the number of values in list1 that are
    smaller than their corresponding value in list2 '''
    if len(list1) == 0 or len(list2) == 0:
        return 0
    else:
        if list1[0] < list2[0]:
            return 1 + compare(list1[1:], list2[1:])
        else:
            return compare(list1[1:], list2[1:])
        
def letter_score(letter):
    ''' returns the value of that letter as a scrabble tile.
    If letter is not a lowercase letter from ‘a’ to ‘z’,
    the function should return 0. '''
    if letter in 'aeilnorstu':
        return 1
    elif letter in 'dg':
        return 2
    elif letter in 'bcmp':
        return 3
    elif letter in 'fhwvy':
        return 4
    elif letter in 'k':
        return 5
    elif letter in 'jx':
        return 8
    elif letter in 'qz':
        return 10
    else:
        return 0

def scrabble_score(word):
    ''' return the scrabble score of that string '''
    if len(word) == 0:
        return 0
    else:
        return letter_score(word[0]) + scrabble_score(word[1:])
    

def test():
    ''' function to test functions '''
    print("copy('da', 2) returns", copy('da', 2))
    print("copy('Go BU!', 4)) returns", copy('Go BU!', 4))
    print("copy('hello', 1) returns", copy('hello', 1))
    print("copy('hello', 0) returns", copy('hello', 0))
    print("copy('hello', -7) returns", copy('hello', -7))
    print("compare([5, 3, 7, 9, 1], [2, 4, 7, 8, 3]) returns", compare([5, 3, 7, 9, 1], [2, 4, 7, 8, 3]))
    print("compare([4, 2, 3, 7], [1, 5]) returns", compare([4, 2, 3, 7], [1, 5]))
    print("compare([4, 2, 3], [6, 5, 0, 8]) returns", compare([4, 2, 3], [6, 5, 0, 8]))
    print("compare([5, 3], []) returns", compare([5, 3], []))
    print("compare([], [5, 3, 7]) returns", compare([], [5, 3, 7]))
    print("letter_score('w') returns", letter_score('w'))
    print("letter_score('q') returns", letter_score('q'))
    print("letter_score('%') returns", letter_score('%'))
    print("letter_score('A') returns", letter_score('A'))
    print("scrabble_score('python') returns", scrabble_score('python'))
    print("scrabble_score('a') returns", scrabble_score('a'))
    print("scrabble_score('quetzal') returns", scrabble_score('quetzal'))
