#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/miniconda3/etc/profile.d/conda.sh;
conda activate happy;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")


longbow_result=$(realpath ../results/longbow_hap)

cd "$longbow_result";
for i in "$base"/results/ERR*;do
	echo "$i";
	ERR=$(basename "$i")
	hap.py "$base"/data/ngs_consensus/"$ERR"/"$ERR"_ngs.vcf "$i"/longbow/"$ERR"_longbow_consensus.vcf -o "$i"_longbow -r "$base"/ref/nCoV-2019/V3/nCoV-2019.reference.fasta  --threads 12 --quiet --set-gt hom;
done
cd "$base"/results;
mv *longbow* "$longbow_result";

