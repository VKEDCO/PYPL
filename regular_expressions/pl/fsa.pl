#!/usr/bin/perl

#################################################
## Three finite-state machines for the 
## following languages:
## - L1 = {a};
## - L2 = {{(ab)^n | n >= 1}
## - L3 = {a^n | n is even} U {b^n | n is odd}
## 
## bugs to vladimir dot kulyukin at gmail dot com
##################################################

use strict;
use warnings;

my @test_strings = (
    '', 'ab', 'abab', 
    'ababab', 'abbb', 
    'aaaa', 'aaa', 'aaaaaa', 
    'b', 'bbb', 'bbbbb', 
    'abbaabba', 'abababababababab', 
    'aa', 'bbbb', 'a'
    );

## fsa_01 accepts {a}.
my %tran_tbl_01 = ('a' => { 1 => [2] } );
my @fsa_01 = (1, [2], \%tran_tbl_01);

## fsa_02 accepts {(ab)^n | n >= 1} or (ab)+.
my %tran_tbl_02 = (
    'a' => {1 => [2], 2 => []},
    'b' => {1 => [],  2 => [3]},
    ''  => {3 => [1]}
    );
my @fsa_02 = (1, [3], \%tran_tbl_02);

## fsa_03 accepts {a^n | n is even} U {b^n | n is odd}
my %tran_tbl_03 = (
    ''  => { 1 => [2, 4] },
    'a' => { 2 => [3], 3 => [2] },
    'b' => { 4 => [5], 5 => [4] }
    );
my @fsa_03 = (1, [2, 5], \%tran_tbl_03);

sub tran_table_lookup 
{
  my ($sym, $state, $tran_tbl) = @_;
  ## check if $sym exists in $tran_tbl.
  if ( exists($tran_tbl->{$sym}) ) {
    ## if it does, get the hash reference that maps 
    ## individual states to lists of states
    my $state_to_states = $tran_tbl->{$sym};
    ## check if the current state $state exists as a key
    if ( exists($state_to_states->{$state}) ) {
      ## if it does, return the reference to the corresponding list of states
      return $state_to_states->{$state};
    }
    else {
      ## return an empty list reference
      my @empty_ary = ();
      return \@empty_ary;
    }
  }
}

sub tran_table_epsilon_lookup 
{
    my ($state, $tran_tbl) = @_;
    return tran_table_lookup('', $state, $tran_tbl);
}

sub get_start_state
{
    return $_[0]->[0];
}

sub get_fin_states
{
    return $_[0]->[1];
}

sub get_tran_table
{
    return $_[0]->[2];
}

sub is_in_list
{
    my ($k, $lst) = @_;
    for(my $i = 0; $i < scalar @{$lst}; $i++) {
	if ( $lst->[$i] == $k ) {
	    return 1;
	}
    }
    return 0;
}

sub match_fsa_aux
{
    my ($txt, $i, $n, $cur_state, $fin_states, $tran_tbl) = @_;
    ## print '$i = ', $i, '$cur_state = ', $cur_state, "\n";
    if ( $i == $n ) {
        if ( is_in_list($cur_state, $fin_states) ) {
            return 1;
        }
        else {
            my $next_epsilon_states = tran_table_epsilon_lookup($cur_state, $tran_tbl);
	    if ( $next_epsilon_states == 0 ) {
		return 0;
	    }
            foreach my $nes (@{$next_epsilon_states}) {
                if ( is_in_list($nes, $fin_states) ) {
                    return 1;
		}
		else {
		    return 0;
		}
	    }
	    return 0;
	}
    }
    else {
        my $next_states = tran_table_lookup(substr($txt, $i, 1), $cur_state, $tran_tbl);
        my $next_epsilon_states = tran_table_epsilon_lookup($cur_state, $tran_tbl);
        if ( $next_states != 0 ) {
            foreach my $ns (@{$next_states}) {
                ## print 'ns=', $ns, "\n";
                my $rslt = match_fsa_aux($txt, $i+1, $n, $ns, $fin_states, $tran_tbl);
		if ( $rslt != 0 ) {
		    return 1;
		}
	    }
	}
	if ( $next_epsilon_states != 0 ) {
            foreach my $nes (@{$next_epsilon_states}) {
                ## print 'nes=', $nes, "\n";
                my $rslt = match_fsa_aux($txt, $i, $n, $nes, $fin_states, $tran_tbl);
		if ( $rslt != 0 ) {
		    return 1;
		}
	    }
	}
	return 0;
    }
}

sub match_fsa
{
    my ($fsa, $txt) = @_;
    return match_fsa_aux($txt, 
			 0, 
			 length($txt), 
			 get_start_state($fsa),
			 get_fin_states($fsa),
			 get_tran_table($fsa));
}

sub test_fsa
{
    my ($fsa, $string_list) = @_;
    foreach my $s (@{$string_list}) {
        if ( match_fsa($fsa, $s) ) {
	    print $s, " -- yes\n";
	}
	else {
	    print $s, " -- no\n";
	}
    }
}

print 'Testing FSA 01', "\n";
test_fsa(\@fsa_01, \@test_strings);
print "\n";

print 'Testing FSA 02', "\n";
test_fsa(\@fsa_02, \@test_strings);
print "\n";

print 'Testing FSA 03', "\n";
test_fsa(\@fsa_03, \@test_strings);
print "\n";



