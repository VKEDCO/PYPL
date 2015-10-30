#!/usr/bin/perl

## print sum of integers from files on command line
use strict;
use warnings;
my $total_sum = 0;
$total_sum += $_ while (<>);
print "total_sum = $total_sum\n";
