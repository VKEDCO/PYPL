#!/usr/bin/perl
## print numbers from STDIN that are >= $ARGV[0]
use strict;
use warnings;
my $thresh = shift();
while ( <> ) { print $_ if ( $_ >= $thresh ); }
