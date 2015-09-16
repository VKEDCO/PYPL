#!/usr/bin/perl

########################################
## fun_refs_01.py
## illustrates how to apply a function to
## each element of a list, collect results
## into a list, and return it.
##
## author: vladimir kulyukin
########################################

def poly1(x):
    return 4*(x**3) + 5*(x**2) + 10*x + 2

def poly2(x):
    return 7*(x**2) + 4*x + 11

def test_poly(poly, range_start, range_end):
    rslt = []
    for n in xrange(range_start, range_end+1):
        rslt.append(poly(n))
    return rslt

print test_poly(poly1, 1, 5)
print test_poly(poly2, 1, 5)
