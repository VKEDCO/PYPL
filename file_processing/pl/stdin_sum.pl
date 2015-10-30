#!/usr/bin/perl
## print sum of numbers in STDIN
use strict;
use warnings;
my $total = 0;
$total += $_ while (<>);
print $total, "\n";
