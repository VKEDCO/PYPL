#!/usr/bin/perl

###############################################
# joins on sequences in PL
# author: vladimir kulyukin
###############################################

use strict;
use warnings;

my @seq1 = qw(your thinking is like a camel driver);
my @seq2 = ('a' .. 'f');

sub join_seq {
    my ($separator, $seq) = @_;
    return join($separator, @{$seq});
}

sub test_join_seq {
    print join_seq('*',    \@_), "\n";
    print join_seq(' ** ', \@_), "\n";
    print join_seq('//',   \@_), "\n";
}

test_join_seq(@seq1);
test_join_seq(@seq2);
