#!/usr/bin/perl
## print max of numbers from STDIN
use strict;
use warnings;
use List::Util qw( max );
my @nums = ();
push(@nums, $_) while ( <> );
print max(@nums), "\n";
