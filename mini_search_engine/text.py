### Module: text.py ###                                            
##  Description: text module
##  of the Mini Search Engine project
##  Includes the following classes:
##  - PickleStrMap
##  - Stoplist
##  - FileToDocSetMap
##  - TextProcessor
##
##  Dependencies:
##  - requires saving Vivake Gupta's PorterStemmer
##    class in porter.py
##  PorterStemmer class can be obtained from
##  http://tartarus.org/~martin/PorterStemmer/python.txt
##
##  Comment out if __name__ == '__main__':
##  statement at the end if you do not intend
##  to use it from command line.
##
##  Comments, bugs, and errors to
##  vladimir dot kulyukin at gmail dot com
##
##  Python version: Python 2.7
##  Operating System: Windows XP/7
##
##  http://www.youtube.com/user/vkedco                                                            
#########################################

__metaclass__ = type

import cPickle
import porter

class PickleStrMap:
    def __init__(self):
        self.__dict = {}

    def __validateKey(self, key):
        if not isinstance(key, basestring):
            raise TypeError
        else:
            return key

    def __len__(self):
        return self.__dict.__len__()

    def __getitem__(self, key):
        return self.__dict.get(key, None)

    def __setitem__(self, key, value):
        ek = self.__validateKey(key)
        self.__dict[ek] = value

    def __delitem__(self, key):
        del self.__dict[key]

    def iteritems(self):
        return self.__dict.iteritems()

    ## this is a decorator to define a static method.
    @staticmethod
    def load(picklefile):
        with open(picklefile, 'rb') as inpickle:
            return cPickle.load(inpickle)

    def hasKey(self, key):
        ek = self.__validateKey(key)
        return self.__dict.has_key(ek)

    def pickle(self, picklefile):
        with open(picklefile, 'wb') as infilehandle:
            cPickle.dump(self, infilehandle)

    def display(self):
        for k, v in self.__dict.iteritems():
            print k, '-->', v

    def clear(self):
        self.__dict.clear()

class Stoplist(PickleStrMap):

    def __init__(self, stopfile):
        super(Stoplist, self).__init__()
        self.__load(stopfile)

    def __process(self, line):
        return line.strip(' \n').lower()

    def __load(self, stopfile):
        with open(stopfile, 'r') as infile:
            for ln in infile:
                pln = self.__process(ln)
                if not pln == '' and not self[pln]:
                    self[pln] = True

    def reload(self, stopfile):
        self.clear()
        self.__load(stopfile)

    def isIn(self, term):
        k = self[term]
        if k:
            return True
        else:
            return False

class FileToDocSetMap(PickleStrMap):
    ''' A map of filenames to document sets '''
    def __init__(self):
        super(FileToDocSetMap, self).__init__()

class TextProcessor:
    '''
    TextProcessor objects remove punctuation, stoplist and stem
    .TXT files.
    '''
    def __init__(self, punctuation_marks, stoplist, stemmer):
        self.__punctuationMarks = punctuation_marks
        self.__stoplist = stoplist
        self.__stemmer = stemmer

    def processString(self, str):
        print 'processing', str
        rslt = [self.__stem(w.strip(self.__punctuationMarks).lower())
                for w in str.split()
                if not self.__stoplist.isIn(w)]
        print rslt
        if not rslt:
            return []
        else:
            return rslt

    def __stem(self, trm):
        return self.__stemmer.stem(trm, 0, len(trm)-1)

    def processFile(self, filename):
        doc_set = set()
        with open(filename, 'r') as infile:
            for ln in infile:
                for trm in self.processString(ln):
                    doc_set.add(self.__stem(trm))
        return doc_set
