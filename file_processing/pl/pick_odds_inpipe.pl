#!/usr/bin/perl

#################################################
## this script 
## 1) takes input file from command line
## 2) opens a file handle and pipes into it
##    the output of applying nmbr_file_sort.pl
##    to the input file
## 3) reads numbers from the input pipe handle
##    and prints odd numbers
##
## To run on Linux:
## >> ./pick_odds_inpipe.pl unsorted_numbers.txt
##
## bugs to vladimir dot kulyukin at gmail dot com
##################################################
use strict;
use warnings;

## 1. get infile path argument from command line
my $infile = shift();

## 2. open a file handle and pipe into it
## the output of nmbr_sort.pl when nmbr_sort.pl
## is applied to $infile. 
## remove ./ to run on DOS.
open(FH, '-|', './nmbr_file_sort.pl ' . $infile);

## 3. pick out and print odd numbers
while(<FH>) {
  if ( $_ % 2 != 0 ) {
    print $_;
  }
}
