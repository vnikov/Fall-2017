#
# Final Project
#
# finalproject.py
#
# Phumin Walaipatchara (phuminw)
#

def clean_text(txt):
    """ returns a list containing the words in txt after it has been
    “cleaned” """
    #return_txt = ''
    for p in ',.?!-:;"':
        txt = txt.replace(p, '')
    return txt.lower()
        
class TextModel():
    """ A TextModel Class """
    def __init__(self, model_name):
        """ A constructor for TextModel object """
        self.name = model_name
        self.words = {}
        self.word_lengths = {}

    def __repr__(self):
        """ returns a string representing TextModel """
        return "Text model name: " + self.name + "\nNumber of words: " +\
               str(len(self.words)) + "\nNumber of word lengths: " +\
               str(len(self.word_lengths))
   
    def add_string(self, s):
        """ adds a string of text s to the model by augmenting the feature
        dictionaries defined in the constructor """
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

    def add_file(self, filename):
        """ adds all of the text in the file identified by filename to the model
        """
        file = open(filename, 'r', encoding='utf8', errors='ignore')
        for line in file:
            line = line[:-1]
            self.add_string(line)

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

    
