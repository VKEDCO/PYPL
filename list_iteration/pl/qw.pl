#!/usr/bin/perl

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

use strict;
use warnings;

my @lstx = qw/1 one 2 two 3 three/;
print "$lstx[0] "; print "$lstx[1]\n";
print "$lstx[2] "; print "$lstx[3]\n";
print "$lstx[4] "; print "$lstx[5]\n";

my @lstx2 = qw{1 one 2 two 3 three};
print "$lstx2[0] "; print "$lstx2[1]\n";
print "$lstx2[2] "; print "$lstx2[3]\n";
print "$lstx2[4] "; print "$lstx2[5]\n";
