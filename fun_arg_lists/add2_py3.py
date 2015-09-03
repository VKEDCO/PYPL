#!/usr/bin/python

##############################
## File: add2_py3.py
##
## Shows how argument lists are handled
## in Py3. It also shows that that
## the number of arguments in a py
## function is firmly fixed once the
## function is defined.
##
## author: vladimir kulyukin
##############################

def add2(x, y):
    return x + y

## This is the only call to add2 that the Python
## interpreter lets through
print('add2(1, 2)=', add2(1, 2), "\n")
print('add2(10, 2.0)=', add2(10, 2.0), "\n")
print('add2(10.0, 2)=', add2(10.0, 2), "\n")
print('add2(2.75, 2.0)=', add2(2.75, 2.0), "\n")

## All calls of add2() below result in the 
## TypeError: add2() takes exactly 2 parameters
print('add2()=', add2(), "\n")
print('add2(1)=', add2(1), "\n")
print('add2(1, 2, 3)=', add2(1, 2, 3), "\n")
