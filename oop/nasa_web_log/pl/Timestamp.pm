#!/usr/bin/perl

## author: vladimir kulyukin

package Timestamp;

use strict;
use warnings;

my $timestamp_pat = '(\d{2})\/(\w{3})\/(\d{4}):(\d{2}):(\d{2}):(\d{2})\s+(-\d+)';
sub new {
  my $self = { 
      mMonth => 1,
      mDay   => 1,
      mYear  => 0,
      mHour  => 0,
      mMins  => 0,
      mSecs  => 0
  };
  bless( $self );
  return $self;
}

sub make {
    my ($type, $month, $day, $year, $hour, $mins, $secs) = @_;
    my $self = { 
	mMonth => $month,
	mDay   => $day,
	mYear  => $year,
	mHour  => $hour,
	mMins  => $mins,
	mSecs  => $secs
    };
    bless( $self );
    return $self;
}

sub toTimestamp {
    my ($type, $str) = @_;
    if ( $str =~ /$timestamp_pat/ ) {
	my $self = {
	    mDay   => $1,
	    mMonth => $2,
	    mYear  => $3,
	    mHour  => $4,
	    mMins  => $5,
	    mSecs  => $6
	};
	bless( $self );
	return $self;
    }
    else {
	return 0;
    }
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
  return int($this->{ mDay });
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

sub getHour {
  my $this = shift();
  return int($this->{ mHour });
}

sub setHour {
  if ( @_ == 2 ) {
    my ($this, $hour) = @_;
    $this->{ mHour } = $hour;
  }
  else {
    die 'method $date->setHour(hour) takes 2 arguments';
  }
}

sub getMins {
  my $this = shift();
  return int($this->{ mMins });
}

sub setMins {
  if ( @_ == 2 ) {
    my ($this, $mins) = @_;
    $this->{ mMins } = $mins;
  }
  else {
    die 'method $date->setMins(mins) takes 2 arguments';
  }
}

sub getSecs {
  my $this = shift();
  return int($this->{ mSecs });
}

sub setSecs {
  if ( @_ == 2 ) {
    my ($this, $secs) = @_;
    $this->{ mSecs } = $secs;
  }
  else {
    die 'method $date->getSecs(secs) takes 2 arguments';
  }
}

sub toString {
    my $this = shift();
    return $this->getDay() . '/' . $this->getMonth() . '/' . $this->getYear() . ' ' .$this->getHour() .
	':' . $this->getMins() . ':' . $this->getSecs();
}

1;
