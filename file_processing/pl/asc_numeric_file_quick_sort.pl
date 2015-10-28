#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them numerically using quicksort.
## 
## To run:
## >> perl asc_file_quick_sort.pl unsorted_numbers.txt
## @author: vladimir kulyukin
###################################################
    
use strict;
use warnings;
use sort '_quicksort'; ## explicit use of quick sort
use sort 'stable';     ## quarantees stability, i.e., the original 
                       ## input ordering is preserved

# 1. get $ARGV[0]
my $file_path = shift;
# 2. open $file_path for reading or die
open(IN, '<', $file_path) or die $!;
# 3. slurp the lines, sort numerically, and print
my @lines = <IN>;
print sort { $a <=> $b } @lines;

