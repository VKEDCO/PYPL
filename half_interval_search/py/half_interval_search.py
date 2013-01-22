#!/usr/bin/python

###################################################
## half_interval_search.py - half interval search
## for finding roots of f(x) = 0 on [a, b], where
## f(x) is continuous and f(a) < 0 < f(b). 
##
## bugs to vladimir dot kulyukin at gmail dot com
###################################################
import math

def average(x, y): return (x + y)/2.0

## error tolerance level
error_tol = 0.0001

## is |x - y| <= error_tol
def is_small_enough(x, y):
    global error_tol
    return abs(x - y) <= error_tol

def interval_search(f, neg_point, pos_point):
    ## 1. find mid_point of [neg_point, pos_point]
    mid_point = average(neg_point, pos_point)
    ## 2. is |neg_point - pos_point| <= error_tol?
    if is_small_enough(neg_point, pos_point):
	## return mid_point if true
        return mid_point
    else:
	## 3. find the value of f(mid_point)
        fval = f(mid_point)
	## 4. if fval is negative, search [mid_point, pos_point]
        if fval < 0:
            return interval_search(f, mid_point, pos_point)
	## 5. if fval is positive, search [neg_point, mid_point]
        elif fval > 0:
            return interval_search(f, neg_point, mid_point)
	## 6. mid_point is it!
        else:
            return mid_point

def half_interval_search(f, a, b):
    ## compute f(a) and f(b)
    av, bv = f(a), f(b)
    ## if f(a) < 0 and f(b) > 0, then
    ## a is the negative point and b is the positive point
    if av < 0 and bv > 0:
        return interval_search(f, a, b)
    ## if f(a) > 0 and f(b) < 0, then
    ## b is the negative point and a is the positive point
    elif av > 0 and bv < 0:
        return interval_search(f, b, a)
    ## raise an Exception because one point must
    ## be negative and the other positive
    else:
        raise Error('values must be of opposite sign')

## f(x) = x^3 - 2x - 3
def poly_01(x): return x**3 - 2*x - 3

## f(x) = x^5 - 5x - 5
def poly_02(x): return x**5 - 5*x - 5

## f(x) = -x + 2
def poly_03(x): return -x + 2

## print out f(x) = x^3 - 2x - 3 = 0, x in [1, 2]
zero_01 = half_interval_search(poly_01, 1, 2)
print 'f(x) = x^3 - 2x - 3 = 0, on [1, 2], ', \
      'zero_01 = ', zero_01, ' f(zero_01) = ', poly_01(zero_01)

## print out f(x) = x^5 - 5x - 5, on [1, 2]
zero_02 = half_interval_search(poly_02, 1, 2)
print 'f(x) = x^5 - 5x - 5 = 0, on [1, 2], ' \
      'zero_02 = ', zero_02, ' f(zero_02) = ', poly_02(zero_02)

## print out f(x) = -x + 2, on [0, 10]
zero_03 = half_interval_search(poly_03, 1, 10)
print 'f(x) = -x + 2 = 0, on [0, 10], ', \
      'zero_03 = ', zero_03, ' f(zero_03) = ', poly_03(zero_03)

## print out cos(x) = 0, on [9, 12]
zero_04 = half_interval_search(math.cos, 9, 12)
print 'cos(x) = 0, on [9, 12], ', \
      'zero_04 = ', zero_04, ' cos(zero_04) = ', math.cos(zero_04)




    


    
    
    
    
