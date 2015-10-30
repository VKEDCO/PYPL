#!/usr/bin/perl
## sort numbers in STDIN in ascending order
use strict;
use warnings;
use sort '_quicksort';
use sort 'stable';
my @lines = ();
push(@lines, $_) while (<>);
print sort { $a <=> $b } @lines;
