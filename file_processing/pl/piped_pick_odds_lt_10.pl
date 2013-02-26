#!/usr/bin/perl

########################################################
## 1. open in-pipe
## 2. get sorted numbers from nmbr_file_sort.pl
## 3. open out-pipe
## 4. pipe out sorted numbers to pick_lt_10.pl
## 5. print numbers < 10
## 6. close pipes
## to run:
## >> ./piped_pick_odds_lt_10.pl unsorted_numbers.txt
## 
## bugs to vladimir dot kulyukin at gmail dot com
#########################################################

use strict;
use warnings;

## 1. get infile path argument from command line
my $infile = shift();

## 2. open a file handle and pipe into it
## the output of nmbr_sort.pl when nmbr_sort.pl
## is applied to $infile.
open(IN_FH, '-|', './nmbr_file_sort.pl ' . $infile);

## 3. open out pipe to 'pick_lt_10.pl'
open(OUT_FH, '|-', './pick_lt_10.pl');

## 3. pick out odds and pipe them out into
## OUT_FH 
while(<IN_FH>) {
  if ( $_ % 2 != 0 ) {
    print OUT_FH $_;
  }
}

## close both file handles
close(IN_FH);
close(OUT_FH);


