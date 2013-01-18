#!/usr/bin/perl

use strict;
use warnings;

## basic sorting operations in Perl
## bugs to vladimir dot kulyukin at gmail dot com
##
## output is
## 2 1 3 4 -1
## @sorted_numbers = -1 1 2 3 4
## @numbers = 2 1 3 4 -1
## @sorted_numbers2 = -1 1 11 2 22 3 4
## @numbers2 = 11 2 1 22 3 4 -1

my @numbers = (2, 1, 3, 4, -1);
print "@numbers\n";

## this prints out -1 1 2 3 4
my @sorted_numbers = sort @numbers;
print "\@sorted_numbers = @sorted_numbers\n"; 
## @numbers did not change. sorting is not in place
print "\@numbers = @numbers\n"; 

## this prints out -1 1 11 2 22 3 4. What gives?
## Perl's default sorting behavior is ASCII sort.
## In the first application of sort above the
## ASCII sort order is the same as the numerical
## order. In this application, however, the
## ASCII sort order is different.
my @numbers2 = (11, 2, 1, 22, 3, 4, -1);
my @sorted_numbers2 = sort @numbers2;
print "\@sorted_numbers2 = @sorted_numbers2\n";
## @numbers2 did not change. sorting is not in place
print "\@numbers2 = @numbers2\n"; 
