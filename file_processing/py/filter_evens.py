#!/usr/bin/python
## print even numbers in file in sys.argv[1]
import sys
file_path = sys.argv[1]
with open(file_path, 'r') as infile:
    for n in [int(x) for x in infile.readlines() if int(x) % 2 == 0]:
        print n
