#!/usr/bin/perl

###################################################
## half_interval_search.pl - half interval search
## for finding roots of f(x) = 0 on [a, b], where
## f(x) is continuous and f(a) < 0 < f(b). 
##
## bugs to vladimir dot kulyukin at gmail dot com
###################################################

use strict;
use warnings;

## error tolerance level
my $error_tol = 0.0001;

sub average {
  return ($_[0] + $_[1])/2.0;
}

sub is_small_enough {
  return abs($_[0] - $_[1]) <= $error_tol;
}

sub interval_search {
  my ($sub_ref, $neg_point, $pos_point) = @_;
  ## 1. find mid_point of [neg_point, pos_point]
  my $mid_point = average($neg_point, $pos_point);
  ## 2. is |neg_point - pos_point| <= error_tol?
  if ( is_small_enough($neg_point, $pos_point) ) {
    ## return mid_point if true
    return $mid_point;
  }
  else {
    ## 3. find the value of f(mid_point)    
    my $fval = $sub_ref->($mid_point);
    ## 4. if fval is negative, search [mid_point, pos_point]
    if ( $fval < 0 ) {
      return interval_search($sub_ref, $mid_point, $pos_point);
    }
    ## 5. if fval is positive, search [neg_point, mid_point]
    elsif ( $fval > 0 ) {
      return interval_search($sub_ref, $neg_point, $mid_point);
    }
    ## 6. mid_point is it!
    else {
      return $mid_point;
    }
  }
}

sub half_interval_search {
  ## compute f(a) and f(b)
  my ($sub_ref, $a, $b) = @_;
  ## if f(a) < 0 and f(b) > 0, then
  ## a is the negative point and b is the positive point
  my $av = $sub_ref->($a);
  my $bv = $sub_ref->($b);
  ## if f(a) > 0 and f(b) < 0, then
  ## b is the negative point and a is the positive point
  if ( $av < 0 && $bv > 0 ) {
    return interval_search($sub_ref, $a, $b);
  }
  ## if f(a) > 0 and f(b) < 0, then
  ## b is the negative point and a is the positive point
  elsif ( $bv < 0 && $av > 0 ) {
    return interval_search($sub_ref, $b, $a);
  }
  ## die because one point must
  ## be negative and the other positive
  else {
    die 'interval bounds must be of opposite signs';
  }
}

## f(x) = x^3 - 2x - 3
sub poly_01 {
  my $x = shift;
  return $x**3 - 2*$x - 3;
}

## f(x) = x^5 - 5x - 5
sub poly_02 {
  my $x = shift;
  return $x**5 - 5*$x - 5;
}

sub poly_03 {
  my $x = shift;
  return -$x + 2;
}

sub wrap_cos {
  $#_ == 0 or die 'wrap_cos takes 1 argument';
  return cos($_[0]);
}

## print out f(x) = x^3 - 2x - 3 = 0, x in [1, 2]
my $zero_01 = half_interval_search(\&poly_01, 1, 2);
print 'f(x) = x^3 - 2x - 3 = 0, on [1, 2], ', 
      'zero_01 = ', $zero_01, ' f(zero_01) = ', poly_01($zero_01), "\n";

## print out f(x) = x^5 - 5x - 5, on [1, 2]
my $zero_02 = half_interval_search(\&poly_02, 1, 2);
print 'f(x) = x^5 - 5x - 5 = 0, on [1, 2], ',
      'zero_02 = ', $zero_02, ' f(zero_02) = ', poly_02($zero_02), "\n";

## print out f(x) = -x + 2, on [0, 10]
my $zero_03 = half_interval_search(\&poly_03, 1, 10);
print 'f(x) = -x + 2 = 0, on [0, 10], ', 
      'zero_02 = ', $zero_03, ' f(zero_03) = ', poly_03($zero_03), "\n";

## print out cos(x) = 0, on [9, 12]
my $zero_04 = half_interval_search(\&wrap_cos, 9, 12);
print 'cos(x) = 0, on [9, 12], ',
      'zero_04 = ', $zero_04, ' f(zero_04) = ', wrap_cos($zero_04), "\n";



