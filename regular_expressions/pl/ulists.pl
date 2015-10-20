#!/usr/bin/perl

##############################################
## using PL regular expressions to find and
## unnumbered list items.
## @author: vladimir kulyukin
##############################################

use strict;
use warnings;

my $UL_TXT_01 = '
<ul>
<li>John   Balbiro	A1001	john.balbiro@usu.edu</li>
<li>Alice  Nelson	A0011	alice.nelson@workflow.net</li>
<li>Jacob  Roberts	A1100	j.s.roberts@gmail.com</li>
</ul>
';

my $ulist_pat = '(<li>(\w|\s|\d|\W)*</li>)';
my @li_items = ();
while ( $UL_TXT_01 =~ /$ulist_pat/g ) {
    push(@li_items, $1);
}
print "@li_items\n";
