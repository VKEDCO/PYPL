#!/usr/bin/perl

#######################################################
## Splitting strings in PL
## author: vladimir kulyukin
#######################################################

use strict;
use warnings;

my $text_01 = 'word1 word2 word3';
my $text_02 = 'word1, word2; word3';

sub split_test_01 { print "$_\n" foreach(split(/ /, $_[0])); }

split_test_01($text_01);
split_test_01($text_02);		    

sub split_test_02 { print "$_\n" foreach(split(/;/, $_[0])); }

split_test_02($text_01);
split_test_02($text_02);

sub split_test_n {
    my ($str, $n) = @_;
    print "$_\n" foreach(split(/ /, $str, $n));
}

# tests;
#print "============\n";
#split_test_n($text_01, 1);
#split_test_n($text_01, 2);
#split_test_n($text_01, 3);
