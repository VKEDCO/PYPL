#!/usr/bin/perl

########################################
# Using PL native File::Copy 
# @author: vladimir kulyukin
########################################

use strict;
use warnings;
use File::Copy;

my ($in, $out) = @ARGV;
copy($in, $out) or die $!;
