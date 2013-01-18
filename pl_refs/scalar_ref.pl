#!/usr/bin/perl

## shows how to define references (single and double)
## to scalar variables.
## bugs to vladimir dot kulyukin at gmail dot com

use strict;
use warnings;

## refs equations to remember:
## $scalar_ref = \$scalar_var
## $list_ref   = \@list_var
## $hash_ref   = \%hash_var
## $fun_ref    = \&fun_var

my $x = 10;
my $x_ref = \$x; ## 1st reference to $x
my $x_ref_ref = \$x_ref; ## 2nd reference to $x

print "value of \$x_ref is $x_ref\n";
print "value of \$x_ref's 1st referent is $$x_ref\n";

print "value of \$x_ref_ref is $x_ref_ref\n";
print "value of \$x_ref_ref's 1st referent is $$x_ref_ref\n";
print "value of \$x_ref_ref's 2nd referent is $$$x_ref_ref\n";

## the output should look as follows:
## value of $x_ref is SCALAR(0x726b50)
## value of $x_ref's 1st referent is 10
## value of $x_ref_ref is REF(0x726b98)
## value of $x_ref_ref's 1st referent is SCALAR(0x726b50)
## value of $x_ref_ref's 2nd referent is 10














