#!/usr/bin/python

import glob, sys, os

## Get all files matching pattern in sys.argv[1]
## sample usage:
## > python glob_ls.py <dir_pat> <abs_or_rel>
## or
## > ./glob_ls.py <dir_pat> <abs_or_rel>
## where <dir_pat> == is a directory pattern, e.g., git/*/
## and <abs_or_rel> == a or <abs_or_rel> == r
##
## 
## suppose that there exists the following directory structure
## in the current working directory (check git.zip in 
## https://github.com/VKEDCO/PYPL/tree/master/file_processing/)
## 
## /git
##  /PYPL
##    /hashing
##        /pl
##    /horspool
##        /pl
##        /py
##    /regular_expressions
##        /pl
##        /py
##
## Then the following outputs will take place:
## 
## >./glob_ls.py 'git/*/' r
## git/PYPL/
##
## >./glob_ls.py 'git/*/*/' r
## git/PYPL/hashing/
## git/PYPL/horspool/
## git/PYPL/regular_expressions/
##
## >./glob_ls.py 'git/*/*/*/' r
## git/PYPL/hashing/pl/
## git/PYPL/horspool/pl/
## git/PYPL/horspool/py/
## git/PYPL/regular_expressions/pl/
## git/PYPL/regular_expressions/py/
## 
## ./glob_ls.py 'git/*/*/*/*.p[ly]' r
## git/PYPL/hashing/pl/hashes_of_arrays.pl
## git/PYPL/hashing/pl/hash_manip_01.pl
## git/PYPL/hashing/pl/table_of_contents_as_hash.pl
## git/PYPL/hashing/pl/hash_construction_01.pl
## git/PYPL/hashing/pl/hash_manip_03.pl
## git/PYPL/hashing/pl/hash_manip_02.pl
## git/PYPL/hashing/pl/hash_construction_02.pl
## git/PYPL/horspool/pl/horspool.pl
## git/PYPL/horspool/py/horspool.py
## git/PYPL/regular_expressions/pl/hyperlinks.pl
## git/PYPL/regular_expressions/pl/re_match_patterns.pl
## git/PYPL/regular_expressions/pl/loose_and_tight_re_matching.pl
## git/PYPL/regular_expressions/pl/backrefs_02.pl
## git/PYPL/regular_expressions/pl/backrefs_01.pl
## git/PYPL/regular_expressions/pl/fsa.pl
## git/PYPL/regular_expressions/pl/m_operator.pl
## git/PYPL/regular_expressions/py/backrefs_01.py
## git/PYPL/regular_expressions/py/re_match_patterns.py
## git/PYPL/regular_expressions/py/fsa.py
## git/PYPL/regular_expressions/py/backrefs_02.py
## git/PYPL/regular_expressions/py/email_search_01.py
##
## bugs to vladimir dot kulyukin at gmail dot com
####################################################

## glob relative dir_pattern
def glob_relative_path(dir_pattern):
   for f in glob.iglob(dir_pattern):
      print f

## glob absolute dir_pattern by joining it
## to the current working directory.
def glob_absolute_path(dir_pattern):
   absolute_path = os.path.join(os.getcwd(), dir_pattern)
   for f in glob.iglob(absolute_path):
      print f

if __name__ == '__main__':
   if len(sys.argv) != 3:
      print 'usage: >./glob_ls.py <dir> <abs_rel>', "\n"
      sys.exit(1)

   dir_pat, abs_or_rel = sys.argv[1], sys.argv[2]

   if abs_or_rel != 'a' and abs_or_rel != 'r':
      print 'second argument must be a or r', "\n"
      sys.exit(1)

   if abs_or_rel == 'a':
      glob_absolute_path(dir_pat)
   elif abs_or_rel == 'r':
      glob_relative_path(dir_pat)
         
   
