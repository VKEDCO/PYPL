#!/usr/bin/perl

##################################
# multiple pl substitutions
# @author: vladimir kulyukin
##################################

use strict;
use warnings;

my $txt0 = 'I like to program in Python.';
my $txt1 = 'I like to program in Perl.';


my @all_substs = [ ['I', 'We'], ['program', 'code'],
		   ['P\w+n', 'C'], ['.e\w+l', 'C#'] ];

sub make_substs {
    my ($substs, $txt) = @_;
    print 'Before substitution: ' . "\t" . $txt . "\n";    
    $txt =~ s/@{$_}[0]/@{$_}[1]/ foreach(@{$substs});
    print 'After substitution: '  . "\t" . $txt, "\n";
    print "******\n";
}

make_substs(\@all_substs, $txt0);
make_substs(\@all_substs, $txt1);
