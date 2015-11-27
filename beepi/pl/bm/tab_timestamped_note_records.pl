#!/usr/bin/perl

################################
## @author: vladimir kulyukin
################################    
use strict;
use warnings;

## 2015-08-15_15-41-32 44100 B2 C3# D3 D3#
my $timestamped_notes_pat = '^(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})\s+(\d{4,6})\s+(.+)$';

sub display_time_note_record_on_one_line {
    my @rec = @{$_[0]};
    my ($year, $month,  $day, $hour, $mins, $secs, $freq, $notes) = @rec;
    print "$year\t$month\t$day\t$hour\t$mins\t$secs\t$freq\t$notes\n";
}

sub get_timestamped_notes_record {
    my @record = ($_[0] =~ /$timestamped_notes_pat/);
    my $rslt = ( scalar(@record) == 8 )? \@record: 0;
    return $rslt;
}

while ( <> ) {
    my $rec = get_timestamped_notes_record($_);
    display_time_note_record_on_one_line($rec) if ( $rec );    
}
