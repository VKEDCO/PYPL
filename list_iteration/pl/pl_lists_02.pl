#!/usr/bin/perl

use strict;
use warnings;

my @lstx = ();
unshift(@lstx, 3);
unshift(@lstx, 2);
unshift(@lstx, 1);

print 'lstx[0]', '=', $lstx[0], "\n";
print 'lstx[1]', '=', $lstx[1], "\n";
print 'lstx[2]', '=', $lstx[2], "\n";

my @lsty = ();
push(@lsty, 1);
push(@lsty, 'one');
push(@lsty, 2);
push(@lsty, 'two');

print 'lsty[0]', '=', $lsty[0], "\n";
print 'lsty[1]', '=', $lsty[1], "\n";
print 'lsty[2]', '=', $lsty[2], "\n";
print 'lsty[3]', '=', $lsty[3], "\n";
