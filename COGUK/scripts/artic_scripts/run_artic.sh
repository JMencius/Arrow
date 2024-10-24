#!/bin/bash

# use random seed 100 to generate random model
bash generate_random_model.sh;

# loop artic on ont data using longbow model, default model, random model
bash loop_artic.sh;

# run bcftools and hap.py
bash ngs_bcftools.sh;
bash ont_bcftools.sh;

# use bcftools to extract each variants
# and evaluate using hap.py
bash longbow_bcftools.sh;
bash longbow_hap.sh

bash random_bcftools.sh;
bash random_hap.sh;

bash default_bcftools.sh;
bash default_hap.sh;

# move the longbow_consensus_bam file to a assemble directory
mkdir -p ../../results/longbow_consensus_bam;
for i in ../../results/ERR*;do
	ERR=$(basename "$i")
	mv "$i"/longbow/"$ERR"_longbow_consensus_sorted.bam ../../results/longbow_consensus_bam;
done
