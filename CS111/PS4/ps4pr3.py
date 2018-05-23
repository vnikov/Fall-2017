# 
# ps4pr3.py - Problem Set 4, Problem 3
#
# Recursive operations on binary numbers
#

def bitwise_and(b1, b2):
    ''' compute the bitwise AND of the two numbers and return
    the result in the form of a string '''
    if b1 =='' and b2 == '':
        return ''
    elif b1 == '':
        return (len(b2) * '0')
    elif b2 == '':
        return (len(b1) * '0')
    else:
        if b1[-1] == '1' and b2[-1] == '1':
            return bitwise_and(b1[:-1], b2[:-1]) + '1'
        else:
            return bitwise_and(b1[:-1], b2[:-1]) + '0'
            


def add_bitwise(b1, b2):
    ''' perform the bitwise, “elementary-school” addition algorithm
    that we discussed in lecture, and return the result '''
    if b1 == '':
        return b2
    elif b2 == '':
        return b1
    else:
        if b1[-1] == '1' and b2[-1] == '1':
            return add_bitwise('1', add_bitwise(b1[:-1], b2[:-1])) + '0'
        elif b1[-1] == '0' and b2[-1] == '0':
            return add_bitwise(b1[:-1], b2[:-1]) + '0'
        else:
            return add_bitwise(b1[:-1], b2[:-1]) + '1'
        

def test():
    print("bitwise_and('11010', '10011') returns", bitwise_and('11010', '10011'))
    print("bitwise_and('1001111', '11011') returns", bitwise_and('1001111', '11011'))
    print("bitwise_and('', '') returns", bitwise_and('', ''))
    print("bitwise_and('101', '') returns", bitwise_and('101', ''))
    print("bitwise_and('', '11010') returns", bitwise_and('', '11010'))
    print("add_bitwise('11100', '11110') returns", add_bitwise('11100', '11110'))
    print("add_bitwise('10101', '10101') returns", add_bitwise('10101', '10101'))
    print("add_bitwise('11', '1') returns", add_bitwise('11', '1'))
    print("add_bitwise('11', '100') returns", add_bitwise('11', '100'))
    print("add_bitwise('11', '') returns", add_bitwise('11', ''))
    print("add_bitwise('', '101') returns", add_bitwise('', '101'))
