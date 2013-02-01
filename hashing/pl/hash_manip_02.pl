#!/usr/bin/perl

#############################################
# 1) hash construction with =>
# 2) checking if a key exists in a hash
#############################################

use warnings;
use strict;

## %tbl_01 is a hash constructed from
## a list of key-value pairs with the
## => operator. everything to the left of
## each => is a double quoted string which
## becomes a key. everything to the left
## of it and before a comma is the value
## to which the key maps.
my %tbl_01 = ( one   => 1,
               two   => 2,
               three => 3,
               four  => 4,
               five  => 5);

print 'Enter key to check with exists: ';
my $key = <STDIN>;
chomp($key);

## check if $key exists in %tbl_01.
if ( exists( $tbl_01{$key} ) ) {
    print "\n$key exists in \%tbl_01\n\n";
}
else {
    print "\n$key does not exist in \%tbl_01\n\n";  
}

print 'Enter key to check with defined: ';
$key = <STDIN>;
chomp($key);

## check if $key is defined in %tble_01.
if ( defined( $tbl_01{$key} ) ) {
    print "\n$key is defined as $tbl_01{$key}\n\n";
}
else {
    print "\n$key is not defined \%tbl_01\n\n";  
}

print 'Enter key to delete: ';
$key = <STDIN>;
chomp($key);

## delete the key.
if ( exists($tbl_01{$key}) ) {
    print "deleting $key...\n";
    delete($tbl_01{$key});
}
else {
    die "$key does not exist in the table...\n";
}

## check the deleted key with exists and
## defined.
if ( exists( $tbl_01{$key} ) ) {
    print "\n$key exists in \%tbl_01\n\n";
}
else {
    print "\n$key does not exist in \%tbl_01\n\n";  
}

if ( defined( $tbl_01{$key} ) ) {
    print "\n$key is defined as $tbl_01{$key}\n\n";
}
else {
    print "\n$key is not defined in \%tbl_01\n\n";  
}
