#!/usr/bin/perl

use strict;
use warnings;

sub copy_file {
  my ($input_fp, $output_fp) = @_;
  open(IN, '<', $input_fp) or die $!;
  open(OUT, '>', $output_fp) or die $!;
  while ( <IN> ) {
    print OUT "$_";
  }
  close(IN);
  close(OUT);
}

my $in = shift();
my $out = shift();
copy_file($in, $out);
