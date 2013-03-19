#!/usr/bin/perl

## bugs to vladimir dot kulyukin at gmail dot com
package MyMathPL::Mult::MultTwo;

## this is the root directory where MyMathPL folder
## is placed. Change it accordingly.
use lib "/home/vladimir/Dropbox/teaching/PythonPerl/s13/lectures/18/";

use strict;
use warnings;
use MyMathPL::Constants;

sub mult2 {
  return $_[0] * $_[1];
}

sub info {
  print 'This is module MultTwo of ', 
    MyMathPL::Constants::app_name(), ' application ', 
        ' version ', 
    MyMathPL::Constants::app_version(), "\n";
}

1;
