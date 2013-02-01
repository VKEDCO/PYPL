#!/usr/bin/perl

#########################################
## 1) => operator in hash construction
## 2) manipulation of hash keys
## 3) hash iteration with EACH
#########################################

use warnings;
use strict;

## %tbl_01 is a hash constructed from
## a list of key-value pairs with the
## => operator. everything to the left of
## each => turns into a string which
## becomes a key. keys cannot have spaces.
## everything to the right
## of it and before a comma is the value
## to which the key maps.
my %tbl_01 = ( one   => 1,
               two   => 2,
	       three => 3,
	       four  => 4,
	       five  => 5);

## get the keys from %tbl_01 and save
## them into an array.
my @tbl_01_keys = keys(%tbl_01);
print "\n\@tbl_01_keys: @tbl_01_keys\n";

## pop the keys one by one from the
## the right end of of @tbl_01_keys
## and display their values in %tbl_01.
print "\nover \%tbl_01 by popping keys:\n";
while ( my $key = pop(@tbl_01_keys) ) {
    print "$key\t=>\t$tbl_01{$key}\n";
}

## get the values from %tbl_01 and
## save them into an array.
my @tbl_01_vals = values(%tbl_01);

## display the values.
print "\n\@tbl_01_vals: @tbl_01_vals\n";

## use the function EACH to iterate
## over the key-value pairs in %tbl_01.
print "\nover \%tbl_01 with each:\n";
my $k;
my $v;
while ( ($k, $v) = each(%tbl_01) ) {
    print "$k => $v\n";
}

## construct a new hash %rev_tbl_01
## by swapping keys and values so that
## in %rev_tbl_01 the values of %tbl_01
## are the keys and the keys of %tbl_01
## are the values.
my %rev_tbl_01 = reverse(%tbl_01);

print "\n\%tbl_01 reversed:\n";
while ( ($k, $v) = each(%rev_tbl_01) ) {
    print "$k => $v\n";
}
