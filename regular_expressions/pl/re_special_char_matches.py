#!/usr/bin/python

################################################
## matching special characters
## author: vladimir kulyukin
############################################

import re

txt_01 = '12345'
txt_02 = 'abcde'
txt_03 = ' .;!?\\'
txt_04 = ' .;!?\\_'
txt_05 = ' .;!?\\_\n';

txt_lst = (txt_01, txt_02, txt_03, txt_04, txt_05)

def find_digit_char(txt):
    if re.search(r'\d', txt):
        print 'there is at least one digit char in ' + repr(txt)
    else:
        print 'there are no digit chars in ' + repr(txt)
        
def digit_char_tests(txts):
    print r'**** \d Tests ****'
    for txt in txts: find_digit_char(txt)

def find_nondigit_char(txt):
    if re.search(r'\D', txt):
        print 'there is at least one nondigit char in ' + repr(txt)
    else:
        print 'there are no nondigit chars in ' + repr(txt)

def nondigit_char_tests(txts):
    print r'**** \D Tests ****'
    for txt in txts: find_nondigit_char(txt)

def find_word_char(txt):
    if re.search(r'\w', txt):
	print 'there is at least one word char in ' + repr(txt)
    else:
	print 'there are no word chars in ' + repr(txt) 

def word_char_tests(txts):
    print r'**** \w Tests ****'
    for txt in txts: find_word_char(txt)

def find_nonword_char(txt):
    if re.search(r'\W', txt):
	print 'there is at least one non-word char in ' + repr(txt)
    else:
	print 'there are no non-word chars in ' + repr(txt)

def nonword_char_tests(txts):
    print r'**** \W Tests ****'
    for txt in txts: find_nonword_char(txt)

def find_whitespace_char(txt):
    if re.search(r'\s', txt):
	print 'there is at least one whitespace char in ' + repr(txt)
    else:
	print 'there are no whitespace chars in ' + repr(txt)

def whitespace_char_tests(txts):
    print r'**** \s Tests ****'
    for txt in txts: find_whitespace_char(txt)

def find_nonwhitespace_char(txt):
    if re.search(r'\S', txt):
	print 'there is at least one non-whitespace char in ' + repr(txt)
    else:
	print 'there are no non-whitespace chars in ' + repr(txt)

def nonwhitespace_char_tests(txts):
    print r'**** \S Tests ****'
    for txt in txts: find_nonwhitespace_char(txt)


# uncomment to run the tests
#digit_char_tests(txt_lst)
#nondigit_char_tests(txt_lst)
#word_char_tests(txt_lst)
#nonword_char_tests(txt_lst)
#whitespace_char_tests(txt_lst)
#nonwhitespace_char_tests(txt_lst)
