#!/usr/bin/perl

use strict;
use warnings;
use 5.10.0;

###############################################################
# creating anonymous functions on the fly
# author: vladimir kulyukin
#
# Your thinking is like a camel driver,
# and you are the camel:
# it drives you in every direction under its bitter control.
# -- Rumi
###############################################################

sub make_adder {
    my $n = $_[0];
    return sub {
	return $_[0] + $n;
    }
}

sub make_multiplier {
    my $k = $_[0];
    return sub {
	return $k*$_[0];
    }
}

sub test_adders {
    my $add3 = make_adder(3);
    my $add4 = make_adder(4);
    say 'Testing adders...';
    map {
	say '$add3->(', $_ , ') = ', $add3->($_);
	say '$add4->(', $_,  ') = ', $add4->($_);
    } (1..5);
}

sub test_multipliers {
    my $mult3 = make_multiplier(3);
    my $mult4 = make_multiplier(4);
    say 'Testing multipliers...';
    foreach((1..5)) {
	say '$mult3->(', $_ , ') = ', $mult3->($_);
	say '$mult4->(', $_,  ') = ', $mult4->($_);
    }
}

sub make_adders { return map { make_adder($_) } @_; }

sub test_make_adders {
    my @adders  = make_adders(@{$_[0]});
    my @numbers = @{$_[1]};
    my @rslt = ();
    map { 
	my $x = $_;
	map {
	    my $adder = $_;
	    push(@rslt, $adder->($x));
	} @adders;
    } @numbers;
    return @rslt;
}

sub make_2nd_deg_poly {
    my ($k2, $k1, $k0) = @_;
    return sub {
	my $x = $_[0];
	return $k2*($x**2) + $k1*$x + $k0;
    }
}

sub test_2nd_deg_polys {
    my $poly1 = make_2nd_deg_poly(1, 2, 3);
    my $poly2 = make_2nd_deg_poly(2, 3, 4);

    say 'Testing 2nd deg polys';
    say '$poly1->(0) = 1*0^2 + 2*0 + 3 = ', $poly1->(0);
    say '$poly1->(1) = 1*1^2 + 2*1 + 3 = ', $poly1->(1);
    say '$poly1->(2) = 1*2^2 + 2*2 + 3 = ', $poly1->(2);

    say '$poly2->(0) = 2*0^2 + 3*0 + 4 = ', $poly2->(0);
    say '$poly2->(1) = 2*1^2 + 3*1 + 4 = ', $poly2->(1);
    say '$poly2->(2) = 2*2^2 + 3*2 + 4 = ', $poly2->(2);
}

test_adders();
test_multipliers();

#test_2nd_deg_polys();
my @adders = map { make_adder($_) } (1..5);
my @addrslts = map { $_->(2) } @adders;
print "@addrslts\n";

my @mults = map make_multiplier($_), (1..5);
my @multrslts = map { $_->(2) } @mults;
print "@multrslts\n";

#my @numbers = (1..3);
#my @rslts = test_make_adders(\@numbers, \@numbers);
#print 'rslts = ' . "@rslts\n";
