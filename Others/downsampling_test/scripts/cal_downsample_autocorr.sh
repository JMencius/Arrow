#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

for file in ../data/downsample/*.fastq;do

	echo $(basename "$file");
	python autocorr.py -t 32 -i "$file" -o ../results/autcorrelation_$(basename "$file").csv;

done
