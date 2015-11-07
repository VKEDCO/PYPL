#!/usr/bin/perl

#######################################
# @author: vladimir kulyukin
#######################################
use strict;
use warnings;

sub display_note_freqs_table {
    my %notes_freq_table = @_;
    my @notes = keys(%notes_freq_table);
    foreach(@notes) { print "$_\t$notes_freq_table{$_}\n"; }
}

my %note_freqs_table;
while ( <> ) {
    if ( $_ =~ /\S+/ ) {
	my @record_splits = split(/\t/, $_);
	my @notes = split(/\s/, $record_splits[7]);
	foreach( @notes ) {
	    if ( defined($note_freqs_table{$_}) ) {
		$note_freqs_table{$_} += 1;
	    }
	    else {
		$note_freqs_table{$_} = 1;
	    }
	}
    }
}

display_note_freqs_table(%note_freqs_table);
