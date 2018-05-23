#
# Name: Phumin W.
#
# lab3task3.py
#

def min_val(values):
    ''' return the minimum value in the list. '''
    if len(values) == 1:
        return values[0]
    else:
        if values[0] < min_val(values[1:]):
            return values[0]
        else:
            return min_val(values[1:])

def test():
    """ test function for min_val() """
    print('min_val([5, 10, 7, 15]) returns', min_val([5, 10, 7, 15]))
    print('min_val([20, 6, 4, 10]) returns', min_val([20, 6, 4, 10]))
    print('min_val([38214812, 34328147, 99782173, 12748217]) returns ', min_val([38214812, 34328147, 99782173, 12748217]))
