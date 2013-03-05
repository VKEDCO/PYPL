#!/usr/bin/python

import sys

####################################################################
## DATA.TXT whose contents are given below is available 
## at https://github.com/VKEDCO/PYPL/tree/master/file_processing/.
'''
A1	10	14.5	15	18.78	20.1
A2	890	10	997	109	13.45
A3	98	11	791	901	45.8
A4	56	61	94	105	4.1
A5	0.3	0.56	91.2	15	543
'''
## using generator chains to extract various statistics
## from DATA.TXT
##
## bugs to vladimir dot kulyukin at gmail dot com
####################################################################

## Take tab-separated line 'KEY  VAL1 VAL2 VAL3 ... VALN', e.g.
## 'A1  10    14.5    15    18.78    20.1' and compute
## (KEY, VAL) pair where VAL is the value for a particular
## column. For example, (A1, 10), (A1, 20.1).
def key_val_pair_for_column(line, col_num):
    splits = line.split('\t')
    return splits[0], float(splits[col_num])

## Take a tab-separated line 'A1  10	14.5	15    18.78  20.1'
## where A1 is a key and return (KEY, SUM) where SUM is
## the sum of all values. 
def key_sum_pair_for_row(line):
    splits = line.split('\t')
    return splits[0], sum((float(s) for s in splits[1:]))

## find (key, val) such that val is the maximum value
## in the sequence of (key, val) pairs, i.e., key_val_pairs.
def max_key_val_pair(key_val_pairs):
    return max(key_val_pairs, key=lambda x: x[1])

## find (key, val) such that val is the minimum value
## in the sequence of (key, val) pairs, i.e., key_val_pairs.
def min_key_val_pair(key_val_pairs):
    return min(key_val_pairs, key=lambda x: x[1])

def val_above_thresh(key_val_pair, thresh):
    if key_val_pair[1] > thresh:
        return key_val_pair[1]
    else:
        return 0

def key_val_pair_above_thresh(key_val_pair, thresh):
    k, v = key_val_pair
    if v > thresh:
        return key_val_pair
    else:
        return k, 0

## extract and process pipe chain data is extracted and then processed
## EXTRACT -> PROCESS
def extract_process_pipe_chain(data_fp, data_extractor, data_processor):
    with open(data_fp, 'r') as data_input:
        extracted_data = (data_extractor(line) 
                          for line in data_input 
                          if line != '' and line != '\n')
        processed_data = data_processor(extracted_data)
        return processed_data

## EXTRACT -> PROCESS -> COLLECT
def extract_process_collect_pipe_chain(data_file_path,
                                       data_extractor,
                                       data_processor,
                                       data_collector):
    with open(data_file_path, 'r') as data_input:
        extracted_data = (data_extractor(line) 
                          for line in data_input 
                          if line != '' and line != '\n')
        processed_data = (data_processor(datum) 
                          for datum in extracted_data)
        collected_data = data_collector(processed_data)
        return collected_data

## find key with maximum data value in column col_num
def max_key_val_for_column(data_fp, col_num):
    return extract_process_pipe_chain(data_fp,
                                      lambda line: key_val_pair_for_column(line, col_num),
                                      max_key_val_pair)


## COL 1 : ('A2', 890.0)
## COL 2 : ('A4', 61.0)
## COL 3 : ('A2', 997.0)
## COL 4 : ('A3', 901.0)
## COL 5 : ('A5', 543.0)
for col_num in xrange(1, 6):
    print 'COL', col_num, ':', max_key_val_for_column('data.txt', col_num)

def max_key_row_sum(data_fp):
    return extract_process_pipe_chain(data_fp, key_sum_pair_for_row, max_key_val_pair)

## prints out ('A2', 2019.45)
print max_key_row_sum('data.txt')

def sum_vals_above_thresh_for_column(data_fp, col_num, thresh):
    return extract_process_collect_pipe_chain(data_fp,
                                 lambda line: key_val_pair_for_column(line, col_num),
                                 lambda kv_pair: val_above_thresh(kv_pair, thresh),
                                 sum)

## prints out 988.0
print sum_vals_above_thresh_for_column('data.txt', 1, 90)

## prints out 0
print sum_vals_above_thresh_for_column('data.txt', 2, 90)



    


