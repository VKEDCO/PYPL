#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them lexicographically as strings using
## the default sorting algorithm.
## To run:
## >> perl ascii_file_sort.pl unsorted_numbers.txt
## @author: vladimir kulyukin
###################################################
use strict;
use warnings;

# 1. get the 0th command line argument
my $infile = shift;
# 2. open the file for reading
open(IN, '<', $infile) or die $!;
# 3. read lines, sort, and print
my @lines = <IN>;
print sort { $a cmp $b } @lines;



