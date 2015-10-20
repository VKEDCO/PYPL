#!/usr/bin/perl

##################################
# multiple pl substitutions with
# /g quantifier
# @author: vladimir kulyukin
##################################

use strict;
use warnings;

my $txt0 = 'I like to program in Python, Python, Python!';
my $txt1 = 'I like to program in Perl, Perl, Perl!';

print $txt0 . "\n";
$txt0 =~ s/Python/C/g;
print $txt0 . "\n";
print "*******\n";

print $txt1 . "\n";
$txt1 =~ s/Perl/C++/g;
print $txt1 . "\n";
print "*******\n";
