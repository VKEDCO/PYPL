#!/usr/bin/perl
use strict;
use warnings;

###############################################
## mapping subroutines over lists with
## MAP EXPRESSION, LIST
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
    return map($poly->($_), ($range_start .. $range_end));
}

## identical with test_poly, just a different syntax for
## map.
sub test_poly2 {
    my ($poly, $range_start, $range_end) = @_;
    return map $poly->($_), $range_start .. $range_end;
}

sub print_list {
    print $_ . " " foreach(@_);
    print "\n";
}

## test
print_list(test_poly(\&poly1, 1, 5));
print_list(test_poly(\&poly2, 1, 5));
print_list(test_poly2(\&poly1, 1, 5));
print_list(test_poly2(\&poly2, 1, 5));
