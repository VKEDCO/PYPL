#!/usr/bin/python
## sort numbers in STDIN in descending order
import sys
for n in sorted([int(x) for x in sys.stdin.readlines()], reverse=True):
    print n
