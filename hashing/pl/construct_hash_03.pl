#!/usr/bin/perl

use warnings;
use strict;

## %tbl_01 is a hash constructed from a list of key-value 
## pairs with the => operator;  everything to the left of each 
## => turns into a string which becomes a key; keys may not 
## have spaces. everything to the right of it and before 
## a comma is the value to which the key maps.
my %tbl_01 = (
    one   => 1,
    two   => 2,
    three => 3,
    four  => 4,
    five  => 5
    );

print '$tbl_01{' . '\'one\'' . '} --> ' . $tbl_01{'one'} . "\n";
print '$tbl_01{' . '\'two\'' . '} --> ' . $tbl_01{'two'} . "\n";
print '$tbl_01{' . '\'three\'' . '} --> ' . $tbl_01{'three'} . "\n";
print '$tbl_01{' . '\'four\'' . '} --> ' . $tbl_01{'four'} . "\n";
print '$tbl_01{' . '\'five\'' . '} --> ' . $tbl_01{'five'} . "\n";
