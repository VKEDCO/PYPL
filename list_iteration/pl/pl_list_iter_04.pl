#!/usr/bin/perl

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

## If you are on linux, do "which perl" to ensure
## that the perl interpreter is installed in /usr/bin/perl.
## Change the shabang statement above if necessary.
##
## author: Vladimir Kulyukin

use strict;
use warnings;

my @lst = (1, 2, 3, 4);

## Method 4
## iterating over the contents of @lst with the
## special variable $_. Output is the same as Method 3.
## $_ is the special variable that contains the default
## input and pattern searching strings.
print "Method 04\n";
print "$_\n" foreach (@lst);

## computing square roots 
## this shows that $_ destructively
## modifies the list.
$_ **= .5 foreach(@lst);
print "@lst\n";

## the last print statement outputs the square roots
## of the numbers in @lst.
## 1 1.4142135623731 1.73205080756888 2
