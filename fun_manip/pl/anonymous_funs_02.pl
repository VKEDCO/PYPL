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

sub make_adders { return map { make_adder($_) } @_; }

sub apply_adders {
    my @adders  = make_adders(@{$_[0]}); my @numbers = @{$_[1]};
    my @rslt = ();
    map { 
	my $adder = $_;
	map {
	    my $x = $_;
	    push(@rslt, $adder->($x));
	} @numbers;
    } @adders;
    return @rslt;
}

sub test_make_adders {
    my @nums_to_add = (1..3);
    my @arg_nums    = (1..5);
    my @addrslts = apply_adders(\@nums_to_add, \@arg_nums);
    print 'addrslts = ' . "@addrslts\n";
}

## ========== Multipliers ========================

sub make_multiplier {
    my $k = $_[0];
    return sub {
	return $k*$_[0];
    }
}

sub make_multipliers { return map { make_multiplier($_) } @_; }

sub apply_multipliers {
    my @mults  = make_multipliers(@{$_[0]}); my @numbers = @{$_[1]};
    my @rslt = ();
    map { 
	my $mult = $_;
	map {
	    my $x = $_;
	    push(@rslt, $mult->($x));
	} @numbers;
    } @mults;
    return @rslt;
}

sub test_make_multipliers {
    my @mult_consts = (1..3);
    my @arg_nums = (1..5);
    my @multrslts = apply_multipliers(\@mult_consts, \@arg_nums);
    print 'multrslts = ' . "@multrslts\n";
}

test_make_multipliers();

## examples of make 2nd deg polys
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

#my @mults = map make_multiplier($_), (1..5);
#my @multrslts = map { $_->(2) } @mults;
#print "@multrslts\n";
