#Created by Suprotik Dey
#@2018
#
#PyOffDict is an Offline Dictionary for Python
#Based on Webster's Unabridged English Dictionary
#Data Taken from https://github.com/matthewreagan/WebstersEnglishDictionary

import pkg_resources

class Dictionary():
    def __init__(self):
        self.__dictionary_path = "dictionary.txt"
        self.__loadAsDictfromTxt(self.__dictionary_path)
        
    def __retDataPath(self):
        f_path = pkg_resources.resource_filename(__name__, self.__dictionary_path)
        return f_path
        
    def __linesplitterFormatter(self,line):
        line = line.strip()
        line = line.rstrip(',')
        word, meaning = line.split(':', 1)
        word = word.strip('"').strip().strip('"').lower()
        meaning = meaning.strip('"').strip().strip('"')
        
        return word,meaning
    
    def __loadAsDictfromTxt(self,filename):
        self.__DataDict = {}
        with open(self.__retDataPath()) as f:
            for line in f:
                word, meaning = self.__linesplitterFormatter(line)
                if word in self.__DataDict:
                    print("Repeat! Word Ignored Word: "+word)
                else:
                    self.__DataDict[word]=meaning  
        
        
    def lookup(self,word):
        word=word.lower()
        if word in self.__DataDict:
            return self.__DataDict[word]
        else:
            return 'Unknown'
    
    def get_numOfWords(self):
        return len(self.__DataDict)
        

dictt = Dictionary()