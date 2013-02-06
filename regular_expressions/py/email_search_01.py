#!/usr/bin/python

######################################################
## using Python regular expressions to find and
## retrieve the components of an email address: 1)
## user name; 2) host name; 3) host extension.
##
## bugs to vladimir dot kulyukin at gmail dot com
######################################################

import re

TXT_01 = '\n\
John   Balbiro	A1001	john.balbiro@usu.edu\n\
Alice  Nelson	A0011	alice.nelson@workflow.net\n\
Jacob  Roberts	A1100	j.s.roberts@gmail.com\n\
'

## group 1 - user name @ host name; group 2 extension
email_pat_with_2_groups = r'([\w.-]+@[\w.-]+)\.(com|net|org|edu)'

## group 2 - user name; group 2 - host name; group 3 - extension
email_pat_with_3_groups = r'([\w.-]+)@([\w.-]+)\.(com|net|org)'

## we do not want to extract com|net|org|edu as a separate
## group, so we add ?: after the left parenthesis. this set of
## parentheses will not count as a group result
email_pat_with_1_group = r'([\w.-]+@[\w.-]+\.(?:com|net|org|edu))'

emails_02 = re.findall(email_pat_with_2_groups, TXT_01)
emails_03 = re.findall(email_pat_with_3_groups, TXT_01)
emails_01 = re.findall(email_pat_with_1_group, TXT_01)

## prints
## [('john.balbiro@usu', 'edu'), ('alice.nelson@workflow', 'net'), ('j.s.roberts@gmail', 'com')]
print emails_02

## prints
## [('alice.nelson', 'workflow', 'net'), ('j.s.roberts', 'gmail', 'com')]
print emails_03

## prints
## ['john.balbiro@usu.edu', 'alice.nelson@workflow.net', 'j.s.roberts@gmail.com']
print emails_01
