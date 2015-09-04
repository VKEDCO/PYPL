#!/usr/bin/perl

#####################################
## Module: add2_no_shift.pl
##
## add2ns uses array assignment to get
## the arguments out of @_ without
## destroying it.
##
## Author: vladimir kulyukin
#####################################

use warnings;
use strict;

## same as add2 shows a different 
## way of handling the @_ arguments; @_ remains 
## undestructed
sub add2ns {
    print 'sub add2ns', "\n";
    print '@_ = ', "@_\n";
    my ($x, $y) = @_;
    print 'no shift: @_ = ', "@_\n";    
    return $x + $y;
}

sub test_add2ns {
    print 'add2ns(1, 2)=', add2ns(1, 2), "\n\n";

    ## call add2ns() issues a warning and initializes
    ## $x and $y to 0.
    print 'add2ns()=', add2ns(), "\n\n";

    ## call add2ns() issues a warning and initializes
    ## $x to 1 and $y to 0.
    print 'add2ns(1)=', add2ns(1), "\n\n";

    ## call add2ns(1, 2, 3) issues no warning; it 
    ## initializes $x to 1, $y to 2 and ignores
    ## parameter 3.
    print 'add2ns(1, 2, 3)=', add2ns(1, 2, 3), "\n\n";
}

## run test_add2a sub
test_add2ns();

