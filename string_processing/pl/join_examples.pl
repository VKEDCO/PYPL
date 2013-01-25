#!/usr/bin/perl

###############################################
# join examples
# bugs to vladimir dot kulyukin at gmail dot com
###############################################
use strict;
use warnings;

my @lst = qw(the sail just needs to open);
## str is 'the**sail**just**needs**to**open';
my $str = join('**', @lst);
print "$str\n";

## str_02 is '1 /\/\/\ 2 /\/\/\ 3 /\/\/\ 4 /\/\/\ 5'
my $str_02 = join(' /\/\/\ ', (1..5));
print "$str_02\n";

## keep accepting lines from the user until
## the user types 'end' and place each line
## in @array_of_inputs and join them with the
## separator '; '.
my $input;
my @array_of_inputs = ();
while ( $input = <STDIN> ) {
  chomp($input);
  if ($input eq 'end') {
    last; ## break
  }
  else {
    push(@array_of_inputs, $input);
  }
}
print join('; ', @array_of_inputs), "\n";

