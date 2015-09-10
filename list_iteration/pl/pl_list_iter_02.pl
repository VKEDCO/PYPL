#!/usr/bin/perl

## If you are on linux, do "which perl" to ensure
## that the perl interpreter is installed in /usr/bin/perl.
## Change the shabang statement above if necessary.
##
## author: Vladimir Kulyukin

use strict;
use warnings;

my @lst = (1, 2, 3, 4);

## Method 2
print "Method 02\n";
foreach my $x (@lst) {
  print "$x\n";
}
print "\n";

## the output of the above code segment:
## Method 02
## 1
## 2
## 3
## 4
