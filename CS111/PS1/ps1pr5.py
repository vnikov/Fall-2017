# 
# ps1pr5.py - Problem Set 1, Problem 5
#
# Functions with numeric inputs
#
# name: Phumin Walaipatchara
# email: phuminw@bu.edu
#

def mirror(s):
    """ return a mirrored version of s that is twice the length of the original string """
    return s + s[-1::-1]

def is_mirror(s):
    """ returns True if s is a mirrored string and False otherwise """
    return s[0:len(s) // 2] == s[-1:(len(s) // 2) - 1:-1]

def replace_end(values, new_end_vals):
    """ return a new list in which the elements in new_end_vals have replaced the last n elements of the list values, where n is the length of new_end_vals """
    if len(new_end_vals) >= len(values):
        return new_end_vals
    else:
        return values[0:len(values) - len(new_end_vals)] + new_end_vals

def repeat_elem(values, index, num_times):
    """ returns a new list in which the element of values at position index has been repeated num_times times """
    return values[0:index] + [values[index]] * num_times + values[index + 1:]

def test():
    print(mirror('bacon'))
    print(mirror('XYZ'))
    print(is_mirror('baconnocab'))
    print(is_mirror('baconcona'))
    print(is_mirror('assa'))
    print(is_mirror('asdf'))
    print(replace_end([1, 2, 3, 4, 5], [7, 8, 9]))
    print(replace_end([1, 2, 3, 4, 5], [12]))
    print(replace_end([0, 2, 4, 6], [4, 3, 2, 1, 0]))
    print(replace_end([0, 2, 4, 6], [4, 3, 2, 1]))
    print(repeat_elem([10, 11, 12, 13], 2, 4))
    print(repeat_elem([10, 11, 12, 13], 2, 6))
    print(repeat_elem([5, 6, 7], 1, 3))
