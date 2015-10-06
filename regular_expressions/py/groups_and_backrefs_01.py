#!/usr/bin/python

################################################
## matching groups & backrefs
## author: vladimir kulyukin
############################################

import re

## define the text strings
txt_01 = '12345'
txt_02 = '1+1=2'
txt_03 = ' 1 + 1 = 2 ' ## an example of text with useless whitespace

def test_1(txt):
    ## match one digit and put it into a group
    match_01 = re.search(r'(\d)', txt)
    print 'group = ',  match_01.group()
    ## span is the beginning and end of the group's matching string
    print 'span  = ', match_01.span()

##test_1(txt_01)    ## txt_01 = '12345', (\d)

def test_2(txt):
    ## (\d+) - match a group of 1 or more digit character
    match_02 = re.search(r'(\d+)', txt)
    print 'group = ', match_02.group()
    print 'span  = ', match_02.span()

#test_2(txt_01) ## (\d+) against '12345'

def test_3(txt):
    ## split the text into three groups: (\d)(\d*)(\d)
    ## match_03 is a match object; the library re defines a special class called Match
    match_03 = re.search(r'(\d)(\d*)(\d)', txt_01)
    print 'groups  = ', match_03.groups() ## ('1', '234', '5') len(match.groups())
    print 'group 1 = ', match_03.group(1)
    print 'group 2 = ', match_03.group(2)
    print 'group 3 = ', match_03.group(3)
    print 'span    = ', match_03.span()

#test_3(txt_01)   ## '12345' (\d)(\d*)(\d); group 1 = '1', group 2 = '234', group 3 = '5'

def test_4(txt):
    match_04 = re.search(r'(\d)\+(\d)=(\d)', txt_02)
    print 'group 1 = ', match_04.group(1)
    print 'group 2 = ', match_04.group(2)
    print 'group 3 = ', match_04.group(3)
    print 'span    = ', match_04.span()

#test_4(txt_01)

## eat white space
def test_5(txt):
    match_05 = re.search(r'\s*(\d)\s*\+\s*(\d)\s*=\s*(\d)\s*', txt_03)
    print 'group 1 = ', match_05.group(1)
    print 'group 2 = ', match_05.group(2)
    print 'group 3 = ', match_05.group(3)
    print 'span    = ', match_05.span()

#test_5(txt_03)
