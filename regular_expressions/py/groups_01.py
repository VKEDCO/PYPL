#!/usr/bin/python

#######################################################
## groups and backreferences
## author: vladimir kulyukin
#######################################################

import re

def match_groups(pat, txt):
    print '------------------'
    print 'pat = ' + str(pat) + '; ' + 'text = ' + txt
    match = re.search(pat, txt)
    if match != None:
        print 'groups = ', match.groups()
    print '------------------'

match_groups(r'(\w*)(\w)(\w)(\w)', 'abc')    
match_groups(r'(\w*)(\w)(\w)', 'abc')
match_groups(r'(\w)(\w)(\w)', 'abc')
match_groups(r'(\w*)(\w)', 'abc')
