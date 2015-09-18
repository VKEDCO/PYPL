#!/usr/bin/perl

use strict;
use warnings;

#####################################################
# illsustrates the use of map EXPRESSION, LIST
# EXPRESSION is an expression that applies
# to $_ and returns a result list
#
# author: vladimir kulyukin
#
# ... nor shall they enter the Garden, until
# the camel enters the eye of the needle.
#####################################################

my @numbers = (1..10);

## *** mapping expression $_ + 5 over a list of numbers
my @map1 = map($_ + 5, @numbers);
print '@map1 = ', "@map1\n";

## *** mapping expression $_**2 + 2*$_ + 10 over a list of numbers
my @map2 = map($_**2 + 2*$_ + 10, @numbers);
print '@map2 = ', "@map2\n";

## **** mapping expression length($_) over a list of strings
my @words = qw(one two three four five);
my @map3 = map(length($_), @words);
print '@map3 = ', "@map3\n";
