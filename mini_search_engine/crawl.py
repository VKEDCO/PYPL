### Module: crawl.py ###                                             
##  Description: crawl module
##  of the Mini Search Engine project
##  Includes the following classes:
##  - Crawler
##
##  Dependencies:
##  - text.py
##
##  Comments, bugs, and errors to
##  vladimir dot kulyukin at gmail dot com
##
##  Python version: Python 2.7
##  Operating System: Windows XP/7
##
##  Make sure indentation is correct when
##  cutting and pasting in a .py file.                                                             
#########################################

import os
from os.path import join, getsize
import text

class Crawler:
    '''
    Crawl a given dictory, process each .txt file, and
    and update the index map.

    When the index map is constructed, it can be persisted
    with pickleFileToDocSetMap.
    '''
    def __init__(self, fileFilter,
                 fileToDocSetMap,
                 fileProcessor):
        self.__fileFilter = fileFilter
        self.__fileToDocSetMap = fileToDocSetMap
        self.__fileProcessor = fileProcessor

    def crawl(self, dirname):
        if os.path.isfile(dirname):
            print dirname, 'is a file'
            return
        for root, dirs, files in os.walk(dirname):
            print 'Crawling ', root, '...'
            for txtf in [join(root, f)
                         for f in files
                         if self.__fileFilter.isValid(join(root,f))]:
                print 'Processing', txtf, '...'
                txtf_docset = self.__fileProcessor.processFile(txtf)
                self.__fileToDocSetMap[txtf] = txtf_docset
                                          

    def pickleFileToDocSetMap(self, picklefile):
        self.__fileToDocSetMap.pickle(picklefile)
