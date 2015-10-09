#!/usr/bin/perl

## Your thinking is like a camel driver,
## and you are the camel:
## it drives you in every direction under its bitter control.
## -- Rumi

#######################################################
## Examples of groups and backreferences and
## special variables $1, $2, $3, etc.
## author: vladimir kulyukin
#######################################################

use strict;
use warnings;

sub match_groups {
    my ($pat, $txt) = @_;
    print "-------------------\n";
    print 'pat = ' . $pat . '; ' . 'text = ' . $txt . "\n";
    my @groups = ($txt =~ /$pat/);
    ## the next line is just an example of how you can compute
    ## the length of a list
    my $n = @groups;
    print 'groups = '; print "$_ " foreach(@groups);
    print "\n--------------------\n";
}

match_groups('(\w*)(\w)(\w)(\w)', 'abc');
match_groups('(\w)(\w)(\w)',      'abc');
match_groups('(\w*)(\w)',         'abc');
match_groups('(\w*)(\w)(\w)',     'abc');
