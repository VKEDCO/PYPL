#!/usr/bin/perl

#######################################################
## Examples of groups and backreferences and
## special variables $1, $2, $3, etc.
## author: vladimir kulyukin
#######################################################

use strict;
use warnings;

sub display_groups_by_backrefs {
    my ($pat, $txt) = @_;
    print "-------------------\n";
    print 'pat = ' . $pat . '; ' . 'text = ' . $txt . "\n";
    my @groups = ($txt =~ /$pat/);
    my $num_of_groups = @groups; ## length of @groups
    print 'num of groups = ' . $num_of_groups . "\n";
    print '$1 --> ' . $1 . "\n" if ( $1 || $1 eq '' );
    print '$2 --> ' . $2 . "\n" if ( $2 );
    print '$3 --> ' . $3 . "\n" if ( $3 );
    print '$4 --> ' . $4 . "\n" if ( $4 );
}

display_groups_by_backrefs('(\w)(\w)(\w)', 'abc');
display_groups_by_backrefs('(\w*)(\w)',    'abc');
display_groups_by_backrefs('(\w*)(\w)(\w)', 'abc');
display_groups_by_backrefs('(\w*)(\w)(\w)(\w)', 'abc');
