#!/bin/bash

for file in ../data/downsample/*.fastq;do

	echo $(basename "$file");
	python get_qscore.py -t 48 -i "$file" -o ../results/qscore_$(basename "$file").csv;

done
