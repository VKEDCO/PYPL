#!/usr/bin/python

##################################################################
## Py list comprehension for 1D list construction
##
## author: vladimir kulytukin
##################################################################

## w/o list comp
def build_list_1a():
    rslt = []
    x = 0
    while x < 11:
        if x % 2 == 0:
            rslt.append(2*x)
        x += 1
    return rslt

print build_list_1a()

## w/ list comp
def build_list_1b():
    return [2*x for x in xrange(11) if x % 2 == 0]

print build_list_1b()

## w/o list comp
def build_list_2a():
    rslt = []
    x = 0
    while x**2 < 100:
        rslt.append(4*x)
        x += 1
    return rslt

print build_list_2a()

## w/ list comp
def build_list_2b():
    return [4*x for x in xrange(101) if x**2 < 100]

print build_list_2b()

## w/o list comp
def build_list_3a():
    rslt = []
    x = 0
    while x < 11:
        if x % 2 != 0:
            rslt.append(x**3)
        x += 1
    return rslt

print build_list_3a()

## w/ list comp
def build_list_3b():
    return [x**3 for x in xrange(11) if x % 2 != 0]

print build_list_3b()

## w/o list comp
def build_list_4a():
    rslt = []
    for x in xrange(6):
        if x % 2 == 0:
            for y in xrange(6):
                if not y % 2 == 0:
                    rslt.append((x,y))
    return rslt

print build_list_4a()

## w/ list comp
def build_list_4b():
    return [(x,y)
            for x in xrange(6) if x % 2 == 0
            for y in xrange(6) if not y % 2 == 0]

print build_list_4b()

## w/o list comp
def int_to_string(x):
    if x == 0:
        return 'zero'
    elif x == 1:
        return 'one'
    elif x == 2:
        return 'two'
    elif x == 3:
        return 'three'
    elif x == 4:
        return 'four'
    elif x == 5:
        return 'five'
    else:
        return 'unknown'

def build_list_5a():
    rslt = []
    for x in xrange(6):
        rslt.append((x, int_to_string(x)))
    return rslt

print build_list_5a()

def build_list_5b():
    return [(x, int_to_string(x)) for x in xrange(6)]

print build_list_5b()
