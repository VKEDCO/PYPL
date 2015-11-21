#!/usr/bin/perl

## author: vladimir kulyukin
package Employee;

## change this path to where Employee.pm is defined.
use lib 'C:/Users/Vladimir/teaching/CS3430_F5/lectures/34/';

use strict;
use warnings;
use Date;

sub new {
    my $type = shift();
    my $class = ref($type) || $type;

    my $date = new Date();
    my $this = { mFirstName => undef,
		 mLastName => undef,
		 mHireDate => $date };
    
    bless($this, $class);
    return $this;
}

sub getFirstName {
  my $this = shift();
  return $this->{ mFirstName };
}

sub getLastName {
  my $this = shift();
  return $this->{ mLastName };
}

sub getHireDate {
  my $this = shift();
  return $this->{ mHireDate };
}

sub setFirstName {
  if ( @_ == 2 ) {
    my ($this, $fn) = @_;
    $this->{ mFirstName } = $fn;
  }
  else {
    die '$emp->setFirstName($fn) takes 2 arguments';
  }
}

sub setLastName {
  if ( @_ == 2 ) {
    my ($this, $ln) = @_;
    $this->{ mLastName } = $ln;
  }
  else {
    die '$emp->setFirstName($ln) takes 2 arguments';
  }
}

sub setHireDate {
  if ( @_ == 2 ) {
    my ($this, $hd) = @_;
    $this->{ mHireDate } = $hd;
  }
  else {
    die '$emp->setHireDate($hd) takes 2 arguments';
  }
}

sub toString {
  my $this = shift();
  print 'Employee ', 
        $this->{ mFirstName }, ' ', 
        $this->{ mLastName },  ' '; 
  $this->{ mHireDate }->toMDYString();
}

1;
