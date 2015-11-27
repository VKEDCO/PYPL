#!/usr/bin/perl

###################################################
## @author: vladimir kulyukin
## sample call:
## >timestamp_notes_for_freq.pl --f 44100 --d beePi\audio_files\real_data\ --o beePi\processed_data\timestamped_notes_44100.txt
###################################################

use strict;
use warnings;
use FileHandle;
use Getopt::Long;

my $f44100_file_pat = '(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})_44100_logo\.txt$';
my $f22050_file_pat = '(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})_22050_logo\.txt$';
my $f11025_file_pat = '(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})_11025_logo\.txt$';
my $f5512_file_pat  = '(\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2})_5512_logo\.txt$';
my $freq_file_pat   = '((\d{4})-(\d{2})-(\d{2})_(\d{2})-(\d{2})-(\d{2}))_(\d{4,6})_logo\.txt$';

my $logo_play_command_pat = '.*\[\[*([\w#\s]+)\]*\]$';
my $logo_play_tuneup_pat  = '.*\[(i\d+)\s+(t\d+)\s+(v\d+)\]$';
    
sub get_timestamp_and_frequency_from_logo_file_name {
    my @matches = ($_[0] =~ /$freq_file_pat/);
    if ( @matches ) {
	## return the date and the frequency
	return ($matches[0], $matches[-1]);
    }
    else {
	return ();
    }
}

sub get_notes_from_logo_play_command {
    my @matches = ($_[0] =~ /$logo_play_command_pat/);
    ##print scalar(@matches), "\n";
    if ( @matches ) {
	return $matches[0];
    }
    else {
	return ();
    }
}

sub grep_files_for_pat_in_dir {
    my ($pat, $dir) = @_;
    opendir(my $dir_handle, $dir) or die $!;
    my @files = grep { $_ =~ /$pat/ } readdir($dir_handle);
    closedir($dir_handle);
    return \@files;
}

sub merge_files_for_freq_pat_in_dir {
    my ($freq_pat, $dir) = @_;
    my @logo_files = @{grep_files_for_pat_in_dir($freq_pat, $dir)};
    foreach (@logo_files) {
	my $logo_fp = $dir . $_;
	my ($timestamp, $freq) = get_timestamp_and_frequency_from_logo_file_name($_);
	open(my $logo_in, '<', $logo_fp) or die $!;
	while ( <$logo_in> ) {
	    my @tuneup = ($_ =~ /$logo_play_tuneup_pat/);
	    if ( !($_ =~ /$logo_play_tuneup_pat/) )  {
		my @notes = get_notes_from_logo_play_command($_);
		print "$timestamp $freq @notes\n" if ( @notes );
	    }
	}
	close($logo_in);
    }
}

sub timestamp_notes_for_freq {
    my ($freq, $bm_dir, $bm_merged_file) = @_;
    if ( $freq == 44100 ) {
	merge_files_for_freq_pat_in_dir($f44100_file_pat, $bm_dir, $bm_merged_file);	
    }
    elsif ( $freq == 22050 ) {
	merge_files_for_freq_pat_in_dir($f22050_file_pat, $bm_dir, $bm_merged_file);	
    }
    elsif ( $freq == 11025 ) {
	merge_files_for_freq_pat_in_dir($f11025_file_pat, $bm_dir, $bm_merged_file);	
    }
    elsif ( $freq == 5512 ) {
	merge_files_for_freq_pat_in_dir($f5512_file_pat, $bm_dir, $bm_merged_file);	
    }
    else {
	print "Unknown frequency $freq\n";
    }
}

my $f =  0; ## option --f for frequency; legal values for --f is 44100, 22050, 11025, 5512
my $d = ''; ## option --d for directory where bee music files are
GetOptions('f=i' => \$f, 'd=s' => \$d);
timestamp_notes_for_freq($f, $d);
