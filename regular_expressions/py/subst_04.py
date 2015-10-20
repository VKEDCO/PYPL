#!/usr/bin/python

import re

txt0 = 'I like to program in python, Python, PYTHON!'

matches = re.findall(r'p\w+n', txt0, re.IGNORECASE)
print matches
