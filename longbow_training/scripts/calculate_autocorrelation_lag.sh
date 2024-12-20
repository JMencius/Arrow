#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;


for group in R9G4 R9G6 R9D0 R10G6 R10D0;do
	python autocorrelation_LOO_lag.py -i ../results/model -s "$group" -o ../results/"$group"_autocorrelation_lag_accuracy.txt;

done
