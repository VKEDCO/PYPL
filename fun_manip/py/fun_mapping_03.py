#!/usr/bin/python

#################################################
# Using Py's map to map unnamed lambdas
# over lists.
#
# author: vladimir kulyukin
#################################################

words = ['one', 'two', 'three', 'four', 'five']

## ******* mapping a lambda over a list of strings
words_and_lengths = map(lambda w: (w, len(w)), words)
for word, length in words_and_lengths:
    print "length of " + word + "\t\tis\t" + str(length)
