#!/usr/bin/python

import sys

## change this path to where Timestamp.py
load_path = 'C:\\users\\vladimir\\programming\\nasa_wlog\\py_nasa_log\\'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from Timestamp import Timestamp

txt = '01/Jul/1995:00:00:01 -0400'
tm2 = Timestamp()
if tm2 != None:
    tm2.setDay('01')
    tm2.setMonth('Jul')
    tm2.setYear('1995')
    tm2.setHour('00')
    tm2.setMins('00')
    tm2.setSecs('01')
    print 'string representation: ' + tm2.toString()
else:
    print 'no timestamp created' + "\n",

