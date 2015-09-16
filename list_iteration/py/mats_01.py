#!/usr/bin/python
import sys

#############################
## two equivalent ways of printing
## 2D mats in Py
##
## author: vladimir kulyukin
#############################

row0 = [1, 2, 3, 4]
row1 = [5, 6, 7, 8]
row2 = [9, 10, 11, 12]

mat = [row0, row1, row2]

def print_2d_mat(mat, num_rows, num_cols):
  for r in xrange(0, num_rows):
    for c in xrange(0, num_cols):
      print mat[r][c], '\t',
    print

def print_2d_mat2(mat, num_rows, num_cols):
  for r in xrange(0, num_rows):
    for c in xrange(0, num_cols):
      sys.stdout.write(str(mat[r][c])+'\t')
    sys.stdout.write('\n')

## let's test and see what prints out
print_2d_mat(mat, 3, 4)
print_2d_mat2(mat, 3, 4)
