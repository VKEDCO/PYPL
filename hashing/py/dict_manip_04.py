#!/usr/bin/python

## define a dictionary
tbl_01 = {}
for key, val in (('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)):
    tbl_01[key] = val

## print its entries (aka items)
for key, val in tbl_01.items():
    print str(key) + ' --> ' + str(val)
