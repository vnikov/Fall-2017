#
# Lab 4, Task 4 - OPTIONAL design challenge
#

def myslice(values, start, stop):
    ''' uses recursion to construct and return the equivalent
    of values[start:stop] '''
    if start == stop:
        return []
    else:
        return [values[start]] + myslice(values, start + 1, stop)

def test():
    ''' function to test functions '''
    print("myslice(['a', 'b', 'c', 'd', 'e'], 2, 4) returns", myslice(['a', 'b', 'c', 'd', 'e'], 2, 4))
    print("myslice(['a', 'b', 'c', 'd', 'e'], 1, 5) returns", myslice(['a', 'b', 'c', 'd', 'e'], 1, 5))
    print("myslice(['a', 'b', 'c', 'd', 'e'], 3, 3) returns", myslice(['a', 'b', 'c', 'd', 'e'], 3, 3))
    print("myslice(['to', 'be', 'or', 'not', 'to', 'be'], 1, 4) returns", myslice(['to', 'be', 'or', 'not', 'to', 'be'], 1, 4))
    print("myslice([6, 5, 4, 3, 2, 1], 0, 3) returns", myslice([6, 5, 4, 3, 2, 1], 0, 3))
    print("myslice(['a', 'b', 'c', 'd', 'e'], 2, 4) returns", myslice(['a', 'b', 'c', 'd', 'e'], 2, 4))
    print("myslice(['b', 'c', 'd', 'e'], 1, 3) returns", myslice(['b', 'c', 'd', 'e'], 1, 3))
