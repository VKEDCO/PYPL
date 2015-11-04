#!/usr/bin/perl

## get the values of a PL hash
use warnings;
use strict;

## define a hash
my %tbl_01 = (one  => 1, two => 2,  three => 3,
	      four  => 4, five  => 5);

##print its values
print $_, "\n" foreach(values(%tbl_01));
