#!/usr/bin/python

#######################################
# Read in a file of numbers and
# pick out odds or events and compute
# their sums.
# @author: vladimir kulyukin
#######################################

import sys

def is_odd(n):  return n % 2 != 0
def is_even(n): return not is_odd(n)

def filter_lines(file_path, fun, pred):
    with open(file_path, 'r') as infile:
        return [fun(line) for line in infile if pred(line)]

def pick_odds(file_path):
    return filter_lines(file_path,
                        lambda x: int(x),
                        lambda x: is_odd(int(x)))

def pick_evens(file_path):
    return filter_lines(file_path,
                        lambda x: int(x),
                        lambda x: is_even(int(x)))

def sum_odds(file_path):  return sum(pick_odds(file_path))
def sum_evens(file_path): return sum(pick_evens(file_path))

def main(file_path):
    for n in pick_evens(file_path): print n

if __name__ == '__main__':
    main(sys.argv[1])
