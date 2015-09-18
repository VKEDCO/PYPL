#!/usr/bin/perl

use strict;
use warnings;

################################################
#
# mapping code blocks over lists.
#
# author: vladimir kulyukin
#
# ... nor shall they enter the Garden, until
# the camel enters the eye of the needle.
#################################################

my @words = qw(one two three four five);

## ******* mapping a code block over a list of strings

my @word_lengths = map {
  my $w = $_;
  my $ln = length($w);
  print "length of \'$w\' \t\t is \t$ln\n";
  $ln;
} @words;
print "\n", '@word_lengths', "\t\tis\t@word_lengths\n\n";

## ******* mapping a code block over a list of strings
## to produce a list of 2-scalar lists.
my @words_and_lengths = map {
  my $w = $_;
  my $ln = length($w);
  my @lst = ($w, $ln);
  \@lst;
} @words;

## print the above list
foreach(@words_and_lengths) {
  my @lst = @$_;
  print "length of \'$lst[0]\' \t\t is \t$lst[1]\n";
}
