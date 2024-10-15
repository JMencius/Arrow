#!/bin/bash

# COLO829_dorado0.4.1_fast whole dataset
python autocorr.py -t 112 -i ../data/all_pod5_dorado0.4.1_fast_whole/COLO829_R10D0FAST_all.fastq -o ../results/autcorrelation_dorado_wholedata.csv;

# COLO829_guppy6.4.6_fast whole dataset
python autocorr.py -t 112 -i ../data/all_pod5_dorado0.4.1_fast_whole/COLO829_R10G6FAST_all.fastq -o ../results/autcorrelation_guppy_wholedata.csv;


