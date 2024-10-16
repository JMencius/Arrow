#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

# COLO829_dorado0.4.1_fast whole dataset
python get_qscore.py -t 32 -i ../data/COLO829_R10D0FAST_whole/COLO829_R10D0FAST_all.fastq -o ../results/qscore_dorado_wholedata.csv;

# COLO829_guppy6.4.6_fast whole dataset
python get_qscore.py -t 32 -i ../data/COLO829_R10G6FAST_whole/COLO829_R10G6FAST_all.fastq -o ../results/qscore_guppy_wholedata.csv;
