#!/usr/bin/perl

#####################################
## Module: add2_with_shift.pl
##
## add2ws uses shift() to get the arguments
## out of @_, which causes @_ to be
## destructively modified.
##
## Author: vladimir kulyukin
#####################################

use warnings;
use strict;

sub add2ws {
    ## my is a keyword which makes the scalars $x and $y local to
    ## add2, i.e., visible only within the scope of add2.
    print 'sub add2ws', "\n";
    print '@_ = ', "@_\n";
    my $x = shift();
    print 'after 1st shift: @_ = ', "@_\n";
    my $y = shift();
    print 'after 2nd shift: @_ = ', "@_\n";
    
    return $x + $y;
}

sub test_add2ws {
    print 'add2ws(1, 2)=', add2ws(1, 2), "\n\n";

    ## call add2() issues a warning and initializes
    ## $x and $y to 0.
    print 'add2ws()=', add2ws(), "\n\n";

    ## call add2() issues a warning and initializes
    ## $x to 1 and $y to 0.
    print 'add2ws(1)=', add2ws(1), "\n\n";

    ## call add2(1, 2, 3) issues no warning; it 
    ## initializes $x to 1, $y to 2 and ignores
    ## parameter 3.
    print 'add2ws(1, 2, 3)=', add2ws(1, 2, 3), "\n\n";
}

test_add2ws();

