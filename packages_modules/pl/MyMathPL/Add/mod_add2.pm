#!/usr/bin/perl

package my_math_pl::pack_add::mod_add2;

use strict;
use warnings;

use lib "d:/Dropbox/teaching/PythonPerl/s13/lectures/17/";
use my_math_pl::mod_constants;

sub add2 {
  return $_[0] + $_[1];
}

sub info {
  print 'This is mod_add2 module of ', app_name(), ' application', 
        ' version ', myversion(), "\n";
}

## remember this 1!!!!
1;




