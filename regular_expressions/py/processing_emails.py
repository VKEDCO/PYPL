#!/usr/bin/python

######################################################
## using Python regular expressions to find and
## retrieve the components of an email address: 1)
## user name; 2) host name; 3) host extension.
## @author: vladimir kulyukin
######################################################

import re

TXT_01 = '\n\
John   Balbiro	A1001	john.balbiro@usu.edu\n\
Alice  Nelson	A0011	alice.nelson@workflow.net\n\
Jacob  Roberts	A1100	j.s.roberts@gmail.com\n\
'

## we do not want to extract com|net|org|edu as a separate
## group, so we add ?: after the left parenthesis. this set of
## parentheses will not count as a group result
## 1 group
email_pat_1 = r'([\w.-]+@[\w.-]+\.(?:com|net|org|edu))'
emails_1 = re.findall(email_pat_1,  TXT_01)
print emails_1

## 2 groups
email_pat_2 = r'([\w.-]+@[\w.-]+)\.(com|net|org|edu)'
emails_2 = re.findall(email_pat_2, TXT_01)
print emails_2

## 3 groups
email_pat_3 = r'([\w.-]+)@([\w.-]+)\.(com|net|org|edu)'
emails_3 = re.findall(email_pat_3, TXT_01)
print emails_3
