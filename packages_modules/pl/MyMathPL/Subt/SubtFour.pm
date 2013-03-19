#!/usr/bin/perl

package MyMathPL::Subt::SubtFour;

## this is the root directory where MyMathPL folder
## is placed.
use lib "d:/Dropbox/teaching/PythonPerl/s13/lectures/18/";


use strict;
use warnings;
use MyMathPL::Constants;

sub subt4 {
  return $_[0] - $_[1] - $_[2] - $_[3];
}

sub info {
  print 'This is module SubtFour of ', 
    MyMathPL::Constants::app_name(), ' application ', 
        ' version ', 
    MyMathPL::Constants::app_version(), "\n";
}

1;



