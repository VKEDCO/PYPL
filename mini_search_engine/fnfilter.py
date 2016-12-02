## Mini Search Engine: fnfilter.TextFileFilter
### Module: fnfilter.py ###                                             
##  Description: TextFileFilter class
##  of the Mini Search Engine project
##            
##  Comments, bugs, and errors to
##  vladimir dot kulyukin at gmail dot com
##
##  Python version: Python 2.7.1
##
##  Make sure indentation is correct
##  when cutting and pasting into
##  a .py file.                             
#########################################

import os

class FileFilter:
    def isValid(self, filename):
        return True

class TextFileFilter(FileFilter):
    def isValid(self, filename):
        return (os.path.isfile(filename) and\
               (filename.endswith('.txt') or\
                filename.endswith('.TXT')))
