#!/usr/bin/perl
use strict;
use warnings;

###############################################
## illustrates how to apply a sub to
## each element of a list, collect
## a result into another list, and return it
##
## author: Vladimir Kulyukin
##
## the camel always delivers...
##############################################

sub poly1 {
    my $x = $_[0];
    return 4*($x**3) + 5*($x**2) + 10*$x + 2;
}

sub poly2 {
    my $x = $_[0];
    return 7*($x**2) + 4*$x + 11;
}

sub test_poly {
    my ($poly, $range_start, $range_end) = @_;
    my @rslt = ();
    push(@rslt, $poly->($_)) foreach($range_start .. $range_end);
    return @rslt;
}

sub print_list {
    print $_ . " " foreach(@_);
    print "\n";
}

## test
print_list(test_poly(\&poly1, 1, 5));
print_list(test_poly(\&poly2, 1, 5));
