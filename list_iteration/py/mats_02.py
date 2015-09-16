#!/usr/bin/python
import sys

####################################
## programmatic construction of 2D mats
##
## author: vladimir kulyukin
#####################################

row0 = range(1, 5)
row1 = range(5, 9)
row2 = range(9, 13)

mat = []
mat.append(row0)
mat.append(row1)
mat.append(row2)

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

print_2d_mat(mat, 3, 4)
print_2d_mat2(mat, 3, 4)
