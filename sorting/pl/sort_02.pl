#!/usr/bin/perl

use strict;
use warnings;

## custom sorting in Perl
## output is
## 11 1 2 24 3
## @sorted_strings = 1 11 2 24 3
## @sorted_numbers = 1 2 3 11 24
## @sorted_words = a b aa bb aaa bbb
## 0 0 1 0 1 
## 4 0 1 
## 1 2 3 5 
##
## bugs to vladimir dot kulyukin at gmail dot com

my @numbers = (11, 1, 2, 24, 3);
print "@numbers\n";

## explictly comparing numbers as ASCII strings, which is
## what the cmp operator does. the scalars $a and $b
## are default arguments.
my @sorted_strings = sort { $a cmp $b } @numbers;
print "\@sorted_strings = @sorted_strings\n";

## explict numeric comparison
my @sorted_numbers = sort { $a <=> $b } @numbers;
print "\@sorted_numbers = @sorted_numbers\n";

## custom function that compares two scalar strings
## by length
sub str_len_cmp {
  my $ln_01 = length($_[0]);
  my $ln_02 = length($_[1]);
  if ($ln_01 < $ln_02) {
    return -1;
  }
  elsif ($ln_01 > $ln_02) {
    return 1;
  }
  else {
    return 0;
  }
}

my @words = qw(aa bb a aaa b bbb);
## sort strings by length
my @sorted_words = sort { str_len_cmp($a, $b) } @words;
print "\@sorted_words = @sorted_words\n";

## function that comparies two lists by the
## sum of their elemements.
sub list_sum_cmp {
  my @list_01 = @{$_[0]};
  my @list_02 = @{$_[1]};
  my ($sum_01, $sum_02) = (0, 0);
  $sum_01 += $_ foreach(@list_01);
  $sum_02 += $_ foreach(@list_02);
  if ( $sum_01 < $sum_02 ) {
    return -1;
  }
  elsif ( $sum_01 > $sum_02 ) {
    return 1;
  }
  else {
    return 0;
  }
  
}

my @sub_list_01 = (1, 2, 3, 5);
my @sub_list_02 = (4, 0, 1);
my @sub_list_03 = (0, 0, 1, 0, 1);
## a list of 3 list references
my @two_d_list = (\@sub_list_01, \@sub_list_02, \@sub_list_03);
## sorting list references by the sums of their referent
## lists.
my @sorted_2d_list = sort { list_sum_cmp($a, $b) } @two_d_list;

## displaying the result of soring by sum.
foreach(@sorted_2d_list) {
  my @sub_list = @{$_};
  print "$_ " foreach(@sub_list);
  print "\n";
}
