#
# ps3pr4.py (Problem Set 3, Problem 4)
#
# More algorithm design
#

def rem_last(elem, values):
    ''' return a version of values in which the last occurrence
    of elem (if any) has been removed '''
    if values == []:
        return []
    elif values[0] == elem:
        if elem in values[1:]:
            return [values[0]] + rem_last(elem, values[1:])
        else:
            return values[1:]
    else:
        return [values[0]] + rem_last(elem, values[1:])

### Helper Function for jscore() ###

def rem_first(elem, values):
    """ removes the first occurrence of elem from the string values
    """
    if values == '':
        return ''
    elif values[0] == elem:
        return values[1:]
    else:
        return values[0] + rem_first(elem, values[1:])

### Helper Function for jscore(s1, s2) ###

def jscore(s1, s2):
    ''' returns the Jotto score of s1 compared with s2 –
    i.e., the number of characters in s1 that are shared by s2 '''
    if len(s1) == 0 or len(s2) == 0:
        return 0
    elif s1[0] in s2:
        return 1 + jscore(s1[1:], rem_first(s1[0], s2))
    else:
        return jscore(s1[1:], s2)

def lcs(s1, s2):
    ''' returns the longest common subsequence (LCS) that they share '''
    if len(s1) == 0 or len(s2) == 0:
        return ''
    elif s1[0] == s2[0]:
        return s1[0] + lcs(s1[1:], s2[1:])
    else:
        result1 = lcs(s1[1:], s2)
        result2 = lcs(s1, s2[1:])
        #return max(result1, result2)
        if len(result1) >= len(result2):
            return result1
        else:
            return result2
            
def test():
    ''' function to test functions '''
    print("rem_last(3, [2, 3, 1, 3, 4, 3, 5]) returns", rem_last(3, [2, 3, 1, 3, 4, 3, 5]))
    print("rem_last(0, [1, 0, 1, 0, 0]) returns", rem_last(0, [1, 0, 1, 0, 0]))
    print("rem_last(1, [1, 0, 1, 0, 0]) returns", rem_last(1, [1, 0, 1, 0, 0]))
    print("rem_last(2, [1, 0, 1, 0, 0]) returns", rem_last(2, [1, 0, 1, 0, 0]))
    print("rem_last(2, []) returns", rem_last(2, []))
    print("jscore('diner', 'syrup')  returns", jscore('diner', 'syrup') )
    print("jscore('always', 'bananas') returns", jscore('always', 'bananas'))
    print("jscore('always', 'walking') returns", jscore('always', 'walking'))
    print("jscore('recursion', 'excursion')  returns", jscore('recursion', 'excursion') )
    print("jscore('recursion', '')  returns", jscore('recursion', '') )
    print("lcs('human', 'chimp')   returns", lcs('human', 'chimp')  )
    print("lcs('gattaca', 'tacgaacta') returns", lcs('gattaca', 'tacgaacta'))
    print("lcs('wow', 'whew') returns", lcs('wow', 'whew'))
    print("lcs('', 'whew') returns", lcs('', 'whew'))
    print("lcs('abcdefgh', 'efghabcd')  returns", lcs('abcdefgh', 'efghabcd'))
    print(" returns", )
    print(" returns", )
    print(" returns", )
    print(" returns", )
