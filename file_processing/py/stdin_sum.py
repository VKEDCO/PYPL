#!/usr/bin/python
## print sum of integers in STDIN
import sys
print sum([int(x) for x in sys.stdin.readlines()])
