#!/usr/bin/perl

use strict;
use warnings;

my $txt0 = 'I like to program in python, Python, PYTHON!';

my @matches = ($txt0 =~ m/p\w+n/gi);
print "@matches\n";
