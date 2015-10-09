#!/usr/bin/python

#######################################################
## Groups and backreferences
## author: vladimir kulyukin
#######################################################

import re

def display_groups_by_backrefs(pat, txt):
    print '------------------'
    print 'pat = ' + str(pat) + '; ' + 'text = ' + txt
    match = re.search(pat, txt)
    if match != None:
        num_of_groups = len(match.groups())
        print 'num of groups = ', num_of_groups;
        for i in xrange(num_of_groups+1):
            print str(i) + ' --> ' + match.group(i)
    print '------------------'

display_groups_by_backrefs(r'(\w)(\w)(\w)',      'abc')
display_groups_by_backrefs(r'(\w*)(\w)',         'abc')
display_groups_by_backrefs(r'(\w*)(\w)(\w)',     'abc')
display_groups_by_backrefs(r'(\w*)(\w)(\w)(\w)', 'abc')
