#!/bin/bash

# partial download the raw ONT FAST5 files
python partial_download.py -i DNA_raw_20240109.txt -w ../data > ../results/download_log.txt;

# preprocess the download files, mostly decompressing
python hexdump_preprocess.py -w ../data;

# Analysi the FAST5 files using `hexdump`
python hexdump_check.py -i ../data -o ../results/sra_fast5_ano.txt > ../results/annotation.log;

