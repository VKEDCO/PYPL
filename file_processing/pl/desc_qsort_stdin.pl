#!/usr/bin/perl
## sort numbers in STDIN in descending order
use strict;
use warnings;
use sort '_quicksort';
use sort 'stable';
my @lines = ();
push(@lines, $_) while (<>);
print sort { $b <=> $a } @lines;
