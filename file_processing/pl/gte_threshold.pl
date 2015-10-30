#!/usr/bin/perl
## print numbers from file in $ARGV[0] that >= $ARGV[1]
## to run: >perl gte_thresh.pl numbers.txt 10
## @author: vladimir kulyukin
use strict;
use warnings;
my $file_path = shift();
my $thresh    = shift();
open(my $infile, '<', $file_path) or die $!;
while ( <$infile> ) { print $_ if ( $_ >= $thresh ); }
