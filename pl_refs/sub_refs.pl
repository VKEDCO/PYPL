#!/usr/bin/perl

use strict;
use warnings;

## shows how to manipulate function references.
## bugs to vladimir dot kulyukin at gmail dot com
##
## The output (modulo the actual hex numbers) is
## as follows:
##
## calling apply_subs_01
## 1
## 8
## 81
##
## calling apply_subs_02
## 1 4 9 16 
## 1 8 27 64 
## 1 16 81 256 
## @rslt = ARRAY(0x1d0aee0) ARRAY(0x1d06650) ARRAY(0x1d065c0)
## 
## displaying contents @rslt
## 1 4 9 16 
## 1 8 27 64 
## 1 16 81 256 

sub square { return $_[0]**2; }
sub cube   { return $_[0]**3; }
sub fourth { return $_[0]**4; }

## list of arguments
my @list = (1, 2, 3, 4);
## list of function references
my @fun_list = (\&square, \&cube, \&fourth);

## applying each of the three functions to
## the corresponding scalar in @list.
sub apply_subs_01 {
  my @fun_list = @{$_[0]};
  my @arg_list = @{$_[1]};
  for(my $i = 0; $i <= $#fun_list; $i++) {
    my $x = $fun_list[$i]->($arg_list[$i]);
    print "$x\n";
  }
}
print "\ncalling apply_subs_01\n";
apply_subs_01(\@fun_list, \@list);

## applying each of the three functions to
## all of the scalars in @list.
sub apply_subs_02 {
  my @fun_list = @{$_[0]};
  my @arg_list = @{$_[1]};
  foreach my $fun_ref (@fun_list) {
    foreach my $fun_arg (@arg_list) {
      my $x = $fun_ref->($fun_arg);
      print "$x ";
    }
    print "\n";
  }
}
print "\ncalling apply_subs_02\n";
apply_subs_02(\@fun_list, \@list);

## applying each of the three functions to
## all of the scalars in @list, collecting
## the outputs of each function call to
## @temp_list and adding @temp_list to
## @rslt. The returned @rslt is a
## list of three list references.
sub apply_subs_03 {
  my @fun_list = @{$_[0]};
  my @arg_list = @{$_[1]};
  ## this is the returned result list.
  my @rslt = ();
  foreach my $fun_ref (@fun_list) {
    ## @temp_rslt is a list of 4 scalars;
    ## each scalar is the output of calling function at $fun_ref
    ## on 1, 2, 3, and 4.
    my @temp_rslt = ();
    foreach my $fun_arg (@arg_list) {
      ## this is how to call a function at $fun_ref
      ## on the scalar argument $fun_arg
      my $x = $fun_ref->($fun_arg);
      ## $x is added to @temp_rslt
      push(@temp_rslt, $x);
    }
    ## @temp_rslt is added to @rslt by reference
    push(@rslt, \@temp_rslt);
  }
  return @rslt;
}

## @rslt is a list of 3 array references
my @rslt = apply_subs_03(\@fun_list, \@list);
print "\@rslt = @rslt\n"; 

## display 2d list.
sub print_2d_list {
  foreach my $list_ref (@_) {
    #my @list = @$list_ref;
    foreach my $x (@$list_ref) {
      print "$x ";
    }
    print "\n";
  }
}

print "\ndisplaying contents \@rslt\n";
print_2d_list(@rslt);
