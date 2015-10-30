#!/usr/bin/perl
## print event numbers from file in $ARGV[0]
use strict;
use warnings;
my $file_path = shift();
open(my $infile, '<', $file_path) or die $!;
while ( <$infile> ) {
    print $_ if ( $_ % 2 == 0 );
}
