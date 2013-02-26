#!/usr/bin/perl

###################################################
## pick odd numbers from the input
## stream and print them out to default STDOUT
##
## To run:
## >>./pick_odds.pl unsorted_numbers.txt
###################################################
use strict;
use warnings;

while (<>) {
  print $_ if ( $_ % 2 != 0 );
}
