#!/usr/bin/python

######################################################
## using Python regular expressions to find and
## unnumbered list items.
## @author: vladimir kulyukin
######################################################

import re

UL_TXT_01 = '\n\
<ul>\n\
<li>John   Balbiro	A1001	john.balbiro@usu.edu</li>\n\
<li>Alice  Nelson	A0011	alice.nelson@workflow.net</li>\n\
<li>Jacob  Roberts	A1100	j.s.roberts@gmail.com</li>\n\
</ul>\n\
';

ulist_pat = r'(<li>(\w|\s|\d|\W)*</li>)'
li_items = []
for line in re.split(r'\n', UL_TXT_01):
    match = re.match(ulist_pat, line)
    if ( match != None ): li_items.append(match.group(1))
print li_items

