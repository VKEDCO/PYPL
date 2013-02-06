#!/usr/bin/python

#######################################################
## Examples of groups and backreferences in
## re.findall(<pat>, <txt>).
##
## bugs to vladimir dot kulyukin at gmail dot com
#######################################################

import re

txt_01 = '1+1=2'

## PY groups are specified with special characters ().
## Corresponding text segments are retrieved by calling
## the group() method of the match object.
## Generally speaking, these groups are aligned with left
## parentheses in the same way as the special variables
## $1, $2 align in Perl. 

## Example 01
## Suppose we match r'(\d)\+(\d)=(\d)' against txt_01.
## Then the group alignment is as follows:
## r'(\d)\+(\d)=(\d)'
##   1     2    3
## In other words, group 1 is bound to '1',
## group 2 is bound to '2' and group 3 is bound to '3'.

## Output is:
## Example 01
##
## [('1', '1', '2')]

print "\nExample 01\n";
list_of_matches_01 = re.findall(r'(\d)\+(\d)=(\d)', txt_01)
print list_of_matches_01

## Example 02
## Suppose we match r'((\d)\+(\d)=(\d))' against txt_01.
## Then the group alignment is:
##  r'((\d)\+(\d)=(\d))'
##    12     3    4
## In other words,  group 1 is bound to '1+1=2',
## group 2 is bound to '1' and group 3 is bound to '1',
## group 4 is bound to '2'.

## Output is:
## Example 02
## 
## [('1+1=2', '1', '1', '2')]

print "\nExample 02\n";
list_of_matches_02 = re.findall(r'((\d)\+(\d)=(\d))', txt_01)
print list_of_matches_02

## Example 03
## Suppose we match r'((\d)\+(\d))=(\d)' against txt_01.
## Then the group alignment is:
##  r'((\d)\+(\d))=(\d)'
##    12     3     4
## In other words, group 1 is bound to '1+1',
## group 2 is bound to '1' and group 3 is bound to '1',
## group 4 is bound to '2'.

## Output is:
## Example 03
## 
## [('1+1', '1', '1', '2')]

print "\nExample 03\n";
list_of_matches_03 = re.findall(r'((\d)\+(\d))=(\d)', txt_01)
print list_of_matches_03

