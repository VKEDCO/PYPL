#!/usr/bin/perl
## print min of numbers in STDIN
use strict;
use warnings;
use List::Util qw( min );
my @nums = ();
push(@nums, $_) while (<>);
print min(@nums), "\n";
