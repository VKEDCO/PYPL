#!/usr/bin/perl

use warnings;
use strict;

## %tbl_01 is a hash constructed from a list of comma-separated key-value 
## pairs.
my %tbl_01 = ( 'key1'  , 1,
	       'key2'  , 2.4,
	       'key3', 3**2 + 10,
	       'key4',  [1 .. 4],
	       'key5', 'This is a string.'
    );

## the values of %tbl_01 can be referenced as
## $tbl_01{'key1'}, $tbl_01{'key2'}, etc.
print "\n" . '%tbl_01 is' . "\n";
print '$tbl_01{\'key1\'} = ' . "$tbl_01{'key1'}\n";
print '$tbl_01{\'key2\'} = ' . "$tbl_01{'key2'}\n";
print '$tbl_01{\'key3\'} = ' . "$tbl_01{'key3'}\n";
print '$tbl_01{\'key4\'} = ' . "$tbl_01{'key4'}\n";
print '$tbl_01{\'key5\'} = ' . "$tbl_01{'key5'}\n";

## Let's add two more key-value pairs: a 3-element list
## and a an anonymous sub
$tbl_01{'key6'} = [1, 2, 3];
$tbl_01{'key7'} = sub { return $_[0] + 1; };

print "two added key-value pairs\n";
print '$tbl_01{\'key6\'} = ' . "$tbl_01{'key6'}\n";
print '$tbl_01{\'key7\'} = ' . "$tbl_01{'key7'}\n";

## some ways to acess the values:
my @val_list = ($tbl_01{'key1'}, $tbl_01{'key4'}[2], 
		$tbl_01{'key7'}->(4));
print $_ . ' ' foreach(@val_list);
