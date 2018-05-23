#
# ps9pr3.py  (Problem Set 9, Problem 3)
#
# Markov text generation      
#

import random

def create_dictionary(filename):
    """ returns a dictionary of key-value pairs """
    file = open(filename, 'r')
    d = {}
    words = []
    for line in file:
        line = line[:-1]
        words += line.split()
    file.close()
    d["$"] = []
    for i in range(0, len(words)):
        if words[i] not in d and words[i][-1] not in ".?!":
            d[words[i]] = []
        if words[i-1][-1] in ".?!":
            d["$"] += [words[i]]
        else:
            d[words[i-1]] += [words[i]]
    return d

def generate_text(word_dict, num_words):
    """ generate and print a string of num_words words """
    sentence = ''
    while num_words > 0:
        word = random.choice(word_dict['$'])
        sentence += word + ' '
        num_words -= 1
        while word[-1] not in '.?!' and num_words > 0:
            word = random.choice(word_dict[word])
            sentence += word + ' '
            num_words -= 1            
    return sentence
