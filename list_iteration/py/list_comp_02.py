#!/usr/bin/python

##################################################################
## Py list comprehension for manipulating 2D matrices represented
## as lists or tuples.
##
## author: vladimir kulytukin
##################################################################

matrix = \
[
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

tuple_matrix = \
(
    (1, 1, 1),
    (2, 2, 2),
    (3, 3, 3)
)

matrix2 = \
[
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

tuple_matrix2 = \
(
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8)
)

## compute sum total of 2D mat w/o list comp
def mat_sum_1a(mat):
    sum_total = 0
    for r in mat:
        sum_total += sum(r)
    return sum_total

print 'list matrix sum  = ', mat_sum_1a(matrix)
print 'tuple matrix sum = ', mat_sum_1a(tuple_matrix)

## compute sum total of 2D mat w/ list comp
def mat_sum_1b(mat):
    return sum([sum(r) for r in mat])

print 'list matrix sum  = ', mat_sum_1b(matrix)
print 'tuple matrix sum = ', mat_sum_1b(tuple_matrix)

## compute sum total of column cn w/o list comp
def mat_col_sum_2a(mat, cn):
    col_sum_total = 0
    for r in mat:
        col_sum_total += r[cn]
    return col_sum_total

def test_mat_col_sum_2a():
    for cn in xrange(3):
        print mat_col_sum_2a(matrix2, cn)

## compute sum total of column cn w/ list comp        
def mat_col_sum_2b(mat, cn):
    return sum([row[cn] for row in mat])

def test_mat_col_sum_2b():
    for cn in xrange(3):
        print mat_col_sum_2b(matrix2, cn)

print 'list matrix column sums:'
test_mat_col_sum_2a()
print 'tuple matrix column sums:'
test_mat_col_sum_2b()
