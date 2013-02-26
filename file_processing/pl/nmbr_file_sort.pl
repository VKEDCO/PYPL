#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them as numbers.
## 
## To run:
## >> nmbr_sort.pl unsorted_numbers.txt
##
## bugs to vladimir dot kulyukin at gmail dot com
###################################################
use strict;
use warnings;

my $infile = shift();
open(IN, '<', $infile) or die $!;
my @lines = <IN>;
print sort { $a <=> $b } @lines;
