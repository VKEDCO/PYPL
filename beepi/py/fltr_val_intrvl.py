#!/usr/bin/python

#############################
# @author: vladimir kulyukin
#############################
import re
import sys

val_index  = int(sys.argv[1])
lower_bound = int(sys.argv[2])
upper_bound = int(sys.argv[3])
for line in sys.stdin.readlines():
    match = re.match(r'\S+', line)
    if match != None:
        val = int(re.split(r'\t', line)[val_index])
        if lower_bound <= val and val <= upper_bound:
            sys.stdout.write(line)
