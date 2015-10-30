#!/usr/bin/python

## print sum of integers from files in sys.argv
import sys
total_sum = 0
for input_file_path in sys.argv[1:]:
    with open(input_file_path, 'r') as infile:
        for n in [int(ln) for ln in infile.readlines()]:
            total_sum += n
print 'total_sum = '  + str(total_sum);
