#!/bin/bash

# build directory structure
mkdir -p ../data/sra_human_10Kreads;
mkdir -p ../results/own_called;
mkdir -p ../results/sra_human;


# Pipeline
# 1. Run LongBow on our own basecalled data
bash run_own_called_longbow.sh;

# 2. Summarize the own basecalled results
bash analysis_own_called_result.sh;

# 3. Download ONT human data from SRA
bash download_all_sra_ont.sh;

# 4. Run LongBow on human ONT SRA records
bash run_sra_ont_longbow.sh > ../results/sra_human_log.txt;

# 5. Summarize the human ONT SRA results
bash analysis_sra_ont.sh;

