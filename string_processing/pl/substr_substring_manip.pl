#!/usr/bin/perl

##################################################
## shows how substr() can be used to retrieve
## substrings of a given string and to
## destructively modify a given string by
## inserting replacement strings at various
## positions.
##
## bugs to vladimir dot kulyukin at gmail dot com
###################################################
use strict;
use warnings;

my $str_01 = 'the sail just needs to open';
my $str_02 = 'the sail just needs to open';

## extract 3 characters from and including
## position 0, i.e., characters in postions 
## 0, 1, and 2.
my $sub_str_01 = substr($str_01, 0, 3);
print "\substr($str_01, 0, 3) = $sub_str_01\n";

## extract 9 characters from and including
## postion 4, i.e., characters in positions
## from 4 upto 12.
my $sub_str_02 = substr($str_01, 4, 9);
print "\substr($str_01, 4, 9) = $sub_str_02\n";

## when the third argument is omitted,
## it is assumed to be the end of the string.
my $sub_str_03 = substr($str_01, 4);
print "\substr($str_01, 4) = $sub_str_03\n";

## when the fourth argument is used it is
## the replacement that replaces the
## characters from offset and upto offset+length-1
## in string. the string is destructively modified.
substr($str_01, 4, 4, 'sky');
print "$str_01\n";

## swallow 's' at the end of 'needs'
substr($str_02, 18, 1, '');
print "$str_02\n";

## insert 'sky and ' at position 4.
substr($str_02, 4, 0, 'sky and ');
print "$str_02\n";

