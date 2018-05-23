#
# Final Project
#
# finalproject.py
#
# Phumin Walaipatchara (phuminw)
#

import math

def test():
    """ your docstring goes here """
    source1 = TextModel('source1')
    source1.add_string('It is interesting that she is interested.')
    print(source1.sentence_lengths)
    source2 = TextModel('source2')
    source2.add_string('I am very, very excited about this!')
    print(source2.sentence_lengths)
    mystery = TextModel('mystery')
    mystery.add_string('Is he interested? No, but I am.')
    print(mystery.sentence_lengths)
    mystery.classify(source1, source2)

def clean_text(txt):
    """ returns a list containing the words in txt after it has been
    “cleaned” """
    for p in ',.?!-:;"':
        txt = txt.replace(p, '')
    return txt.lower()

def stem(s):
    """ returns the stem of s """
    s = s.lower()
    prefix =['inter', 'super', 'trans', 'under', 'anti', 'fore', 'over', 'semi', 'dis', 'mid', 'mis', 'non', 'pre', 'sub', 'de', 'en', 'em', 'in', 'im', 'il', 'ir', 're', 'un']
    suffix = ['ation', 'ition', 'ative', 'itive', 'able', 'ible', 'tion', 'less', 'ment', 'ness', 'eous', 'ious', 'ies', 'ial', 'est', 'ful', 'ing', 'ion', 'ity', 'ive', 'ous', 'al', 'ed', 'en', 'er', 'ic', 'ty', 'ly', 'es', 'e', 's', 'y']
    for pre in prefix:
        if pre == s[0:len(pre)]:
            s = s[len(pre):]
    for suf in suffix:
        if suf == s[-len(suf):]:
            s = s[0:-len(suf)]
    return s

def article(s):
    """ return the dictionary of article frequency """
    articles = []
    for a in s:
        if a in ['a', 'an', 'the']:
            articles += [a]
    return articles

def compare_dictionaries(d1, d2):
    """ compute and return their log similarity score """
    score = 0
    total = sum([d1[n] for n in d1])
    for elem in d2:
        if elem in d1:
            pos = d1[elem] / total
            score += math.log(pos ** d2[elem])
        else:
            score += math.log((0.5 / total) ** d2[elem])
    return score

class TextModel():
    """ A TextModel Class """
    def __init__(self, model_name):
        """ A constructor for TextModel object """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}
        self.stems = {}
        self.sentence_lengths = {}
        self.article = {}

    def __repr__(self):
        """ returns a string representing TextModel """
        return "Text model name: " + self.name + "\nNumber of words: " +\
               str(len(self.words)) + "\nNumber of word lengths: " +\
               str(len(self.word_lengths)) + "\nNumber of stems: " +\
               str(len(self.stems)) + "\nNumber of sentence lengths: " +\
               str(len(self.sentence_lengths)) + "\nPercentage of article: " +\
               str(sum([self.article[n] for n in self.article])*100/\
                   sum([self.words[n] for n in self.words]))
   
    def add_string(self, s):
        """ adds a string of text s to the model by augmenting the feature
        dictionaries defined in the constructor """
        sentences = s.replace('?', '.').replace('!', '.').split('.')
        for sen in sentences:
            if len(sen) != 0:
                if len(sen.split()) not in self.sentence_lengths:
                    self.sentence_lengths[len(sen.split())] = 1
                else:
                    self.sentence_lengths[len(sen.split())] += 1
        word_list = clean_text(s).split()
        for w in word_list:
            if w not in self.words:
                self.words[w] = 1
            else:
                self.words[w] += 1
        word_list_len = [len(w) for w in word_list]
        for l in word_list_len:
            if l not in self.word_lengths:
                self.word_lengths[l] = 1
            else:
                self.word_lengths[l] += 1
        word_stem = [stem(word) for word in word_list]
        for word in word_stem:
            if word not in self.stems:
                self.stems[word] = 1
            else:
                self.stems[word] += 1
        for a in article(word_list):
            if a not in self.article:
                self.article[a] = 1
            else:
                self.article[a] += 1

    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model
        """
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        for line in file:
            line = line[:-1]
            self.add_string(line)

    def similarity_scores(self, other):
        """ computes and returns a list of log similarity scores measuring
        the similarity of self and other """
        return [compare_dictionaries(other.words, self.words)] + \
               [compare_dictionaries(other.word_lengths, self.word_lengths)] + \
               [compare_dictionaries(other.stems, self.stems)] + \
               [compare_dictionaries(other.sentence_lengths, self.sentence_lengths)] + \
               [compare_dictionaries(other.article, self.article)]

    def classify(self, source1, source2):
        """ compares the called TextModel object (self) to two other
        “source” TextModel objects  """
        scores1 = self.similarity_scores(source1)
        scores2 = self.similarity_scores(source2)
        print("Scores for ", source1.name, ": ", scores1)
        print("Scores for ", source2.name, ": ", scores2)
        weighted_sum1 = 10*scores1[0] + 4*scores1[1] + 7*scores1[2] + 6*scores2[3] + 9*scores2[4]
        weighted_sum2 = 10*scores2[0] + 4*scores2[1] + 7*scores2[2] + 6*scores2[3] + 9*scores2[4]
        if weighted_sum1 > weighted_sum2:
            print(self.name, "is more likely to have come from", source1.name)
        elif weighted_sum1 < weighted_sum2:
            print(self.name, "is more likely to have come from", source2.name)
        else:
            print("The result cannot be concluded")
        
    def save_model(self):
        """ saves the TextModel object self by writing its various feature
        dictionaries to files """
        name = ""
        for n in self.name.split():
            name += n[0]
        file = open(name + "_words", 'w')
        file.write(str(self.words))
        file.close()
        file = open(name + "_word_lengths", 'w')
        file.write(str(self.word_lengths))
        file.close()
        file = open(name + "_stems", 'w')
        file.write(str(self.stems))
        file.close()
        file = open(name + "_sentence_lengths", 'w')
        file.write(str(self.sentence_lengths))
        file.close()
        file = open(name + "_article", 'w')
        file.write(str(self.article))
        file.close()

    def read_model(self):
        """ reads the stored dictionaries """
        name = ""
        for n in self.name.split():
            name += n[0]
        file = open(name + "_words", 'r')
        self.words = dict(eval(file.read()))
        file.close()
        file = open(name + "_word_lengths", 'r')
        self.word_lengths = dict(eval(file.read()))
        file.close()
        file = open(name + "_stems", 'r')
        self.stems = dict(eval(file.read()))
        file.close()
        file = open(name + "_sentence_lengths", 'r')
        self.sentence_lengths = dict(eval(file.read()))
        file.close()
        file = open(name + "_article", 'r')
        self.article = dict(eval(file.read()))
        file.close()
    
