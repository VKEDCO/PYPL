#!/usr/bin/python

################################################
#
# illustrates basic sorting in Py.
#
# author: vladimir kulyukin
#
#################################################

## you can use the sorted() function to sort understructively in Py. This
## is similar to PL sort, except it does not do the lexicographic
## sorting but numerical.

def sorting_test_0():
    print "**** SORTING TEST 0 ****"
    numbers = [2, 1, 3, 4, -1]
    print "numbers before sort:\t\t", numbers
    sorted_numbers = sorted(numbers)
    print "sorted_ numbers:    \t\t", sorted_numbers
    print "numbers after sort:\t\t", numbers
    print

## it is also possible to sort with the sort method of the list class.
## do not do: sorted_numbers = lst.sort(), because sort does not return anything;
## it destructively modifies the list
## if you to preserve the original list, you can make a copy of it &
## then user the sort method on the copy.
## numbers = [2, 1, 3, 4, -1]
## numbers_copy = numbers[:]
## numbers_copy.sort()
def sorting_test_0a():
    print "**** SORTING TEST 0a ****"
    numbers = [2, 1, 3, 4, -1];
    print "numbers before sort:\t\t", numbers
    numbers.sort();
    ## numbers list is destructively modified; sort() sorts in place
    print "numbers after sort:\t\t", numbers
    print

def sorting_test_1():
    print "**** SORTING TEST 1 ****"
    numbers = [11, 2, 1, 22, 3, 4, -1]
    print "numbers before sort:\t\t", numbers
    numbers.sort();
    ## numbers list is destructively modified; sort() sorts in place
    print "numbers after sort:\t\t", numbers
    print
    
## ASCII SORTS    
def sorting_test_2():
    print "**** SORTING TEST 2 ****"
    str_numbers = ['2', '1', '3', '4', '-1']
    print "str_numbers before sort:\t\t", str_numbers
    sorted_str_numbers = sorted(str_numbers)
    print "sorted_str_numbers:     \t\t", sorted_str_numbers
    print "str_numbers after sort: \t\t", str_numbers
    print

def sorting_test_3():
    print "**** SORTING TEST 3 ****"
    str_numbers = ['11', '2', '1', '22', '3', '4', '-1']
    print "str_numbers before sort:\t\t", str_numbers
    sorted_str_numbers = sorted(str_numbers)
    print "sorted_str_numbers:     \t\t", sorted_str_numbers
    print "str_numbers after sort: \t\t", str_numbers
    print

sorting_test_0();
sorting_test_0a();
sorting_test_1();
sorting_test_2();
sorting_test_3();

    





