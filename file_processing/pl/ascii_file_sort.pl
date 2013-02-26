#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them as strings.
## 
## To run:
## >> nmbr_sort.pl unsorted_numbers.txt
##
## bugs to vladimir dot kulyukin at gmail dot com
###################################################
use strict;
use warnings;

my $infile = shift;
open(FH, '<', $infile) or die $!;
my @lines = <FH>;
print sort { $a cmp $b } @lines;




