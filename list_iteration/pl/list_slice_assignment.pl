#!/usr/bin/perl

##########################################
## List slice assignment in PL
## change the value of $k to play with
## the size of the slice being assigned to.
##
## author: vladimir kulyukin
##
## the camel always delivers...
##########################################

use warnings;
use strict;

## @fa is bound to ('file0', 'file1', 'file2',
## 'file3', 'file4', 'file5', 'file6', 'file7',
## 'file8', 'file9'), because it is defined with the
## .. range operator.
my @flist = ('file0' .. 'file9');
## the single dot operator concatenates two strings
print '@flist = ' . "@flist\n\n";

my $k = 1;
@flist[1 .. $k] = qw(one two three);
print "\n@flist\n\n";
