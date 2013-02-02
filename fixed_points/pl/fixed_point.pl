#!/usr/bin/perl

########################################################
## fixed points of functions, ith roots of positive
## integers, the golden ratio as a fixed point
## 
## bugs to vladimir dot kulyukin at gmail dot com
######################################################

use strict;
use warnings;

sub average { return ($_[0] + $_[1])/2.0; }

## (x, f(x))/2.0
sub average_damp {
  my $f = $_[0]; 
  return
    ## return lambda x: average(x, f(x))
    sub { 
      return average($_[0], $f->($_[0])); 
    }
}

my $error_tolerance = 0.00001;

sub find_fixed_point {
  sub is_close_enough { 
    return (abs($_[0] - $_[1]) <= $error_tolerance)? 1: 0; 
  }

  my ($f, $guess) = @_;
  my $next_guess = $f->($guess);
  if (is_close_enough($guess, $next_guess)) {
    return $next_guess;
  }
  else {
    return find_fixed_point($f, $next_guess);
  }
}

## lambda x: n / (x**(i-1))
## the it-th root of a positive integer n can
## be computed as a fixed point of the average damp of
## lambda x: n / (x**(i-1))
sub ith_root_lambda {
  my ($n, $i) = @_;
  $i > 1 or die '$i must be > 1';
  return sub {
    ## $_[0] is x in lambda x: n / (x**(i-1))
    return $n / $_[0] ** ($i-1);
  }
}

sub square_root_lambda {
  my $n = $_[0];
  ## sub { $n / $_[0]; } is Perl's equivalent of lambda x: n/x
  ## $_[0] is x
  return sub {
    return $n / $_[0];
 }
}

sub cubic_root_lambda {
  my $n = $_[0];
  ## sub { return $n / $_[0]**2; } is Perl's equivalent of
  ## lambda x: n/(x**2)
  return sub {
    return $n / $_[0]**2;
 }
}

## lambda x: 1 + 1/x
sub golden_ratio_lambda {
  ## sub { return 1 + 1/$_[0];} is Perl's equivalent of
  ## lambda x: 1 + 1/x
  return sub {
    return 1 + 1/$_[0];
 }
}

## sqrt(n) is a fixed point of the average damp
## of lambda x: n/x; 1.0 is the 1st guess
## square_root_lambda($n), returns sub { $n / $_[0]; }
sub square_root_01 {
  return find_fixed_point(average_damp(square_root_lambda($_[0])), 
			  1.0);
}

## equivalent to square_root_01
sub square_root_02 {
  my $n = $_[0];
  return find_fixed_point(average_damp(sub{return $n/$_[0];}), 
			  1.0);
}

sub square_root_03 {
  return find_fixed_point(average_damp(ith_root_lambda($_[0], 2)), 
			  1.0);
}

## n^(1/3) is a fixed point of the average damp
## of lambda x: n / (x * x); 1.0 is the 1st guess.
## cubic_root_lambda returns sub { return $n / $_[0]**2; }
sub cubic_root_01 {
  return find_fixed_point(average_damp(cubic_root_lambda($_[0])), 
			  1.0);
}

## equivalent to cubic_root_01
sub cubic_root_02 {
  my $n = $_[0];
  return 
    find_fixed_point(average_damp(sub{return $n/($_[0]**2);}), 
		     1.0);
}

## n^(1/3) is a fixed point of the average damp
## of ith_root_lambda(n, 3) == lambda x: n / (x**2)
## ith_root_lambda($n, 3) returns 
## sub {
##    return $n / $_[0] ** 2;
##  };
## 1.0 is 1st guess.
sub cubic_root_03 {
  return 
    find_fixed_point(average_damp(ith_root_lambda($_[0], 3)), 
		     1.0);
}

## the golden ratio is a fixed point of the average
## damp of the average damp of lambda x: 1 + 1/x; 1.0 is
## 1st guess.
## golden_ratio_lambda($n) returns
## sub { return 1 + 1/$_[0];}
sub the_golden_ratio {
  return 
    find_fixed_point(average_damp(golden_ratio_lambda($_[0])),
		     1.0);
}

sub the_golden_ratio_02 {
  return
    find_fixed_point(average_damp(sub{return 1 + 1/$_[0];}),
		     1.0);
}

print square_root_01(2), ' ', square_root_02(2), ' ', 
  square_root_03(2), ' ', 2**0.5, "\n";
print square_root_01(3), ' ', square_root_02(3), ' ', 
  square_root_03(3), ' ', 3**0.5, "\n";
print square_root_01(9), ' ', square_root_02(9), ' ', 
  square_root_03(9), ' ', 9**0.5, "\n";

print cubic_root_01(2), ' ', cubic_root_02(2), ' ',
  cubic_root_02(2), ' ', 2**(1/3.0), "\n";
print cubic_root_01(3), ' ', cubic_root_02(3), ' ',
  cubic_root_03(3), ' ', 3**(1/3.0), "\n";
print cubic_root_01(9), ' ', cubic_root_02(9), ' ',
  cubic_root_03(9), ' ', 9**(1/3.0), "\n";

print the_golden_ratio(), ' ', the_golden_ratio_02(), "\n";
