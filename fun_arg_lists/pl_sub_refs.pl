#!/usr/bin/perl

use warnings;
use strict;

# Your thinking is like a camel driver,
# and you are the camel:
# it drives you in every direction under its bitter control.
# -- Rumi

## examples of subroutine refs
## author: Vladimir Kulyukin

use strict;
use warnings;

sub square { return $_[0]**2; }
sub cube   { return $_[0]**3; }
sub fourth { return $_[0]**4; }

my @list = (2, 3, 4);
my @fun_list = (\&square, \&cube, \&fourth);

sub apply_subs_to_list {
  my @fun_list = @{$_[0]};
  my @arg_list = @{$_[1]};
  for(my $i = 0; $i <= $#fun_list; $i++) {
    my $x = $fun_list[$i]->($arg_list[$i]);
    print "$x\n";
  }
}

print "@list\n";
apply_subs_to_list(\@fun_list, \@list);
print "@list\n";
