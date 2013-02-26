#!/usr/bin/perl

## pick odd numbers from the input stream
## and print it to default STDOUT.
## to run:
## >> ./pick_lt_10.pl unsorted_numbers.txt
## remember to chmod u+x pick_lt_10.pl
use strict;
use warnings;

while (<>) {
  print $_ if ( $_ < 10 );
}
