#!/usr/bin/python

#####################################
## reading a file and sorting
## its lines lexicographically.
## @author: vladimir kulyukin
#####################################

import sys

# 1. get the 1st command line argument
file_path = sys.argv[1]
# 2. open the file for reading
infile = open(file_path, 'r')
# 3. read lines, sort, and print
for n in sorted([line for line in infile.readlines()]):
    print n,
