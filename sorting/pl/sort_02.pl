#!/usr/bin/perl

use strict;
use warnings;

################################################
#
# illustrates that the custom sorts in PL.
#
# author: vladimir kulyukin
#
# ... nor shall they enter the Garden, until
# the camel enters the eye of the needle.
#################################################

## explictly comparing numbers as ASCII strings, which is
## what the cmp operator does. the scalars $a and $b
## are default arguments.
sub sorting_test_4 {
    print "**** SORTING TEST 4 ****\n\n";
    my @numbers = (3, 1, 11, 2, 24);
    print '@numbers before sort:', "\t@numbers\n";
    my @sorted_numbers = sort { $a cmp $b } @numbers;
    print '@sorted_numbers:', "\t@sorted_numbers\n";
    print '@numbers after sort:', "\t@numbers\n";
    print "\n";
}

## explict numeric comparison, i.e., scalars
## are sorted as numbers.
sub sorting_test_5 {
    print "**** SORTING TEST 5 ****\n\n";
    my @numbers = (11, 1, 2, 24, 3);
    print '@numbers before sort:', "\t@numbers\n";
    my @sorted_numbers = sort { $a <=> $b } @numbers;
    print '@sorted_numbers:', "\t@sorted_numbers\n";
    print '@numbers before sort:', "\t@numbers\n";
    print "\n";
}

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

## scalar strings are sorted by length
sub sorting_test_6 {
    print "**** SORTING TEST 6 ****\n\n";
    my @words = qw(aa bb a aaa b bbb);
    print '@words before sort:', "\t@words\n";
    ## sort strings by length
    my @sorted_words = sort { str_len_cmp($a, $b) } @words;
    print '@sorted_words:     ', "\t@sorted_words\n";
    print '@words after  sort:', "\t@words\n";
}

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

sub sorting_test_7 {
    print "****** SORTING TEST 7 *******\n\n";
    my @sub_list_01 = (1, 2, 3, 5);
    my @sub_list_02 = (4, 0, 1);
    my @sub_list_03 = (0, 0, 1, 0, 1);
    ## a list of 3 list references
    my @list_of_lists = (\@sub_list_01, \@sub_list_02, \@sub_list_03);
    ## sorting list references by the sums of their referent
    ## lists.
    my @sorted_list = sort { list_sum_cmp($a, $b) } @list_of_lists;
    ## displaying the result of soring by sum.
    foreach(@sorted_list) {
	my @sub_list = @{$_};
	print "$_ " foreach(@sub_list);
	print "\n";
    }
}

sorting_test_7;
