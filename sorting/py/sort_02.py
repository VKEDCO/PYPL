#!/usr/bin/python

##################################################################
## custom sorting operations in Py
##
## author: vladimir kulytukin
##################################################################

## convert each number to string and sorted lexicographically
def my_num_comp(x, y):
    if str(x) < str(y):
        return -1
    elif str(x) > str(y):
        return 1
    else:
        return 0
    
def sorting_test_4():
    print "**** SORTING TEST 4 ****"
    numbers = [3, 1, 11, 2, 24]
    print "numbers before sort:\t\t", numbers
    ## convert each number into string and sort
    ## numbers.sort(key=str);
    sorted_numbers = sorted(numbers, cmp=my_num_comp)
    print "sorted_ numbers:    \t\t", sorted_numbers
    print "numbers after sort:\t\t", numbers
    print

sorting_test_4()

## sorted sorts the numbers as numbers by default.
def sorting_test_5():
    pass

## convert each string to its length and sort by
## length. use words.sort(key=len) if you want to
## sort in place.
def sorting_test_6():
    print "**** SORTING TEST 6 ****"
    words = ['aa', 'bb', 'a', 'aaa', 'b', 'bbb']
    print "words before sort:\t\t", words
    sorted_words = sorted(words, key=len)
    print "sorted_words:     \t\t", sorted_words
    print "words after  sort:\t\t", words
    print

## define custom comparator
## comparator compares lst_01 and list_02 by
## length.
def list_sum_cmp(lst_01, lst_02):
    sum_01, sum_02 = sum(lst_01), sum(lst_02)
    if sum_01 < sum_02:
        return -1
    elif sum_01 > sum_02:
        return 1
    else:
        return 0

## list_of_lists.sort(list_sum_cmp) sorts the list destructively.
## sorted() preserves the original copy.
def sorting_test_7():
    print "**** SORTING TEST 7 ****"
    list_of_lists  = [[1, 2, 3, 5], [4, 0, 1], [0, 0, 1, 0, 1]]
    print "list_of_lists before sort:\t\t", list_of_lists
    sorted_list = sorted(list_of_lists, list_sum_cmp)
    print "sorted list_of_lists:     \t\t", sorted_list
    print "list_of_lists after sort:\t\t", list_of_lists
    print

sorting_test_7()
