#!/usr/bin/python

############################
# py substitutions
# @author: vladimir kulyukin
############################

import re

txt0 = 'I like to program in Python.'
txt1 = 'I like to program in Perl.'

def make_subst(txt, pat, repl):
    print "Before substitution:\t" + txt
    temp_txt = re.sub(pat, repl, txt)
    print "After substitution:\t" + temp_txt
    print '******'

## how to replace one string with another
make_subst(txt0, 'Python', 'C++') ## replace 'Python' with 'C++' in txt0
make_subst(txt1, 'Perl', 'Java') ## replace 'Perl' with 'Java' in txt1

## how to replace a pattern with a string
make_subst(txt0, r'P\w+n', 'C') ## replace 'P\w+n' with 'C' in txt0
make_subst(txt1, r'.e\w+l', 'C#') ## replace 'P\w+n' with 'C' in txt1
