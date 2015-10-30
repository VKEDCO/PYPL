#!/usr/bin/python
## print numbers from file in sys.argv[1] that are <= int(sys.argv[2])
## to run: >python lte_thresh.py numbers.txt 10
## @author: vladimir kulyukin
import sys
file_path, thresh = sys.argv[1], int(sys.argv[2])
with open(file_path, 'r') as infile:
    for n in [int(line) for line in infile.readlines()
              if int(line) <= thresh]:
        print n
