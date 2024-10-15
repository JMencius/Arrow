#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate happy;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")

default_result=$(realpath "$base"/results/default_hap)

cd "$random_result";
for i in "$base"/results/ERR*;do
        echo "$i";
        ERR=$(basename "$i")
        hap.py "$base"/data/ngs_consensus/"$ERR"/"$ERR"_ngs.vcf "$i"/random/"$ERR"_default_consensus.vcf -o "$i"_random -r "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta  --threads 12 --set-gt hom --quiet;
done
cd "$base"/results;
mv *random* "$random_result"
