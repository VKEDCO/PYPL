#!/usr/bin/perl

use warnings;
use strict;

# Your thinking is like a camel driver,
# and you are the camel:
# it drives you in every direction under its bitter control.
# -- Rumi

#####################################
## Module: add2.pl
## Illustrates simple subroutines
## and @_ array manipulation
##
## add2 uses shift() to get the arguments
## out of @_, which causes @_ to be
## destructively modified.
##
## author: vladimir kulyukin
#####################################

sub add2 {
    ## my is a keyword which makes the scalars $x and $y local to
    ## add2, i.e., visible only within the scope of add2.
    print 'sub add2', "\n";
    print '@_ = ', "@_\n";
    my $x = shift();
    print 'after 1st shift: @_ = ', "@_\n";
    my $y = shift();
    print 'after 2nd shift: @_ = ', "@_\n";
    
    return $x + $y;
}

sub test_add2 {
    print "\n";

    print 'add2(1, 2)=', add2(1, 2), "\n\n";

    ## call add2() issues a warning and initializes
    ## $x and $y to 0.
    print 'add2()=', add2(), "\n\n";

    ## call add2() issues a warning and initializes
    ## $x to 1 and $y to 0.
    print 'add2(1)=', add2(1), "\n\n";

    ## call add2(1, 2, 3) issues no warning; it 
    ## initializes $x to 1, $y to 2 and ignores
    ## parameter 3.
    print 'add2(1, 2, 3)=', add2(1, 2, 3), "\n\n";
    print "\n";
}

test_add2();
