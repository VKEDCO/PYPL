#!/usr/bin/python

'''
===============================================
module: factorization.py
author: vladimir kulyukin
===============================================
'''

def proper_factors(n):
    if n == 0 or n == 1:
        return []
    pf = []
    for x in xrange(1, n):
        if n % x == 0:
            pf.append(x)
    return pf

def is_deficient(n):
    return sum(proper_factors(n)) < n

def is_abundant(n):
    return sum(proper_factors(n)) > n

def is_perfect(n):
    if n == 0:
        return False
    else:
        return sum(proper_factors(n)) == n

def perfects_in_range(lower, upper):
    if lower > upper:
        return []
    pns = []
    for x in xrange(lower, upper+1):
        if is_perfect(x):
            pns.append(x)
    return pns

def gcd(a, b):
    if b == 0:
        return abs(a)
    x, y = b, a % b
    while y != 0:
        tx, ty = y, x % y
        x, y = tx, ty
    return abs(x)

def lcm(a, b):
    return abs(a * b)/gcd(a, b)
