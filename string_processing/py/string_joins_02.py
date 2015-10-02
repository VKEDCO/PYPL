#!/usr/bin/python

####################################
# Py joins on number ranges
# author: vladimir kulyukin
####################################

range1 = xrange(1, 6)

def join_number_range(separator, rng):
  return separator.join([str(x) for x in rng])

def range_tests(r):
  print join_number_range('*',     r)
  print join_number_range(' ** ',  r)
  print join_number_range('//',    r)

range_tests(range1)
