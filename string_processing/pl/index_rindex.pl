#!/usr/bin/perl

############################################################
# Your thinking is like a camel driver,
# and you are the camel:
# it drives you in every direction under its bitter control.
# -- Rumi
#############################################################
# PL index and rindex
# author: vladimir kulyukin
#############################################################

use strict;
use warnings;

my $txt = 'the sail just needs to open';

print 'index of \'sail\' in \'' . "$txt" . '\' with start=0 is ', index($txt, 'sail'), "\n";    ## prints 4
print 'index of \'sail\' in \'' . "$txt" . '\' with start=5 is ', index($txt, 'sail', 5), "\n"; ## prints -1
print 'index of \'just\' in \'' . "$txt" . '\' with start=5 is ', index($txt, 'just', 5), "\n"; ## prints 9
print 'index of \'sky\'  in \'' . "$txt" . '\' with start=0 is ', index($txt, 'sky'), "\n";     ## prints -1

my $txt2 = 'sail sail sail';
print 'rindex of \'sail\' in \'' . "$txt2" . '\' with start=0 is ', rindex($txt2, 'sail'), "\n";    ## prints 10
print 'rindex of \'sail\' in \'' . "$txt2" . '\' with start=9 is ', rindex($txt2, 'sail', 9), "\n"; ## prints 5
print 'rindex of \'open\' in \'' . "$txt2" . '\' with start=0 is ', rindex($txt2, 'open'), "\n";    ## prints -1

