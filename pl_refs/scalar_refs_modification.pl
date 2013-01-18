#!/usr/bin/perl

## shows how references can be used
## to modify their referents.
## bugs to vladimir dot kulyukin gmail dot com

use strict;
use warnings;

## $scalar_ref = \$scalar_var
## $list_ref   = \@list_var
## $fun_ref    = \&fun_var
## $hash_ref   = \%hash_var

my $x = 10;
my $x_ref = \$x; ## 1st reference to $x
my $x_ref_ref = \$x_ref; ## 2nd reference to $x

print "value of \$x_ref is $x_ref\n";
print "value of \$x_ref's 1st referent is $$x_ref\n";

## adding 1 to the referent of $xref. the value
## of $x is now 11.
$$x_ref++;

print "value of \$x_ref is $x_ref\n";
print "value of \$x_ref's 1st referent is $$x_ref\n";

## adding 1 to the 2nd referent of $xref_ref_ref. the value
## of $x is now 12.
$$$x_ref_ref += 1;

print "value of \$x_ref_ref is $x_ref_ref\n";
print "value of \$x_ref_ref's 1st referent is $$x_ref_ref\n";
print "value of \$x_ref_ref's 2nd referent is $$$x_ref_ref\n";

## squaring the value of the 1st referent of $xref. the value
## of $x is now 144.
$$x_ref **= 2;

print "value of \$x_ref is $x_ref\n";
print "value of \$x_ref's 1st referent is $$x_ref\n";

## square rooting the value of the 2nd referent of $xref. the value
## of $x is back to 12.
$$$x_ref_ref **= .5;

print "value of \$x_ref_ref is $x_ref_ref\n";
print "value of \$x_ref_ref's 1st referent is $$x_ref_ref\n";
print "value of \$x_ref_ref's 2nd referent is $$$x_ref_ref\n";



