#
# ps3pr3.py (Problem Set 3, Problem 3)
#
# Caesar cipher / decipher
#

# A template for a helper function called rot that we recommend you write
# as part of your work on the encipher function.
def rot(c, n):
   ''' rotates a single character c forward by n spots in the alphabet '''
   # check to ensure that c is a single character
   assert(type(c) == str and len(c) == 1)

   # Put the rest of your code for this function below.
   if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
      if 'a' <= c <= 'z':
         rot = chr(ord(c) + n)
         if 'a' <= rot <= 'z':
            return rot
         else:
            return chr(ord(c) + n - 26)
      else:
         rot = chr(ord(c) + n)
         if 'A' <= rot <= 'Z':
            return rot
         else:
            return chr(ord(c) + n - 26)
   else:
      return c

### Put your code for the encipher function below. ###

def encipher(s, n):
    ''' returns a new string in which the letters in s have been
    “rotated” by n characters forward in the alphabet,
    wrapping around as needed '''
    if len(s) == 0:
        return ''
    else:
        #if 'a' <= s[0] <= 'z' or 'A' <= s[0] <= 'Z':
            return rot(s[0], n) + encipher(s[1:], n)
        #else:
             #return s[0] + encipher(s[1:], n)

# A helper function that could be useful when assessing
# the "Englishness" of a phrase.
# You do *NOT* need to modify this function.
def letter_prob(c):
    """ if c is the space character (' ') or an alphabetic character,
        returns c's monogram probability (for English);
        returns 1.0 for any other character.
        adapted from:
        http://www.cs.chalmers.se/Cs/Grundutb/Kurser/krypto/en_stat.html
    """
    # check to ensure that c is a single character
    assert(type(c) == str and len(c) == 1)

    if c == ' ': return 0.1904
    if c == 'e' or c == 'E': return 0.1017
    if c == 't' or c == 'T': return 0.0737
    if c == 'a' or c == 'A': return 0.0661
    if c == 'o' or c == 'O': return 0.0610
    if c == 'i' or c == 'I': return 0.0562
    if c == 'n' or c == 'N': return 0.0557
    if c == 'h' or c == 'H': return 0.0542
    if c == 's' or c == 'S': return 0.0508
    if c == 'r' or c == 'R': return 0.0458
    if c == 'd' or c == 'D': return 0.0369
    if c == 'l' or c == 'L': return 0.0325
    if c == 'u' or c == 'U': return 0.0228
    if c == 'm' or c == 'M': return 0.0205
    if c == 'c' or c == 'C': return 0.0192
    if c == 'w' or c == 'W': return 0.0190
    if c == 'f' or c == 'F': return 0.0175
    if c == 'y' or c == 'Y': return 0.0165
    if c == 'g' or c == 'G': return 0.0161
    if c == 'p' or c == 'P': return 0.0131
    if c == 'b' or c == 'B': return 0.0115
    if c == 'v' or c == 'V': return 0.0088
    if c == 'k' or c == 'K': return 0.0066
    if c == 'x' or c == 'X': return 0.0014
    if c == 'j' or c == 'J': return 0.0008
    if c == 'q' or c == 'Q': return 0.0008
    if c == 'z' or c == 'Z': return 0.0005
    return 1.0

#### Put your code for the decipher function below. ####

def score(s):
   ''' return the score of "Englishness" of the string '''
   if len(s) == 0:
      return 0
   else:
      return letter_prob(s[0]) + score(s[1:])

def decipher(s):
   ''' the function lists all possible string that was rotated by the value
   from 0 to 25, then calculates the score of each string by using score(s).
   Finally, return the string that has the maximum value for "Englishness"'''
   return max([[score(x), x] for x in [encipher(s, n) for n in range(26)]])[1]

def test():
   ''' function to test functions '''
   print("encipher('hello', 1) returns", encipher('hello', 1))
   print("encipher('hello', 2) returns", encipher('hello', 2))
   print("encipher('hello', 4) returns", encipher('hello', 4))
   print("encipher('XYZ', 3) returns", encipher('XYZ', 3))
   print("encipher('xyz', 3) returns", encipher('xyz', 3))
   print("encipher('#caesar!', 2) returns", encipher('#caesar!', 2))
   print("encipher('xyza', 1) returns", encipher('xyza', 1))
   print("encipher('Z A', 2) returns", encipher('Z A', 2))
   print("encipher('Caesar cipher? I prefer Caesar salad.', 25) returns", encipher('Caesar cipher? I prefer Caesar salad.', 25))
   print("decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.') returns", decipher('Hu lkbjhapvu pz doha ylthpuz hmaly dl mvynla lclyfaopun dl ohcl slhyulk.'))
   print("decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj') returns", decipher('kwvozibctibqwva izm qv wzlmz nwz iv mfkmttmvb rwj'))
   print("decipher('bhogdq? oqdedq rzkzc.') returns", decipher('bhogdq? oqdedq rzkzc.'))
   print("decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.') returns", decipher('Bzdrzq bhogdq? H oqdedq Bzdrzq rzkzc.'))
   print("decipher('python') returns", decipher('python')) 
   print("decipher('Stpg vgpstgh, eatpht qt zxcs pcs vxkt bt ujaa rgtsxih udg iwxh epgi.') returns", decipher('Stpg vgpstgh, eatpht qt zxcs pcs vxkt bt ujaa rgtsxih udg iwxh epgi.'))

