#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;


for file in ../data/downsample/*.fastq;do

	echo $(basename "$file");
	python get_qscore.py -t 32 -i "$file" -o ../results/qscore_$(basename "$file").csv;

done
