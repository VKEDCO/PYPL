#!/usr/bin/perl

##########################
# construction of hashes from
# a list of key-value pairs in the
# hash context
##########################
use warnings;
use strict;

my @ary = ('one', 1, 'two', 2, 'three', 3);
my %tbl_02 = @ary;

print "\n" . '%tbl_02 is' . "\n";
print '$tbl_02{\'one\'}   = ' . "$tbl_02{'one'}\n";
print '$tbl_02{\'two\'}   = ' . "$tbl_02{'two'}\n";
print '$tbl_02{\'three\'} = ' . "$tbl_02{'three'}\n";
