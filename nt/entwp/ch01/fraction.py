#!/usr/bin/python

'''
===============================================
module: fraction.py
author: vladimir kulyukin
===============================================
'''

from factorization import gcd, lcm

class fraction:

    def __init__(self, n, d):
        if d == 0:
            raise Exception('denominator is zero')
        self.__n = n
        self.__d = d

    def get_numerator(self):
        return self.__n

    def get_denominator(self):
        return self.__d

    def set_numerator(self, n):
        self.__n = n

    def set_denominator(self, d):
        if d == 0:
            raise Exception('Denominator is 0')
        self.__d = d

    def is_proper(self):
        return self.__n < self.__d

    def is_unit(self):
        return self.__n == 1

    @staticmethod
    def reduce_to_lowest_terms(frac):
        n, d = frac.get_numerator(), frac.get_denominator()
        g = gcd(n, d)
        return fraction(n/g, d/g) 

    def __str__(self):
        return str(self.__n) + str('/') + str(self.__d)

    @staticmethod
    def add(frac1, frac2):
        n1, n2 = frac1.get_numerator(), frac2.get_numerator()
        d1, d2 = frac1.get_denominator(), frac2.get_denominator()
        l = lcm(d1, d2)
        m1, m2 = l/d1, l/d2
        num = m1*n1 + m2*n2
        rf = fraction(num, l)
        return fraction.reduce_to_lowest_terms(rf)

    @staticmethod
    def add_fracs(flist):
        if len(flist) == 1:
            return fraction.reduce_to_lowest_terms(flist[0])
        rslt = flist[0]
        for i in xrange(1, len(flist)):
            rslt = fraction.add(rslt, flist[i])
            rslt = fraction.reduce_to_lowest_terms(rslt)
        return rslt
    
    @staticmethod
    def unit_split_frac(frac):
        '''1/n = 1/(n+1) + 1/(n(n+1))'''
        assert frac.get_numerator() == 1
        d = frac.get_denominator()
        return fraction(1, d+1), fraction(1, d*(d+1))

    @staticmethod
    def sclr_mult(scalar, frac):
        n, d = scalar*frac.get_numerator(), frac.get_denominator()
        return fraction.reduce_to_lowest_terms(fraction(n, d))

    @staticmethod
    def mult(frac1, frac2):
        n1, d1 = frac1.get_numerator(), frac1.get_denominator()
        n2, d2 = frac2.get_numerator(), frac2.get_denominator()
        rslt_frac = fraction(n1 * n2, d1 * d2)
        return fraction.reduce_to_lowest_terms(rslt_frac)

    @staticmethod
    def subtract(frac1, frac2):
        return fraction.add(frac1, fraction.sclr_mult(-1, frac2))
