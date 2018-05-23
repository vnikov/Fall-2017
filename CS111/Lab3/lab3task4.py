#
# Name: Phumin W.
#
# lab3task4.py
#

# part 0: Example function
def mult_by_two(n):
    """ creates and returns a list in which the integers from 0 to n - 1 
        have been multiplied by 2.
        parameter: n is a non-negative integer
    """

    return [2*x for x in range(n)]


# part 1
def div_by_two(n):
    """ creates and returns a list in which the integers from 0 to n - 1 
        have been divided by 2 using integer division.
        parameter: n is a non-negative integer
    """

    return [x // 2 for x in range(n)]


# part 2
def lengths(string_list):
    """ takes a list of strings and creates and returns the list of integers 
        that represent the lengths of the strings. 
        parameter: string_list is a list of strings
    """

    return [len(s) for s in string_list]


# part 3
def add_prefix(prefix, string_list):
    """ takes a string prefix and a list of strings and creates and returns 
        a list in which all of the elements from the original list are 
        preceded by the specified prefix.
        parameters: prefix - a string
                    string_list - a list of strings
    """

    return[prefix + s for s in string_list]
