#!/usr/bin/python

import sys

## change this path to where Date.py is defined.
load_path = '/home/vladimir/programming/python/oop/'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from Date import Date

dates = []
dates.append(Date(11, 19, 2015))
dates.append(Date(11, 20, 2015))
dates.append(Date(11, 21, 2015))

dates.sort(key=lambda d: d.getDay())
for d in dates: print d.toMDYString()
