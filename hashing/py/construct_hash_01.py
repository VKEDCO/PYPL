#!/usr/bin/python

######################################
# construction of a dictionary from
# a tupe of key-value pairs.
######################################
tbl_01 = {}
for key, val in (('key1', 1),
                 ('key2', 2.4),
                 ('key3', 3**2 + 10),
                 ('key4', [1, 2, 3, 4]),
                 ('key5', 'This is a string.')):
    tbl_01[key] = val

## the values of tbl_01 can be referenced as
## tbl_01['key1'], tbl_01['key2'], etc.    
print 'tbl_01[' + 'key1' + '] --> ' + str(tbl_01['key1'])
print 'tbl_01[' + 'key2' + '] --> ' + str(tbl_01['key2'])
print 'tbl_01[' + 'key3' + '] --> ' + str(tbl_01['key3'])
print 'tbl_01[' + 'key4' + '] --> ' + str(tbl_01['key4'])
print 'tbl_01[' + 'key5' + '] --> ' + str(tbl_01['key5'])

## let's add a couple more key-value pairs:
## a 3-toop and an anonymous function
tbl_01['key6'] = (1, 2, 3)
tbl_01['key7'] = lambda x: x + 1
## now let's print them
print 'two added key-value pairs:'
print 'tbl_01[' + 'key6' + '] --> ' + str(tbl_01['key6'])
print 'tbl_01[' + 'key7' + '] --> ' + str(tbl_01['key7'])

## some ways to access the values:
val_list = [tbl_01['key1'], tbl_01['key4'][2], tbl_01['key7'](4)]
print val_list
