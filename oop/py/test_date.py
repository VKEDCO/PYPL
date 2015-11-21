#!/usr/bin/python

import sys

## change this path to where Date.py
load_path = '/home/vladimir/programming/py/oop/'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from Date import Date

d1 = Date()
d1.setYear(2015)
d1.setMonth(11)
d1.setDay(19)

print d1.toMDYString()

d2 = Date()
Date.setYear(d2, 2015)
Date.setMonth(d2, 11)
Date.setDay(d2, 19)

print d2.toYMDString()
