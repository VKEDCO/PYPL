#!/usr/bin/python

####################################
##
## A Py implementation of Newton's
## square root approximation
##
## Author: Vladimir Kulyukin
## Uncomment the test calls to run the
## tests.
#####################################

import math

def average(x, y): return (x+y)/2.0

def next_guess(n, g):
    return average(g, n/g)

def is_good_enough(n, g, error):
    return abs(n - g*g) <= error

def newton_sqrt_aux(n, g, error):
    if is_good_enough(n, g, error):
        return g
    else:
        ng = next_guess(n, g)
        return newton_sqrt_aux(n, ng, error)

def newton_sqrt(n):
    return newton_sqrt_aux(n, 1, 0.00001)

## ====== tests ===========

def test_average():
    print average(1, 2)
    print average(2, 3)
    print average(2, 2)
    
def test_next_guess():
    print next_guess(2, 1)
    print next_guess(2, next_guess(2, 1))

def test_newton_sqrt():
    print 'newton_sqrt(2)=', newton_sqrt(2), 'math.sqrt(2)=', math.sqrt(2)
    print 'newton_sqrt(3)=', newton_sqrt(3), 'math.sqrt(3)=', math.sqrt(3)
    print 'newton_sqrt(4)=', newton_sqrt(4), 'math.sqrt(4)=', math.sqrt(4)
    print 'newton_sqrt(5)=', newton_sqrt(5), 'math.sqrt(5)=', math.sqrt(5)

## test_average()
## test_next_guess()
## test_newton_sqrt()
    
    













    
