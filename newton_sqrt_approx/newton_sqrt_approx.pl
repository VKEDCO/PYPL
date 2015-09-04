#!/usr/bin/perl

########################################
##
## A PL implementation of Newton's square
## root approximation procedure as outlined
## in "Structure & Interpretation of Computer
## Programs" by Sussman & Abelson.
##
## Author: Vladimir Kulyukin
########################################

use strict; 	## strict scoping
use warnings; 	## warnings in case we have problems

sub average {
    return ($_[0] + $_[1])/2.0;
}

sub square {
    return $_[0]**2;
}

sub next_guess {
    my ($n, $guess) = @_;
    return average($guess, $n/$guess);
}

sub newton_sqrt {
    my $n = $_[0];
    return newton_sqrt_aux($n, 1, 0.00001);
}

sub newton_sqrt_aux {
    my ($n, $guess, $error) = @_;
    if ( is_good_enough($n, $guess, $error) ) {
	return $guess;
    }
    else {
	return newton_sqrt_aux($n, next_guess($n, $guess), $error);
    }
}

sub is_good_enough {
    my ($n, $guess, $error) = @_;
    if (abs(square($guess) - $n) <= $error) {
	return 1;
    }
    else {
	return 0;
    }
}

## =================== Tests ===============

sub test_average {
    print 'average(1, 2)=', average(1, 2), "\n";
    print 'average(2, 3)=', average(2, 3), "\n";
    print 'average(2, 2)=', average(2, 2), "\n";
}
    
sub test_next_guess {
    print 'next_guess(2, 1)=', next_guess(2, 1), "\n";
    print 'next_guess(2, next_guess(2, 1))=', next_guess(2, next_guess(2, 1)), "\n";
}

sub test_newton_sqrt {
    print 'newton_sqrt(2)=', newton_sqrt(2), ' sqrt(2)=', sqrt(2), "\n";
    print 'newton_sqrt(3)=', newton_sqrt(3), ' sqrt(3)=', sqrt(3), "\n";
    print 'newton_sqrt(4)=', newton_sqrt(4), ' sqrt(4)=', sqrt(4), "\n";
    print 'newton_sqrt(5)=', newton_sqrt(5), ' sqrt(5)=', sqrt(5), "\n";
}

##test_average();
##test_next_guess();
##test_newton_sqrt();
