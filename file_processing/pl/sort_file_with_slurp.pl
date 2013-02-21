#!/usr/bin/perl

## to run:
## > sort_file_with_slurp.pl unsorted_numbers.txt

use strict;
use warnings;

my $infile = shift();
open(IN, '<', $infile) or die $!;
my @lines = <IN>;
print sort { $a <=> $b } @lines;



