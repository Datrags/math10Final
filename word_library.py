#Word Library class by Stephan Green
#Used to create an object that will contain all words from a given file
#8/12/2021
class Word_Library(object):

    def __init__(self, textfile):
        f = open(textfile,'r')
        self.library = f.readlines()
        f.close()
    def return_word_range(self, start, end):
        return self.library[start:end]

    def get_library(self):
        return self.library
