def double(s):
    ''' return the string formed by doubling each character in the string '''
    result = ''
    for c in s:
        result += c * 2
    return result

def weave(s1, s2):
    ''' return a new string that is formed by “weaving” together the
    characters in the strings s1 and s2 to create a single string '''
    result = ''
    len_shorter = min(len(s1), len(s2))
    for i in range(len_shorter):
        result += s1[i] + s2[i]
    if len(s1) == len_shorter:
        return result + s2[len_shorter:]
    else:
        return result + s1[len_shorter:]

def index(elem, seq):
    '''  return the index of the first occurrence of elem in seq '''
    for i in range(len(seq)):
        if seq[i] == elem:
            return i
    return -1

def test():
    ''' function to test funtions '''
    print("double('hello') returns", double('hello'))
    print("double('python') returns", double('python'))
    print("double('') returns", double(''))
    print("weave('aaaaaa', 'bbbbbb') returns", weave('aaaaaa', 'bbbbbb'))
    print("weave('abcde', 'VWXYZ') returns", weave('abcde', 'VWXYZ'))
    print("weave('aaaaaa', 'bb')  returns", weave('aaaaaa', 'bb') )
    print("weave('aaaa', 'bbbbbb') returns", weave('aaaa', 'bbbbbb'))
    print("weave('aaaa', '')  returns", weave('aaaa', '') )
    print("weave('', 'bbbb') returns", weave('', 'bbbb'))
    print("weave('', '') returns", weave('', ''))
    print("index(5, [4, 10, 5, 3, 7, 5]) returns", index(5, [4, 10, 5, 3, 7, 5]))
    print("index('hi', ['well', 'hi', 'there']) returns", index('hi', ['well', 'hi', 'there']))
    print("index('b', 'banana') returns", index('b', 'banana'))
    print("index('A', 'banana') returns", index('A', 'banana'))
    print("index('i', 'team') returns", index('i', 'team'))
    print("index('hi', ['hello', 111, True]) returns", index('hi', ['hello', 111, True]))
    print("index('a', '') returns", index('a', ''))
    print("index(8, [4, 10, 5, 3]) returns", index(8, [4, 10, 5, 3]))
    print('index(5, [4, 10, 8, 5, 3, 5]) returns', index(5, [4, 10, 8, 5, 3, 5]))

