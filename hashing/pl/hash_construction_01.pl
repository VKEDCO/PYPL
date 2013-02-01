#!/usr/bin/perl

#######################################
## construction of hash construction
## from key/value pairs
#######################################

use warnings;
use strict;

## %tbl_01 is a hash constructed from
## a list of comma-separated key value pairs:
## 'one',  1 is the first key-value pair,
## 'two',  2 is the second key-value pair,
## 'three, 3 is the third key-value pair.
## numerical expressions in value places are evaluated;
## a non-numerical expression in a value place
## is evaluated as a double quoted string.
my %tbl_01 = ( 'one'  , 1,
	       'two'  , 2,
	       'three', 3**2 + 10,
	       'four', "(1..4)",
	       'five', 'This is value 5'
    );

## the values of %tbl_01 can be referenced as
## $tbl_01{'one'}, $tbl_01{'two'}, $tbl_01{'three'}.
## now we can print all the values from %tbl_01.
print "\n" . '%tbl_01 is' . "\n";
print '$tbl_01{\'one\'}   = ' . "$tbl_01{'one'}\n";
print '$tbl_01{\'two\'}   = ' . "$tbl_01{'two'}\n";
print '$tbl_01{\'three\'} = ' . "$tbl_01{'three'}\n";
print '$tbl_01{\'four\'} = '  . "$tbl_01{'four'}\n";
print '$tbl_01{\'five\'} = '  . "$tbl_01{'five'}\n";

## we can add new key-value pairs.
$tbl_01{'six'} = 4;
$tbl_01{'seven'} = 5;

## print all key-value pairs from %tbl_01 again.
print "\n" . '%tbl_01 is' . "\n";
print '$tbl_01{\'one\'}   = ' . "$tbl_01{'one'}\n";
print '$tbl_01{\'two\'}   = ' . "$tbl_01{'two'}\n";
print '$tbl_01{\'three\'} = ' . "$tbl_01{'three'}\n";
print '$tbl_01{\'four\'}  = ' . "$tbl_01{'four'}\n";
print '$tbl_01{\'five\'}  = ' . "$tbl_01{'five'}\n";
print '$tbl_01{\'seven\'}  = ' . "$tbl_01{'six'}\n";


## %tbl_02 is constructed from an array
## of key-value pairs.
my @ary = ('one', 1, 'two', 2, 'three', 3);
my %tbl_02 = @ary;

print "\n" . '%tbl_02 is' . "\n";
print '$tbl_02{\'one\'}   = ' . "$tbl_02{'one'}\n";
print '$tbl_02{\'two\'}   = ' . "$tbl_02{'two'}\n";
print '$tbl_02{\'three\'} = ' . "$tbl_02{'three'}\n";
