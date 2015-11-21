#!/usr/bin/perl

## author: vladimir kulyukin

package Date;

use strict;
use warnings;

sub new {
  my $date = { mMonth => 1,
	       mDay   => 1,
	       mYear  => 0 };

  bless( $date );
  return $date;
}

sub make {
    my ($type, $month, $day, $year) = @_;
    my $date = { mMonth => $month,
		 mDay   => $day,
		 mYear  => $year };
    bless( $date );
    return $date;
}

sub getYear {
  ## get a reference to this object - it is passed
  ## as the first argument
  my $this = shift();
  return $this->{ mYear };
}

sub setYear {
  if ( @_ == 2 ) {
    my ($this, $year) = @_;
    $this->{ mYear } = $year;
  }
  else {
    die 'method $date->setYear(year) takes 2 arguments';
  }
}

sub getMonth {
  my $this = shift();
  return $this->{ mMonth };
}

sub setMonth {
  if ( @_ == 2 ) {
    my ($this, $month) = @_;
    $this->{ mMonth } = $month;
  }
  else {
    die 'method $date->setMonth(month) takes 2 arguments';
  }
}

sub getDay {
  my $this = shift();
  return $this->{ mDay };
}

sub setDay {
  if ( @_ == 2 ) {
    my ($this, $day) = @_;
    $this->{ mDay } = $day;
  }
  else {
    die 'method $date->setDay(day) takes 2 arguments';
  }
}

sub toMDYString {
  my $this = shift();
  return $this->getMonth() . '/' . $this->getDay() . '/' . 
        $this->getYear();
}

sub toYMDString {
  my $this = shift();
  return $this->getYear() . '/' . $this->getMonth() . '/' . 
        $this->getDay();
}

1;

