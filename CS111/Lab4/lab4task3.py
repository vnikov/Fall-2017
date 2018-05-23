#
# Lab 4, Task 3 - debugging a recursive function
#

def remove_spaces(s):
    ''' return a string in which all of the spaces have been removed '''
    if len(s) == 0:
        return ''
    elif s[0] == ' ':
        return '' + remove_spaces(s[1:])
    else:
        return s[0] + remove_spaces(s[1:])


def test():
    ''' function to test functions '''
    print("remove_spaces('hi how are you?') returns", remove_spaces('hi how are you?'))
    print("remove_spaces('    fine thanks!   ') returns", remove_spaces('    fine thanks!   '))
    print("remove_spaces('a b c d') returns", remove_spaces('a b c d'))
    print("remove_spaces(' b c d') returns", remove_spaces(' b c d'))
