#!/usr/bin/perl

########################################
# PL joins on ranges
# author: vladimir kulyukin
########################################

use strict;
use warnings;
use 5.10.0;

my @range1 = (1 .. 5);

sub join_number_range {
    my ($separator, $range) = @_;
    return join($separator, @{$range});
}

sub range_tests {
    print join_number_range('*',    \@_), "\n";
    print join_number_range(' ** ', \@_), "\n";
    print join_number_range('//',   \@_), "\n";
}

## a different version of join_number_range2 that 
## uses shift();
sub join_number_range2 {
    my $separator = shift();
    return join($separator, @_);
}

sub range_tests2 {
    print join_number_range2('*',    @_), "\n";
    print join_number_range2(' ** ', @_), "\n";
    print join_number_range2('//',   @_), "\n";
}

range_tests(@range1);
range_tests2(@range1);
