import sys, os

### change my_root_dir below to the directory
### with all the modules imported below:
### 1. porter.py
### 2. text.py
### 3. rtrvr.py
### mse_tests.py imports fnfilter.py

my_root_dir = '/home/vladimir/code/python/mse/'

if not my_root_dir in sys.path:
   sys.path.append(my_root_dir)

import porter
import text
import rtrvr
import py_mse_srvr
