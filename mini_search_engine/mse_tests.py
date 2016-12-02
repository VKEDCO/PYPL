### Module: mse_tests.py ###                                             
##  Description: tests of the Mini
##  Search Engine project
##
##  Comments, bugs, and errors to
##  vladimir dot kulyukin at gmail dot com
##
##  Python version: Python 2.7.1
##
##  Make sure indentation is correct when
##  cutting and pasting in a .py file.                                                             
#########################################

import crawl
import fnfilter
import text
import porter ## you need to install this.
import rtrvr

### change this variable accordingly.
my_test_dir = '/home/vladimir/code/python/mse/'

def test_00():
    sm = text.PickleStrMap()
    sm['a'] = 1
    sm['b'] = 2
    print len(sm)
    sm.display()
    del sm['a']
    print len(sm)
    sm.display()
    pkl_file = my_test_dir + 'map.pkl'
    sm.pickle(pkl_file)
    sm2 = text.PickleStrMap.load(pkl_file)
    sm2.display()

#test_00()

my_test_dir = '/home/vladimir/code/python/mse/'

def test_00():
    sm = text.PickleStrMap()
    sm['a'] = 1
    sm['b'] = 2
    print len(sm)
    sm.display()
    del sm['a']
    print len(sm)
    sm.display()
    pkl_file = my_test_dir + 'map.pkl'
    sm.pickle(pkl_file)
    sm2 = text.PickleStrMap.load(pkl_file)
    sm2.display()

#test_01()

#######################################################
# test_03() works with the following poem saved in poem.txt
#
# Two Kinds of Intelligence
#
# There are two kinds of intelligence: One acquired,
# as a child in school memorizes facts and concepts
# from books and from what the teacher says,
# collecting information from the traditional sciences
# as well as from the new sciences.
#
# With such intelligence you rise in the world.
# You get ranked ahead or behind others
# in regard to your competence in retaining
# informaiton. You stroll with this intelligence
# in and out of fields of knowledge, getting always more
# marks on your preserving tables.
#
# There is another kind of table, one
# already completed and preserved inside you.
# A spring overflowing its springbox. A freshness
# in the center of the chest. This other intelligence
# does not turn yellow or stagnate. It's fluid,
# and it does not move from outside to inside
# through the conduits of plumbing-learning.
#
# This second knowing is a fountainhead
# from within you, moving out.
#
#Jelaluddin Rumi  (1207 - 1273)
# Translated from Persian by Coleman Barks
# Book: This Longining, Shambala Publications, Inc.
########################################

def test_02():
    stp = text.PickleStrMap.load(my_test_dir + 'stoplist.pkl')
    stm = porter.PorterStemmer()
    tp = text.TextProcessor(' `~!@#$%%^&*()_+{}|\[];\':";\',./?><',
                            stp, stm)
    docset = tp.processFile(my_test_dir + 'poem.txt')
    print docset


# test_02()

def test_03():
    stp = text.PickleStrMap.load(my_test_dir + 'stoplist.pkl')
    fnfltr = fnfilter.TextFileFilter()
    ftdsmap = text.FileToDocSetMap()
    stm = porter.PorterStemmer()
    tp = text.TextProcessor(' `~!@#$%%^&*()_+{}|\[];\':";\',./?><',
                            stp, stm)
    crwlr = crawl.Crawler(fnfltr, ftdsmap, tp)
    crwlr.crawl(my_test_dir + 'texts/')
    crwlr.pickleFileToDocSetMap(my_test_dir + 'file_to_docset_map.pkl')


#test_03()

def test_04():
    docsets = text.PickleStrMap.load(my_test_dir + 'file_to_docset_map.pkl')
    docsets.display()
    print len(docsets)

# test_04()

## poem.txt contains the same poem by Rumi referenced above.
def test_05():
    stp = text.PickleStrMap.load(my_test_dir + 'stoplist.pkl')
    fnfltr = fnfilter.TextFileFilter()
    ftdsmap = text.FileToDocSetMap()
    stm = porter.PorterStemmer()
    tp = text.TextProcessor(' `~!@#$%%^&*()_+{}|\[];\':";\',./?><',
                            stp, stm)
    docset = tp.processFile(my_test_dir + 'poem.txt')
    print docset

#test_05()

def test_06():
    docmap = my_test_dir + 'file_to_docset_map.pkl'
    stoplst = my_test_dir + 'stoplist.pkl'
    rt = rtrvr.TextRtrvr(docset_map_file=docmap,
                            punctuation_marks=' `~!@#$%%^&*()_+{}|\[];\':";\',./?><',
                            stoplist_file=stoplst)
    rt.startQueryLoop()

#test_06()

