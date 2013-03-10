#!/usr/bin/python

## filter_after_timestamp filters all files in a given directory by 
## timestamps saving only those files that have been saved on or 
## before a given time stamp.
## 
## bugs to vladimir dot kulyukin at gmail dot com.

import os.path, time, sys
import fnmatch
import glob

def is_on_or_before_time(fp, month_name='Feb', day=23, h=23, year=2013):
    ## get time stamp string of the last modified date
    time_str = time.ctime(os.path.getmtime(fp))
    ## split by space
    splits = time_str.split(' ')
    ## remove ''
    if '' in splits: splits.remove('')
    wd, mo_name, mo_day, hms_time, y = splits
    hr, mn, secs = hms_time.split(':')
    return mo_name == month_name and\
           int(mo_day) <= day and\
           int(hr) <= h and\
           int(y) == year

def filter_after_timestamp(root_dir, extensions=['py', 'pl'],
                           mo_name='Feb', 
                           day=23, h=23, year=2013):
    filtered_files = []
    ## loop through each sub_dir of root_dir
    for sub_dir in glob.iglob(root_dir):
        ## walk each sub_dir
        ## root is the current dir, dirs are sub dirs of current dir, files are the
        ## files in the current directory
        for root, dirs, files in os.walk(sub_dir):
            for f in files:
                if (fnmatch.fnmatch(f, '*.py') or fnmatch.fnmatch(f, '*.pl')) and\
                        (not is_on_or_before_time(os.path.join(root, f),
                                                  month_name=mo_name, day=day, h=h,
                                                  year=year)):
                        filtered_files.append(os.path.join(root, f))
    return filtered_files

if __name__ == '__main__':
    if len(sys.argv) == 2:
        filtered_files = filter_after_timestamp(sys.argv[1])
        print filtered_files

                                 
        
    
    
