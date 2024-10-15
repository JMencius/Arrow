#!/bin/bash

# Pipeline
# 1. Run LongBow on our own basecalled data
bash run_own_called_longbow.sh;

# 2. Summarize the own basecalled results
python analysis_own_called_result.py -i ../results/own_called -o ../results/own_called.csv;

# 3. Download ONT human data from SRA
python download_all_sra_ont.py -t 16 -o ../results/sra_human -p ./sratoolkit/sratoolkit.3.0.7-ubuntu64/bin -i sra_list.txt;

# 4. Run LongBow on human ONT SRA records
bash run_sra_ont_longbow.sh > ../results/sra_human_log.txt;

# 5. Summarize the human ONT SRA results
python analysis_sra_ont.py -g ../results/sra_human_log.txt -i ../results/sra_human -s ../data/sra_human_10Kreads -l sra_list.txt -o ../results/sra_ont_result.csv;

