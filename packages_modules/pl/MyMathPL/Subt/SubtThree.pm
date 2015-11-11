#!/usr/bin/perl

package MyMathPL::Subt::SubtThree;

## this is the root directory where MyMathPL folder
## is placed. Change it accordingly.
use lib 'C:/Users/Vladimir/programming/pl/MyMathPL/';

use strict;
use warnings;
use MyMathPL::Constants;

sub subt3 {
  return $_[0] - $_[1] - $_[2];
}

sub info {
  print 'This is module SubtThree of ', 
    MyMathPL::Constants::app_name(), ' application ', 
        ' version ', 
    MyMathPL::Constants::app_version(), "\n";
}

1;



