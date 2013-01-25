#!/usr/bin/python

#######################################################
## examples of map in Python
## bugs to vladimir dot kulyukin at gmail dot com
#######################################################

## construct a list of numbers
## numbers == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers = [i for i in xrange(1, 11)]
## apply lambda x: x+5 to each int in numbers
sums = map(lambda x: x+5, numbers)
## output is 'sums=[6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
print 'sums=' + str(sums)

## same as sums=map(lambda x: x+5, numbers)
## sums2 == [6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
sums2 = [i+5 for i in xrange(1, 11)]
print 'sums2=' + str(sums)

def poly(x):
    return x**2 + 5*x - 10

## map can take a function
poly_nums = map(poly, numbers)
# output is 'poly_nums=[-4, 4, 14, 26, 40, 56, 74, 94, 116, 140]'
print 'poly_nums=' + str(poly_nums)

## same as poly_nums = map(poly, numbers)
poly_nums2 = [poly(x) for x in numbers]
## output is 'poly_nums2=[-4, 4, 14, 26, 40, 56, 74, 94, 116, 140]'
print 'poly_nums2=' + str(poly_nums)

words = ['one', 'two', 'three', 'four', 'five']
## apply function len to each string in words
word_lengths = map(len, words)
## output is 'word_lengths=[3, 3, 5, 4, 4]'
print 'word_lengths=' + str(word_lengths)

## same as word_lengths2=map(len, words)
word_lengths2 = [len(w) for w in words]
## output is 'word_lengths2=[3, 3, 5, 4, 4]'
print 'word_lengths2=' + str(word_lengths2)

## we can construct a list of 2-tuples
words_and_lengths = [(w, len(w)) for w in words]
## output is 'words_and_lengths=[('one', 3), ('two', 3), ('three', 5), ('four', 4), ('five', 4)]'
print 'words_and_lengths=' + str(words_and_lengths)

ints = [1, 2, 3, 4, 5]
## map can take functions of multiple arguments
## x gets bound to each word in words and y gets bound
## to each number in ints
rslt = map(lambda x, y: (x, y), words, ints)
## output is '[('one', 1), ('two', 2), ('three', 3), ('four', 4), ('five', 5)]'
print rslt
 








