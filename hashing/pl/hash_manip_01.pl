#!/usr/bin/perl

## shows how to test for existence of keys
## in a hash with defined and exists.
use warnings;
use strict;

my %tbl_01 = (
    one  => 1, 
    two => 2,  
    three => 3,
    four  => 4, 
    five  => 5);

if ( defined($tbl_01{'one'}) ) {
    print '%tbl_01 has key \'one\'' . "\n";
}

if ( exists($tbl_01{'one'}) ) {
    print '%tbl_01 has key \'one\'' . "\n";
}

if ( !defined($tbl_01{'ten'}) ) {
    print '%tbl_01 has no key \'ten\'' . "\n";
}

if ( !exists($tbl_01{'ten'}) ) {
    print '%tbl_01 has no key \'ten\'' . "\n";
}

## remove the pair 'one' - 1 from %tbl_01
delete($tbl_01{'one'});
if ( defined($tbl_01{'one'}) ) {
    print '%tbl_01 has key \'one\'' . "\n";
}
else {
    print '%tbl_01 has no key \'one\'' . "\n";
}
