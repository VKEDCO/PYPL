#!/usr/bin/python

############################
# multiple substitutions
# @author: vladimir kulyukin
############################

import re

txt0 = 'I like to program in Python.'
txt1 = 'I like to program in Perl.'

all_substs = ((r'I', 'We'), (r'program', 'code'),
              (r'P\w+n', 'C'), (r'.e\w+l', 'C#'))

def make_substs(substs, txt):
    print "Before substitution:\t" + txt
    temp_txt = txt
    for pat, repl in substs:
        temp_txt = re.sub(pat, repl, temp_txt)
    print "After substitution:\t" + temp_txt
    print '******'

make_substs(all_substs, txt0)
make_substs(all_substs, txt1)
