#!/usr/bin/perl

###########################################################
## Examples of loose and tight regular expression matching
## two regular languages:
## L1 = {(ab)^n | n >= 1}
## L2 = {a^n | n is even} U {b^n | n is odd}
##
## bugs to vladimir dot kulyukin at gmail dot com
###########################################################

use strict;
use warnings;

my @list = ('', 'ab', 'abab', 'ababab', 
	    'abbb', 'aaaa', 
	    'aaa', 'aaaaaa', 'b', 
	    'bbb', 'bbbbb', 'abbaabba');

sub test_regex {
  my ($regex, $list) = @_;
  print "\nMatching '$regex'\n";
  foreach (@{$list}) {
    print 'match for ', "'$_'", "\n" if $_ =~ /$regex/ ;     
  }
  print "\n";
}

#############################################################
## Two Regular Expressions for L1
#############################################################

## $re_01_L01 matches all strings that will contain at least one
my $re_01_L01 = '(ab)+';
test_regex($re_01_L01, \@list);

## Output of test_regex($re_01_L01, \@list) is:
## match for 'ab'
## match for 'abab'
## match for 'ababab'
## match for 'abbb'
## match for 'abbaabba'

## $re_02_L01 matches a string if it contains only non-empty
## concatenations of 'ab'.
my $re_02_L01 = '^(ab)+$';
test_regex($re_02_L01, \@list);

## Output of test_regex($re_02_L01, \@list) is:
## Matching '^(ab)+$'
## match for 'ab'
## match for 'abab'
## match for 'ababab'

#############################################################
## Two Regular Expressions for L2
#############################################################

## $re_01_L02 matches a string if it contains either an even 
## number of consecutive a's or an odd number of consecutive b's. 
## Thus, it will match 'aaa' or 'abbaabba'.
my $re_01_L02 = '((aa)*|b(bb)*)';
test_regex($re_01_L02, \@list);

## Matching '((aa)*|b(bb)*)'
## match for ''
## match for 'ab'
## match for 'abab'
## match for 'ababab'
## match for 'abbb'
## match for 'aaaa'
## match for 'aaa'
## match for 'aaaaaa'
## match for 'b'
## match for 'bbb'
## match for 'bbbbb'
## match for 'abbaabba'

## $re_02_L2 matches a string if and only if the string has only an 
## even number of consecutive a's or an odd number of consecutive 
## b's.
my $re_02_L02 = '^((aa)*|b(bb)*)$';
test_regex($re_02_L02, \@list);

## Output of test_regex($re_02_L02, \@list) is:
## Matching '^((aa)*|b(bb)*)$'
## match for ''
## match for 'aaaa'
## match for 'aaaaaa'
## match for 'b'
## match for 'bbb'
## match for 'bbbbb'
