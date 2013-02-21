#!/usr/bin/perl

use strict;
use warnings;

sub open_input_file {
  my $file_path = $_[0];
  open(FH, '<', $file_path) or die $!;
  ## STDOUT filehandle can be omitted
  print STDOUT $file_path, ' is opened for input', "\n";
  close(FH);
  print STDOUT $file_path, ' is closed for input', "\n";
}

open_input_file('al_ghazali_knowledge.txt');
