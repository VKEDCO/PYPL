### Module: rtrvr.py ##################                                             
##  Description: retriever module
##  of the Mini Search Engine project
##  Includes the following classes:
##  - TextRetriever
##
##  Comments, bugs, and errors to
##  vladimir dot kulyukin at gmail dot com
##
##  Python version: Python 2.7.1
##
##  Make sure indentation is correct when
##  cutting and pasting in a .py file.                                                             
#################################
__metaclass__ = type

import text
import porter

class TextRtrvr:

    def __init__(self,
                 docset_map_file='',
                 punctuation_marks='',
                 stoplist_file=''):
        self.__docMap = text.PickleStrMap.load(docset_map_file)
        self.__txtprr = text.TextProcessor(punctuation_marks,
                                           text.PickleStrMap.load(stoplist_file),
                                           porter.PorterStemmer())

    @staticmethod
    ## compute the length of two sets of strings
    def __docSetMatch(docset1, docset2):
        inter_size = len(docset1.intersection(docset2))
        return inter_size

    ## 1. Take a user query
    ## 2. Process the user query, i.e. remove punctuation,
    ##    stem, and stoplist
    ## 3. Iterate over the doc sets in the database and
    ##    compute the match b/w the user query set and each
    ##    document set
    ## 4. Sort the document sets by the match scores and
    ##    and retrieve the top three matches.
    def matchQuery(self, query):
        docscores = []
        qset = set(self.__txtprr.processString(query))
        dit = self.__docMap.iteritems()
        for fn, docset in dit:
            docscores.append((fn, TextRtrvr.__docSetMatch(qset, docset)))
        return [m for m in sorted(docscores, key = lambda x: x[1], reverse=True)[0:3]
                if m[1] > 0]

    def displayRslts(self, rslts):
        for (fn, score) in rslts:
            print fn, '\t', '--->', '\t', score  

    ## keep taking user queries and displaying
    ## the match results until the user enters ''.
    def startQueryLoop(self):
        while True:
            user_input = raw_input('Enter query: ')
            if user_input == '': break
            rslts = self.matchQuery(user_input)
            self.displayRslts(rslts)
        print 'Thank you'
