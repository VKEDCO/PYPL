#!/usr/bin/perl

####################################################################################################
# solution to the square bottom line relief
# tank problem at http://www.vkedco.blogspot.com/2013/02/python-perl-square-bottom-line-relief.html
# bugs to vladimir dot kulyukin at gmail dot com
####################################################################################################

use strict;
use warnings;

sub build_sblr_tank 
{
  my ($tank_specs) = shift;
  my %tank = ();
  foreach (@{$tank_specs}) {
    $tank{$_->[0]} = $_->[1];
  }
  return \%tank;
}

my $left_tank_fig_01  = build_sblr_tank([[1, 1], [2, 2], [3, 3]]);
my $mid_tank_fig_01   = build_sblr_tank([[1, 1], [2, 2], [3, 1]]);
my $right_tank_fig_01 = build_sblr_tank([[1, 1], [2, 1], [3, 1]]);
my $tank_fig_07 = build_sblr_tank([[1, 2], [2, 5], [3, 0], [4, 4],
				   [4, 4], [5, 6], [6, 3], [7, 4]]);

sub square_relief_tank_water_volume 
{
    my ($tank, $tw, $th, $wl) = @_;
    ($wl <= $th) or die 'Water level cannot be greater than tank height';
    my $vol = 0;
    my $relief_h = 0;
    foreach my $col_num (1..$tw) {
	$relief_h = $tank->{$col_num};
	if ( $relief_h < $wl ) {
	    $vol += ($wl - $relief_h);
	}
    }
    return $vol;
}

my %water_tank_01 = (1 => 1, 2 => 2, 3 => 3);
my %water_tank_02 = (1 => 3, 2 => 2, 3 => 2);
my %water_tank_03 = (1 => 2, 
		     2 => 5,
		     3 => 0,
		     4 => 4,
		     5 => 6,
		     6 => 3,
		     7 => 4);

print square_relief_tank_water_volume(\%water_tank_01, 3, 4, 4), "\n";
print square_relief_tank_water_volume(\%water_tank_02, 3, 4, 3), "\n";
print square_relief_tank_water_volume(\%water_tank_03, 7, 7, 7), "\n";
print square_relief_tank_water_volume(\%water_tank_03, 7, 7, 4), "\n";

print square_relief_tank_water_volume($left_tank_fig_01, 3, 3, 1), "\n";
print square_relief_tank_water_volume($mid_tank_fig_01, 3, 3, 2), "\n";
print square_relief_tank_water_volume($right_tank_fig_01, 3, 3, 3), "\n";
print square_relief_tank_water_volume($tank_fig_07, 7, 7, 4), "\n";
print square_relief_tank_water_volume($tank_fig_07, 7, 7, 5), "\n";
print square_relief_tank_water_volume($tank_fig_07, 7, 7, 7), "\n";



