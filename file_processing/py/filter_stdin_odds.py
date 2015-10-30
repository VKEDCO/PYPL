#!/usr/bin/python
## print odd integers from STDIN
## to test:
## > more numbers.txt | python filter_stdin_odds.py
import sys
for n in [int(x) for x in sys.stdin.readlines() if int(x) % 2 != 0]:
    print n
