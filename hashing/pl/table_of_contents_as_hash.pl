#!/usr/bin/perl

######################################################################################
## Examples of hashes of named arrays, hashes of unnamed arrays and hashes of
## hashes.
## bugs to vladimir dot kulyukin at gmail dot com
######################################################################################

######################################################################################
## This is the table of contents of the first three chapters of 
## Daniel Maki, Maynard Thompson. "Finite Mathematics," 4th Edition, McGraw-Hill, Inc.
##
## Chapter 1 Sets, Partitions, and Tree Diagrams			3
##        1.0 The Setting and Overview					3
##	  1.1 Review of Sets and Set Operations			        3
##	  1.2 Venn Diagrams and Partitions				11
##	  1.3 Sizes of Sets						20
##	  1.4 Sets of Outcomes and Trees				29
##	  Important Terms and Concepts					40
##	  Review Exercises						40
##
## Chapter 2 Probabilities, Counting, and Equally Likely Outcomes	44
##	2.0 The Setting and Overview					44
##	2.1 Probabilities, Events, and Equally Likely Outcomes		44
##	2.2 Counting Arrangements: Permutations				57
##	2.3 Counting Partitions: Combinations				66
##	2.4 Computing Probabilities by Using Equally Likely Outcomes	77
##	Important Terms and Concepts					83
##	Review Exercises						83
##
## Chapter 3 Probability
##	3.0 The Setting and Overview					88
##	3.1 Probability Measures: Axioms and Properties			88
##	3.2 Conditional Probability and Independence			99
##	3.3 Stochastic Processes and Trees				107
##	3.4 Bayes Probabilities						117
##	3.5 Bernoulli Trials						127
##	Important Terms and Concepts					138
##	Review Exercises						138
########################################################################################

use strict;
use warnings;

################## Hash of Named Arrays ##################################
## Let's create several named array. Each named array encodes the array
## of section titles for a specific chapter.

my @chapter_01_sections = 
  (
   'The Setting and Overview', 
   'Review of Sets and Set Operations',
   'Venn Diagrams and Partitions',
   'Sizes of Sets',
   'Sets of Outcomes and Trees',
   'Important Terms and Concepts',
   'Review Exercises'
   );

my @chapter_02_sections = 
  (
   'The Setting and Overview',
   'Probabilities, Events, and Equally Likely Outcomes',
   'Counting Arrangements: Permutations',
   'Counting Partitions: Combinations',
   'Computing Probabilities by Using Equally Likely Outcomes',
   'Important Terms and Concepts',
   'Review Exercises'
   );

my @chapter_03_sections = 
  (
   'The Setting and Overview',
   'Probability Measures: Axioms and Properties',
   'Conditional Probability and Independence',
   'Stochastic Processes and Trees',
   'Bayes Probabilities',
   'Bernoulli Trials',
   'Important Terms and Concepts',
   'Review Exercises'
   );

## this textbook hash maps chapter numbers to
## references to named arrays.   
my %textbook_ht_01 = 
  (
   1 => \@chapter_01_sections,
   2 => \@chapter_02_sections,
   3 => \@chapter_03_sections
   );

while ( my ($ch_number, $section_names) = each(%textbook_ht_01) ) {
  print "Chapter $ch_number:\n";
  print "\t - $_\n" foreach(@{$section_names});
}

## The above while loop's output is:
## 
#Chapter 1:
#         - The Setting and Overview
#         - Review of Sets and Set Operations
#         - Venn Diagrams and Partitions
#         - Sizes of Sets
#         - Sets of Outcomes and Trees
#         - Important Terms and Concepts
#         - Review Exercises
#Chapter 3:
#         - The Setting and Overview
#         - Probability Measures: Axioms and Properties
#         - Conditional Probability and Independence
#         - Stochastic Processes and Trees
#         - Bayes Probabilities
#         - Bernoulli Trials
#         - Important Terms and Concepts
#         - Review Exercises
#Chapter 2:
#         - The Setting and Overview
#         - Probabilities, Events, and Equally Likely Outcomes
#         - Counting Arrangements: Permutations
#         - Counting Partitions: Combinations
#         - Computing Probabilities by Using Equally Likely Outcomes
#         - Important Terms and Concepts
#         - Review Exercises

###################### Hash of Unnamed Arrays ##################################

## this hash maps string keys ('Chapter 1', 'Chapter 2', 'Chapter 3') to 
## unnamed arrays of the section titles of the corresponding chapter.

my %textbook_ht_02 = 
  (
   'Chapter 1' => ['The Setting and Overview', 
		   'Review of Sets and Set Operations',
		   'Venn Diagrams and Partitions', 
		   'Sizes of Sets', 
		   'Sets of Outcomes and Trees',
		   'Important Terms and Concepts', 
		   'Review Exercises'],

   'Chapter 2' => ['The Setting and Overview', 
		   'Probabilities, Events, and Equally Likely Outcomes',
		   'Counting Arrangements: Permutations', 
		   'Counting Partitions: Combinations',
		   'Computing Probabilities by Using Equally Likely Outcomes', 
		   'Important Terms and Concepts',
		   'Review Exercises'],

   'Chapter 3' => ['The Setting and Overview', 
		   'Probability Measures: Axioms and Properties',
		   'Conditional Probability and Independence', 
		   'Stochastic Processes and Trees',
		   'Bayes Probabilities', 
		   'Bernoulli Trials', 
		   'Important Terms and Concepts',
		   'Review Exercises'],

  );

