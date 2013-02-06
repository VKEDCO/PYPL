#!/usr/bin/perl

#######################################################
## Examples of groups and backreferences and
## special variables $1, $2, $3, etc.
##
## bugs to vladimir dot kulyukin at gmail dot com
#######################################################

use strict;
use warnings;

my $txt_01 = '1+1=2';

## PL groups are specified with special characters ().
## Corresponding text segments are retrieved with special
## variables $1, $2, $3, etc. Generally speaking, these
## variables are aligned with left parentheses. In other
## words, $1 is aligned with the 1st left parenthesis,
## $2 is aligned with the 2nd left parenthesis, etc.

## Example 01
## Suppose we match /(\d)\+(\d)\=(\d)/ against $txt_01.
$txt_01 =~ /(\d)\+(\d)\=(\d)/;

## Then the variable alignment is as follows:
## /(\d)\+(\d)\=(\d)/
##  $1    $2    $3
## In other words, $1 is bound to '1',
## $2 is bound to '2' and $3 is bound to '3'.

print "\nExample 01\n";
print "\$1 -> $1\n\$2 -> $2\n\$3 -> $3\n"; 

## Example 02
## Suppose we match /((\d)\+(\d)\=(\d))/ against $txt_01.
$txt_01 =~ /((\d)\+(\d)=(\d))/;

## Then the special variable alignment is:
##  /((\d)\+(\d)=(\d))/;
##  $1$2    $3   $4
## In other words, $1 is bound to '1+1=2',
## $2 is bound to '1' and $3 is bound to '1',
## $4 is bound to '2'.

print "\nExample 02\n";
print "\$1 -> $1\n\$2 -> $2\n\$3 -> $3\n\$4 -> $4\n"; 

## Example 03
## Suppose we match ((\d)\+(\d))=(\d) against $txt_01.
$txt_01 =~ /((\d)\+(\d))=(\d)$/;

## Then the special variable alignment is:
##  /((\d)\+(\d))=(\d)$/
##  $1$2    $3    $4
## In other words, $1 is bound to '1+1',
## $2 is bound to '1' and $3 is bound to '1',
## $4 is bound to '2'.
print "\nExample 03\n";
print "\$1 -> $1\n\$2 -> $2\n\$3 -> $3\n\$4 -> $4\n"; 

