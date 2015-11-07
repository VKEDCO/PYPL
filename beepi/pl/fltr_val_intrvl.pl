#!/usr/bin/perl

################################################################
## @author: vladimir kulyukin
################################################################    
use strict;
use warnings;

my $VAL_INDEX         = shift();
my $LOWER_BOUND = shift();
my $UPPER_BOUND  = shift();
while ( <> ) {
    if ( $_ =~ /\S+/ ) {
	my @splits = split(/\t/, $_);
	my $val = $splits[$VAL_INDEX];
	print $_ if ( $val >= $LOWER_BOUND && $val <= $UPPER_BOUND );
    }
}