while ( my ($chapter, $section_names) = each(%textbook_ht_02) ) {
  print "$chapter:\n";
  print "\t - $_\n" foreach(@{$section_names});
}

## The above while loop's output is:
##
#Chapter 1:
#         - The Setting and Overview
#         - Review of Sets and Set Operations
#         - Venn Diagrams and Partitions
#         - Sizes of Sets
#         - Sets of Outcomes and Trees
#         - Important Terms and Concepts
#         - Review Exercises
#Chapter 3:
#         - The Setting and Overview
#         - Probability Measures: Axioms and Properties
#         - Conditional Probability and Independence
#         - Stochastic Processes and Trees
#         - Bayes Probabilities
#         - Bernoulli Trials
#         - Important Terms and Concepts
#         - Review Exercises
#Chapter 2:
#         - The Setting and Overview
#         - Probabilities, Events, and Equally Likely Outcomes
#         - Counting Arrangements: Permutations
#         - Counting Partitions: Combinations
#         - Computing Probabilities by Using Equally Likely Outcomes
#         - Important Terms and Concepts
#         - Review Exercises

##################################### Hash of Hashes ########################################

## this hash encodes complete table of contents for the 1st 
## three chapters. 
my %complete_textbook = 
   (
    ## hash of chapter 01
    1 => { 
	  Title => 'Sets, Partitions, and Tree Diagrams',
	  Page  => 3,
	  Sections => { 0 => { Title => 'The Setting and Overview', 
			       Page  => 3 },
			1 => { Title => 'Review of Sets and Set Operations',
			       Page  => 3 },
			2 => { Title => 'Venn Diagrams and Partitions',
			       Page  => 11 },
			3 => { Title => 'Sizes of Sets',
			       Page  => 20 },
			4 => { Title => 'Sets of Outcomes and Trees',
		               Page  => 29 },
			5 => { Title => 'Important Terms and Concepts',
			       Page  => 40 },
			6 => { Title => 'Review Exercises',
			       Page  => 40 }
		      }
	 },

    ## hash of chapter 02
    2 => {
	  Title => 'Probabilities, Counting, and Equally Likely Outcomes',
	  Page  => 44,
	  Sections => {
		       0 => { Title => 'The Setting and Overview',
			      Page  => 44 },
		       1 => { Title => 'Probabilities, Events, and Equally Likely Outcomes',
			      Page  => 44 },
		       2 => { Title => 'Counting Arrangements: Permutations',
			      Page  => 57 },
		       3 => { Title => 'Counting Partitions: Combinations',
			      Page  => 66 },
		       4 => { Title => 'Computing Probabilities by Using Equally Likely Outcomes',
			      Page  => 77 },
		       5 => { Title => 'Important Terms and Concepts',
			      Page  => 83 },
		       6 => { Title => 'Review Exercises',
			      Page  => 83 }
		      }
	 },

    ## hash of chapter 03
    3 => {
	  Title    => 'Probability',
	  Page     => 88,
	  Sections => {
		       0 => { Title => 'The Setting and Overview', 
			      Page => 88 },
		       1 => { Title => 'Probability Measures: Axioms and Properties', 
			      Page  => 88 },
		       2 => { Title => 'Conditional Probability and Independence', Page => 99 },
		       3 => { Title => 'Stochastic Processes and Trees', Page => 107 },
		       4 => { Title => 'Bayes Probabilities', Page => 117 },
		       5 => { Title => 'Bernoulli Trials', Page => 127 },
		       6 => { Title => 'Important Terms', Page => 138 },
		       7 => { Title => 'Review Exercises', Page => 138 }
	              }

         }
   );

## retrieve the reference to the hash table of chapter 1.
my $ch_01_ht = $complete_textbook{1};
print $ch_01_ht->{'Title'}, "\n";
print $ch_01_ht->{Title}, "\n";
print $ch_01_ht->{'Page'}, "\n";
print $ch_01_ht->{Page}, "\n";

## retrieve the reference to the hash table of the sections of chapter 1.
my $ch_01_sections = $ch_01_ht->{'Sections'};

## this prints out the title of the 2nd section of chapter 1:
## 'Venn Diagrams and Partitions',
print $complete_textbook{1}->{Sections}->{2}->{Title}, "\n";
print $complete_textbook{1}{Sections}{1}{Title}, "\n";

## this is how we can modify the value of a deep key.
$complete_textbook{1}->{'Sections'}->{2}->{'Title'} = 'VENN DIAGRAMS AND PARTITIONS';
print $complete_textbook{1}->{'Sections'}->{2}->{'Title'}, "\n";
print $complete_textbook{1}{Sections}{2}{Title}, "\n";

while ( my ($key, $val) = each(%{$complete_textbook{1}->{'Sections'}->{3}}) ) {
  print "$key -> $val\n";
}
