#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate python3-env;

# calculate Artex extra variants compared to Artic pipelines
python get_extra_variant.py;

# calcualte delta recovery rate
python recovery_rate.py;

# calculate overall F1 score
mkdir -p ../../results/F1_score_file;
python get_f1.py -l ../err_id.txt -d ../../results/longbow_hap -o ../../results/F1_score_file/longbow_SNP.csv -m SNP -p longbow;
python get_f1.py -l ../err_id.txt -d ../../results/longbow_hap -o ../../results/F1_score_file/longbow_INDEL.csv -m INDEL -p longbow;
python get_f1.py -l ../err_id.txt -d ../../results/default_hap -o ../../results/F1_score_file/default_SNP.csv -m SNP -p default;
python get_f1.py -l ../err_id.txt -d ../../results/default_hap -o ../../results/F1_score_file/default_INDEL.csv -m INDEL -p default;
python get_f1.py -l ../err_id.txt -d ../../results/random_hap -o ../../results/F1_score_file/random_SNP.csv -m SNP -p random;
python get_f1.py -l ../err_id.txt -d ../../results/random_hap -o ../../results/F1_score_file/random_INDEL.csv -m INDEL -p random;
python get_f1.py -l ../err_id.txt -d ../../results/ont_consensus_hap -o ../../results/F1_score_file/ont_consensus_SNP.csv -m SNP -p ont;
python get_f1.py -l ../err_id.txt -d ../../results/ont_consensus_hap -o ../../results/F1_score_file/ont_consensus_INDEL.csv -m INDEL -p ont;
python get_f1.py -l ../err_id.txt -d ../../results/artex_hap -o ../../results/F1_score_file/artex_SNP.csv -m SNP -p artex;
python get_f1.py -l ../err_id.txt -d ../../results/artex_hap -o ../../results/F1_score_file/artex_SNP.csv -m INDEL -p artex;
