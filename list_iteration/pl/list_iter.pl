#!/usr/bin/perl

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

## If you are on linux, do "which perl" to ensure
## that the perl interpreter is installed in /usr/bin/perl.
## Change the shabang statement above if necessary.
##
## bugs to vladimir dot kulyukin at gmail dot com.
use strict;
use warnings;

my @lst = (1, 2, 3, 4);

## Method 1
print "Method 01\n";
for(my $i = 0; $i <= $#lst; $i++) {
  print "\$lst[$i] = $lst[$i]\n";
}
print "\n";

## the output of the above code segment:
## Method 01
## $lst[0] = 1
## $lst[1] = 2
## $lst[2] = 3
## $lst[3] = 4

## Method 2
print "Method 02\n";
foreach my $x (@lst) {
  print "$x\n";
}
print "\n";

## the output of the above code segment:
## Method 02
## 1
## 2
## 3
## 4

## Method 3
print "Method 03\n";
foreach (@lst) {
  print "$_\n";
}
print "\n";

## output of Method 3 is the same as Method 2

## Method 4
## iterating over the contents of @lst with the
## special variable $_. Output is the same as Method 3.
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









