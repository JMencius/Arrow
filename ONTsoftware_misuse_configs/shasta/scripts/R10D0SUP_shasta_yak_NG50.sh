#!/bin/bash

# Run shasta
## wrong config to R9G4
./shasta-Linux-0.11.1 --input ../../basecalled_data/HG002_R10D0SUP_q10.fastq --config Nanopore-Sep2020 --threads 128 --assemblyDirectory ../results/R10D0SUP_R9G4;

## wrong config to R9G6
./shasta-Linux-0.11.1 --input ../../basecalled_data/HG002_R10D0SUP_q10.fastq --config Nanopore-May2022 --threads 128 --assemblyDirectory ../results/R10D0SUP_R9G6;

## correct config
./shasta-Linux-0.11.1 --input ../../basecalled_data/HG002_R10D0SUP_q10.fastq --config Nanopore-R10-Fast-Nov2022 --threads 128 --assemblyDirectory ../results/R10D0SUP_R10;


# Run cal50
conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate caln50;

## calculate NG50 for each config
calN50.js -f ../ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta.fai ../results/R10D0SUP_R10/Assembly.fasta > ../results/R10D0SUP_R10/calN50_result.txt;
calN50.js -f ../ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta.fai ../results/R10D0SUP_R9G4/Assembly.fasta > ../results/R10D0SUP_R9G4/calN50_result.txt;
calN50.js -f ../ref/GCA_000001405.15_GRCh38_no_alt_analysis_set.fasta.fai ../results/R10D0SUP_R9G6/Assembly.fasta > ../results/R10D0SUP_R9G6/calN50_result.txt;


# Run yak QV evaluation
conda activate yak;
yak qv -t 32 -p -K 3.2g -l 100k ../ref/sr.yak ../results/R10D0SUP_R10/Assembly.fasta > ../results/R10D0SUP_R10/yak.txt;
yak qv -t 32 -p -K 3.2g -l 100k ../ref/sr.yak ../results/R10D0SUP_R9G4/Assembly.fasta > ../results/R10D0SUP_R9G4/yak.txt;
yak qv -t 32 -p -K 3.2g -l 100k ../ref/sr.yak ../results/R10D0SUP_R9G6/Assembly.fasta > ../results/R10D0SUP_R9G6/yak.txt;
