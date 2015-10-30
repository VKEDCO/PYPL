#!/usr/bin/python
## print integers from STDIN that are <= sys.argv[1]
## to run: more numbers.txt | python lte_input_thresh.py 10
import sys
thresh = int(sys.argv[1])
for n in [int(x) for x in sys.stdin.readlines() if int(x) <= thresh]:
    print n
