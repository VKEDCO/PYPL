#!/usr/bin/python

## basic sorting operations

## Output is
## [-1, 1, 2, 3, 4]
## lst_02 = [2, 1, 3, 4, -1]
## [-1, 1, 2, 3, 4]
## [2, 1, 3, 4, -1]
## [-1, 1, 2, 3, 4]

lst = [2, 1, 3, 4, -1];
## do not do: sorted_lst = lst.sort()
lst.sort();
## lst is destructively modified; sort() sorts in place
print lst

## if you do not want to modify lst, you need
## to make a copy first and then sort it
lst_02 = [2, 1, 3, 4, -1]
lst_02_copy = lst[:]
lst_02_copy.sort()
## lst_02 does not change
print 'lst_02 = ' + str(lst_02)
print lst_02_copy

## another way to sort copies is to use sorted()
lst_03 = [2, 1, 3, 4, -1]
sorted_lst_03 = sorted(lst_03)
print lst_03
print sorted_lst_03





