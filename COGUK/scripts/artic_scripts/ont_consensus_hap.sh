#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate happy;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")

mkdir -p ../../results/ont_consensus_hap;

for i in "$base"/results/ERR*;do
        echo "$i";
        ERR=$(basename "$i")
        hap.py "$base"/data/ngs_consensus/"$ERR"/"$ERR"_ngs.vcf "$base"/data/ont_consensus/"$ERR"/"$ERR"_ont.vcf -o "$base"/results/ont_consensus_hap/"$ERR"_ont -r "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta  --threads 12 --set-gt hom --quiet;
done
