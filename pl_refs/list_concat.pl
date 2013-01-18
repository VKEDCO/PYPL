#!/usr/bin/perl

use strict;
use warnings;

## shows how to concatenate 2 lists
## by passing their references to
## list_concat. 
## bugs to vladimir dot kulyukin at gmail dot com

## The output is
## 1 2 3 4 a b c d
## @left_list  = 1 2 3 4
## @right_list = a b c d
## @concat = 1 2 3 4 a b c d
## @list_01 = 1 2 3 4
## @list_02 = a b c d

my @list_01 = (1, 2, 3, 4);
my @list_02 = ('a', 'b', 'c', 'd');

sub try_2_lists {
  print "@_\n";
}
## @list_01 and @list_02 are flattened into
## one list.
try_2_lists(@list_01, @list_02);

## concatenates 2 lists. the argument
## lists passed by reference are not
## modified.
sub list_concat {
  my @left_list = @{$_[0]};
  my @right_list = @{$_[1]};
  print "\@left_list  = @left_list\n";
  print "\@right_list = @right_list\n";
  push(@left_list, $_) foreach(@right_list);
  return @left_list;
}

my @concat = list_concat(\@list_01, \@list_02);
print "\@concat = @concat\n";
print "\@list_01 = @list_01\n";
print "\@list_02 = @list_02\n";
