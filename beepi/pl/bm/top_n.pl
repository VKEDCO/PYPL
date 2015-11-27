#!/usr/bin/perl
use strict;
use warnings;
my $n = shift();
my $count = 0;
while ( <> ) {
    if ( $count < $n ) {
	print $_;
	$count++;
    }
    else {
	last;
    }
}
