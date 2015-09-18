#!/usr/bin/python

########################################
## illustrates how to apply a Py lamda
## function to each element of a list with
## map.
##
## author: vladimir kulyukin
########################################

## *** mapping expression lambda x: x+5 function over
## a list of numbers
numbers = range(1, 11)
map1 = map(lambda x: x+5, numbers)
print 'map1 = ', map1

## *** mapping expression lambda x: x**2 + 2*x + 10
## over a list of numbers
map2 = map(lambda x: x**2 + 2*x + 10, numbers)
print 'map2 = ', map2

## ***mapping function len over a list of strings
words = ['one', 'two', 'three', 'four', 'five']
map3 = map(len, words) ## same as map3 = map(lambda x: len(x), words)
print 'map3 = ', map3
