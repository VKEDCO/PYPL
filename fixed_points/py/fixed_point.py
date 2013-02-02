#!/usr/bin/python

########################################################
## fixed points of functions, ith roots of positive
## integers, the golden ratio as a fixed point
## 
## bugs to vladimir dot kulyukin at gmail dot com
######################################################

import math

def average(x, y): return (x + y)/2.0

## (x, f(x))/2.0
def average_damp(f): return lambda x: average(x, f(x))

error_tolerance = .00001

def find_fixed_point(f, guess):
    global error_tolerance
    def is_close_enough(x, y):
        return abs(x - y) <= error_tolerance

    next_guess = f(guess)
    if is_close_enough(guess, next_guess):
        return next_guess
    else:
        return find_fixed_point(f, next_guess)

## f(x): n/x^(i-1)
## the it-th root of a positive integer n can
## be computed as a fixed point of the average damp of
## lambda x: n / (x**(i-1))
def ith_root_lambda(n, i):
    return lambda x: n / (x**(i-1))

## sqrt(n) is a fixed point of the average damp
## of lambda x: n/x; 1.0 is the 1st guess
def square_root_01(n):
    return find_fixed_point(average_damp(lambda x: n/x),
			    1.0)

## sqrt(n) is a fixed point of the average damp
## of ith_root_lambda(n, 2) == lambda x: n / (x**1)
def square_root_03(n):
    return find_fixed_point(average_damp(ith_root_lambda(n, 2)),
			    1.0)

## n^(1/3) is a fixed point of the average damp
## of lambda x: n / (x * x); 1.0 is the 1st guess.
def cubic_root_01(n):
    return find_fixed_point(average_damp(lambda x: n / (x * x)),
			    1.0)

## n^(1/3) is a fixed point of the average damp
## of ith_root_lambda(n, 3) == lambda x: n / (x**2)
def cubic_root_03(n):
    return find_fixed_point(average_damp(ith_root_lambda(n, 3)),
			    1.0)

## the golden ratio is a fixed point of the average
## damp of the average damp of lambda x: 1 + 1/x; 1.0 is
## 1st guess.
def the_golden_ratio():
    return find_fixed_point(average_damp(lambda x: 1 + 1/x), 1.0)

print square_root_01(2), ' ', square_root_03(2), ' ',\
      2**0.5, "\n"
print square_root_01(3), ' ', square_root_03(3), ' ',\
      3**0.5, "\n""\n"
print square_root_01(9), ' ', square_root_03(9), ' ',\
      9**0.5, "\n""\n""\n"

print cubic_root_01(2), ' ', cubic_root_03(2), ' ',\
      2**(1/3.0), "\n"
print cubic_root_01(3), ' ', cubic_root_03(3), ' ',\
      3**(1/3.0), "\n"
print cubic_root_01(9), ' ', cubic_root_03(9), ' ',\
      9**(1/3.0), "\n"

print the_golden_ratio(), "\n"




