# 
# ps1pr3.py - Problem Set 1, Problem 3
#
# Functions with numeric inputs
#
# name: Phumin Walaipatchara
# email: phuminw@bu.edu
#
# If you worked with a partner, put his or her contact info below:
# partner's name: -
# partner's email: -
#

# function 0
def opposite(x):
    """ returns the opposite of its input
        input x: any number (int or float)
    """
    return -1*x

# put your definitions for the remaining functions below

def square(x):
    """ returns the square of its input """
    return x * x

def interpolate(low, high, fraction):
    """ takes three numeric inputs and returns a number that linearly interpolates between low and high by the amount specified by fraction """
    return low + fraction * (high - low)

def convert_from_inches(inches):
    """ takes a nonnegative integer inches and returns a list of three integers in which that length has been broken up into yards, feet, and inches """
    a = [] + [inches // 36]
    inches = inches % 36
    a = a + [inches // 12]
    inches = inches % 12
    a = a + [inches]
    return a

def median(a, b, c):
    """ three numeric inputs and returns the median of the three inputs """
    if a <= b <= c:
        return b
    elif c <= b <= a:
        return b
    elif a <= c <= b:
        return c
    elif b <= c <= a:
        return c
    elif b <= a <= c:
        return a
    else:
        return a

# test function with a sample test call for function 0
def test():
    """ performs test calls on the functions above """
    print('opposite(-8) returns', opposite(-8))
    
        # optional but encouraged: add test calls for your functions below
        
    print('opposite(3) returns', opposite(3))
    print('square(5) returns', square(5))
    print('square(-2) returns', square(-2))
    print('square(0) returns', square(0))
    print('interpolate(4.0, 10.0, 0.5) returns', interpolate(4.0, 10.0, 0.5))
    print('interpolate(1.0, 3, 0.25) returns', interpolate(1.0, 3, 0.25))
    print('interpolate(5, 9, 1.0) returns', interpolate(5, 9, 1.0))
    print('interpolate(5, 9, 0) returns', interpolate(5, 9, 0))
    print('interpolate(-4, -9, 0.25) returns', interpolate(-4, -9, 0.25))
    print('interpolate(0, 0, 0.83) returns', interpolate(0, 0, 0.83))
    print('interpolate(3, 10, 1.55) returns', interpolate(3, 10, 1.55))
    print('interpolate(3, 8, -0.65) returns', interpolate(3, 8, -0.65))
    print('convert_from_inches(67) returns', convert_from_inches(67))
    print('convert_from_inches(75) returns', convert_from_inches(75))
    print('median(10, 2, 7) returns', median(10, 2, 7))
    print('median(7, 2, 10) returns', median(7, 2, 10))
    print('median(8, 6, 4) returns', median(8, 6, 4))
    print('median(10, 2, 2) returns', median(10, 2, 2))
    print('median(-5, -8, 6) returns', median(-5, -8, 6))
    print('median(0, 0, 0) returns', median(0, 0, 0))
    print('median(5, 5, 5) returns', median(5, 5, 5))
