#!/usr/bin/python

#######################################
# Read in a file of numbers and
# sort them from smallest to largest.
# @author: vladimir kulyukin
#######################################


import sys

# 1. get 1st command line arg
file_path = sys.argv[1]
# 2. open file_path for reading
infile = open(file_path, 'r')
# 3. read the lines, sort, print
for n in sorted([int(line) for line in infile.readlines()]):
    print n

