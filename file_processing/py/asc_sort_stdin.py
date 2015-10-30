#!/usr/bin/python
## sort numbers in STDIN in ascending order
import sys
for n in sorted([int(x) for x in sys.stdin.readlines()]):
    print n
