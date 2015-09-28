#!/usr/bin/perl

# ----------------------------------------------------------
# Your thinking is like a camel driver,
# and you are the camel:
# it drives you in every direction under its bitter control.
# -- Rumi

# If you are on linux, do "which perl" to ensure
# that the perl interpreter is installed in /usr/bin/perl.
# Change the shabang statement above if necessary.
#
# author: Vladimir Kulyukin
# ------------------------------------------------------------

use strict;
use warnings;

my @lst = (1, 2, 3, 4);

## Method 1
print "Method 01\n";
for(my $i = 0; $i <= $#lst; $i++) {
  print "\$lst[$i] = $lst[$i]\n";
}
print "\n";

## the output of the above code segment:
## Method 01
## $lst[0] = 1
## $lst[1] = 2
## $lst[2] = 3
## $lst[3] = 4
