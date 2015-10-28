#!/usr/bin/perl

###################################################
## slurp lines from file of numbers 
## and sort them as strings.
## 
## To run:
## >> perl desc_numeric_file_merge_sort.pl numbers.txt
## @author: vladimir kulyukin
###################################################
use strict;
use warnings;
use sort '_mergesort'; ## explicit use of merge sort
use sort 'stable';     ## quarantees stability, i.e., the original 
                       ## input ordering is preserved

# 1. get $ARGV[0]
my $infile_path = shift;
# 2. open $file_path for reading or die
open(IN, '<', $infile_path) or die $!;
# 3. slurp the lines, sort, print
my @lines = <IN>;
print sort { $b <=> $a } @lines;
