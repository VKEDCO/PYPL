#!/usr/bin/python

## test for key existence.
tbl_01 = {}
for key, val in ( ('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)):
    tbl_01[key] = val

if tbl_01.has_key('one'):
    print 'tbl_01 has key \'one\''

if not tbl_01.has_key('key10'):
    print 'tbl_01 has no key \'five\''

## remove the pair 'one' - 1 from tbl_01
del tbl_01['one']
if tbl_01.has_key('one'):
    print 'tbl_01 has key \'one\''
else:
    print 'tbl_01 has no key \'one\''
