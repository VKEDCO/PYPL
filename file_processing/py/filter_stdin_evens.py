#!/usr/bin/python
## print even integers from STDIN
## to test:
## > more numbers.txt | python filter_stdin_evens.py
import sys
for n in [int(x) for x in sys.stdin.readlines() if int(x) % 2 == 0]:
    print n
