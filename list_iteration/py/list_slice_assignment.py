#!/usr/bin/python

##################################
## List slice assignment in Py2
## change the value of k to experiment
## with different slice sizes.
##
## author: vladimir kulyukin
##################################

flist = ['file0', 'file1', 'file2', 'file3', 'file4',\
         'file5', 'file6', 'file7', 'file8', 'file9']

## assignment into a slice
k = 1
flist[1:k] = ['one', 'two', 'three']
print repr(flist)
