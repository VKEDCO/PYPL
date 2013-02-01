#!/usr/bin/perl

##########################################
## - construction of hashes with =>
## - definition of arrays and ranges as
##   values
########################################## 

use warnings;
use strict;

my @ary = ('a' .. 'e');

## here is a hash constructed from a list of
## key-value pairs using the => operator.
## whatever appears to the left of
## => is evaluated as if it was
## a double quoted string. Ranges and arrays
## should be placed inside a double-quoted
## string. The hash key to the left of
## => cannot have white space.
my %tbl_01 = ( one   => 1,
	       two   => 2+3,
	       three => "@ary",
	       four  => "this is value 4"
    );

## print all values from %tbl_01.
print "\n" . '%tbl_01 is' . "\n";
print '$tbl_01{\'one\'}   = ' . "$tbl_01{'one'}\n";
print '$tbl_01{\'two\'}   = ' . "$tbl_01{'two'}\n";
print '$tbl_01{\'three\'} = ' . "$tbl_01{'three'}\n";
print '$tbl_01{\'four\'} = ' . "$tbl_01{'four'}\n";

## add new key-value pairs.
$tbl_01{'five'} = 'This is value 5';
$tbl_01{'six'} = 12;

## print all key-value pairs from %tbl_01 again.
print "\n" . '%tbl_01 is' . "\n";
print '$tbl_01{\'one\'}   = ' . "$tbl_01{'one'}\n";
print '$tbl_01{\'two\'}   = ' . "$tbl_01{'two'}\n";
print '$tbl_01{\'three\'} = ' . "$tbl_01{'three'}\n";
print '$tbl_01{\'four\'}  = ' . "$tbl_01{'four'}\n";
print '$tbl_01{\'five\'}  = ' . "$tbl_01{'five'}\n";
print '$tbl_01{\'six\'}  = ' . "$tbl_01{'six'}\n";

