#!/usr/bin/perl

## If you are on linux, do "which perl" to ensure
## that the perl interpreter is installed in /usr/bin/perl.
## Change the shabang statement above if necessary.
##
## author: Vladimir Kulyukin

use strict;
use warnings;

my @lst = (1, 2, 3, 4);


## Method 3
print "Method 03\n";
foreach (@lst) {
  print "$_\n";
}
print "\n";

## output of Method 3 is the same as Method 2 in pl_list_02.pl
