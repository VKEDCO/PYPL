#!/usr/bin/python

## custom sorting operations
## bugs to vladimir dot kulyukin at gmail dot com
## 
## output is
## [1, 11, 2, 24, 3]
## ['a', 'b', 'aa', 'bb', 'aaa', 'bbb']
## before sorting two_d_list=[[1, 2, 3, 5], [4, 0, 1], [0, 0, 1, 0]]
## after sorting two_d_list=[[0, 0, 1, 0], [4, 0, 1], [1, 2, 3, 5]]

numbers = [11, 1, 2, 24, 3]
## convert each number into string and sort
numbers.sort(key=str);
## lst is destructively modified; sort() sorts in place
print numbers

## convert each string to its length and sort
words = ['aa', 'bb', 'a', 'aaa', 'b', 'bbb']
words.sort(key=len)
print words

two_d_list  = [[1, 2, 3, 5], [4, 0, 1], [0, 0, 1, 0]]

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

print 'before sorting two_d_list=' + str(two_d_list)
two_d_list.sort(list_sum_cmp)
print 'after sorting two_d_list=' + str(two_d_list)








