#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate ont-longbow;

script_dir=$(dirname "$(realpath "$0")")
base=$(dirname "$script_dir")


for i in ../data/G4G6_passonly/*.fastq; do
	echo "$i";
	name=$(basename "$i")
	python ../../longbow_code/longbow2.2.0/longbow.py -t 32 -i "$i" -b -o "$base"/results/own_called/"$name".json;
done
