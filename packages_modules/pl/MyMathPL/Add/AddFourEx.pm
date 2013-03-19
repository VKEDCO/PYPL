#!/usr/bin/perl

## bugs to vladimir dot kulyukin at gmail dot com
package MyMathPL::Add::AddFourEx;

## this is the root directory where MyMathPL folder
## is placed.
use lib "home/vladimir/Dropbox/teaching/PythonPerl/s13/lectures/18/";

use strict;
use warnings;
use MyMathPL::Constants;

use Exporter;
use base 'Exporter';
our @EXPORT = qw(add4);

sub add4 {
  return $_[0] + $_[1] + $_[2] + $_[3];
}

sub info {
  print 'This is module AddFourEx of ', 
    MyMathPL::Constants::app_name(), ' application ', 
        ' version ', 
    MyMathPL::Constants::app_version(), "\n";
}

1;



