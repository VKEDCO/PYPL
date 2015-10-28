#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and mergesort them as strings.
## 
## To run:
## >> perl asc_numeric_file_merge_sort.pl unsorted_numbers.txt
## @author: vladimir kulyukin
###################################################

use strict;
use warnings;
use sort '_mergesort'; ## explicit use of merge sort
use sort 'stable';     ## quarantees stability, i.e., the original 
                       ## input ordering is preserved

# 1. get $ARGV[0]
my $file_path = shift;
# 2. open $file_path for reading or die
open(IN, '<', $file_path) or die $!;
# 3. slurp the lines, sort, and print
my @lines = <IN>;
print sort { $a <=> $b } @lines;
