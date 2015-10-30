#!/usr/bin/perl
## prints numbers in a file in $ARGV[0] that are <= $ARV[1]
## to run: >perl lte_thresh.pl numbers.txt 10
## @author: vladimir kulyukin
use strict;
use warnings;
my $file_path = shift();
my $thresh    = shift();
open(my $infile, '<', $file_path) or die $!;
while ( <$infile> ) { print $_ if ( $_ <= $thresh ); }
