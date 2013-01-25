#!/usr/bin/perl

use strict;
use warnings;

my $str = 'the sail just needs to open';
print index($str, 'sail'), "\n"; ## prints 4
print index($str, 'just', 5), "\n"; ## prints 9
print index($str, 'sky'), "\n"; ## prints -1

print rindex('sail sail sail', 'sail'), "\n"; ## prints 10
print rindex('sail sail sail', 'sail', 9), "\n"; ## prints 5
print rindex('sail sail sail', 'open'), "\n"; ## prints -1
