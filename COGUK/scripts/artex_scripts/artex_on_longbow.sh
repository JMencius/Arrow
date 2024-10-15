#!/bin/bash

conda_base=$(conda info --base);
source "$conda_base"/etc/profile.d/conda.sh;
conda activate artex;

script_dir=$(dirname "$(realpath "$0")")
script_base=$(dirname "$script_dir")
base=$(dirname "$script_base")

for i in "$base"/results/ERR*;do
	ERR=$(basename "$i")
	python "$base"/scripts/artex/artex.py -i "$base"/results/"$ERR"/longbow -o "$base"/results/"$ERR"/artex  -p clair3 -c R9G4 --verbose;
done
