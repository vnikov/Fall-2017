# 
# ps3pr2.py - Problem Set 3, Problem 2
#
# Algorithm design
#

def consonants_lc(s):
    ''' return a list containing the consonants (if any) in s '''
    return [c for c in s if c not in 'aeiou']

def consonants_rec(s):
    ''' return a list containing the consonants (if any) in s '''
    if len(s) == 0:
        return []
    else:
        if s[0] not in 'aeiou':
            return [s[0]] + consonants_rec(s[1:])
        else:
            return consonants_rec(s[1:])

def most_consonants(wordlist):
    ''' returns the word in the list with the most consonants '''
    return max([[len(consonants_lc(w)), w] for w in wordlist])[1]
    # I just want to make the code concise :-D .

def num_multiples(m, values):
    ''' returns the number of integers in values that are multiples of m '''
    return len([n for n in values if n % m == 0])

def test():
    ''' function to test functions '''
    print("consonants_lc('computer') returns", consonants_lc('computer'))
    print("consonants_lc('science') returns", consonants_lc('science'))
    print("consonants_lc('aeiou') returns", consonants_lc('aeiou'))
    print("consonants_rec('computer') returns", consonants_rec('computer'))
    print("most_consonants(['computer', 'science']) returns", most_consonants(['computer', 'science']))
    print("most_consonants(['obama', 'bush', 'clinton']) returns", most_consonants(['obama', 'bush', 'clinton']))
    print("num_multiples(5, [2, 15, 10])   returns", num_multiples(5, [2, 15, 10])  )
    print("num_multiples(3, [12, 3, 6, 7, 9]) returns", num_multiples(3, [12, 3, 6, 7, 9]))
    print("num_multiples(9, [15, 18]) returns", num_multiples(9, [15, 18]))
