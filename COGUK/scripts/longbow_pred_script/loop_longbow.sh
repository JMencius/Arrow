#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

for i in ../../data/ont_raw_reads/*.fastq;do
	echo "$i";
	python ../../../longbow_code/longbow2.2.0/longbow.py -i "$i" -t 24;
done

