#!/usr/bin/perl

#######################################################
## Examples of split subroutine in Perl.
## author: vladimir kulyukin
#######################################################

use strict;
use warnings;

my $text_01 = 'word01 word02 word03';
my $text_02 = 'word01, word02; word03';

#######################################################
# Output of split_test_01():
# SPLIT 01
# text: word01 word02 word03
# we have 3 split elements
# word01
# word02
# word03

sub split_test_01 {
  print "SPLIT 01\n";
  print 'text: ' . $text_01 . "\n";
  my @split_01 = split(/ /, $text_01, 3);
  ## @split_01 == ('word01', 'word02', 'word03');
  ## get the length of @split_01
  my $len_of_split_01 = @split_01;
  print 'we have ' . $len_of_split_01 . " split elements\n";
  print "$_\n" foreach (@split_01);
  print "\n";
}

#######################################################
#Output of split_test_02():
#SPLIT 02
#text: word01 word02 word03
#we have 2 split elements
#word01
#word02 word03

sub split_test_02() {
  print "SPLIT 02\n";
  print 'text: ' . $text_01 . "\n";
  my @split_02 = split(/ /, $text_01, 2);
  my $len_of_split_02 = @split_02;
  print 'we have ' . $len_of_split_02 . " split elements\n";
  print "$_\n" foreach (@split_02);
  print "\n";
}

######################################
#Output of split_test_03():
#SPLIT 03
#text: word01, word02; word03
#we have 3 split elements
#word01
#word02
#word03

sub split_test_03 {
  print "SPLIT 03\n";
  my $text_02 = 'word01, word02; word03';
  print 'text: ' . $text_02 . "\n";
  ## split on ,; or space
  my @split_03 = split(/[,;] /, $text_02, 3);
  my $len_of_split_03 = @split_03;
  print 'we have ' . $len_of_split_03 . " split elements\n";
  print "$_\n" foreach (@split_03);
  print "\n";
}

#####################################################
#Output of split_test_04()
#SPLIT 04
#text: word01, word02; word03
#we have 3 split elements
#word01
#word02
#word03

sub split_test_04 {
  print "SPLIT 04\n";
  my @split_04 = split(/[,;] /, $text_02);
  print 'text: ' . $text_02 . "\n";
  ## split on ,; or space but do not specify the
  ## number of splits in the output. In this
  ## case, all empty string matches, if there are
  ## any, are not placed in the result list.
  my $len_of_split_04 = @split_04;
  print 'we have ' . $len_of_split_04 . " split elements\n";
  print "$_\n" foreach (@split_04);
  print "\n";
}


########################################################
#Output
#SPLIT 05
#text: word01, word02; word03
#we have 3 split elements
#word01
#word02
#word03


## this example demonstrates that by default split is called
## on $_ when the string argument is ommitted
sub split_test_05 {
  print "SPLIT 05\n";
  $_ = $text_02;
  print 'text: ' . $text_02 . "\n";
  my @split_05 = split(/[,;] /);
  my $len_of_split_05 = @split_05;
  print 'we have ' . $len_of_split_05 . " split elements\n";
  print "$_\n" foreach (@split_05);
  print "\n";
}

##################################################
#Output of split_test_06():
#SPLIT 06
#text: word01 word02 word03
#we have 3 split elements
#word01
#word02
#word03

## this example shows that split, when called with
## no arguments, splits on \s+ and uses $_ as its
## string.
sub split_test_06 {
  print "SPLIT 06\n";
  $_ = $text_01;
  print 'text: ' . $text_01 . "\n";
  my @split_06 = split;
  my $len_of_split_06 = @split_06;
  print 'we have ' . $len_of_split_06 . " split elements\n";
  print "$_\n" foreach (@split_06);
  print "\n";
}

#split_test_01();
#split_test_02();
#split_test_03();
#split_test_04();
#split_test_05();
#split_test_06();
