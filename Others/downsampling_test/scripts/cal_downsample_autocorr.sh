#!/bin/bash

for file in ../downsample/*.fastq;do

	echo $(basename "$file");
	python autocorr.py -t 112 -i "$file" -o ../results/autcorrelation_$(basename "$file").csv;

done
