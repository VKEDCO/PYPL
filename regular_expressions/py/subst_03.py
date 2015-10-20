#!/usr/bin/python

import re

txt0 = 'I like to program in Python, Python, Python!'
txt1 = 'I like to program in Perl, Perl, Perl!'

print txt0
print re.sub(r'Python', 'C', txt0)
print '*******'

print txt1
print re.sub(r'Perl', 'C++', txt1)
print '*******'
