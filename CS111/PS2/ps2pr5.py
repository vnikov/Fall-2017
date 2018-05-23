#
# Name: Phumin W.
# 
# ps2pr5.py - Problem Set 2, Problem 5
#
# list comprehensions
#

# Problem 5-1: LC puzzles!
# This code won't work until you complete the list comprehensions!
# If you can't figure out how to complete one of them, please
# comment out the corresponding lines by putting a # at the start
# of the appropriate lines.

# part a
lc1 = [ x + 7 for x in range(5)]
print(lc1)

# part b
words = ['hello', 'world', 'how', 'goes', 'it?']
lc2 = [ w[-1] for w in words]
print(lc2)

# part c
lc3 = [ word[::2] for word in ['hello', 'bye', 'no']]
print(lc3)

# part d
lc4 = [ x for x in range(1, 20) if x % 6 == 0]
print(lc4)

# part e
lc5 = [ c == 'a' for c in 'aardvark']
print(lc5)


# Problem 5-2: Put your definition of the powers_of() function below.

def powers_of(base, count):
    ''' return a list containing the first count powers of base,
    beginning with the 0th power '''
    return [base ** n for n in range(count)]


# Problem 5-3: Put your definition of the longer_than() function below.

def longer_than(n, wordlist):
    ''' return a list consisting of all words from wordlist
    that are longer than n '''
    return [s for s in wordlist if len(s) > n]

def test():
    ''' function to test functions '''
    print('powers_of(2, 5) returns', powers_of(2, 5))
    print('powers_of(3, 4) returns', powers_of(3, 4))
    print("longer_than(3, ['only', 'recursion', 'on', 'the', 'brain']) returns", longer_than(3, ['only', 'recursion', 'on', 'the', 'brain']))
    print("longer_than(6, ['Boston', 'Chicago', 'Washington', 'Houston']) returns", longer_than(6, ['Boston', 'Chicago', 'Washington', 'Houston']))
    print("longer_than(7, ['Boston', 'Chicago', 'Washington', 'Houston'] returns", longer_than(7, ['Boston', 'Chicago', 'Washington', 'Houston']))
    print("longer_than(10, ['Boston', 'Chicago', 'Washington', 'Houston'] returns", longer_than(10, ['Boston', 'Chicago', 'Washington', 'Houston']))
    #print(' returns', longer_than(6, )
    #print(' returns', )
    
