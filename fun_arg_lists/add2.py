#!/usr/bin/python

##############################
## File: add2.py
##
## Shows how argument lists are handled
## in Python
##
## author: vladimir kulyukin
##
##############################

def add2(x, y):
    return x + y

print "\n";

## This is the only call to add2 that the Python
## interpreter lets through
print 'add2(1, 2)=', add2(1, 2), "\n\n";

## All calls of add2() below result in the 
## TypeError: add2() takes exactly 2 parameters
print 'add2()=', add2(), "\n\n";
print 'add2(1)=', add2(1), "\n\n";
print 'add2(1, 2, 3)=', add2(1, 2, 3), "\n\n";
print "\n";
