#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them numerically using the default
## sort.
## To run:
## >> perl asc_numeric_file_sort.pl numbers.txt
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
print sort { $a <=> $b } @lines;
