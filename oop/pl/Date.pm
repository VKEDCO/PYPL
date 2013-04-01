#!/usr/bin/perl

package Date;

use strict;
use warnings;

## new can be called in one of type ways
## 1) Type->new() or new Type(), e.g. Date->new() or new Date();
## 2) $object->new() where $object is a reference of Type
## if method 1 was used, the ref($type) sets $class to Type
## if method 2 was used, then $class is set of just $type

sub new {
  my $type = shift();
  my $class = ref($type) || $type;

  my $date_hash = { mMonth => 1,
		    mDate  => 1,
		    mYear  => 0 };

  bless( $date_hash, $class );
  return $date_hash;
}

## Perl programmers do not have to use new to define
## constructors. We can use make instead of new.
sub make {
  my $type = shift();
  my $class = ref($type) || $type;

  my $date_hash = { mMonth => 1,
		    mDate  => 1,
		    mYear  => 0 };

  bless( $date_hash, $class );
  return $date_hash;
}


sub year {
  ## get a reference to this object - it is passed
  ## as the first argument
  my $this = shift();

  ## if there is a second argument, then
  ## set the value of the key mYear in the
  ## object hash to it. 
  if ( @_ ) {
    $this->{ mYear } = shift();
  }
  return $this->{ mYear };
}

sub month {
  my $this = shift();
  if ( @_ ) {
    $this->{ mMonth } = shift();
  }
  return $this->{ mMonth };
}

sub day {
  my $this = shift();
  if ( @_ ) {
    $this->{ mDay } = shift();
  }
  return $this->{ mDay };
}

sub printMDY {
  my $this = shift();
  print $this->month(), '/', $this->day(), '/', $this->year();
}

## this is one of the so-called implicit functions.
## Check online doc for other implicit functions: BEGIN, END, AUTOLOAD.
sub DESTROY {
  my $this = shift();
  
  print 'Destroying Date ';
  $this->printMDY();
  print "\n";

  $this->{ mMonth } = undef;
  $this->{ mYear  } = undef;
  $this->{ mDay   } = undef;
}

1;


