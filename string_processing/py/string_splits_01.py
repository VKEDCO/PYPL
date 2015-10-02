#!/usr/bin/python

#######################################################
## Splitting strings in Py
## author: vladimir kulyukin
#######################################################

text_01 = 'word1 word2 word3'
text_02 = 'word1, word2; word3'

def split_test_01(txt):
    for s in txt.split(' '):
        print s

split_test_01(text_01)
split_test_01(text_02)

def split_test_02(txt):
    for s in txt.split(';'):
        print s

split_test_02(text_01)
split_test_02(text_02)
