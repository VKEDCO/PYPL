#!/usr/bin/perl

##################################
# pl substitutions
# @author: vladimir kulyukin
##################################
use strict;
use warnings;

my $txt0 = 'I like to program in Python.';
my $txt1 = 'I like to program in Perl.';

sub make_subst {
    my ($txt, $pat, $repl) = @_;
    print 'Before substitution: ' . "\t" . $txt . "\n";
    $txt =~ s/$pat/$repl/; 
    print 'After substitution: '  . "\t" . $txt, "\n";
    print "******\n";
}

## how to replace one string with another
make_subst($txt0, 'Python', 'C++');  ## replace 'Python' with 'C++' in $txt0
make_subst($txt1, 'Perl',   'Java'); ## replace 'Perl' with 'Java' in $txt1

## how to replace a pattern with a string
make_subst($txt0, 'P\w+n', 'C');   ## replace 'P\w+n' with 'C' in $txt0
make_subst($txt1, '.e\w+l', 'C#'); ## replace 'P\w+n' with 'C#' in $txt1
