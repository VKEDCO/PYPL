#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them numerically using the default sort.
## 
## To run:
## >> perl desc_numeric_file_sort.pl numbers.txt
## @author: vladimir kulyukin
###################################################
use strict;
use warnings;

# 1. get $ARGV[0]
my $infile_path = shift;
# 2. open $file_path for reading or die
open(IN, '<', $infile_path) or die $!;
# 3. slurp the lines, sort, print
my @lines = <IN>;
print sort { $b <=> $a } @lines;
