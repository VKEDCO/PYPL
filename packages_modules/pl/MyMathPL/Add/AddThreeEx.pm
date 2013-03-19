#!/usr/bin/perl

package MyMathPL::Add::AddThreeEx;

## this is the root directory where MyMathPL folder
## is placed.
use lib "d:/Dropbox/teaching/PythonPerl/s13/lectures/18/";

use strict;
use warnings;
use MyMathPL::Constants;

use Exporter;
use base 'Exporter';
our @EXPORT = qw(add3);

sub add3 {
  return $_[0] + $_[1] + $_[2];
}

sub info {
  print 'This is module AddThreeEx of ', 
    MyMathPL::Constants::app_name(), ' application ', 
        ' version ', 
    MyMathPL::Constants::app_version(), "\n";
}

1;



