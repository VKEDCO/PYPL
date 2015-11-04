#!/usr/bin/perl

use warnings;
use strict;

## define a hash
my %tbl_01 = (one  => 1, two => 2,  three => 3,
	      four  => 4, five  => 5);

##print its keys
print $_, "\n" foreach(keys(%tbl_01));
