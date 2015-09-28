#!/usr/bin/perl

use strict;
use warnings;

# Your thinking is like a camel driver,
# and you are the camel:
# it drives you in every direction under its bitter control.
# -- Rumi

#################################################
# Using PL's map to map named subs of 1, 2, and 3
# arguments over lists.
#
# author: vladimir kulyukin
#
# ... nor shall they enter the Garden, until
# the camel enters the eye of the needle.
#################################################

my @numbers = (1..10);

## *** mapping a named 1-arg sub over a list of numbers ***

## poly defines f(x) = x^2 + 5x - 10, which
## is a function of 1 argument.
sub poly {
  my $x = $_[0];
  return $x**2 + 5*$x - 10;
}

## let's map poly over @numbers
my @map1 = map poly($_), @numbers;
print '@map1 = ', "@map1\n";

## *** Mapping a nambed 2-arg sub over a list of numbers ***

## fun 2 defines f(x, y) = x^2 + y^3.
sub fun2 { 
    my ($x, $y) = @_; 
    return $x**2 + $y**3; 
}

## let's construct a list of 2-scalar lists
my @two_num_lst0 = (1, 2);
my @two_num_lst1 = (3, 4);
my @two_num_lst2 = (5, 6);
my @two_lst = (\@two_num_lst0, \@two_num_lst1, \@two_num_lst2);

## let's map
my @map2 = map fun2(@{$_}), @two_lst;
print '@map2 = ', "@map2\n";

## *** Mapping a named 3-arg sub over a list of 3-scalar lists ****

## fun3 defines f(x, y, z) = x^2 + y^3 + z^4;
sub fun3 {
    my ($x, $y, $z) = @_;
    return $x**2 + $y**3 + $z**4;
}

## let's contruct a list of 3-scalar lists
my @three_num_lst0 = (1, 2, 3);
my @three_num_lst1 = (4, 5, 6);
my @three_num_lst2 = (7, 8, 9);
my @three_lst  = (\@three_num_lst0, \@three_num_lst1, \@three_num_lst2); 

## let's map
my @map3 = map fun3(@{$_}), @three_lst;
print '@map3 = ', "@map3\n";
