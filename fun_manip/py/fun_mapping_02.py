#!/usr/bin/python

#################################################
# Using Py's map to map named functions of 1, 2, and 3
# arguments over lists.
#
# author: vladimir kulyukin
#################################################

numbers = range(1, 11);

## *** mapping a named 1-arg sub over a list of numbers ***

## poly defines f(x) = x^2 + 5x - 10, which
## is a function of 1 argument.
def poly(x): return x**2 + 5*x - 10

## let's map poly over @numbers
map1 = map(poly, numbers)
print 'map1 = ', map1

## *** Mapping a nambed 2-arg sub over a list of numbers ***

## fun 2 defines f(x, y) = x^2 + y^3.
def fun2(x, y): return x**2 + y**3 

## let's map fun2 over 2 lists.
map2 = map(fun2, [1, 3, 5], [2, 4, 6])
print 'map2 = ', map2

## *** Mapping a named 3-arg sub over a list of 3-tuples ****

## fun3 defines f(x, y, z) = x^2 + y^3 + z^4;
def fun3(x, y, z): return x**2 + y**3 + z**4

## let's map fun2 over three lists
map3 = map(fun3, [1, 4, 7], [2, 5, 8], [3, 6, 9])
print 'map3 = ', map3

## ****** slicker, more Py-like, ways of doing the same computations
map2a = map(lambda xy: fun2(xy[0], xy[1]), zip(xrange(1, 6, 2), xrange(2, 7, 2)))
print 'map2a = ', map2a

map3a = map(lambda xyz: fun3(xyz[0], xyz[1], xyz[2]), zip(xrange(1, 8, 3), xrange(2, 9, 3), xrange(3, 10, 3)))
print 'map3a = ', map3a
