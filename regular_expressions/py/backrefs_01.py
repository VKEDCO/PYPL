#!/usr/bin/perl

#######################################################
## Examples of groups and backreferences and
## extracting groups from match objects.
##
## bugs to vladimir dot kulyukin at gmail dot com
#######################################################

import re

txt_01 = '1+1=2'

## PL groups are specified with special characters ().
## Corresponding text segments are retrieved with special
## variables $1, $2, $3, etc. Generally speaking, these
## variables are aligned with left parentheses. In other
## words, $1 is aligned with the 1st left parenthesis,
## $2 is aligned with the 2nd left parenthesis, etc.

## Example 01
## Suppose we match /(\d)\+(\d)\=(\d)/ against txt_01.
match_01 = re.search(r'(\d)\+(\d)\=(\d)', txt_01)

## Then the group alignment is as follows:
## /(\d)\+(\d)\=(\d)/
##  1    2    3
## In other words, group 1 is bound to '1',
## group 2 is bound to '2' and  group 3 is bound to '3'.

## Output is:
## Example 01
## 
## group 1 ->  1
## group 2 ->  1
## group 3 ->  2

print "\nExample 01\n";
print "group 1 -> ", match_01.group(1)
print "group 2 -> ", match_01.group(2)
print "group 3 -> ", match_01.group(3)

## Example 02
## Suppose we match /((\d)\+(\d)\=(\d))/ against txt_01.
match_02 = re.search(r'((\d)\+(\d)=(\d))', txt_01)

## Then the special variable alignment is:
##  /((\d)\+(\d)=(\d))/;
##   12     3    4
## In other words,  group 1 is bound to '1+1=2',
## group 2 is bound to '1' and  group 3 is bound to '1',
## group 4 is bound to '2'.

## Output is:
## Example 02
## 
## group 1 ->  1+1=2
## group 2 ->  1
## group 3 ->  1
## group 4 ->  2

print "\nExample 02\n";
print "group 1 -> ", match_02.group(1)
print "group 2 -> ", match_02.group(2)
print "group 3 -> ", match_02.group(3)
print "group 4 -> ", match_02.group(4)

## Example 03
## Suppose we match ((\d)\+(\d))=(\d) against txt_01.
match_03 = re.search(r'((\d)\+(\d))=(\d)', txt_01);

## Then the special variable alignment is:
##  /((\d)\+(\d))=(\d)$/
##   12     3     4
## In other words, group 1 is bound to '1+1',
## group 2 is bound to '1' and group 3 is bound to '1',
## group 4 is bound to '2'.

## Output is:
## Example 03
##
## group 1 ->  1+1
## group 2 ->  1
## group 3 ->  1
## group 4 -> 2 

print "\nExample 03\n";
print "group 1 -> ", match_03.group(1)
print "group 2 -> ", match_03.group(2)
print "group 3 -> ", match_03.group(3)
print "group 4 -> ", match_03.group(4)


