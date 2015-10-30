#!/usr/bin/python
## print max integer in STDIN
import sys
print max([int(x) for x in sys.stdin.readlines()])
