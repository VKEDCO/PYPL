#!/usr/bin/python

################################################
## Examples of re match patterns with special
## characters ^ and $ case sensitively and
## case insensitively.
##
## bugs to vladimir dot kulyukin at gmail dot com
################################################

############################################
## Match Pattern 01: Match pattern pat against
## text txt case sensitively
## 
## match = re.search(r'pat', txt)
############################################

import re

txt_01 = 'ab Ab aB AB'

## match pattern (ab)* against txt_01 case sensitively
re_match_pat_01_match_01 = re.search(r'(ab)*', txt_01)

## print the entire match group
## prints 'group =  ab'
print 'group = ', re_match_pat_01_match_01.group()

## print the spand of the entire match group;
## prints 'span  =  (0, 2)'
print 'span  = ', re_match_pat_01_match_01.span()

##################################################
## Match Pattern 02: Match pattern pat at the
## left side of text txt (left adjusted match)
## case sensitively
##
## match = re.search(r'^pat', txt)
##################################################

txt_02 = 'abc de fg'
## pattern = r'^(abc)*': match zero or more
## occurrences of abc at the left end of txt_02
re_match_pat_02_match_01 = re.search(r'^(abc)*', txt_02)

## print the entire match group
## prints 'group = abc'
print 'group = ', re_match_pat_02_match_01.group()

## print the span of the entire match group;
## prints 'span  =  (0, 3)'
print 'span  = ', re_match_pat_02_match_01.span()

####################################################
## Match Pattern 03: Match pattern pat at the
## right side of text txt (right adjusted match)
## case sensitively
## 
## match = re.search(r'pat$', txt)
####################################################

## match (abc)* at the right end of txt_02
re_match_pat_03_match_01 = re.search(r'(abc)*$', txt_02)

## print the entire match group, which is empty
## in this case.
## prints 'group = '
print 'group = ', re_match_pat_03_match_01.group()
## prints 'span = (9, 9)'
print 'span  = ', re_match_pat_03_match_01.span()

txt_03 = 'abc de 123'

## match (\d)+ at the right end of txt_03
re_match_pat_03_match_02 = re.search(r'(\d)+$', txt_03)

## prints 'group = 123'
print 'group = ', re_match_pat_03_match_02.group()
## prints 'span = (7, 10)'
print 'span  = ', re_match_pat_03_match_02.span()

#######################################################
## Match Pattern 04: Match pattern pat against
## the entire text txt
## 
## match = re.search(r'^pat$', txt)
#######################################################

txt_04 = '12345';

## match (\d)+ against the entire txt_04.
re_match_pat_04_match_01 = re.search(r'^(\d)+$', txt_04)

## prints 'group = 12345'
print 'group = ', re_match_pat_04_match_01.group()
## prints 'span = (0, 5)'
print 'span  = ', re_match_pat_04_match_01.span()

########################################################
## Match Pattern 05: Match pattern pat against
## text txt case insensitively
## 
## match = re.search(r'pat', txt, re.IGNORECASE)
########################################################

txt_05 = 'aBc';

## match (abc) against txt_05 case insensitively.
re_match_pat_05_match_01 = re.search(r'abc', txt_05, re.IGNORECASE)

## prints 'group = aBc'
print 'group = ', re_match_pat_05_match_01.group()
## prints 'span = (0, 3)'
print 'span  = ', re_match_pat_05_match_01.span()

## match (abc)+ against txt_05 case sensitively.
## there is no case sensitive match
re_match_pat_05_match_02 = re.search(r'abc', txt_05)

if re_match_pat_05_match_02 == None:
    print 'no case sensitive match'
else:
    print 'group = ', re_match_pat_05_match_02.group()
    print 'span  = ', re_match_pat_05_match_02.span()
















			 



