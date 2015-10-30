#!/usr/bin/perl
## prints numbers from STDIN that are <= $ARGV[0]
## to run: more numbers.txt | perl lte_input_thresh.pl 10
use strict;
use warnings;
my $thresh = shift();
while ( <> ) { print $_ if ( $_ <= $thresh ); }
