#!/usr/bin/python
## print min integer in STDIN
import sys
print min([int(x) for x in sys.stdin.readlines()])
