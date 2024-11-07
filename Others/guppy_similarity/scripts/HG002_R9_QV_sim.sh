#!/bin/bash

# build directory strucutre
mkdir -p ../results/QV_similarity;


conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

base=../data/HG002_R9

groups=(guppy2.3.7 guppy3.6.1_fast guppy3.6.1_hac guppy4.5.4_fast guppy4.5.4_hac guppy5.1.16_fast guppy5.1.16_hac guppy5.1.16_sup guppy6.4.6_fast guppy6.4.6_hac guppy6.4.6_sup)

for i in "${groups[@]}";do
	for j in "${groups[@]}";do
		python seq_bha_sim.py -t 432 -r "$base"/"$i"/all.fastq -q "$base"/"$j"/all.fastq -o ../results/QV_similarity/"$i"_"$j"_QVsim.csv;
	done
done
