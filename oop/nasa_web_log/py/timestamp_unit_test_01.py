#!/usr/bin/python

import sys

## change this path to where Timestamp.py
load_path = 'C:\\users\\vladimir\\programming\\nasa_wlog\\py_nasa_log\\'

if __name__ == '__main__':
    if not load_path in sys.path:
        sys.path.append(load_path)

from Timestamp import Timestamp

txt = '01/Jul/1995:00:00:01 -0400'
tm1 = Timestamp()
if tm1.toTimestamp(txt):
    print 'month: ' + tm1.getMonth() + "\n",
    print 'day:   ' + tm1.getDay()   + "\n",
    print 'year:  ' + tm1.getYear()  + "\n",
    print 'hour:  ' + tm1.getHour() + "\n",
    print 'mins:  ' + tm1.getMins()  + "\n",
    print 'secs:  ' + tm1.getSecs()  + "\n",

    print 'string representation: ' + tm1.toString()
else:
    print 'no timestamp created' + "\n",
