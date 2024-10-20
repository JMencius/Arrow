#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

python analysis_sra_ont.py -g ../results/sra_human_log.txt -i ../results/sra_human -s ../data/sra_human_10Kreads -l sra_list.txt -o ../results/sra_ont_result.csv;
