def mysum(x, y):
    """ takes two numbers and returns their sum """
    total = x + y
    return total

def sum_double(a, b):
    """ return the sum of the integers, unless the two values are the same, in which case the function should return double their sum """
    if a == b:
        return 2 * (a + b)
    else:
        return a + b
    
def test():
    """ function for testing """
    test1 = sum_double(1, 2)
    print('first test returns', test1)
    test2 = sum_double(3, 2)
    print('second test returns', test2)
    test3 = sum_double(2, 2)
    print('third test returns', test3)
    test4 = sum_double(0, 0)
    print('forth test returns', test4)
    test5 = sum_double(-4, -2)
    print('fifth test returns', test5)
    test6 = sum_double(-3, -3)
    print('sixth test returns', test6)
