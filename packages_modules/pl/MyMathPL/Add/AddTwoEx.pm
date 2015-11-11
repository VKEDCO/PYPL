#!/usr/bin/perl

package MyMathPL::Add::AddTwoEx;

## this is the root directory where MyMathPL folder
## is placed. Change it accordingly.
use lib 'C:/Users/Vladimir/programming/pl/MyMathPL/';

use strict;
use warnings;
use MyMathPL::Constants;

## This is the exporting stuff
use Exporter;
use base 'Exporter';
our @EXPORT = qw(add2);

sub add2 {
  return $_[0] + $_[1];
}

sub info {
  print 'This is module AddTwoEx of ', 
    MyMathPL::Constants::app_name(), ' application ', 
        ' version ', 
    MyMathPL::Constants::app_version(), "\n";
}

1;





