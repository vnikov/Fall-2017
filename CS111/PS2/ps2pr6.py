#
# Name: Phumin W.
# 
# ps2pr6.py - Problem Set 2, Problem 6
#

def double(s):
    ''' return the string formed by doubling each character in the string '''
    if len(s) == 0:
        return ''
    else:
        return (s[0] * 2 ) + double(s[1:])

def weave(s1, s2):
    ''' return a new string that is formed by “weaving” together
    the characters in the strings s1 and s2 to create a single string '''
    if len(s1) == 0:
        return s2
    elif len(s2) == 0:
        return s1
    else:
        return s1[0] + weave(s2, s1[1:])

def index(elem, seq):
    ''' return the index of the first occurrence of elem in seq '''
    if seq == '' or seq == []:
        return -1
    elif elem == seq[0]:
        return 0
    else:
        ifindex = 1 + index(elem, seq[1:])
        if ifindex == 0:
            return -1
        else:
            return ifindex

def one_dna_to_rna(c):
    ''' returns the corresponding messenger-RNA nucleotide '''
    if c == 'A':
        return 'U'
    elif c == 'G':
        return 'C'
    elif c == 'C':
        return 'G'
    elif c == 'T':
        return 'A'
    else:
        return ''

def transcribe(s):
    ''' return a string representing the corresponding RNA '''
    if len(s) == 0:
        return ''
    else:
        return one_dna_to_rna(s[0]) + transcribe(s[1:])
    
def test():
    ''' function to test functions '''
    print("double('hello') returns", double('hello'))
    print("double('python') returns", double('python'))
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
    print("index(42, []) returns", index(42, []))
    print("one_dna_to_rna('C') returns", one_dna_to_rna('C'))
    print("one_dna_to_rna('T') returns", one_dna_to_rna('T'))
    print("one_dna_to_rna('X') returns", one_dna_to_rna('X'))
    print("one_dna_to_rna('c') returns", one_dna_to_rna('c'))
    print("transcribe('ACGT TGCA') returns", transcribe('ACGT TGCA'))
    print("transcribe('GATTACA') returns", transcribe('GATTACA'))
