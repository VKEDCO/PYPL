#!/usr/bin/perl

################################################
## Examples of re match patterns with special
## characters ^ and $ case sensitively and
## case insensitively.
##
## bugs to vladimir dot kulyukin at gmail dot com
################################################

use strict;
use warnings;

################################################
## Match Pattern 01: Match pattern pat against 
## text txt case sensitively
## 
##  $txt =~ /pat/;
################################################

my $txt_01 = 'ab Ab aB AB';

## match pattern (ab)* against txt_01 case sensitively
$txt_01 =~ /(ab)*/;

## print the entire match group via backreference $1.
print "group = $1\n";

## the following PL print statement simulates the following 
## Python statement:
## print 'span  = ', re_match_pat_01_match_01.span()
## $1 is a backreference to the substring of $txt_01
## that matches /(ab)*/.
## index($txt_01, $1) returns the leftmost index of $1 in $txt_01.
## prints 'span = (0, 2)'
my $index_01 = index($txt_01, $1);
print 'span = ', '(', $index_01, ', ', $index_01 + length($1), ')', "\n";

##################################################
## Match Pattern 02: Match pattern pat at the
## left side of text txt (left adjusted match)
## case sensitively
##
## $txt =~ /^pat/;
##################################################

my $txt_02 = 'abc de fg';
## pattern = '^(abc)*': match zero or more
## occurrences of abc at the beginning of $txt_02
$txt_02 =~ /^(abc)*/;

## $1 is a backreference to the substring of $txt_02
## that matches '^(abc)*'
## prints 'group = abc'
print 'group = ', $1, "\n";

## index($txt_02, $1) returns the leftmost index of $1 in $txt_02.
## prints 'span  =  (0, 3)'
my $index_02 = index($txt_02, $1);
print 'span = ', '(', $index_02, ', ', $index_02 + length($1), ')', "\n";

####################################################
## Match Pattern 03: Match pattern pat at the
## right side of text txt (right adjusted match)
## case sensitively
## 
## $txt =~ /pat$/;
####################################################

## match (abc)* at the right end of $txt_02
$txt_02 =~ /(abc)*$/;

## prints 'group = ' with a warning that $1 is not
## initialized, because there is no match for (abc)* in $txt_02.
print 'group = ', $1, "\n";

## index($txt_02, $1) returns the leftmost index of $1 in $txt_02.
## prints 'span  =  (0, )' with a warning, because $1 is not defined
my $index_03 = index($txt_02, $1);
print 'span = ', '(', $index_03, ', ', $index_03 + length($1), ')', "\n";

my $txt_03 = 'abc de 123';

## match (\d)+ at the right end of $txt_03
$txt_03 =~ /((\d)+)$/;

## prints 'group = 3'
print 'group = ', $1, "\n";
## prints 'span = (9, 10)
## NOTE: if the reg expression is /(\d)+$/, then 'group = 3' is
## printed out.
my $index_04 = index($txt_03, $1);
print 'span = ', '(', $index_04, ', ', $index_04 + length($1), ')', "\n";

#######################################################
## Match Pattern 04: Match pattern pat against
## the entire text txt
## 
## $txt =~ /^pat$/;
#######################################################

my $txt_04 = '12345';

## match (\d)+ against the entire $txt_04.
## prints 'group = 12345'
$txt_04 =~ /(^(\d)+$)/;
print 'group = ', $1, "\n";

## prints 'span = (0, 5)'
my $index_05 = index($txt_04, $1);
print 'span = ', '(', $index_05, ', ', $index_05 + length($1), ')', "\n";

#######################################################
## Match Pattern 04: Match pattern pat against
## the entire text txt
## 
## $txt =~ /pat/i;
#######################################################

my $txt_05 = 'aBc';

## match (abc) against $txt_05 case insensitively.
$txt_05 =~ /(abc)/i;

## prints 'group = (aBc)'
print 'group = ', $1, "\n";
## prints 'span = (0, 3)'
my $index_06 = index($txt_05, $1);
print 'span = ', '(', $index_06, ', ', $index_06 + length($1), ')', "\n";

## match (abc) against $txt_05 case sensitively.
## prints 'no match found' because (abc) does not match aBc.
if ( $txt_05 =~ /(abc)/ ) {
  print 'group = ', $1, "\n";
  my $index_07 = index($txt_05, $1);
  print 'span = ', '(', $index_07, ', ', $index_07 + length($1), ')', "\n";
}
else {
  print 'no match found', "\n";
}


