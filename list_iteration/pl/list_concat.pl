#!/usr/bin/perl

use strict;
use warnings;

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

##########################################################
## shows how to concatenation 2 or more lists in PL
## author: vladimir kulyukin
##
##########################################################

## The output is
## 1 2 3 4 a b c d
## @left_list  = 1 2 3 4
## @right_list = a b c d
## @concat = 1 2 3 4 a b c d
## @list_01 = 1 2 3 4
## @list_02 = a b c d

my @lst1 = (1, 2);
my @lst2 = ('a', 'b', 'c');
my @lst3 = (5, 10, 'd', 'e');

sub try_lists {
  print "@_\n";
}

## just to show that @lst1 and @lst2 are flattened 
## into one list.
try_lists(@lst1, @lst2);
try_lists(@lst1, @lst2, @lst3);

## concatenates 2 lists. the argument lists passed 
## by reference are not modified, because the first 
## two statements
## copy lists.
sub list_concat2 {
  my @rslt  = @{$_[0]};
  my @lst1  = @{$_[1]};
  push(@rslt, $_) foreach(@lst1);
  return @rslt;
}

sub list_concat3 {
  my @rslt  = @{$_[0]};
  my @lst1  = @{$_[1]};
  my @lst2  = @{$_[2]};
  push(@rslt, $_) foreach(@lst1);
  push(@rslt, $_) foreach(@lst2);
  return @rslt;
}

my @concat12 = list_concat2(\@lst1, \@lst2);
my @concat123 = list_concat3(\@lst1, \@lst2, \@lst3);
print "\@concat12 = @concat12\n";
print "\@concat123 = @concat123\n";
